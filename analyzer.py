import requests

def analyze_repo(repo_url):
    try:
        owner, repo = repo_url.replace("https://github.com/", "").split("/")
        base_url = f"https://api.github.com/repos/{owner}/{repo}"

        repo_data = requests.get(base_url).json()
        commits = requests.get(base_url + "/commits").json()
        contents = requests.get(base_url + "/contents").json()

        return {
            "files": len(contents) if isinstance(contents, list) else 0,
            "commits": len(commits) if isinstance(commits, list) else 0,
            "has_readme": any(
                item["name"].lower() == "readme.md"
                for item in contents if isinstance(contents, list)
            ),
            "stars": repo_data.get("stargazers_count", 0),
            "forks": repo_data.get("forks_count", 0)
        }

    except:
        return None
