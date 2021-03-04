# import requests

# headers = {
#     "Authorization": "Basic QWxleHNhdXJpbzpjODI0ZDBkZjRhZjNiODc1MDA0ZmFmYzY2MTc5NmM2YTk1ZDM1Y2Y4"
#     # "token = c824d0df4af3b875004fafc661796c6a95d35cf8",
#     "Accept" : "application/vnd.github.v3+json"
# }

# payload = {
#     "name": "Alexsaurio"
# }

# r = requests.get('https://api.github.com/user', data=payload, headers=headers)
# print(r.status_code)

from github import Github
import json
import sys

# using username and password
g = Github("19997270956c233ea833eb82829c531ebc001b9d")
repo = g.get_repo("Alexsaurio/Pokedex")
user = g.get_user()

# print(repo.get_pull(3).edit(state="open"))

# pulls = repo.get_pulls(state="closed")

# for pull in pulls:
#         print(pull.title)
# print(json.dumps(repo.__dict__))
# branches = repo.get_branches()

# # head = repo.get_branch('master').commit
# # print(head.commit.sha)  
# # print(head.sha)  

# # for br in branches:
# #     print(br.name)
# #     commits = repo.get_commits(br.name)
# #     for cm in commits:
#         # print(cm.sha)

# # branch = g.get_repo("Alexsaurio/Pokedex").get_commits("master")
# # print(branch.totalCount)

# pulls = repo.get_pulls()
# test = repo.get_pull(1)
# .merge(commit_title="Este es una prueba de un titulo",commit_message="esto es la prueba de un mensaje"))
# # print(test.edit(state="open"))

#                         # pr
try:
        pr = repo.create_pull(title="Usando libreria pygithub",body="test tes test test", head="test", base="master")
        print(pr.number)
except Exception:
        e = sys.exc_info()[1]
        print(e.args[1],e.args[0])
# except:
#         print("viendo errores")
# # print(test.merge(commit_title="Este es una prueba de un titulo",commit_message="esto es la prueba de un mensaje"))
# print(test.is_merged(), test.title)

# pull = repo.get_pulls()

# for pull in pulls:
#     print(pull.number, pull.state, pull.is_merged())

# PullRequestMergeStatus(sha="b0f308487f611451b74b6a4f42903fb474955342", merged=True)
# github.GithubException.GithubException: 405 {"message": "Pull Request is not mergeable", "documentation_url": "https://docs.github.com/rest/reference/pulls#merge-a-pull-request"}
"""
{
        "title":"Usando libreria pygithub",
        "body":"test",
        "head":"test",
        "base":"master"
}
"""

