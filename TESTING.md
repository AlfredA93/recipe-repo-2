# Testing
## Manual Testing



## Validation
All code is written by myself, excluding the injected code from DjangoQuill, AllAuth, Bootstrap and Django Framesworks and Libraries. For more detailed look at which code was written by myself, see this GitHub repository as this was all written by me, all page source material may have injected pieces of code, specifically from Django-Quill on all forms pages and recipe detailed pages.

### PEP8 Compliant

All custom Python code is valid and complient to PEP8 standards as per [CI Python Linter](https://pep8ci.herokuapp.com/)

### HTML W3C Validator

All custom written HTML code is valid.

![HTML Valid](/documentation/readme-img/html-valid.webp)

![Bug 2](/static/readme-img/bug-2.webp)

**The 2 Errors listed above appear on front-end pages - Add A Recipe, Edit Recipe and under Admin panel - Add Recipe. This error comes directly from the Django-Quill injected code - this is further explained in the fix attempts section below**

- **Problem**: Forms provided by Django Quill fail HTML W3C Validation for having a `for` attribute of a `hidden` input type. 

- ***Fix Attempts*** - No fix required. I spent a full mentor call and many hours before/after trying to fix this issue however it is still present. I spoke with both my cohort lead, peers within the CodeInstitute community and to the tutor team at Code Institute for support on this matter and they all advised me that this is a common issue and should be noted within the README but not necessary to take action over. This is something which I will continue to look at if and when future development of this website happens; as I continue to learn more and increase my skills as a developer I hope that I can overcome these bugs.

- **Problem**: 2 Errors on injected html from QuillField within Recipe Model on Recipe Detail pages.
- ***Fix***: No fix required. As mentioned above in the previous error, tutors, my mentor and support team at CodeInstitute advised me that this a common occurance. I have detailed the errors that are here in the images below, which highlight a potential overuse of the <p> element when looking at things with semantic markup. For further clarity errors pictured below occured on [this webpage](https://recipe-repo-2-e23f0ecfdc52.herokuapp.com/Scrambled-Eggs/) which is for all recipe detailed views.

![Recipe Detail HTML Errors](/documentation/readme-img/recipe-detail-html.webp)
![Recipe Detail HTML Error in Depth](/documentation/readme-img/recipe-detail-html-depth.webp)

### Jigsaw CSS Validator

All custom CSS code is Valid
![CSS Valid](/documentation/readme-img/css-valid.webp)

### Lighthouse Validation

Lighthouse marked this site with a 90 on Performance, 95 on Accessibility and 100 on Best Practices
![Lighthouse](/documentation/readme-img/lighthouse.webp)

## Bugs

**Bug 1**
- Problem: When entering a recipe title with characters outside of alphanumeric, hyphens and underscores, an error occured when the slug field tried to be pre-populated. This appeared when the form creation for users to add recipes, as the form needed extra validation.

![Bug 1](/documentation/readme-img/bug-1.webp)
![Bug 1.2](/documentation/readme-img/bug-1-2.webp)

- *Solution:* Adding Regex Validation to the Model field, along with adding an `if` statement to the `AddRecipe` view. [This](https://stackoverflow.com/questions/17165147/how-can-i-make-a-django-form-field-contain-only-alphanumeric-characters) webpage helped explain this further, more helpsheets regarding Regex Expression are linked in the Credits Section

**Bug 2**
- Problem: Images not saving when added via the user form in add_recipe.html
- *Fix:* add `enctype='multipart/form-data'` to the form tags

## Unfixed Bugs
- As above in ***HTML W3C Validator*** section

 # Mistakes

 During the setup of this project, I changed my Model Design from having separate Ingredients and Recipe Models respectively to including the Ingredients Model within the Recipe Model. During the conversion of this I made a mistake where I didn't delete the recipes before removing the Model which caused an error. During my investigation and attempts to recover the database from the error messages, I created deeper errors which I didn't understand fully. At this point, I decided to create a whole new repository and project and start again. 
 
![Mistake](/documentation/readme-img/mistake.webp)

 The abandoned project is [this repository](https://github.com/AlfredA93/recipe-repo). I copied the code bit by bit (not literal bits I should add), across this current repository (where you're reading this now), so you may see similarities with the foundation code of this project from the original abandoned repository.

 My mentor Alex later told me that there was a solution to it, which was good to know; although I was already well into the new repository at that point.

 ![Mistake fix](/documentation/readme-img/mistake-fix.webp)
