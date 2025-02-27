import os
import re
import time
import requests

USERNAME = 'linkoffee'
TOKEN = os.getenv('LIN_TOKEN')
HEADERS = {'Authorization': f'token {TOKEN}'}


def get_all_repos():
    repos = []
    page = 1

    while True:
        url = f"https://api.github.com/user/repos?per_page=100&page={page}&type=all"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            print("Ошибка при получении репозиториев:", response.text)
            break

        data = response.json()
        if not data:
            break

        repos.extend(data)
        page += 1

    return repos


def get_total_commits(repo_full_name):
    commits_count = 0
    page = 1

    while True:
        url = f"https://api.github.com/repos/{repo_full_name}/commits?per_page=100&page={page}&author={USERNAME}"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            print(f"Ошибка при получении коммитов {repo_full_name}: {response.text}")
            break

        commits_data = response.json()
        commits_count += len(commits_data)

        if len(commits_data) < 100:
            break

        page += 1

    return commits_count


def get_lines_of_code(repo_full_name):
    url = f"https://api.github.com/repos/{repo_full_name}/languages"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        return sum(data.values())

    print(f"Ошибка при получении строк кода для {repo_full_name}: {response.text}")
    return 0


def get_github_stats():
    repos_data = get_all_repos()
    repos = len(repos_data)
    stars = sum(repo.get("stargazers_count", 0) for repo in repos_data)

    commits = 0
    lines_of_code = 0

    for repo in repos_data:
        repo_full_name = repo["full_name"]
        print(f"Обрабатывается: {repo_full_name}...")

        commits += get_total_commits(repo_full_name)
        time.sleep(1)

        lines_of_code += get_lines_of_code(repo_full_name)
        time.sleep(1)

    return repos, commits, lines_of_code, stars


def update_readme():
    repos, commits, lines_of_code, stars = get_github_stats()

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(r"Repositories: \d+", f"Repositories: {repos}", content)
    content = re.sub(r"Commits: \d+", f"Commits: {commits}", content)
    content = re.sub(r"LinesOfCode: \d+",
                     f"LinesOfCode: {lines_of_code}", content)
    content = re.sub(r"Stars: \d+", f"Stars: {stars}", content)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("README.md обновлен!")


if __name__ == "__main__":
    update_readme()
