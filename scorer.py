def calculate_score(data):
    score = 0

    if data["files"] >= 5:
        score += 20
    if data["commits"] >= 10:
        score += 20
    if data["has_readme"]:
        score += 20
    if data["stars"] > 0:
        score += 10
    if data["forks"] > 0:
        score += 10

    if score >= 70:
        readiness = "Recruiter-Ready"
    elif score >= 40:
        readiness = "Almost Ready"
    else:
        readiness = "Not Ready"

    return score, readiness
