from django.contrib import admin
from .models import Recipe, Comment

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    "Recipe Admin fields and filtering"
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'season', 'published_on')
    list_display = ('title', 'status', 'season', 'published_on')
    search_fields = ['title', 'instructions', 'tags']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    "Comment Admin fields and filtering"
    list_filter = ['published']
    list_display = ('user', 'recipe', 'content', 'published')
    search_fields = ['recipe', 'content']
