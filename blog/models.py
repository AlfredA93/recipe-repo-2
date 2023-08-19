"""Database Models for Recipe and Comments on the website"""
from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager

STATUS = ((0, "Draft"), (1, "Published"))
SEASON = ((0, "All"), (1, "Spring"), (2, "Summer"),
          (3, "Autumn"), (4, "Winter"))


class Recipe(models.Model):
    """Recipe Database Model"""
    # Credit - alphanumeric, see README Credits.

    title = models.SlugField(max_length=140, unique=True, allow_unicode=True)
    slug = models.SlugField(max_length=140, unique=True, allow_unicode=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe_post')
    status = models.IntegerField(choices=STATUS, default=0)
    image = CloudinaryField('image', default='default')
    image_alt = models.CharField(max_length=140)
    season = models.IntegerField(choices=SEASON, default=0)
    summary = models.TextField(max_length=240)
    ingredients = QuillField()
    instructions = QuillField()
    tags = TaggableManager()
    published_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='recipe_like', blank=True)
    bookmarks = models.ManyToManyField(
        User, related_name='recipe_bookmark', blank=True)

    class Meta:
        """Organise recipes posts by published in desc order"""
        ordering = ['-published_on']

    def __str__(self):
        return str(self.title)

    def number_of_likes(self):
        "Count number of likes per post"
        return self.likes.count()

    def number_of_bookmarks(self):
        "Count number of bookmarks per post"
        return self.bookmarks.count()


class Comment(models.Model):
    """Comments Database Model"""
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    published = models.DateField(auto_now_add=True)

    class Meta:
        """Order by published in desc order"""
        ordering = ['-published']

    def __str__(self):
        return f"Comment {self.content} by {self.user}"
