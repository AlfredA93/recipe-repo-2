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
## Bugs

## Unfixed Bugs
- None

 # Mistakes

 During the set up of this project, I changed my Model Design from having ingredients in a separate Model, to including it within the Recipe Model. During the convertion of this I made a mistake where I didn't delete a recipe before removing the field, which caused an error. During my investigation and attempts to recover the database, I created deeper errors which I didn't understand fully. At this point I created a whole new repository and project and started again. 
 
 The original project is at [this repository](https://github.com/AlfredA93/recipe-repo). I copied the code bit by bit (not literal bits I should add), across from the old repository to this new one, so you may see similarities with the foundation code of this project from the original abandoned repository.

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

 ## Code

 - [Nav Bar Styling](https://stackoverflow.com/questions/39639264/django-highlight-current-page-in-navbar) - Using template tags to implement the active bootstrap class.
 - [Saving form images to DB field](https://stackoverflow.com/questions/29171077/imagefield-not-saving-images-in-modelform-django-python) - Add 
`enctype='multipart/form-data'` to the form attributes
- [Accessing user whilst in ListView](https://stackoverflow.com/questions/33809345/how-to-access-current-user-in-django-class-based-view) - how to access a queryset within a class-based view - `ListView`
- [Regex Validation Expression](https://stackoverflow.com/questions/13283470/regex-for-allowing-alphanumeric-and-space) - This expression was used to help validate the title field in the `RecipeModel` in Models.py file, to make for easy pre-population of the slug field - `regex=r'^[\w\-\s]+$',`
- [If Queryset Empty](https://stackoverflow.com/questions/1387727/checking-for-empty-queryset-in-django) - used in search.html if statement
 ## Helpsheets, Documentation and Useful Resources
- [Bootstrap Documentation](https://getbootstrap.com/docs)
- [Django Documenation](https://docs.djangoproject.com/)
- [Django Taggit Documentation](https://django-taggit.readthedocs.io/en/latest/)
- [Django AllAuth Documenation](https://django-allauth.readthedocs.io/en/latest/)
- [WhiteNoise Documenation](https://whitenoise.readthedocs.io/en/latest/index.html)
- [Regex Documentation](https://docs.python.org/3/library/re.html)


 ## Technology
 - [Tiny-img](https://tiny-img.com/webp/) - webp image convertion
 - [Canva](canva.com) - Logo design
 - [Pixelcut Image Upscaler](https://create.pixelcut.ai/upscaler) - Logo upscaler
 - [Background Remover](https://www.remove.bg/) - Logo white background remover
 - [Favicon Creator](https://formito.com/tools/favicon) - Favicon Icon
 - [Colour Palettes](https://mycolor.space/?hex=%23E9ECEF&sub=1) - UX Design
 - 