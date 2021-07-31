# From Field to Frame
## A Milestone 4 Project by Rachel Sherlock

[View the live project]()

![The Belles of Three Spires Site Homework Tracker]()

This website was designed to be a e-commerce site for a local artist, Holly Dawes. As well as a site to sell her work, the site is also designed to promote her work upcycling furniture. 

![Am I responsive]()

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
        2. I want to be able to earn more through reading the blogs on the site

    * **As the owner of the store**
        1. I want to be able to sell my art through the site
        2. I want to be able to upload new pieces to the site, edit the existing ones, and delete any that are no longer available
        3. I want to be able to showcase my previous upcycling projects
        4. I want to be able to upload new furniture projects to the site, edit the existing ones, and delete any that I no longer want to feature
        5. I want people to be able to contact me for information about my art or furniture projects
        6. I want to be able to share my love of art though my blog

        
---

## Database Model

MongoDB's non-relational database structure was ideal for this site as there were very few relationships between the collections on the site. 

#### **Models**
|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|section_name|string|The section that the homework task is being allocated to.|
|song_name|string|The song that the homework relates to|
|task_title|string|A brief title of the homework|
|due_date|date|The date that the homework should be completed by|
|task_description|string|A more in-depth write up of the allocated homework task|
|created_by|string|The name of the person who has set the task|

#### **Sections collection**
|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|section_name|string|The section that the homework task is being allocated to.|

#### **Song collection**
|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|song_name|string|The song that the homewrok task relates to|

#### **User collection**
|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|username|string|The username that the member registers with|
|password|string|The password that the user chooses when they register|
|is_musicteam|boolean|When members register they can select if they are a member of the music team or not. This then alters their user rights on some of the pages|

---


## Testing

[View the full TESTING.md documentation](TESTING.md)

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

The wireframes for the site were created in balsamiq and uploaded as a pdf. They can be found as a pdf file [here.]

---

## Features

### Users



### Existing Features

The site is responsive across all screen sizes. The layout of the pages change depending on the size of screen. This has created a tidy and clean look on all screens.

### 1. Log in / Registration Page



---


### **Features Left To Implement**

1. The blogs only render properly when they are uploaded with the html line breaks in place. This means that it would not be easy for the owner of the site to upload logs without basic coding knowledge. While this is not ideal, it is not possible to do this through django and any way of changing this would be outside the scope of this project.


---

### **Features Changed from Original Wireframe**

### 1. 



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
    * Balsamiq was used to design the site and create [wireframes](documentation/images/Homework-Tracker-Wireframe-pdf.pdf).
8. [Heroku:](https://heroku.com) 
    * Heroku was used to host the deployed site
9. [AWS:](https://aws.amazon.com/)
    * AWS was used to host the static files
10. [Stripe](https://stripe.com/gb)
    * Stripe was used for the payments on the checkout page
9. [Django](https://www.djangoproject.com/)
    * The Django framework was used across the site
9. Languages used
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

Please note that this project will only run locally if am env.py file is set up containing the IP, PORT, SECRET_KEY, MONGO-URI and MONGO_DBNAME. 
For security reasons these details will not be shared on this documentation. The env.py file should be added to your gitignore file or held within the Environment variables help on gitpod.io.

1. Navigate to rachel2308/from-field-to-frame
2. Click on the green Code button
3. Select the code dropdown button beside the Gitpod button
4. Copy the URL listed.
5. Start up your IDE and navigate to the file location.
6. To clone, copy this code and input it into your terminal:

https://github.com/Rachel2308/from-field-to-frame

### **Heroku**

**Deployment to Heroku**

**Create the application:**

    * Login in to heroku.com
    * Click on New, and Create new app
    * Enter your app name
    * Select the region that is closest to you

**Connect to you GitHub repository**

    * Click Deploy and select GitHub - Connect to GitHub
    * Enter your repository name and search
    * Click Connect on the correct repository

**Set Your Environment Variables**

Go to settings, and within Config Vars enter the following

    * IP: 0.0.0.0
    * PORT: 5000
    * MONGO_DBNAME: (enter the database name that you are connecting to)
    * MONGO_URI: (enter your mongo uri. This is found by going to clusters> connect> connect to your application and entering your passwords and dbname within the link)
    * SECRET_KEY: (This is a secret password that must be very secure.)

**Enable Automatic Deploys**

    * Go to the deploy tab
    * Within the automatic deploys section, choose the branch that you want to deploy from and select Enable Automatic Deploys. 


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




Bugs

Burger Menu jumped when clicked

Fix

Bootstrap spacing classes were causing the margins to change when the burger menu was open

Sort function in Blogs home page caused account dropdown to show

Fix

FOund missing container-fluid div, problem solved once opening div added

Contact and More info links on furniture pages - link only on margin on the first card

Fix

???