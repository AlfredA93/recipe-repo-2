""" Libraries """
from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('bookmarks/', views.BookmarkList.as_view(), name='bookmarks_list'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('my_recipes/', views.MyRecipeList.as_view(), name='my_recipes'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
    path('save/<slug:slug>/', views.RecipeBookmark.as_view(),
         name='recipe_bookmark'),
    path('edit_comment/<pk>/', views.EditComment.as_view(),
         name='edit_comment'),
    path('delete_comment/<pk>/', views.DeleteComment.as_view(),
         name='delete_comment'),
    ]
