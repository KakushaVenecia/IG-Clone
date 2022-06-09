# Instagram Clone
## Author
Kakusha Venecia

## Description
This is an attenpt at a clone of instagram website built using Django Framework

### Prerequisites
You need to install the following:
```
  Django - 4.0.4
  Virtual Environment
```

### Installation
```
  -Git clone https://github.com/KakushaVenecia/IG-Clone.git

  -cd Instagram-Clone

  -install virtual virtual

  -pip install -r requirements.txt

  -python3.8 manage.py runserver

```
## Technologies Used

  * Python-3.8.10
  * Django 4.0.4
  * Bootstrap4
  * PostgreSQL
  * CSS
  * Heroku

## Running tests
```
  -python3.8 manage.py test instagram
```


## User Story
A user can:

  * Sign in to the application to start using.
  * Upload pictures to the application.
  * See his/her profile with their my pictures.


## BDD

Scenario: A new user can input registration details and login using the details

  Given I am a new user and on the register page

  When I add my user information and click 'Sign Up' button

  Then I am redirected to login page

  Then I input my login details

  Then I click sign in

  Then I can use the application

  Then I can upload a picture to my timeline

#Known Bugs 

The images of all users appear in everyones profile. 



### Preview

[Live Link](https://star-in.herokuapp.com/)

### License

[MIT License](https://github.com/KakushaVenecia/IG-Clone/blob/master/LICENCE)
