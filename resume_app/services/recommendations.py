def generate_recommendations(missing_skills):

    recommendations = []

    advice = {
        "javascript": "Learn JavaScript to improve your web development skills.",
        "github": "Create GitHub repositories to showcase your programming projects.",
        "machine learning": "Study Machine Learning fundamentals for AI-related roles.",
        "sql": "Learn SQL and database management for software and data roles.",
        "python": "Improve your Python programming skills through projects.",
        "data analysis": "Practice data analysis using tools like Excel, Python, and Pandas."
    }


    for skill in missing_skills:

        if skill in advice:
            recommendations.append(advice[skill])


    return recommendations