"""git_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from git_api import views

urlpatterns = [
    path('user/', views.getUserData),
    path('user/repos/', views.getUserRepos),
    path('user/repos/branches/', views.getRepoBranches),
    path('user/repos/pullrequest/', views.getPullRequestRepo),
    path('user/repos/pullrequest/changestate/<number_pr>', views.setChangeStatePullRequest),
    path('user/repos/pullrequest/create', views.createPullRequestRepo),
    path('user/repos/pullrequest/create/merge', views.createMergePullRequestRepo),
    path('user/repos/branch/commits/<branch>', views.getBranchCommits),
    path('user/repos/branch/compare/<base>/<compare>', views.getComparateTwoBranches),
    
]
