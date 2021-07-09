## TESTING

### **Code Validation**

**HTML**

All the pages on the website have been put through **W3C Markup Validation Service**. There were 3 errors:

1. Footer element in the base.html template had double footer tags. The issue was fixed by removing one of the tags.
2. Duplicate id on the members page was detected. The ID in question was a custom made padding for the card title. I
   have removed the id and placed the *sp* within the class attribute. I have then changed the style.css file by
   changing the id selector for the class selector. That fixed the issue.
3. Section Lacks heading error. Flash messages have been wraped inside the section tag which has caused the error. I
   have changed the tags to div, and the error was fixed.

After fixing above errors I have passed every page one more time through the validation service and no errors were
detected. The screenshot of the HTML Validation can be seen [here](./static/img/html_validation.png).

**CSS**

Code has been through **W3C CSS Validation Service** and there was one error. I cannot fix that error because it is
in  *Materialize* library. Screenshot of the error can be seen [here](./static/img/css_validator_error.png)

**Javascript**

This project uses small portion of custom Javascript code. It is only used to initiate Materialize library. It had been
through JSHint and no errors were detected.

**Python**

The code from app.py has been passed through PEP8 Online. There were 7 lines which were too long which can be
seen [here](./static/img/python_pep8_bad.png). Those issues were resolved by breaking the long lines into smaller ones.
Code was once again passed through PEP8 Online and no errors were detected. Screenshot of passed test can be
seen [here](./static/img/python_pep8_good.png).

**Form Validation**

All the form are validated with HTML. Manual testing has been carried out for the forms to confirm they are working
correctly.

1. **Register**
    - For the username and password form accepts only letters from a-z, numbers from 0-9 with a minimum length of 6
      characters and a maximum length of 15 characters. Password is case-sensitive.
    - Instructions for the users are placed underneath the form.
    - Manual testing has been carried out with multiple different combinations of usernames and passwords and form works
      as intended. Username is saved to the User collection in the database. For security reasons password is first
      encrypted and then saved the same way.
    - If user trys to register again with the username that already exists flash message will be shown to the user that
      username is already in use

2. **Login**
    - Usernames and passwords are saved within database. Once user tys to log in the function checks if the username and
      password match. If they do user will be logged in to the website. If either username or password do not match
      flash message will display letting user know that username or password are not correct.

3. **Add Bike**
    - All the fields work as intended. form focuses on the field properly and is validated.
    - All the fields are correctly saved to the database.
    - Manual testing of all the fields carried out.

4. **Edit Bike**
    - Same layout as the add bike form. Difference is that this form comes with the pre-populated form so the user can
      see what he/she has had there before and make desired changes
    - After submitting changes the database gets updated.
    - Manual test carried out for all the fields.

*More about the errors and fixes in later section.*

### Defensive programming

Some features of the website are not visible to the users without permission.

1. **Navigation**

- Unregistered user is unable to see the *Profile* page and *Logout* page of the navigation

2. **Profile page**

    - If a user wants to edit or delete his/hers motorcycle they can do so only when they are logged in and on their
      profile. Buttons that direct user to the *edit* and *delete* pages are available only to a logged in user looking
      at his own profile

3. **Url**

    - Trying to enter *logout*, *add bike*, *edit bike* or *delete* page manually via url gets directed to 404 page

### Browser testing

Desktop

Website performs as intended on desktop PC and on a Laptop running Windows 10 with the latest version of browser in
question.

1. Chrome

    - Everything in perfect order, no layout loss, all animations work perfectly. Forms and validations work as
      intended. 

2. Opera

    - Everything in perfect order, no layout loss, all animations work perfectly. Forms and validations work as
      intended.

3. Mozilla

    - Everything in perfect order, no layout loss, all animations work perfectly. Forms and validations work as
      intended.

Mobile

1. Device / browser

    - One Plus 8T / Chrome: 
2. Device / browser

    - Apple Iphone 12 / Safari:

3. Device / browser

    - Apple Iphone 12 / Chrome:

### Functionality of website

1. Responsiveness

    -
2. Links

    -
3. Buttons

    -
4. Forms

    -
5. Database

    -
6. Deployment

    -

### Bugs and fixes

### Issues encountered

### Quality by **Lighthouse**

1. Landing Page
2. Members Page
3. Profile Page
4. Login Page
5. Register Page
6. Edit Bike Page
7. Delete Bike page
8. Search Page