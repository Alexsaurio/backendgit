# from django_framework import serializers
from rest_framework import serializers
from git_api.models import *

class PullRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PullRequest
        fields = '__all__'
