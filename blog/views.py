""" Libraries """
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView, FormView

from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm


class RecipeList(generic.ListView):
    "Recipe List View for homepage"
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-likes')
    template_name = 'index.html'
    paginate_by = 9
    ordering = ['published_on']


class RecipeDetail(View):
    "Full Recipe View, Single Recipe per page"
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1, slug=slug)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('published')
        liked = False
        bookmarked = False

        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        if recipe.bookmarks.filter(id=self.request.user.id).exists():
            bookmarked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "bookmarked": bookmarked,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Recipe.objects.filter(status=1, slug=slug)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('published')
        liked = False
        bookmarked = False

        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        if recipe.bookmarks.filter(id=self.request.user.id).exists():
            bookmarked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "bookmarked": bookmarked,
                "comment_form": CommentForm(),
            },
        )


class RecipeLike(View):
    "Add a like to a recipe"

    def post(self, request, slug):
        "Find recipe and toggle liked status"
        recipe = get_object_or_404(Recipe, slug=slug)
        origin = request.META.get("HTTP_REFERER")

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        return redirect(origin)


class RecipeBookmark(View):
    "Bookmark"
    def post(self, request, slug):
        "Post bookmark"
        recipe = get_object_or_404(Recipe, slug=slug)
        origin = request.META.get("HTTP_REFERER")

        if recipe.bookmarks.filter(id=request.user.id).exists():
            recipe.bookmarks.remove(request.user)
        else:
            recipe.bookmarks.add(request.user)
        return redirect(origin)


class EditComment(UpdateView):
    "edit comment field"
    model = Comment
    form_class = CommentForm
    template_name = "edit_comment.html"

    def get_success_url(self):
        recipe = self.object.recipe
        recipe_slug = recipe.slug
        return reverse('recipe_detail', kwargs={"slug": recipe_slug})


class DeleteComment(DeleteView):
    "Delete Comment"
    model = Comment
    template_name = "delete_comment.html"

    def get_success_url(self):
        recipe = self.object.recipe
        recipe_slug = recipe.slug
        return reverse('recipe_detail', kwargs={"slug": recipe_slug})


class BookmarkList(generic.ListView):
    "Recipe List View for homepage"
    model = Recipe
    queryset = Recipe.objects.filter(status=1)
    template_name = 'bookmarks.html'
    paginate_by = 10
    ordering = ['published_on']


class AddRecipe(View):
    "Add Recipe Form"
    def get(self, request):
        """Get Form"""

        return render(
            request,
            "add_recipe.html",
            {'form': RecipeForm()}
        )

    def post(self, request, *args, **kwargs):

        add_recipe = RecipeForm(data=request.POST)

        if add_recipe.is_valid():
            add_recipe.instance.author = request.user
            add_recipe.instance.slug = add_recipe.instance.title.replace(" ", "-")
            add_recipe.save()
        else:
            add_recipe = RecipeForm()

        return render(
            request,
            "index.html",
            {},
        )

class MyRecipeList(generic.ListView):
    "Recipe List View for my recipes"
    model = Recipe
    queryset = Recipe.objects
    template_name = 'my_recipes.html'
    paginate_by = 10
    ordering = ['status']
