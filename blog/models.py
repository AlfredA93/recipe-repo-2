"""Database Models for Recipe and Comments on the website"""
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django_quill.fields import QuillField
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager

STATUS = ((0, "Draft"), (1, "Published"))
SEASON = ((0, "All"), (1, "Spring"), (2, "Summer"),
          (3, "Autumn"), (4, "Winter"))


class Recipe(models.Model):
    """Recipe Database Model"""
    title = models.CharField(
        max_length=100,
        unique=True,
        help_text="Format: Letters, Numbers, Hyphens & Underscores only.",
        validators=[
            RegexValidator(
                regex=r'^[\w\-\s]+$',
                message='Title: Letters, Numbers, Hyphens & Underscores only.',
                code='invalid_title'
            )
        ]
    )
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe_post')
    status = models.IntegerField(
        choices=STATUS,
        default=0,
        help_text="Status: Draft or Published"
    )
    image = CloudinaryField('image', default='default',
                            help_text="Images are auto-cropped to 1:1 ratio")
    season = models.IntegerField(choices=SEASON, default=0)
    summary = models.TextField(
        max_length=200,
        help_text="Summarise your recipe in 240 Characters"
    )
    ingredients = QuillField(default="Write your ingredients here")
    instructions = QuillField(default="Write your instructions here")
    tags = TaggableManager(
        help_text="A comma-seperated list of tags. Eg. Pasta, Italian"
    )
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
