""" 
    funciones para optener la informacion de los repos
    mediante la libreria pygithub
"""
from utils.authtoken import *
from github import Github
from git_api.serializers import *
from git_api.models import *
import sys
import json

def getFilesCommit(commit):
    # funcion para iterar los files obtenidos del commit
    files_list = []
    for f in commit.files:
        files_list.append({
            "filename": f.filename,
            "changes": f.changes
        })
    return files_list

def getDataUser(user):
    """ 
        funcion para formatear datos del usuario 
        apartir de un objeto user regresado por la libreria
    """
    return {
        "author" : user.login,
        "name" : user.name,
        "avatar_url" : user.avatar_url,
        "email" : user.email,
        "bio" : user.bio
    }

def getRepoAuth():
    """ obtener el repositorio auntentificando con el token """
    g = Github(gittk)
    repo = g.get_repo(gitrepo)
    return repo

def getUser():
    """ regresa los datos del usuario del token"""
    g = Github(gittk)
    user = g.get_user()
    return getDataUser(user)

def getBranches():
    """  Obtener las branches del repositorio obtenido  """
    repo = getRepoAuth()
    branches = repo.get_branches()
    branches_list = []
    for branch in branches:
        branches_list.append(branch.name)
    return {"branches": branches_list}

def getCommitDetail(sha):
    """ Obtiene los detalles del commmit seleccionado mediante el sha"""
    repo = getRepoAuth()
    commit = repo.get_commit(sha=sha)

    return {
        "autor": getDataUser(commit.author),
        "message": commit.commit.message,
        "comments": commit.comments_url,
        "timestamp": commit.commit.last_modified,
        "sha": commit.commit.sha,
        "files": getFilesCommit(commit)
        }

def getCommits(branch):
    """ Obtiene todos los commits de la branch seleccionada """
    repo = getRepoAuth()
    commits = repo.get_commits(branch)
    commits_list = []
    for commit in commits:
        commits_list.append(getCommitDetail(commit.sha))
    return {"commits" : commits_list }

def getComparate(base,compare):
    """ comparar dos branches mediante su sha del commit de la cabecera """
    repo = getRepoAuth()
    headCommitBase = repo.get_branch(base).commit
    headCommitCompare = repo.get_branch(compare).commit

    return {
        "result":[
            {
                "branch": base,
                "detail": getCommitDetail(headCommitBase.sha)
            },
            {
                "branch": compare,
                "detail": getCommitDetail(headCommitCompare.sha)
                
            }
        ]
    }

def getPullRequest():
    """ Obtiene los pull request del repositorio estatico """
    repo = getRepoAuth()
    prs = repo.get_pulls()
    prs_list = []
    for pr in prs:
        prs_list.append(
            {
                "id" : pr.id,
                "number" : pr.number,
                "title" : pr.title,
                "state" : pr.state,
                "is_merged": pr.is_merged(),
                "autor" : getDataUser(pr.user),
                "created_at" : pr.created_at,
                "issue_url": pr.issue_url,
                "body": pr.body
            }
        )
    prs_closed = repo.get_pulls(state="closed")
    for pr in prs_closed:
        prs_list.append(
            {
                "id" : pr.id,
                "number" : pr.number,
                "title" : pr.title,
                "state" : pr.state,
                "is_merged": pr.is_merged(),
                "autor" : getDataUser(pr.user),
                "created_at" : pr.created_at,
                "issue_url": pr.issue_url,
                "body": pr.body
            }
        )
    return {
        "prs" : prs_list
        }

def setChangeStatePR(number_pr):
    """ cambia el estado a cerrado de una pull request en github y en la bd"""
    repo = getRepoAuth()

    try:
        # cambio de estado en github
        repo.get_pull(int(number_pr)).edit(state="closed")
        # cambio de estado en la bd
        pullrequest = PullRequest.objects.get(number=number_pr)
        pullrequest.status = "closed"
        pullrequest.save()
        return { 
            "message": "Se ha cambiado correctamente el estado.",
            "code": 200
            }

    except Exception:
        try:
            e = sys.exc_info()[1]
            return {
                "message": e.args[1],
                "code": e.args[0]
                }
        except:
            return {
                "message": "¡Ups!... ocurrio un erro desconocido.",
                "code": 404
            }

def createPullRequest(request_data):
    """ crea un pull resquest con los datos seleccionados """
    try:
        repo = getRepoAuth()
        user = getUser()
        # crear en github
        pr = repo.create_pull(
            title = request_data['title'],
            body = request_data['body'], 
            base = request_data['base'],
            head = request_data['compare']
        )
        # guardar en la bd
        pullrequest = PullRequest(
                author = user['author'],
                avatar_url = user['avatar_url'],
                title = request_data['title'],
                description = request_data['body'], 
                base = request_data['base'],
                head = request_data['compare'],
                merged = False,
                status = "open",
                number = str(pr.number)
                )
        pullrequest.save()
        return {
            "message": "Se creo correctamente la pullrequest.",
            "code": 200
            }
    except Exception:
        try:           
            e = sys.exc_info()[1]
            return {
                "message": e.args[1],
                "code": e.args[0]
                }
        except:
            return {
                "message": "¡Ups!... ocurrio un error desconocido.",
                "code": 404
            }

def createMergePullRequest(request_data):
    """ crea un pull resquest y hacer un merge con los datos seleccionados """
    try:
        repo = getRepoAuth()
        user = getUser()
        # crear en github pull request
        pr = repo.create_pull(
            title = request_data['title'],
            body = request_data['body'], 
            base = request_data['base'],
            head = request_data['compare']
        )
        # crear merge en githuv
        repo.get_pull(pr.number).merge(commit_title=request_data['title'],commit_message=request_data['body'])

        # almacenar en la bd
        pullrequest = PullRequest(
                author = user['author'],
                avatar_url = user['avatar_url'],
                title = request_data['title'],
                description = request_data['body'], 
                base = request_data['base'],
                head = request_data['compare'],
                merged = True,
                status = "closed",
                number = str(pr.number)
                )
        pullrequest.save()
        return {
            "message": "Se creo correctamente el merge.",
            "code": 200
            }
    except Exception:
        try:           
            e = sys.exc_info()[1]
            return {
                "message": e.args[1],
                "code": e.args[0]
                }
        except:
            return {
                "message": "¡Ups!... ocurrio un error desconocido.",
                "code": 404
            }