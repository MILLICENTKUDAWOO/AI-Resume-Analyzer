from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet



def create_pdf_report(
        filename,
        score,
        match_level,
        resume_rating,
        strengths,
        matched,
        missing,
        recommendations,
        improvement_report,
        careers
):

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )


    styles = getSampleStyleSheet()

    content = []


    content.append(
        Paragraph(
            "AI Resume Analysis Report",
            styles["Title"]
        )
    )


    content.append(Spacer(1, 12))


    content.append(
        Paragraph(
            f"Resume Match Score: {score}%",
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            f"Match Level: {match_level}",
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            f"Resume Rating: {resume_rating}",
            styles["Normal"]
        )
    )


    content.append(Spacer(1, 12))


    content.append(
        Paragraph(
            "Resume Strengths:",
            styles["Heading2"]
        )
    )


    for item in strengths:

        content.append(
            Paragraph(
                "- " + item,
                styles["Normal"]
            )
        )


    content.append(Spacer(1, 12))


    content.append(
        Paragraph(
            "Matched Skills:",
            styles["Heading2"]
        )
    )


    content.append(
        Paragraph(
            ", ".join(matched),
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            "Missing Skills:",
            styles["Heading2"]
        )
    )


    content.append(
        Paragraph(
            ", ".join(missing),
            styles["Normal"]
        )
    )


    content.append(
        Paragraph(
            "Improvement Report:",
            styles["Heading2"]
        )
    )


    for item in improvement_report:

        content.append(
            Paragraph(
                "- " + item,
                styles["Normal"]
            )
        )


    content.append(
        Paragraph(
            "Recommendations:",
            styles["Heading2"]
        )
    )


    for item in recommendations:

        content.append(
            Paragraph(
                "- " + item,
                styles["Normal"]
            )
        )


    content.append(
        Paragraph(
            "Recommended Career Paths:",
            styles["Heading2"]
        )
    )


    content.append(
        Paragraph(
            ", ".join(careers),
            styles["Normal"]
        )
    )


    doc.build(content)