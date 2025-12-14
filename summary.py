def generate_summary(score):
    if score >= 70:
        return (
            "This repository demonstrates strong structure and consistent development "
            "practices. With minor improvements, it is suitable for recruiter evaluation."
        )
    elif score >= 40:
        return (
            "This project shows potential but lacks consistency in documentation or commit "
            "practices. Improvements can significantly enhance its quality."
        )
    else:
        return (
            "This repository is at an early stage and requires better structure, "
            "documentation, and development discipline."
        )
