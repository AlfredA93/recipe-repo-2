# Testing

## Manual Testing

When carrying out manual tests, I went through each of the user and admin processes for adding, editing and deleting to test if any errors can occur in the process. This would be applicable for comments and recipes especially.

The main custom validation I implemented was Regex Validation on the Title Field within my RecipeModel. This needed validation to stop URL pathway errors along with other errors when the Title Field would be automatically converted into the slug field. You can see the extent of the validation and error messages thrown in the sections below. I added if statements for more minor validation regarding search bars which is also shown in the example screenshots below. The validation for the accounts pages is built into the AllAuth library, however, this will still need testing, as I have shown below.

### Admin Panel

In the admin panel, we need to test editing comments and recipes as this is where errors can be introduced.

- Possible error - the wrong format for Title is used. This would through an error as the slug field only accepts Letters, Numbers, Hyphens and Underscores. As the slug field is automatically populated from the Title field, this is very important that we validate the title field. We did this through Regex Validation directly on the model. If a user or admin tries to use a format not accepted by the model, then this error is thrown. 
- Regex Validation directly on the Model
  - ![Regex](/documentation/readme-img/manual-tests/regex.webp)
- Error Thrown
  - ![Recipe Title Error](/documentation/readme-img/manual-tests/admin-testing.webp)

- When choosing to add a comment, the admin must choose a recipe and user to comment as, otherwise the error below is thrown.

  - ![Admin Test](/documentation/readme-img/manual-tests/admin-comment-test.webp)
  - ![Admin Test 3](/documentation/readme-img/manual-tests/admin-test3.webp)

- The image below shows the message that is thrown when a recipe is deleted successfully, the same type of message is thrown whenever a successful edit is made to comments or recipes across the admin panel.

  - ![Admin Test 2](/documentation/readme-img/manual-tests/admin-testing2.webp)

### Add/Edit Recipe

The errors that can occur within the add/edit recipe are the same as the Admin Panel Add Recipe, so we needed to add some validation within the views.py file to check whether the data entered was indeed valid, if not, then the error is thrown above and on the Edit Recipe Page this is thrown under the title.

- Views.py Code if statement
  - ![if statement](/documentation/readme-img/manual-tests/if-statement.webp)
- Errors Thrown
  - ![Recipe Test Title](/documentation/readme-img/manual-tests/add-recipe-test.webp)
- Regex Validation Error note which comes directly from RecipeModel through the generic - UpdateView.
![Title Regex Validation](/documentation/readme-img/manual-tests/title-regex-validator.webp)
- For the fields required to be filled - Title, Status, Summary and Tags, the 'Please fill out this field' validation is placed, requiring the user to add information into this field.
  - ![Fields Filled](/documentation/readme-img/manual-tests/fields-filled.webp)

### Search Bar

For the search bar, we need to check whether an empty dataset is coming back within the search query. If not, then this is what is shown.

  - ![Search bar test](/documentation/readme-img/manual-tests/searchbar-test1.webp)
  - ![Search bar test](/documentation/readme-img/manual-tests/searchbar-test2.webp)

### Account Section - Login/Signup

For the account registration and login, we need to test numerous scenarios.

- Password/User Matching
  - ![Login Test](/documentation/readme-img/manual-tests/login-test.webp)
- Email needs to be a valid email address, with an '@'
  - ![Email needing '@'](/documentation/readme-img/manual-tests/email-test.webp)
- During Registration, the passwords need to be identical
  - ![Wrong Passwords](/documentation/readme-img/manual-tests/password-retype.webp)
- Username's need to be unique
  - ![Sign Up Test](/documentation/readme-img/manual-tests/signup-test.webp)

### 404 Error Page

This is used for when a user enters an URL that isn't a valid extension from the root.

Here is the 404 Error Page -

  - ![404 Error Page](/documentation/readme-img/manual-tests/error-404-test.webp)

Originally I also included a 500 Error Page, however, I searched extensively online for how to test or generate a server handler error and couldn't find an understandable way of doing this within my current setup. So I chose to remove this feature and use the Generic Django Server Error which is pre-tested upon release instead as I wasn't able to test mine. This is an area I need to do more research on.

## Responsive Design

### The website is built and tested to be responsive to small screens to desktop computer screens. This was adjusted through Bootstrap classes and through custom css.

### Below we have screenshots of the responsive design to an iPhone SE Screen - the smallest main stream screen on the market at the moment.

![Phone 1](/documentation/readme-img/responsive/responsive-iphone-se-1.webp)
![Phone 2](/documentation/readme-img/responsive/responsive-iphone-se-2.webp)
![Phone 3](/documentation/readme-img/responsive/responsive-iphone-se-3.webp)
![Phone 4](/documentation/readme-img/responsive/responsive-iphone-se-4.webp)
![Phone 5](/documentation/readme-img/responsive/responsive-iphone-se-5.webp)

