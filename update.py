import os
import re
import requests

USERNAME = 'linkoffee'
TOKEN = os.getenv('GITHUB_TOKEN')
API_URL = f'https://api.github.com/users/{USERNAME}'
REPOS_URL = f'https://api.github.com/users/{USERNAME}/repos'
HEADERS = {'Authorization': f'token {TOKEN}'}


def get_github_stats():
    user_data = requests.get(API_URL, headers=HEADERS).json()
    repos_data = requests.get(REPOS_URL, headers=HEADERS).json()

    repos = user_data.get("public_repos", 0)
    stars = sum(repo.get("stargazers_count", 0) for repo in repos_data)

    events = requests.get(
        f"https://api.github.com/users/{USERNAME}/events", headers=HEADERS
    ).json()
    commits = sum(1 for event in events if event.get("type") == "PushEvent")

    lines_of_code = sum(
        len(
            requests.get(repo["url"] + "/languages", headers=HEADERS).json()
        ) for repo in repos_data
    )

    return repos, commits, lines_of_code, stars


def update_readme():
    repos, commits, lines_of_code, stars = get_github_stats()

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r"Repositories: \d+", f"Repositories: {repos}", content
    )
    content = re.sub(
        r"Commits: \d+", f"Commits: {commits}", content
    )
    content = re.sub(
        r"LinesOfCode: \d+", f"LinesOfCode: {lines_of_code}", content
    )
    content = re.sub(
        r"Stars: \d+", f"Stars: {stars}", content
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    update_readme()
