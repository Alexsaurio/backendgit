# Generated by Django 3.1.7 on 2021-03-04 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('git_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pullrequest',
            name='base',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='pullrequest',
            name='head',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='pullrequest',
            name='merged',
            field=models.BooleanField(default=False),
        ),
    ]
