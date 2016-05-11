from django.contrib import admin

from django.contrib import messages
from django.shortcuts import render

from movies.forms import *

class MovieAdmin(admin.ModelAdmin):
    action_form = UpdateScoreForm
    list_display = ('title', 'genre','score',)
    actions = ['set_genre_action','set_score_action']

    def set_score_action(self, request, queryset):
        score = int(request.POST['score'])
        queryset.update(score=score)    
        messages.success(request, '{0} movies were updated'.format(queryset.count()))
    set_score_action.short_description = u'Update score of selected movies' 
    
    
    def set_genre_action(self, request, queryset):
        if 'do_action' in request.POST:
            form = GenreForm(request.POST)
            if form.is_valid():
                genre = form.cleaned_data['genre']
                updated = queryset.update(genre=genre)
                messages.success(request, '{0} movies were updated'.format(updated))
                return
        else:
            form = GenreForm()

        return render(request, 'movies/action_genre.html',
            {'title': u'Choose genre',
             'objects': queryset,
             'form': form})
    set_genre_action.short_description = u'Update genre of selected movies'
admin.site.register(Movie, MovieAdmin)   

  


admin.site.register(Genre)
