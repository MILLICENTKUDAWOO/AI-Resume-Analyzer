def generate_improvement_report(missing_skills):

    report = []


    for skill in missing_skills:

        skill = skill.lower()


        if skill == "github":
            report.append(
                "Create GitHub repositories to showcase your programming projects."
            )


        elif skill == "sql":
            report.append(
                "Learn SQL and database management for software and data roles."
            )


        elif skill == "machine learning":
            report.append(
                "Study Machine Learning fundamentals for AI-related roles."
            )


        elif skill == "javascript":
            report.append(
                "Learn JavaScript to improve your web development skills."
            )


        else:
            report.append(
                f"Improve your knowledge of {skill}."
            )


    if len(report) == 0:

        report.append(
            "Your resume covers most required skills. Continue building projects."
        )


    return report