""" Libraries """
from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
    path('bookmark/<slug:slug>/', views.RecipeBookmark.as_view(),
         name='recipe_bookmark'),
    path('edit_comment/<pk>/', views.EditComment.as_view(),
         name='edit_comment'),
    path('delete_comment/<pk>/', views.DeleteComment.as_view(),
         name='delete_comment'),
    ]
