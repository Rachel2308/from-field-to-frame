# **Testing**

## **Bugs**

* **Issue**
  


    **Fix**
  


  ---

* **Issue**



    **Fix**



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

### **Section**

* #### Header
    * **When logged in**
        

    * **When not logged in** 

    * **When logged in as a superuser**
        



* #### **Log in**
    * 
   

* #### **Registration**
    * 


* #### **Log out**
    * 


* #### ** **
    * 

    

 





 

* #### **delete_task**
   

 



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