from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors

import os



def create_report(
        analysis,
        careers,
        interview_questions,
        report_folder
):

    filename = "AI_Career_Coach_Report.pdf"

    filepath = os.path.join(
        report_folder,
        filename
    )


    doc = SimpleDocTemplate(
        filepath,
        pagesize=letter,
        title="AI Career Coach Report"
    )


    styles = getSampleStyleSheet()


    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=22,
        spaceAfter=20
    )


    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        textColor=colors.HexColor("#2563eb"),
        spaceBefore=15,
        spaceAfter=10
    )


    body_style = ParagraphStyle(
        "BodyStyle",
        parent=styles["BodyText"],
        fontSize=11,
        leading=16
    )


    content = []


    content.append(
        Paragraph(
            "AI Career Coach Pro",
            title_style
        )
    )


    content.append(
        Paragraph(
            "Transforming Resumes Into Career Opportunities",
            body_style
        )
    )


    content.append(Spacer(1,20))



    content.append(
        Paragraph(
            "Resume Performance",
            heading_style
        )
    )


    score_table = Table(
        [
            ["Resume Health", f"{analysis['score']}%"],
            ["ATS Compatibility", f"{analysis['ats_score']}%"]
        ],
        colWidths=[180,100]
    )


    score_table.setStyle(
        TableStyle([
            ("GRID",(0,0),(-1,-1),0.5,colors.grey),
            ("BACKGROUND",(0,0),(-1,-1),colors.whitesmoke)
        ])
    )


    content.append(score_table)



    content.append(
        Spacer(1,20)
    )



    content.append(
        Paragraph(
            "AI Resume Summary",
            heading_style
        )
    )


    content.append(
        Paragraph(
            analysis["summary"],
            body_style
        )
    )



    content.append(
        Paragraph(
            "Skills Detected",
            heading_style
        )
    )


    content.append(
        Paragraph(
            ", ".join(analysis["skills"]),
            body_style
        )
    )



    content.append(
        Paragraph(
            "Skills To Improve",
            heading_style
        )
    )


    content.append(
        Paragraph(
            ", ".join(analysis["missing_skills"]),
            body_style
        )
    )



    content.append(
        Paragraph(
            "Recommended Career Paths",
            heading_style
        )
    )



    career_data = [
        ["Career", "Match Score"]
    ]


    for career in careers:

        career_data.append(
            [
                career["title"],
                f"{career['score']}%"
            ]
        )



    career_table = Table(career_data)


    career_table.setStyle(
        TableStyle([
            ("GRID",(0,0),(-1,-1),0.5,colors.grey),
            ("BACKGROUND",(0,0),(-1,0),colors.lightgrey)
        ])
    )


    content.append(career_table)



    content.append(
        Paragraph(
            "AI Interview Preparation",
            heading_style
        )
    )



    for question in interview_questions:

        content.append(
            Paragraph(
                "• " + question,
                body_style
            )
        )



    content.append(
        Paragraph(
            "Career Roadmap",
            heading_style
        )
    )


    for step in analysis["roadmap"]:

        content.append(
            Paragraph(
                "• " + step,
                body_style
            )
        )



    content.append(
        Spacer(1,25)
    )


    content.append(
        Paragraph(
            "Built by Millicent Kudawoo",
            body_style
        )
    )



    doc.build(content)


    return filename