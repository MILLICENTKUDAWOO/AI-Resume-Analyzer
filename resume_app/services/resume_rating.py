def get_resume_rating(score):

    if score >= 80:
        return "⭐⭐⭐⭐⭐ Excellent Resume"

    elif score >= 60:
        return "⭐⭐⭐⭐ Good Resume"

    elif score >= 40:
        return "⭐⭐⭐ Average Resume"

    else:
        return "⭐⭐ Needs Improvement"