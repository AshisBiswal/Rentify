# Rentify-Where renting meets simplicity

Rentify is a comprehensive platform designed to simplify the rental process for both tenants and landlords. Our application offers a seamless, efficient, and transparent experience for managing property rentals.it provides various features like user authentication,posting property,live like tracking,and filtering properties on various parameters of the buyers.

## Table of contents

* Introduction
* features
* usage

## Introduction
The Rental Application is built using Python,Django a high-level Python web framework and frontend Technologies like HTML,CSS,Javascript and the database used is Mysql. It offers a user-friendly interface for managing properties,posting properties,buying and selling properties based on various user choices.

## Features
### Registration page
* Account Creation: Enables new users to register for an account,the authentication system takes firstname,lastname,username,password,phone number and email id.
* Form Validation: Validates user inputs to ensure data integrity.
### Login page
* Authentication: Allows registered users to log in securely.
* Access Control: Restricts access to authenticated users only.
### Main page/home page
* Only authenticated users are able to see the main page .login is mandatory
* The main page contains a nav bar for navigation having options like posted properties to look at the history of the properties posted by the user,post property option to post property for renting or selling purpose, and the user dropdown menu to logout of the application.
* The user can see all the posted properties by different sellers .
* The Search Bar contains two input bars one is a dropdown menu to filter on various criterias and other to input the value they want to filter based on the criteria.
* The user can like the property and if interested to be the tenant or buy the property he can click ont he interested button to see all the details regarding the property and the seller .when clicked on interested the seller will get the details of the buyer in his mail and the buyer will get the details of the seller in his mail.
* Each conatiner contains a caraousel to see the images of the property
* The main page also contains a paginator for better user interface.
### Post Property page
* The Post property option in the navbar takes you to the page where you can post a property and the form is validated and form validation is properly handled.
* After posting a property the user is redirected to the main page where he can see his posted property along with all other posted properties
### Posted Properties
* The user can see all the properties posted by him.
* The user can manage images,update and delete properties posted by him.
* The form validation is properly handled in update and manage images templates.
### Email Notifications
* Email notifications are sent to both buyer and seller when clicked on interested.
### Data Persistance
* The Application uses a RDBMS Mysql for maintaining and storing Data.
### Usage
* Visit the registration page and register yourself if already have an account then you can login using the link in the page just below the form
* once logged in,if authenticated you are redirected to the main page else you will get an error and need to log in with correct credentials.
* Once you are in the main page the nav bar has options to post property,see all the posted properties and surf all the properties by the users.
* The user can like the proper and if interested can click on the interested button to see all the details related to the property along with seller details.
* The user can log out using the logout option in the dropdown menu at the extreme top right corner just beside the username.
# Templates
![reg_page](https://github.com/AshisBiswal/Rental-Application/assets/113982683/511fe9f4-a936-4cae-adb3-5d0d612ba7f9)
***
![login_page](https://github.com/AshisBiswal/Rental-Application/assets/113982683/fedf1ed3-c8b7-47dd-8736-0deba6e1e911)
***
![main_page](https://github.com/AshisBiswal/Rental-Application/assets/113982683/3e6a27ef-afab-44eb-8db1-88ff6521c8c6)
***
![Post_property](https://github.com/AshisBiswal/Rental-Application/assets/113982683/7a93c549-314b-4023-9305-19e12c84d24c)
***
![posted_prop](https://github.com/AshisBiswal/Rental-Application/assets/113982683/151f10e6-24f4-4650-8cb2-5ad9f13b325b)
***
![update-prop](https://github.com/AshisBiswal/Rental-Application/assets/113982683/a7a25941-c8d5-4cbe-96d2-aff93d4be0a7)
***
![manage_images](https://github.com/AshisBiswal/Rental-Application/assets/113982683/1ec2efb7-c54c-407a-a9ff-c428570a6a0e)
***
![Interested_page](https://github.com/AshisBiswal/Rental-Application/assets/113982683/530f48d2-278a-4cc0-a18d-d5f63b2e1a09)
***








