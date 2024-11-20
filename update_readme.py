import requests

# GitHub username
USERNAME = "Khantdotcom"

# Fetch repositories
url = f"https://api.github.com/users/{USERNAME}/repos"
response = requests.get(url)
repos = response.json()

# Create a list of repository names
repo_list = "\n".join([f"- [{repo['name']}]({repo['html_url']})" for repo in repos[:5]])

# Update README content
with open("README.md", "w") as file:
    file.write(f"# Hi there! 👋\n\n## Latest Repositories\n{repo_list}")
