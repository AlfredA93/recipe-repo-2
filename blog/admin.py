"""Admin page to display data as registered in this file"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    "Recipe Admin fields and filtering"
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'season', 'author', 'published_on')
    list_display = ('title', 'author', 'status', 'season', 'published_on')
    summernote_fields = ('zutaten', 'directions')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    "Comment Admin fields and filtering"
    list_filter = ['published', 'user', 'recipe']
    list_display = ('user', 'recipe', 'content', 'published')
