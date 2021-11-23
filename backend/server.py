import requests
from flask import Flask
from github import Github
from configs.configs import Config

app = Flask(__name__)

g = Github(Config.github_access_token)

@app.route('/get_my_repos')
def get_user_repos(methods=['GET']):
    repos = {}
    for repo in g.get_user().get_starred():
        repo_name = repo.name
        repo_url = repo.html_url
        langs = []
        for lang, num in repo.get_languages().items():
            langs.append(lang) 
        repos[repo_name] = {"url":repo_url,
                                "lang":langs}
    return repos 

if __name__ == "__main__":
    app.run(debug=True)
