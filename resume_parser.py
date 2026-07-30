import spacy


nlp = spacy.load("en_core_web_sm")



SKILLS_DATABASE = [

    "Python",
    "HTML",
    "CSS",
    "JavaScript",
    "Excel",
    "Data Analysis",
    "SQL",
    "Flask",
    "Machine Learning",
    "Natural Language Processing",
    "Git",
    "GitHub"

]





def analyze_resume(text):


    result = {

        "skills": [],
        "missing_skills": [],
        "education": [],
        "experience": [],
        "score": 0,
        "ats_score": 0,
        "summary": "",
        "recommendations": [],
        "roadmap": []

    }



    text = text.lower()



    # Skill detection

    for skill in SKILLS_DATABASE:

        if skill.lower() in text:

            result["skills"].append(skill)



    # Missing skills

    for skill in SKILLS_DATABASE:

        if skill not in result["skills"]:

            result["missing_skills"].append(skill)





    # Education

    if any(word in text for word in [

        "university",
        "degree",
        "bsc",
        "education"

    ]):

        result["education"].append(
            "University education found"
        )





    # Experience

    if any(word in text for word in [

        "experience",
        "work",
        "intern",
        "job"

    ]):

        result["experience"].append(
            "Work experience found"
        )





    # Resume score

    score = 0


    if len(result["skills"]) >= 3:

        score += 40


    if result["education"]:

        score += 30


    if result["experience"]:

        score += 30



    result["score"] = score





    # ATS score

    ats = 0


    if len(result["skills"]) >= 3:

        ats += 30


    if result["education"]:

        ats += 20


    if result["experience"]:

        ats += 20


    if len(result["missing_skills"]) <= 5:

        ats += 30



    result["ats_score"] = ats






    # Summary

    if result["skills"]:


        skills = ", ".join(result["skills"])


        result["summary"] = (

            f"This candidate demonstrates a strong foundation in {skills}. "

            "Their education and professional experience show potential "

            "for entry-level technology roles. Further improvement in "

            "advanced technical skills and practical projects can "

            "strengthen their career profile."

        )


    else:


        result["summary"] = (

            "This resume requires more technical skills, "

            "projects and achievements."

        )






    # Recommendations


    if "SQL" not in result["skills"]:

        result["recommendations"].append(
            "Consider adding SQL skills"
        )


    if "Machine Learning" not in result["skills"]:

        result["recommendations"].append(
            "Consider adding Machine Learning projects"
        )


    if "GitHub" not in result["skills"]:

        result["recommendations"].append(
            "Add GitHub projects to strengthen your portfolio"
        )






    result["roadmap"] = [

        "Learn SQL for better data and software opportunities",

        "Explore AI and Machine Learning projects",

        "Build more practical projects and showcase them",

        "Add measurable achievements to your resume"

    ]



    return result







def match_job(resume_skills, job_description):


    matched = []

    missing = []



    job_text = job_description.lower()



    for skill in SKILLS_DATABASE:


        if skill.lower() in job_text:


            if skill in resume_skills:

                matched.append(skill)

            else:

                missing.append(skill)




    total = len(matched) + len(missing)



    if total > 0:

        score = int(

            (len(matched) / total) * 100

        )

    else:

        score = 0



    return {

        "score": score,

        "matched": matched,

        "missing": missing

    }








def recommend_careers(resume_skills):


    careers = [

        {

            "title": "Data Analyst Intern",

            "skills": [

                "Excel",
                "Data Analysis",
                "SQL"

            ]

        },


        {

            "title": "Frontend Developer Intern",

            "skills": [

                "HTML",
                "CSS",
                "JavaScript"

            ]

        },


        {

            "title": "Junior Python Developer",

            "skills": [

                "Python",
                "HTML",
                "CSS",
                "Flask",
                "Git"

            ]

        },


        {

            "title": "AI / Machine Learning Intern",

            "skills": [

                "Python",
                "Machine Learning",
                "Natural Language Processing"

            ]

        }

    ]



    results = []



    for career in careers:


        matched = []

        missing = []



        for skill in career["skills"]:


            if skill in resume_skills:

                matched.append(skill)

            else:

                missing.append(skill)



        score = int(

            (len(matched) / len(career["skills"])) * 100

        )



        results.append({

            "title": career["title"],

            "score": score,

            "matched": matched,

            "missing": missing

        })



    results.sort(

        key=lambda x:x["score"],

        reverse=True

    )



    return results[:3]









def generate_interview_questions(skills, job_description=""):


    questions = []



    if "Python" in skills:

        questions.append(
            "Explain your experience with Python programming."
        )


    if "HTML" in skills or "CSS" in skills:

        questions.append(
            "How do you create responsive web pages using HTML and CSS?"
        )


    if "Excel" in skills:

        questions.append(
            "How have you used Excel for data analysis?"
        )


    if "Data Analysis" in skills:

        questions.append(
            "Explain your process for analyzing data."
        )


    if "Flask" in skills:

        questions.append(
            "How would you build a Flask application?"
        )



    questions.extend([

        "Tell us about yourself.",

        "Describe a challenging project you completed.",

        "Why should we hire you?"

    ])



    return questions[:8]
def resume_strength(skills):

    strengths = []

    weaknesses = []


    if "Python" in skills:

        strengths.append(
            "Strong Python programming foundation"
        )


    if "HTML" in skills and "CSS" in skills:

        strengths.append(
            "Good web development foundation"
        )


    if "Excel" in skills or "Data Analysis" in skills:

        strengths.append(
            "Good data handling and analysis skills"
        )


    if "SQL" not in skills:

        weaknesses.append(
            "Improve database skills by learning SQL"
        )


    if "GitHub" not in skills:

        weaknesses.append(
            "Create GitHub projects to build your portfolio"
        )


    return {

        "strengths": strengths,

        "weaknesses": weaknesses

    }