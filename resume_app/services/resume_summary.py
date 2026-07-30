def generate_summary(resume_text):

    text = resume_text.lower()

    summary = "The candidate "

    if "computer science" in text:
        summary += "is a Computer Science student "

    if "python" in text:
        summary += "with experience in Python programming "

    if "html" in text and "css" in text:
        summary += "and web development using HTML and CSS "

    if "data analysis" in text:
        summary += "with knowledge of data analysis "

    if "quickbooks" in text:
        summary += "and administrative experience using QuickBooks "

    summary += "."

    return summary.capitalize()