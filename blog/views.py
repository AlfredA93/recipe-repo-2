""" Libraries """
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe
from .forms import CommentForm


class RecipeList(generic.ListView):
    "Recipe List View for homepage"
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-likes')
    template_name = 'index.html'
    paginate_by = 9

class RecipeDetail(View):
    "Full Recipe View, Single Recipe per page"
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1, slug=slug)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('published')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )
