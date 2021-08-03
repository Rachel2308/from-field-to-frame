# **Testing**

## **Bugs**

* **Issue**
    Buttons were not aligning on some of the allauth templates


    **Fix**
    Found to be an issue with getting the home button aligning with the input on some of the pages. Additional CSS class written to change the home button CSS when it was paired with an input instead of a button


  ---

* **Issue**
    Toasts were not displaying on anything other than the basket page


    **Fix**
    {{ block.super }} was missed off the templates. The BTT JS was overriding the base template JS so the toasts could not be displayed


---

*   **Issue**



    **Fix**



*   **Issue**



    **Fix**


*   **Issue**



    **Fix**



*   **Issue**



    **Fix**
    


*   **Issue**



    **Fix**



*   **Issue**



    **Fix**

 

*   **Issue**



    **Fix**



---

## **Manual User testing**

* Testing has been undertaken on devices down to 320px.

#### App - Home
* #### Homepage
    * **When logged in**
        

    * **When not logged in** 

    * **When logged in as a superuser**
        



* #### **Contact Page**
    * 
   
#### App - Art

* #### **Art Home Page**
    * 


* #### **Art Detail Page**
    * 


* #### **Add Art Page**
    * 

* #### **Edit Art Page**
    * 

* #### **Delete Art Page**
    * 

#### App - Furniture

* #### **Furniture Home Page**
    * 


* #### **Furniture Detail Page**
    * 


* #### **Add Furniture Page**
    * 

* #### **Edit Furniture Page**
    * 

* #### **Delete Furniture Page**
    * 
    

#### App - Blog

* #### **Blog Home Page**
    * 


* #### **Blog Detail Page**
    * 


* #### **Add Blog Page**
    * 

* #### **Edit Blog Page**
    * 

* #### **Delete Blog Page**
    * 
 


   

 



---
    
 ## **Code Validator**

The HTML and CSS were tested using W3C Markup Validator and W3C CSS Validator to ensure that there 
were no syntax errors on any of the pages of the project. The python was checked against Git pod's internal PEP8 checker, and double checked using PEP8 Online.

* [W3C Markup Validator]()
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator)
* [PEP8 Checker](http://pep8online.com/)

Each page of HTML and the CSS file were all checked. All results came back as completely clear of errors.

* **Results**
    * HTML
        * []()

        
    
        

      
    * [CSS]()


    * [Python]()

---

### **Testing User Stories from User Experience (UX) Section**

* **User Stories** 
    * **As a member of the music team**
       

    * **As a Non-music team member of the chorus**
        1. 
    
    * **As the director of the chorus**
        1. 
### **Further Testing**

* The Website was tested on:
    * Google Chrome 
    * Internet Explorer 
    * Microsoft Edge w
    * Firefox 
    * Safari 

* The website was viewed on a variety of devices such as 
   * Laptop 
   * iPhone7 
   * iPhone 11 
   * iPhoneX
   * Oppo A9
   * Huawei p20 pro

* Friends were asked to review the site on different devices, screenshot any issues and point out any bugs or 
user experience issues.




---




Testing on checkout page. If user closes the page before form has been submitted but after the payment has been confirmed, the order eill be created in the webhook. This was tested through commenting out the form submission to emulate a customer who closes the page before the form was submitted

testing on add_product page

invlaid form is entered (tested through adding invalid price) - error message pops up advising user to correct the price (But not a toast)

testing on edit_product page

invlaid form is entered (tested through adding invalid price) - error message pops up advising user to correct the price (But not a toast)