from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_user_repos():
    r = requests.get('https://api.github.com/users/zacharygilliom/repos')
    repos = {}
    for repo in r.json():
        repo_name = repo["name"]
        repo_url = repo["html_url"]
        print(repo['languages_url'])
        repo_languages = repo["languages_url"]
        r_l = requests.get(repo_languages)
        langs = []
        for lang, num in r_l.json().items():
            langs.append(lang) 
        repos[repo_name] = {"url":repo_url,
                            "lang":langs}
    return repos 

if __name__ == "__main__":
    app.run(debug=True)
