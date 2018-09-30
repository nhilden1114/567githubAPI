'''
@author Nicole Hilden
September 30 2018

'''

import requests
import json

def get_repos(githubID):

    repos = requests.get("https://api.github.com/users/" +githubID+ "/repos")
    retrieved = repos.json()

    mockdata = []
    for repo in retrieved:
        commits = requests.get("https://api.github.com/repos/" +githubID+ "/" +repo["name"]+ "/commits")
        cretrieved = commits.json()
        print("Repo: "+repo["name"]+" Number of commits: "+str(len(cretrieved)))
        mockdata.append((str(repo["name"]), len(cretrieved)))

    return mockdata

def main():
    get_repos("nhilden1114")


if __name__ == "__main__":
    main()
