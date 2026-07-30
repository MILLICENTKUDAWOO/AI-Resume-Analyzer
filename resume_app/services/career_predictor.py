def predict_career(resume_text):

    careers = []

    text = resume_text.lower()


    if "python" in text:
        careers.append("🐍 Python Developer")


    if "html" in text and "css" in text:
        careers.append("🌐 Frontend Developer")


    if "data analysis" in text or "excel" in text:
        careers.append("📊 Data Analyst")


    if "machine learning" in text or "ai" in text:
        careers.append("🤖 AI/Machine Learning Engineer")


    if "sql" in text:
        careers.append("🗄️ Database Developer")


    if "github" in text:
        careers.append("💻 Software Engineer")


    if len(careers) == 0:
        careers.append("💡 Explore Software Development and Technology Roles")


    return careers