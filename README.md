# From Field to Frame
## A Milestone 4 Project by Rachel Sherlock

[View the live project](https://from-field-to-frame.herokuapp.com/)


This website was designed to be a e-commerce site for a local artist, Holly Dawes. As well as a site to sell her work, the site is also designed to promote her work upcycling furniture. 

![Am I responsive](documentation/images/MS4-am-i-responsive.jpg)

---

## User Experience (UX)

* **User Stories** 
    * **As a customer looking for new art**
        1. I want to be able to look through Holly's art to see her style
        2. I want to be able to sort the art by price to be able to shop to my budget
        3. I want to be able to register an account so that my default information can be saved for future purchased
        4. I want to be able to see my previous purchases

    * **As a customer looking for someone to upcycle their furniture**
        1. I want to be able to see Holly's previous work to get ideas and to see the quality of her work
        2. I want to be able to contact Holly in order to discuss the project and get a quote
    
    * **As someone interested in art**
        1. I want to be able to see the work that Holly does in order to learn more about her style
        2. I want to be able to learn more through reading the blogs on the site

    * **As the owner of the store**
        1. I want to be able to sell my art through the site
        2. I want to be able to upload new pieces to the site, edit the existing ones, and delete any that are no longer available
        3. I want to be able to showcase my previous upcycling projects
        4. I want to be able to upload new furniture projects to the site, edit the existing ones, and delete any that I no longer want to feature
        5. I want people to be able to contact me for information about my art or furniture projects
        6. I want to be able to share my love of art though my blog

        
---

## Models

For this project I have used the following models:

* **art**
   * This model holds all the information needed for the pieces of art for sale on the site

            1. title 
            2. description
            3. medium
            4. product_type
            5. price

* **furniture**
    * This model holds all the information needed for the example furniture projects on the site

            1. title
            2. product
            3. medium
            4. description
            5. image

* **blog**
    * This model holds all the information needed for the blog section on the site
    
            1. title
            2. description
            3. content
            4. published date
            5. image


* **profile**
    * This model holds the information needed for users profiles to be created and stored

            1. full name
            2. email
            3. phone number
            4. street address line 1
            5. street address line 2
            6. county
            7. country
            8. post code

---


## Testing

[View the full TESTING.md documentation](https://github.com/Rachel2308/from-field-to-frame/blob/master/TESTING.md)

---

## Design

### Colour Scheme  
As Holly mainly paints flowers and outside scenes, and in fitting with the name "From Field to Frame" I wanted to have green as the main colour of the site. I chose #567d46 as it was a nice neutral and calming shade of green, and a natural shade that could be found in nature. I did not want the background to be all white as I feel this can be uncomfortable to look at for any length of time. I chose #fffaf0 as it paired well with the main colour, and also worked well with her art work, complimenting the natural shades in her art and not contrasting harshly. White was used in text boxes to provide contrast for the content. For the text, I have gone for shades of dark charcoal grey as this causes less eye strain than black, making the site a more calming and pleasant site to browse.


### Typography

For the headers I have picked Niconne with a back up of cursive. This worked well with the flowing lines of the featured artwork on the site, and provided a contrast to the main font used throughout the site. For the main font I have gone for Lato, with a back up fot of sans-serif. This font is clear and easy to read, making the site comfortable to peruse for any length of time.

### Imagery

The images used throughout the site are the artwork of Holly Dawes, and real examples of her furniture upcycling. I have picked the bluebell rainbow image as It was a lovely cheerful piece to feature on the front page, and the rainbow over the top created a circular image that worked well as a main image. This piece was carried on through to any other area of the site that would have otherwise been a plain page.

---
### Wireframes

The wireframes for the site were created in balsamiq and uploaded as a pdf. They can be found as a pdf file [here.](https://github.com/Rachel2308/from-field-to-frame/blob/master/from-field-to-frame-wireframes.pdf)

---

## Features

### Users

People can use the site anonymously and still look at the art, her furniture projects and read the blogs. However if a user registers an account then their delivery details will be retained for future purchases, and also their profile will store the details of previous purchases. 

The store owner will be logged in as a superuser and can add, edit, and delete artwork, furniture examples and blogs. 


### Existing Features

The site is responsive across all screen sizes. The layout of the pages change depending on the size of screen. This has created a tidy and clean look on all screens.

### 1. Log in page
The log in page enables a user to log in to their account to update their details or access theor purchase history. Once logged in, users can checkout easier as their delivery information will be saved and autofilled into the checkout. If a user does not have an  account then there is a link to take them to the registration page.

![](documentation/images/existing-feature-login.jpg)

### 2. Registration page
The registration page enables new users to register for an account. From this page, existing customer can also go to the log in page.

![](documentation/images/existing-feature-register.jpg)

### 3. Art page
The art page shows all available art work, it's title and cost. There is a link for users to get more information on the piece. If the user is logged in as a superuser, the artwork can be deleted or edited from this page.

![](documentation/images/existing-feature-art.jpg)

### 4. Art detail page
The art detail page shows a larger image of the artwork, with a link to show an even larger image. The page also holds the description of the artwork, the price and the ability to add the artwork to their basket. If the user is logged in as a superuser, the artwork can be deleted or edited from this page. Users can sort the artwork by price to enable them to find pieces that suit their budget.

![](documentation/images/existing-feature-art-detail.jpg)

### 5. Furniture page
The furniture page shows all of the artist's previous furniture restoration project which allows people to see her skill and style. There is a link for users to get more information on the piece. If the user is logged in as a superuser, the furniture can be deleted or edited from this page.

![](documentation/images/existing-feature-furniture.jpg)

### 6. Furniture detail page
The furniture detail page shows a larger image of the piece, with a link to show an even larger image. The page also holds the description of the piece, and a link to contact the artist. If the user is logged in as a superuser, the piece can be deleted or edited from this page.

![](documentation/images/existing-feature-furniture-detail.jpg)

### 7. Blog page
The blog page shows all blogs on the site, with an image, published date, title and short description. They can click to read the full blog, and sort the blogs by published date. If the user is logged in as a superuser, the blog can be deleted or edited from this page.

![](documentation/images/existing-feature-blog.jpg)

### 8. Blog detail page
The blog detail page shows the full blog and published date.

![](documentation/images/existing-feature-blog-detail.jpg)

### 9. Basket page
The basket page shows a summary of their order. A small thumbnail image shows the art work chosen, and they can see the name, price, quantity, subtotal, whether there is a delivery charge and the order total. If the order is under the amount for free delivery, a red message will display telling them how much more they need to spend to get free delivery.

![](documentation/images/existing-feature-basket.jpg)

### 10. Checkout page
The checkout page will show the order summary and has a form to enter their details. If they have an account and have chosen to save their details, this form will be prefilled with their default delivery information.

![](documentation/images/existing-feature-checkout.jpg)

### 11. Checkout success page
Once a customer has successfully made a purchase, a page will display showing their order summary and delivery details. It will show their registered email address and advise them that an order confirmation email will be sent to their registered address.

![](documentation/images/existing-feature-checkout-success.jpg)

### 12. Profile page
On the user's profile page, the customer can find a record of their default delivery address, which they can update, and previous orders they have made. The order number acts as a link to view their previous order confirmation.

![](documentation/images/existing-feature-profile.jpg)

### 13. Contact page
The contact page enables customers to contact the artist to get information, or discuss a quote for a furniture restoration project.

![](documentation/images/existing-feature-contact.jpg)

### 14. Toasts
The toasts on the site with give the user messaged in a pop up window in the top right of the screen. If the user has items in their shopping cart then these will also be listed in the toast.

---


### **Features Left To Implement**

1. The blogs only render properly when they are uploaded with the html line breaks in place. This means that it would not be easy for the owner of the site to upload logs without basic coding knowledge. While this is not ideal, it is not possible to do this through django and any way of changing this would be outside the scope of this project.

2. In future I would add in the ability to log in to the site with social media.
 



---

## Frameworks, Libraries & Programmes Used

1. [Bootstrap](https://getbootstrap.com/) 
    * Bootstrap was used to help with the styling and responsiveness of the site.
2. [Google Fonts:](https://fonts.google.com/) 
    * Google fonts were used to import the Lato and Niconne fonts which are used throughout the site.
3. [Font Awesome:](https://fontawesome.com/) 
    * Font Awesome was used for the icons on the footer links, and the musical notes on the task cards, pon the header and on the log in and registration forms.
4. [jQuery:](https://jquery.com/) 
    * jQuery was used in conjunction with Materialize across the site.
5. [Git:](https://git-scm.com/) 
    * Git was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
6. [GitHub:](https://github.com/) 
    * GitHub is used to store the project's code after being pushed from Git.
7. [Balsamiq:](https://balsamiq.com/) 
    * Balsamiq was used to design the site and create [wireframes](https://github.com/Rachel2308/from-field-to-frame/blob/master/from-field-to-frame-wireframes.pdf).
8. [Heroku:](https://heroku.com) 
    * Heroku was used to host the deployed site
9. [AWS:](https://aws.amazon.com/)
    * AWS was used to host the static files
10. [Stripe](https://stripe.com/gb)
    * Stripe was used for the payments on the checkout page
11. [Django](https://www.djangoproject.com/)
    * The Django framework was used across the site
12. Languages used
    * HTML
    * CSS
    * Python
    * Javascript
 

---



## Deployment

From Field to Frame was created on Gitpod. Commits to git pushed the project to the GitHub repository. The project was deployed to Heroku for the live site and the pushes to GitHub automatically pushed to Heroku to update the live site. The static files were hosted through Amazon AWS.

**Running From Field to Frame Online Locally**

### **GitHub**

How to clone From Field to Frame from GitHub

Please note that this project will only run locally if am env.py file is set up containing the IP, PORT and SECRET_KEY. 
For security reasons these details will not be shared on this documentation. The env.py file should be added to your gitignore file or held within the Environment variables help on gitpod.io.

    1. Navigate to rachel2308/from-field-to-frame
    2. Click on the green Code button
    3. Select the code dropdown button beside the Gitpod button
    4. Copy the URL listed.
    5. Start up your IDE and navigate to the file location.
    6. To clone, copy this code and input it into your terminal:

https://github.com/Rachel2308/from-field-to-frame

**Set Your Environment Variables**

Go to settings, and within Config Vars enter the following

    * IP: 0.0.0.0
    * PORT: 5000
    * SECRET_KEY: (This is a secret password that must be very secure.)
    * STRIPE_PUBLIC_KEY (From stripe.com)
    * STRIPE_SECRET_KEY (From stripe.com, secret password that must be kept secure)
    * STRIPE_WH_KEY (Webhook key from stripe.com, secret password that must be kept secure)

To get your Stripe keys, login to Stripe and under the Developers tab look for the 'Publishable Key' and 'Secret Key' under API keys

The webhook secret key is found under Webhooks once you have created an endpoint, which should be set to receive all events and match this url structure:

<site base url/checkout/wh/>

A different endpoint will need to be created for both the local and deployed site. 

**Install the app requirements**

    pip3 install requirements.txt

**Apply database migrations**

    python3 manage.py migrate

**Create a new superuser to access admin features**

    python manage.py createsuperuser

**Run the app locally**

    python manage.py runserver

## **Heroku**

**1. Deployment to Heroku**

**2. Create the application:**

    * Login in to heroku.com
    * Click on New, and Create new app
    * Enter your app name
    * Select the region that is closest to you

**3. Connect to your GitHub repository**

    * Click Deploy and select GitHub - Connect to GitHub
    * Enter your repository name and search
    * Click Connect on the correct repository

**4. Log in to Heroku via the CLI**

    heroku login -i

**5. Create a new superuser and fill in your details:**
    
    python manage.py createsuperuser

**6. Install gunicorn**

    pip3 install gunicorn

**7. Freeze the app's requirements**

    pip3 freeze > requirements.txt

**8. Create a Procfile and include the following code**

    web: gunicorn moose_juice.wsgi:application

**9. Temporarily disable Heroku's static file collection**

    heroku config:set DISABLE_COLLECTSTATIC=1 --app from-field-to-frame

**10. Add the hostname of your Heroku app to settings.py**
    ALLOWED_HOSTS = ['from-field-to-frame.herokuapp.com', 'localhost']
 

**11. Add config Vars to Heroku**

In heroku go to settings, reveal config vars and enter the following:


|**Key**|**Value**|
|:-----|:-----|
|AWS_ACCESS_KEY_ID| enter your variable here |
|AWS_SECRET_ACCESS_KEY|enter your variable here|
|DATABASE_URL|added by Heroku when Postgres installed|
|DISABLE_COLLECTSTATIC|this variable will be deleted later|
|EMAIL_HOST_PASS|	enter your variable here|
|EMAIL_HOST_USER|	enter your variable here|
|SECRET_KEY|	enter your variable here|
|STRIPE_PUBLIC_KEY|	enter your variable here|
|STRIPE_SECRET_KEY|	enter your variable here|
|STRIPE_WH_SECRET|	enter your variable here|
|USE_AWS|	True|

**12. Enable Automatic Deploys**

    * Go to the deploy tab
    * Within the automatic deploys section, choose the branch that you want to deploy from and select Enable Automatic Deploys.

**13. Launch deployed site**

    Click on Open App from the app page within Heroku to launch your deployed site.

---

## **Setting up an S3 bucket**

1. Create an Amazon AWS account**
2. Search for S3 and create a new bucket
    * Allow public access

3. Under Properties > Static website hosting
    * Enable
    * Index.html as index document
    * Save

4. Under Permissions > CORS use:

                [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
        ]

5. Under Permissions > Bucket Policy:
    * Generate Bucket Policy and save Bucket ARN
    * Type of Policy is S3 Bucket Policy
    * Enter * for Principal
    * Enter ARN previously copied
    * Add Statement
    * Generate Policy
    * Copy Policy JSON Document
    * Paste policy into the Edit Bucket policy on the previous tab
    * Save your changes

6. Under Access Control List (ACL):
    * Under Everyone (public access), tick List
    * Acknowledge that everyone will be able to access the Bucket
    * Save changes


## **Setting up AWS IAM (Identity and Access Management)**

1. From the IAM dashboard within AWS, click User Groups:
    * Create new group and name it e.g. manage-from-field-to-frame
    * Click through but do not add a policy
    * Create Group

2. Select Policies:
    * Create the policy
    * Under JSON tab, click Import managed policy
    * Select AmazongS3FullAccess
    * Edit the resource including the Bucket ARN from the Bucket Policy:

			"Resource": [
			                "arn:aws:s3:::from-field-to-frame",
			                "arn:aws:s3:::from-field-to-frame/*"
            ]
    * Click next step > review policy
    * Name the policy e.g from-field-to-frame-policy
    * Create the policy

3. Return to User Groups and select the group created earlier
    * Under Permissions > Add permissions, select Attach Policies and select the one you have just created
    * Add permissions

4. Under Users:
    * Choose a user name e.g. from-field-to-frame-staticfiles-user
    * Access type is Programmatic access
    * Click Next
    * Add user to the Group you have just created
    * Click Next and Create User

5. Download the .csv which contains the access key and secret access key. This cannot be downloaded again so ensure that it is saved securely

## **Commecting Django to S3** 
1. Install boto3 and django-storages

        * pip3 install boto3
        * pip3 install django-storages
        * pip3 freeze > requirements.txt

2. In Heroku CVARS, under settings, add the following values from the .csv file that was downloaded in the previous step.

        * AWS_ACCESS_KEY_ID
        * AWS_SECRET_ACCESS_KEY

3. Delete the DISABLE_COLLECTSTATIC variable from your CVARS in Heroku, and deploy your Heroku app

4. Once the S3 bucket is set up, create a new folder called media (at the same level as the static folder). Any media files required by your site can be uploaded here. Ensure they are pulicly accessible under permissions within the S3 bucket.

---

## Credits

### Code

* The code that formed the basis of the project is based on the Boutique Ado Walkthrough project on the LMS. 
* The code for the contact form is based this [ordinarycoders tutorial](https://www.ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend)



### Acknowledgements

Thanks to 

* Holly Dawes who is a real, and very talented artist. Her work has made this project a pleasure to work on
* Katharine Allison, who has written the original content for the site
* The slack community for help and support when things got tough
* My mentor Brian, for being ready with help and tips on every call

