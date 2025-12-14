def generate_roadmap(data, score):
    roadmap = []

    if not data["has_readme"]:
        roadmap.append("Add a detailed README with project overview and setup steps.")

    if data["commits"] < 10:
        roadmap.append("Commit code more frequently with clear and meaningful messages.")

    if data["files"] < 5:
        roadmap.append("Improve project structure by modularizing the codebase.")

    if score >= 70:
        roadmap.append("Add unit tests and CI/CD to make the project production-ready.")

    return roadmap
