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
        1. 
        2. 
        3. 
        4. 

    * **As a customer looking for someone to upcycle their furniture**
        1. 
        2. 
    
    * **As someone interested in art**
        1.
        2. 
        3. 

    * **As the owner of the store**
        1.
        2. 
        3. 
        
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


### Typography



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

1. 





---

### **Features Changed from Original Wireframe**

### 1. 



---

## Frameworks, Libraries & Programmes Used

1. [Materialize](https://materializecss.com/) 
    * Materialize was used to help with the styling and responsiveness of the site.
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
9. [MongoDB](https://www.mongodb.com/)
    * MongoDB was used for the database for the site
8. Languages used
    * HTML
    * CSS
    * Python
    * Javascript
 

---



## Deployment

From Field to Frame was created on Gitpod. Commits to git pushed the project to the GitHub repository. The project was deployed to Heroku for the live site
and the pushes to GitHub automatically pushed to Heroku to update the live site. 

**Running From Field to Frame Online Locally**

### **GitHub**

How to clone From Field to Frame from GitHub

Please note that this project will only run locally if am env.py file is set up containing the IP, PORT, SECRET_KEY, MONGO-URI and MONGO_DBNAME. 
For security reasons these details will not be shared on this documentation. The env.py file should be added to your gitignore file.

1. Navigate to rachel2308/MS3-from-field-to-frame
2. Click on the green Code button
3. Select the code dropdown button beside the Gitpod button
4. Copy the URL listed.
5. Start up your IDE and navigate to the file location.
6. To clone, copy this code and input it into your terminal:

https://github.com/Rachel2308/MS3-belles-task-manager

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

* 
* 
* 



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