### Below is now the screen at the size of a Medium Screen iPad Air

![Tablet 1](/documentation/readme-img/responsive/responsive-tablet-1.webp)
![Tablet 2](/documentation/readme-img/responsive/responsive-tablet-2.webp)
![Tablet 3](/documentation/readme-img/responsive/responsive-tablet-3.webp)


## Validation

All code is written by myself, excluding the injected code from DjangoQuill, AllAuth, Bootstrap and Django Frameworks and Libraries. For a more detailed look at which code was written by myself, see this GitHub repository as this was all written by me, all page source material may have injected pieces of code, specifically from Django-Quill on all forms pages and recipe detailed pages.

### PEP8 Compliant

All custom Python code is valid and compliant to PEP8 standards as per [CI Python Linter](https://pep8ci.herokuapp.com/)

### HTML W3C Validator

All custom-written HTML code is valid. However a some small errors came up for code injected from Django-Quill-Editor, these are listed below.

![HTML Valid](/documentation/readme-img/html-valid.webp)


**The 2 Errors listed below appear on front-end pages - Add A Recipe, Edit Recipe and under Admin panel - Add Recipe/Recipe when in detailed view. This error comes directly from the Django-Quill injected code - this is further explained in the section below**

- **Problem**: Forms code provided by Django Quill failed HTML W3C Validation for having a `for` attribute referencing a `hidden` input type.

- **_Fix Attempts_** - No fix required. I spent a full mentor call and many hours before/after trying to fix this issue however it is still present. I looked at swapping the Quill Editor field for using Summernote, which was another python library which would keep the UX design consistent. However Summernote had markedly more HTML errors in the code than Quill (see second screenshot of summernote errors below), so I decided to stay with Quill. I spoke with my mentor, my cohort lead, peers within the CodeInstitute community and the tutor team at Code Institute for support on this matter. They all advised me that this is a common issue, that should be noted within the README but it is not necessary to take action over. This is something that I will continue to look at if and when future development of this website happens; as I continue to learn more and increase my skills as a developer I hope that I can overcome these bugs.

- Quill Errors
  - ![Quill Errors](/documentation/readme-img/bug-2.webp)

- Summernote 
  - ![Summernote Errors](/documentation/readme-img/summernote.webp)

- **Problem**: 2 Errors on injected HTML from the ingredients and instructions QuillFields within Recipe Model on Recipe Detail pages (example URL - https://recipe-repo-2-e23f0ecfdc52.herokuapp.com/Scrambled-Eggs/ ).
- **_Fix_**: No fix required. As mentioned above in the previous error, tutors, my mentor and support team at CodeInstitute advised me that this a common occurance. I have detailed the errors that are here in the images below, which highlight a potential overuse of the `<p>` element when looking at things with semantic markup. For further clarity errors pictured below occurred on [this webpage](https://recipe-repo-2-e23f0ecfdc52.herokuapp.com/Scrambled-Eggs/) which is for all recipe detailed views.

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

- Problem: When entering a recipe title with characters outside of alphanumeric, hyphens and underscores, an error occurred when the slug field tried to be pre-populated. This appeared from form creation for users to add recipes, as the form needed extra validation.

![Bug 1](/documentation/readme-img/bug-1.webp)
![Bug 1.2](/documentation/readme-img/bug-1-2.webp)

- _Solution:_ Adding Regex Validation to the Model field, along with adding an `if` statement to the `AddRecipe` view. [This](https://stackoverflow.com/questions/17165147/how-can-i-make-a-django-form-field-contain-only-alphanumeric-characters) webpage helped explain this further, more helpsheets regarding Regex Expression are linked in the Credits Section

**Bug 2**

- Problem: Images not saving when added via the user form in add_recipe.html
- _Fix:_ add `enctype='multipart/form-data'` to the form tags along with `request.FILES` to the views.py post function

## Unfixed Bugs

- No unfixed bugs, unless specified as above in ***HTML W3C Validator*** section

# Mistakes

During the setup of this project, I changed my Model Design from having separate Ingredients and Recipe Models respectively to including the Ingredients Model within the Recipe Model. During the conversion, I made a mistake where I didn't delete the recipes before removing the Model which caused an error. During my investigation and attempts to recover the database from the error messages, I created deeper errors, which I didn't understand fully. At this point, I decided to create a whole new repository and project and start again.

![Mistake](/documentation/readme-img/mistake.webp)

The abandoned project is [this repository](https://github.com/AlfredA93/recipe-repo). I copied the code bit by bit (not literal bits I should add), across this current repository (where you're reading this now), so you may see similarities with the foundation code of this project from the original abandoned repository.

My mentor Alex later told me that there was a solution to it, which was good to know; although I was already well into the new repository at that point.

![Mistake fix](/documentation/readme-img/mistake-fix.webp)
