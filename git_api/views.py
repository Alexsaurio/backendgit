from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from utils.formatter import *
from git_api.models import *
from git_api.serializers import *


#libreria pygithub
from github import Github

@api_view(['GET'])
def getUserData(request):
    """ Obtener las repositorios de un usuario """
    return Response(getUser())

@api_view(['GET'])
def getUserRepos(request):
    """ Obtener las repositorios de un usuario """
    g = Github(gittk)
    repo = g.get_user().get_repos().totalCount
    cont = { "total" : repo}
    return Response(cont)

@api_view(['GET'])
def getRepoBranches(request):
    """ Obtener las branches de un repositorio de usuario estaticos """
    return Response(getBranches())

@api_view(['GET'])
def getBranchCommits(request, branch):
    """ obtener los commits de una branch """
    return Response(getCommits(branch))
    # return Response(getCommitDetail("fc6c40f23783e1abde54b439651e13da212d9f09"));

@api_view(['GET'])
def getComparateTwoBranches(request,base,compare):
    """ Comparar dos branches """
    return Response(getComparate(base,compare))
    
@api_view(['GET'])
def getPullRequestRepo(request):
    """ Recuperar los pull request de un guardados"""
    queryset = PullRequest.objects.all()
    serializer= PullRequestSerializer(queryset, many=True)
    return Response(serializer.data)
    # return Response(getPullRequest()) obtener pr del repo


@api_view(['GET'])
def setChangeStatePullRequest(request, number_pr):
    """ Cambiar el estado de un pull request """
    return Response(setChangeStatePR(number_pr))

@api_view(['POST'])
def createPullRequestRepo(request):
    """ hace una peticion para un pull request  """
    return Response(createPullRequest(request.data))

@api_view(['POST'])
def createMergePullRequestRepo(request):
    """ hace una peticion para un pull request merge """
    return Response(createMergePullRequest(request.data))

