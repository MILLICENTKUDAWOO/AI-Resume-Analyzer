from flask import Flask, render_template, request, send_file, abort
import os
from uuid import uuid4
from werkzeug.utils import secure_filename

from pypdf import PdfReader

from resume_parser import (
    analyze_resume,
    match_job,
    recommend_careers,
    generate_interview_questions,
    resume_strength
)

from pdf_report import create_report


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
REPORT_FOLDER = os.path.join(BASE_DIR, "reports")


app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["REPORT_FOLDER"] = REPORT_FOLDER

# Limit uploads to 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB

ALLOWED_EXTENSIONS = {"pdf"}


os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_resume():
    resume = request.files.get("resume")
    job_description = request.form.get("job_description", "")

    if not resume:
        return "Please upload a resume", 400

    if not allowed_file(resume.filename):
        return "Only PDF files are allowed", 400

    # Sanitize filename and make it unique to avoid collisions
    filename = secure_filename(resume.filename)
    unique_name = f"{uuid4().hex}_{filename}"
    file_path = os.path.join(UPLOAD_FOLDER, unique_name)

    try:
        resume.save(file_path)
    except Exception as e:
        return f"Failed to save uploaded file: {e}", 500

    # Extract text from PDF safely
    try:
        reader = PdfReader(file_path)
    except Exception as e:
        return f"Failed to read uploaded PDF: {e}", 400

    resume_text = ""
    for page in reader.pages:
        try:
            text = page.extract_text()
        except Exception:
            text = ""
        if text:
            resume_text += text

    if not resume_text.strip():
        return "Could not extract text from the uploaded PDF. Please check the file and try again.", 400

    analysis = analyze_resume(resume_text)

    job_result = None
    if job_description.strip():
        job_result = match_job(analysis["skills"], job_description)

    careers = recommend_careers(analysis["skills"])

    interview_questions = generate_interview_questions(analysis["skills"], job_description)

    strength = resume_strength(analysis["skills"])

    report_file = create_report(analysis, careers, interview_questions, REPORT_FOLDER)

    return render_template(
        "result.html",
        analysis=analysis,
        job_result=job_result,
        career_recommendations=careers,
        interview_questions=interview_questions,
        strength=strength,
        report_file=report_file
    )


@app.route("/download/<filename>")
def download_report(filename):
    # Ensure the filename is within the reports folder (prevent path traversal)
    requested_path = os.path.abspath(os.path.join(REPORT_FOLDER, filename))
    reports_dir = os.path.abspath(REPORT_FOLDER)

    if not requested_path.startswith(reports_dir + os.sep):
        abort(404)

    if not os.path.exists(requested_path):
        abort(404)

    return send_file(requested_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
