"""
    @author Jenish Kevadia

    Script fetches the repositories and commits from user's GitHub account
"""

import requests
import json


def get_repositories(usr):
    """ Get user repositories and commits"""

    repo = []
    commits = []

    r_url = "https://api.github.com/users/"
    c_url = "https://api.github.com/repos/"

    repo_url = r_url + f'{usr}/' + 'repos'

    try:
        repo_url = requests.get(url = repo_url)
    except (TypeError, KeyError, IndexError):
        return "Failed to fetch the repos"

    repo_url = json.loads(repo_url.text)

    for repository in repo_url:
        try:
            repo.append(repository['name'])
        except (TypeError, KeyError, IndexError):
            return "Repos name doesn't exist"
    
    for r in repo:
        commit_url = c_url + f'{usr}/{r}/commits'
        
        try:
            res = requests.get(url = commit_url)
        except (TypeError, KeyError, IndexError):
            return "Failed to fetch the commits"

        res_jason = json.loads(res.text)
        commits.append(f'Repo: {r}, Number of commits: {len(res_jason)}')

    return commits

def main():
    """ Get user's name as an input """

    usr = input("Enter user name: ")

    for repo in get_repositories(usr):
        print(repo)
    

if __name__ == '__main__':
    """ Run the main function on startup """
    main()

