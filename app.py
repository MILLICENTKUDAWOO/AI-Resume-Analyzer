from flask import Flask, render_template, request, send_file
import os

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



os.makedirs(UPLOAD_FOLDER, exist_ok=True)

os.makedirs(REPORT_FOLDER, exist_ok=True)







@app.route("/")
def home():

    return render_template("index.html")








@app.route("/upload", methods=["POST"])
def upload_resume():


    resume = request.files.get("resume")

    job_description = request.form.get(
        "job_description",
        ""
    )



    if not resume:

        return "Please upload a resume"




    file_path = os.path.join(

        UPLOAD_FOLDER,

        resume.filename

    )



    resume.save(file_path)






    reader = PdfReader(file_path)


    resume_text = ""



    for page in reader.pages:


        text = page.extract_text()



        if text:

            resume_text += text





    analysis = analyze_resume(resume_text)




    job_result = None



    if job_description.strip():


        job_result = match_job(

            analysis["skills"],

            job_description

        )







    careers = recommend_careers(

        analysis["skills"]

    )






    interview_questions = generate_interview_questions(

        analysis["skills"],

        job_description

    )






    strength = resume_strength(

        analysis["skills"]

    )






    report_file = create_report(

        analysis,

        careers,

        interview_questions,

        REPORT_FOLDER

    )






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


    path = os.path.join(

        REPORT_FOLDER,

        filename

    )



    return send_file(

        path,

        as_attachment=True

    )








if __name__ == "__main__":

    app.run(debug=True)