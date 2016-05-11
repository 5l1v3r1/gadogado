from __future__ import unicode_literals

from django.db import models

class Genre(models.Model):
    title = models.CharField(u'Title', max_length=100)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(u'Title', max_length=200)
    genre = models.ForeignKey(Genre, verbose_name=u'Genre')
    score = models.IntegerField(u'Score')

    def __str__(self):
        return self.title
