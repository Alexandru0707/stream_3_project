## Cozma Alexandru Photography
## Final Project Stream 3
___

This is Code Institute Stream Three Project as part of the Full Stack Development course
 It is a brand new Django project composed of multiple apps.
### Overview
**Cozma Alexandru Photography** is a web application(portofolio),the users can
create an account,login,logout ,There is functionality to allow users to reset
their password and update profile if needed,the application has contact form where users can send e-mails
as well has a page where users can buy a photo session
__The project__ was made from scratch following the guidance of the course material.
### Functionality
__Django project has the following apps__
  - home  
    - Home app has two views to render homepage and gallerypage
  - photo_website  
     -  Is the main app  has urls file where urls from all other apps are imported.
  - accounts
    - Accounts app has customized user model.
    It accepts email as a username and  
     has fields first_name and last_name. Superuser must be created in the back-end using "python manage.py createsuperuser" command, it allows users  to reset password, and update profile,The account is not created  
     if the e-mail address was used.
  - blog
    - The user can see how many times the post was viewed also,who created the post  
    it was used __ disqus__ that alows user to add comments,to the post can be added
    images, on the blog page just users with admin privileges can post
  - checkout  
    - Has PaymentForm for registering order. It has fields for billing address and card details,payment is made with __stripe__
  - contact  
    - Has ContactForm for sending email, Mail is sent using the __SMTP MODULE__  
    and an __G-MAIL__ account
  - cart  
    - the cart page was created following some tutorials(Github,Stackoverflow), the user can add product and remove product from cart
    to store the product it was used __django.contrib.sessions__,the product session ends when the user paid or press for log out  
    aswell the user can update the cart
     
__The website has the following pages__:
  - Homepage
  - Gallery
  - Shop
  - Blog
  - Contact
  - Register
  - Profile
  - Shopping Cart
  - Checkout
  - Profile update
  - Reset password
  - Log In
  - Log Out

### Built with...


  - [Django](www.djangoproject.com)  
    - I used __Django__ to handle page routing and manage the majority of the functionality on the app.
  - [Bootstrap](https://getbootstrap.com/)  
    - I used __Bootstrap__ to give my project a simple, responsive layout,
  - [Font-awesome](https://fontawesome.com/)  
    - I used __font-awesome__ to include images for icons.
  - [Fancybox](http://fancybox.net/)  
    - I used __FancyBox__ to include a lightbox in gallery page
  - [Google Fonts](https://fonts.google.com/)
    - __Google Fonts__ for style the text
  - [Stripe](https://stripe.com/gb)  
    - __Stripe__ to manage the payment
  - [Disqus](https://disqus.com/)  
    - __Disqus__ to allow user to comment on the blog page  

### Testing

The HTML and CSS code was validated using CSS validator The W3C CSS Validation Service.  
I've tested Google Chrome, Firefox, Internet Explorer on small, medium and large screens as well as on mobile screens.
Forms,cart,product page,and payment was teste visually  
On mobile screens min-width 240px

### Deployment  
  - Settings directory was created with different settings files (base settings, development settings and staging settings)  
  - Requirements directory was created with different requirements files as well (base requirements, development requirements and staging requirements). The file with full requirements list was also kept in the root folder for deploying on Heroku
  - Heroku app was created on Heroku website  
  - Python package gunicorn was installed
  - Procfile and Procfile.windows files created
  - DJANGO_SETTINGS_MODULE variable set to settings.dev locally, on heroku DJANGO_SETTINGS_MODULE variable set to settings.staging
  - whitenoise package was installed to serve static files on heroku
  - heroku app connected to GitHub repository in the section Deploy
  - The command "heroku ps:scale web=1" was run
  - ClearDB MySQL was added as an add-on on heroku for database
  - CLEARDB_DATABASE_URL variable set on heroku
  - dj-database-url package installed for the project
  - migrations were run to create tables on heroku database
  - local database dumped in json file which was pushed to GitHub repository and heroku database tables populated with data from dumped json file
  
### Test User
```email:test_user@test.com```  
```password:testuser1```

### The deployed website is available [here](https://cozma-alexandru-photography.herokuapp.com)

### Authors
 - Cozma Alexandru Adrian
