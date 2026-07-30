def extract_skills(text):
    skills_database = [
        "python",
        "html",
        "css",
        "javascript",
        "github",
        "data analysis",
        "machine learning",
        "sql",
        "excel",
        "quickbooks",
        "flask"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_database:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def calculate_match(resume_text, job_text):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    matched = []

    missing = []

    for skill in job_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    if len(job_skills) > 0:
        score = round((len(matched) / len(job_skills)) * 100)
    else:
        score = 0

    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }