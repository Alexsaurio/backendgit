from django.db import models

# Seccion para los modelos

class PullRequest(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    base =  models.CharField(max_length=50, default="")
    head =  models.CharField(max_length=50, default="")
    avatar_url = models.CharField(max_length=200, default="https://cdn4.iconfinder.com/data/icons/avatars-xmas-giveaway/128/batman_hero_avatar_comics-512.png")
    merged = models.BooleanField(default=False)
