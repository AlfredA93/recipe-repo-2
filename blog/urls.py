""" Libraries """
from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
    path('bookmark/<slug:slug>/', views.RecipeBookmark.as_view(),
         name='recipe_bookmark'),
    ]
