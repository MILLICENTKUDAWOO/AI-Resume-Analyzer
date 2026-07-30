def analyze_strengths(resume_text):

    strengths = []

    text = resume_text.lower()


    if "python" in text:
        strengths.append("🐍 Strong Python programming foundation")


    if "html" in text and "css" in text:
        strengths.append("🌐 Has web development experience")


    if "data analysis" in text or "excel" in text:
        strengths.append("📊 Has data analysis knowledge")


    if "project" in text or "built" in text:
        strengths.append("🚀 Has practical project experience")


    if "quickbooks" in text:
        strengths.append("💼 Has administrative and business software experience")


    if len(strengths) == 0:
        strengths.append("💡 Continue building technical skills and projects")


    return strengths