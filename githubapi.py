'''
@author Nicole Hilden
September 22 2018

'''

import requests
import json

def get_repos(githubID):

    repos = requests.get("https://api.github.com/users/" +githubID+ "/repos")
    retrieved = json.loads(repos.text)

    repo_list = []
    
    for i in retrieved:
        try: repo_list += [i.get('name')]
        except:
            print ("Cannot get repositories for "+githubID)
            return []

    return repo_list

def get_commits(githubID, repo_name):

    commits = requests.get("https://api.github.com/repos/" +githubID+ "/" +repo_name+ "/commits")
    retrieved = json.loads(commits.text)

    #print(retrieved)

    return len(retrieved)

def main():
    githubID = input("What is your GitHub username? ")
    
    repositories = get_repos(githubID)

    for repo in repositories:
        print("Repo: " +repo+ " Number of commits: " +str(get_commits(githubID, repo)))

    #print(get_commits("nhilden1114", "667565ffghf"))


if __name__ == "__main__":
    main()
