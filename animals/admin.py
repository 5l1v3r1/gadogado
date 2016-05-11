from django.contrib import admin
from .models import Comment, Picture,Author

class PictureAdmin(admin.ModelAdmin):
    list_display_fields = ('photo', 'animal_kind', 'author', 'is_promoted', )


class AuthorAdmin(admin.ModelAdmin):
    list_display_fields = ('name', 'email', )


class CommentAdmin(admin.ModelAdmin):
    list_display_fields = ('picture', 'author', )
    

admin.site.register(Picture, PictureAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
