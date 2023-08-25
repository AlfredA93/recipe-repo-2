# Testing
## Manual Testing


## Validation
All code is written by myself, excluding the injected code from DjangoQuill, AllAuth, Bootstrap and Django Framesworks and Libraries. For more detailed look at which code was written by myself, see this GitHub repository as this was all written by me, all page source material may have injected pieces of code, specifically from Django-Quill on all forms pages.

### PEP8 Compliant

### HTML W3C Validator

**2 Errors on all Django-Quill forms which appear on the Admin Add Recipe Page, the Front-End User Add Recipe page and the Front-End User Edit Recipe Page **
- Problem: Forms provided by Django Quill fail HTML W3C Validation for having a `for` attribute of a `hidden` input type. 
![Bug 2](/static/readme-img/bug-2.webp)

- ***Fix*** - No fix required. I spent a full mentor call and many hours before/after trying to fix this issue however it is still present. I spoke with both my cohort lead, peers within the CodeInstitute community and to the tutor team at Code Institute for support on this matter and they all advised me that this is a common issue and should be noted within the README but not necessary to take action over. This is something which I will continue to look at if and when future development of this website happens; as I continue to learn more and increase my skills as a developer I hope that I can overcome these bugs.

### Jigsaw CSS Validator

### Lighthouse Validation

## Bugs

**Bug 1**
- Problem: When entering a recipe title with characters outside of alphanumeric, hyphens and underscores, an error occured when the slug field tried to be pre-populated. This appeared when the form creation for users to add recipes, as the form needed extra validation.

![Bug 1](/static/readme-img/bug-1.webp)
![Bug 1.2](/static/readme-img/bug-1-2.webp)

- *Solution:* Adding Regex Validation to the Model field, along with adding an `if` statement to the `AddRecipe` view. [This](https://stackoverflow.com/questions/17165147/how-can-i-make-a-django-form-field-contain-only-alphanumeric-characters) webpage helped explain this further, more helpsheets regarding Regex Expression are linked in the Credits Section

**Bug 2**
- Problem: Images not saving when added via the user form in add_recipe.html
- *Fix:* add `enctype='multipart/form-data'` to the form tags

## Unfixed Bugs
- As in HTML W3C Validator

 # Mistakes

 During the setup of this project, I changed my Model Design from having separate Ingredients and Recipe Models respectively to including the Ingredients Model within the Recipe Model. During the conversion of this I made a mistake where I didn't delete the recipes before removing the Model which caused an error. During my investigation and attempts to recover the database from the error messages, I created deeper errors which I didn't understand fully. At this point, I decided to create a whole new repository and project and start again. 
 
![Mistake](/static/readme-img/mistake.webp)

 The abandoned project is [this repository](https://github.com/AlfredA93/recipe-repo). I copied the code bit by bit (not literal bits I should add), across this current repository (where you're reading this now), so you may see similarities with the foundation code of this project from the original abandoned repository.

 My mentor Alex later told me that there was a solution to it, which was good to know; although I was already well into the new repository at that point.

 ![Mistake fix](/static/readme-img/mistake-fix.webp)
