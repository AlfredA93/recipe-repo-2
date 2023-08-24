![Recipe Repo Logo](static/images/logo1.webp)


# Introduction

Recipe Repo is a website designed for user's to share their love for cooking and baking. You can see the live website [insert link here]()

# Design


## Agile Strategy

### Project Goals

### User Stories 

| Title | Number | Definition | Completed? | Label |
|-------|--------|------------|------------|-------|
| USER STORY: Create Landing Page | [#1](https://github.com/AlfredA93/recipe-repo-2/issues/1) | As a new site visitor I can easily identify website's aim so that decide whether to can stay or go | [x] | Must Have |
| USER STORY: Sign Up Form | [#2](https://github.com/AlfredA93/recipe-repo-2/issues/2) | As a new site visitor I can simply sign up to the website so that I can interact with the content | [x] | Must Have |
| USER STORY: Paginate Recipes | [#3](https://github.com/AlfredA93/recipe-repo-2/issues/3) | As a new site visitor I can clearly see paginated content so that I can click on the content I want | [x] | Must Have |
| USER STORY: Add bookmark functionality | [#4](https://github.com/AlfredA93/recipe-repo-2/issues/4) | As a authorised site visitor I can bookmark recipes so that I can view them in the future | [x] | Must Have |
| USER STORY: Add comment functionality | [#5](https://github.com/AlfredA93/recipe-repo-2/issues/5) | As an authorised site visitor I can comment on recipes so that I can interact with the community | [x] | Must Have |
| USER STORY: Add like functionality | [#6](https://github.com/AlfredA93/recipe-repo-2/issues/6) | As an authorised site visitor I can like recipes so that the author knows this is a recipe I like | [x] | Must Have |
| USER STORY: Manage Recipe Posts | [#7](https://github.com/AlfredA93/recipe-repo-2/issues/7) | As an admin I can create, read, edit/update and delete recipes so that I can manage my content | [x] | Must Have |
| USER STORY: Add tags to recipes | [#8](https://github.com/AlfredA93/recipe-repo-2/issues/8) | As a site user I can see tags on recipes so that I can associate the recipes with a category or theme | [x] | Could Have |
| USER STORY: View Likes | [#9](https://github.com/AlfredA93/recipe-repo-2/issues/9) | As an admin/site user I can see likes so that I can see how popular a recipe is  | [x] | Must Have |
| USER STORY: View Comments | [#10](https://github.com/AlfredA93/recipe-repo-2/issues/10) | As an admin/site user I can read comments so that I can see what the community thinks about recipes | [x] | Must Have |
| USER STORY: Season Pages | [#11](https://github.com/AlfredA93/recipe-repo-2/issues/11) | As a user I can click on different pages in the navigation so that I can see the recipes organised by season | [x] | Could Have |
| USER STORY: Recipe Detailed Page | [#12](https://github.com/AlfredA93/recipe-repo-2/issues/12) | As a user I can click on the recipe card to open a detailed page of the recipe so that I can see the full recipe | [x] | Must Have |
| USER STORY: View Tags and Search via Tag | [#13](https://github.com/AlfredA93/recipe-repo-2/issues/13) | As a user I can see and click on a tag/hashtag so that see similar recipes with the same tag | [x] | Could Have |
| USER STORY: Edit and Delete Comments | [#14](https://github.com/AlfredA93/recipe-repo-2/issues/14) | As a user I can edit or delete my comments so that I can update my comments if I need to | [x] | Must Have |
| USER STORY: Bookmarks Page | [#15](https://github.com/AlfredA93/recipe-repo-2/issues/15) | As a user with an account I can see a page where my bookmarks are stored so that I can easily find the recipes I save | [x] | Must Have |
| USER STORY: User Dropdown Nav Menu | [#16](https://github.com/AlfredA93/recipe-repo-2/issues/16) | As a user I can click on my name in the navbar so that access recipes related to my user data | [x] | Should Have |
| USER STORY: Add a user recipe | [#17](https://github.com/AlfredA93/recipe-repo-2/issues/17) | As a user I can create a recipe to submit on the website so that I can share my recipes with the community | [x] | Should Have |
| USER STORY: Edit/Delete User Recipe | [#18](https://github.com/AlfredA93/recipe-repo-2/issues/18) | As a user I can edit or delete recipes that I have created so that I can correct any errors or remove recipes I don't want anymore | [x] | Should Have |

### Scope

### Structure


### Wireframes
# Features

# Testing

## Manual Testing
Please see [TESTING](TESTING.md) page for all manual testing, this is extensively screenshotted and shown.

## Validation

### PEP8 Compliant

### HTML W3C Validator

### Jigsaw CSS Validator

### Lighthouse Validation

## Bugs

**Bug 1**
- Problem: When entering a recipe title with characters outside of alphanumeric, hyphens and underscores, an error occured when the slug field tried to be pre-populated. This appeared when the form creation for users to add recipes, as the form needed extra validation.
- *Solution:* Adding Regex Validation to the Model field, along with adding an `if` statement to the `AddRecipe` view. [This](https://stackoverflow.com/questions/17165147/how-can-i-make-a-django-form-field-contain-only-alphanumeric-characters) webpage helped explain this further, more helpsheets regarding Regex Expression are linked in the Credits Section

**Bug 2**
- Problem: Forms provided by Django Quill fail HTML W3C Validation for having an `for` attribute of a `hidden` input type. 
  - *Solution part 1:* Find the corresponding code within the [Django-Quill Repository](https://github.com/LeeHanYeong/django-quill-editor/blob/master/django_quill/templates/django_quill/widget.html) which is causing the error and change the input from `hidden` to `text`. Then in custom css, target the id's and mark the `visibility: hidden` so that this now passes HTML W3C Validation.
  - *Soultion part 2:* add `auto_id=True` to the form within the corresponding view, as shown in [this](https://docs.djangoproject.com/en/4.2/ref/forms/fields/#django.forms.Field.label) Django documentation link

**Bug 3**
- Problem: Images not saving when added via the user form in add_recipe.html
- *Fix:* add `enctype='multipart/form-data'` to the form tags

## Unfixed Bugs
- None

 # Mistakes

 During the setup of this project, I changed my Model Design from having separate Ingredients and Recipe Models respectively to including the Ingredients Model within the Recipe Model. During the conversion of this I made a mistake where I didn't delete the recipes before removing the Model which caused an error. During my investigation and attempts to recover the database from the error messages, I created deeper errors which I didn't understand fully. At this point, I decided to create a whole new repository and project and start again. 
 
 The abandoned project is [this repository](https://github.com/AlfredA93/recipe-repo). I copied the code bit by bit (not literal bits I should add), across this current repository (where you're reading this now), so you may see similarities with the foundation code of this project from the original abandoned repository.

 # Deployment

 # Libraries Used and Why?
- Django Quill Editor
  - This allows the user to create text in a much more flexible format, they can choose to add bold, emphasis and other types of text formatting to display their text in the desired way.
- AllAuth
  - This Library allows for easy integration of accounts and account validation into the website.
- Django
  - This framework helps to easily create a full-stack project and has a lot of supportive documentation which helps greatly with implementation.
- Bootstrap
  - This framework allows for easy and quick element styling.
- Django Taggit
  - This allows users to create tags for posts, in this case, recipes, which can then be searched/queried.
- Cloudinary
  - Media storage
- WhiteNoise
  - Static files management

 # Credits
Many thanks to both Code Institute and my mentor Alex K, I learnt a lot throughout this project and understand that this is just the tip of the iceberg. I used Stack Overflow a lot in this project to help understand some of the errors I was making, along with discovering whether certain ideas were possible.
 ## Code

 - [Nav Bar Styling](https://stackoverflow.com/questions/39639264/django-highlight-current-page-in-navbar) - Using template tags to implement the active bootstrap class.
 - [Saving form images to DB field](https://stackoverflow.com/questions/29171077/imagefield-not-saving-images-in-modelform-django-python) - Add 
`enctype='multipart/form-data'` to the form attributes
- [Accessing user whilst in ListView](https://stackoverflow.com/questions/33809345/how-to-access-current-user-in-django-class-based-view) - how to access a queryset within a class-based view - `ListView`
- [Regex Validation Expression](https://stackoverflow.com/questions/13283470/regex-for-allowing-alphanumeric-and-space) - This expression was used to help validate the title field in the `RecipeModel` in Models.py file, to make for easy pre-population of the slug field - `regex=r'^[\w\-\s]+$',`
- [If Queryset Empty](https://stackoverflow.com/questions/1387727/checking-for-empty-queryset-in-django) - used in search.html if statement
- [Django Taggit Tutorial](https://dev.to/thepylot/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704) - This tutorial helped me to set up Django Taggit for Models and the tag search feature
- [Responsive Squares](https://stackoverflow.com/questions/20456694/grid-of-responsive-squares) - This link helped me keep a 1:1 aspect ratio for the Recipe Cards
- [Non-Case Sensitive Search](https://stackoverflow.com/questions/12132368/django-queryset-contains-case-sensitive) - This link helped me find the correct syntax for searching without case sensitivity
- [HTTP Referrer](https://stackoverflow.com/questions/4406377/django-request-to-find-previous-referrer) - Alex my mentor helped me find out the code needed to request the site referrer. This was used in views.py RecipeBookmark so that a user can bookmark a page and it would just reload the current page instead of directing to a set url


 ## Helpsheets, Documentation and Useful Resources
- [Bootstrap Documentation](https://getbootstrap.com/docs)
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Quill Editor Documentation](https://pypi.org/project/django-quill-editor/)
- [Further Django Quill Editor Docs](https://django-quill-editor.readthedocs.io/en/latest/pages/using-in-admin.html)
- [Django Taggit Documentation](https://django-taggit.readthedocs.io/en/latest/)
- [Django AllAuth Documenation](https://django-allauth.readthedocs.io/en/latest/)
- [WhiteNoise Documenation](https://whitenoise.readthedocs.io/en/latest/index.html)
- [Regex Documentation](https://docs.python.org/3/library/re.html)
- [UpdateView & DeleteView Django Documentation](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/)
- [Styling Forms](https://stackoverflow.com/questions/61860145/django-adding-custom-css-in-updateview) with attribute `widgets`
- [Codemy YouTube Channel](https://www.youtube.com/c/Codemycom) - This channel helped me understand many aspects of Django, as follows: 
  - [Form Styling](https://www.youtube.com/watch?v=CVEKe39VFu8&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=7)
  - [Edit and Delete A Model Field](https://www.youtube.com/watch?v=jCM-m_3Ysqk)
  - [Search Bar](https://www.youtube.com/watch?v=AGtae4L5BbI)
- [Regex Explained YouTube Video](https://www.youtube.com/watch?v=FY9W3MN8jBQ)
- [Editing a success url](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown) - This webpage helped me understand `get_success_url`
- [Add & Delete Comments in Django YouTube Video](https://www.youtube.com/watch?v=MmLRE2fCcec)
- [Attributes of TextArea](https://www.w3docs.com/snippets/html/how-to-set-the-size-of-the-textarea-element.html) in forms
- Text within the headings of the Seasons Pages was found at [RHS](rhs.org.uk) and [Squires Garden Centre](https://www.squiresgardencentres.co.uk/)
 ## Technology
 - [Tiny-img](https://tiny-img.com/webp/) - webp image convertion
 - [Canva](canva.com) - Logo design
 - [Pixelcut Image Upscaler](https://create.pixelcut.ai/upscaler) - Logo upscaler
 - [Background Remover](https://www.remove.bg/) - Logo white background remover
 - [Favicon Creator](https://formito.com/tools/favicon) - Favicon Icon
 - [Colour Palettes](https://mycolor.space/?hex=%23E9ECEF&sub=1) - UX Design
 - [Dopely Colors](https://colors.dopely.top/inside-colors/40-elegant-color-palettes-with-their-gradients/) - UX Design
 - [Django Key Generator](https://djecrety.ir/)

 ## Media
 - All pictures were sourced from [Unsplash](https://unsplash.com/) under their free license.