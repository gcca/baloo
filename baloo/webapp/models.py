from django.db import models


class Profile(models.Model):
    type = models.CharField(max_length=32, default='user')


class Post(models.Model):

    TYPE_CHOICES = (
        (0, 'Post'),
        (1, 'Question'),
        (2, 'Answer'),
        (3, 'Comment'))

    title = models.CharField(max_length=128, default='')
    body = models.TextField(max_length=8194, default='')
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    parent = models.ForeignKey('Post', null=True)
    type = models.IntegerField(default=0, choices=TYPE_CHOICES)
    profile = models.ForeignKey(Profile)

    @property
    def comments(self):
        return []


class Question(Post):

    @property
    def anwsers(self):
        return []

    class Meta:
        proxy = True


class Answer(Post):

    class Meta:
        proxy = True

