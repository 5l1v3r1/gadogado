from django import forms
from django.contrib.admin.helpers import ActionForm
from movies.models import *

class GenreForm(forms.Form):
    genre = forms.ModelChoiceField(queryset=Genre.objects.all())


class UpdateScoreForm(ActionForm):
    score = forms.IntegerField()    