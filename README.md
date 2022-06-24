### ITBrew - Digital Resume

> Digital Resume - A RESTful API project in Python and Django where users can create, test, and consume Backend json endpoints data using Postman Client

### Project Contributors

- Lorraine Chepkemoi
- Danis Muga
- Maureen Muriithi
- Bianca Nyambura
- Fridah Kitunguu
- Joylene Kirui

### Table of Contents

- [Technologies Used](#technologies-used)
- [User Story](#user-story)
- [API Spec](#api-spec)
- [Setup/Requirements](#setup/requirements)
- [Test Driven Development](#test-driven-development)
- [Known Bugs](#known-bugs)
- [License](#license)


#### Technologies Used

- Python
- Django
- Postgres

#### User Story
The user is able to:
1. Sign in and register
2. Get an authentication token
3. Post and update profile which contains:
    - name
    - prof pic
    - bio
4. Get and Post a Skill
5. Get and Post  contact information
6. Get, Post, Update and Delete blogs
7. Get, Post, Update and Delete portfolios
8. Get, Post, Update and Delete media
9. Get, Post, Update and Delete testimonials
10. Get, Post, Update and Delete certificates

#### API Spec
- The preferred JSON object to be returned by the API should be structured as follows:

    ## User Registration
        'register/'
        ```
        {
            "CustomUser": {
                "email": "rainelorraine@gmail.com",
                "username": "Rraine",
                "f_name": "Mwandali",
                "l_name": "Lorraine",
                "profile": {
                    "user": 29,
                    "prof_pic": null,
                    "bio": "please update your bio"
                }
            }
        }
        ```

    ## Login
        'login/'
        ```
        {
            "CustomUser": {
                "email": "rainelorraine@gmail.com",
                "username": "Rraine",
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2RhdGEiOnsiZW1haWwiOiJyYWluZWxvcnJhaW5lQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiUnJhaW5lIn0sImV4cCI6MTY1NjEzMzc4MH0.H0xPP-oOjvBcvmqQczaqi6LryXvf7Pi25_aTCbcLgh8"
            }
        }
        ```

    ## Profile
        'profile/<str:username>/'
        ```
        {
            "profile": {
                "user": 29,
                "prof_pic": null,
                "bio": "I have updated my bio"
            }
        }
        ```

    ## All Skills
        'theresume/'
        'theresume/<int:pk>/' (single skill)
        ```
        {
            "id": 1,
            "name": "Javascript",
            "score": 80,
            "image": "http://127.0.0.1:8000/media/skills/js.jpeg"
        }
        ```

    ## Testimonials
        'api/testimonial/'
        'api/testimonial/<int:pk>/' (single testimonial)
        ```
        {
            "id": 8,
            "name": "Peter Panther",
            "thumbnail": null,
            "role": "New Mentor",
            "quote": "An Excellent partner",
            "is_active": true
        }
        ```

    ## Contact Information
        'api/contactprofile/'
        ```
        {
            "id": 3,
            "name": "Maureen Meta",
            "email": "moh2wanja@gmail.com",
            "message": "I would like to request for help in revamping my resume and portfolio.\r\nThank you."
        }
        ```

    ## Portfolios
        'api/portfolios/'
        ```
        {
            "date": "",
            "name": "Peter Don",
            "description ": "Some code"
            "body": "This is my portfolio",
            "image": "null",

        }
        ```

    ## Blogs
        'api/blogs/'
        ```
            {
                "timestamp": "",
                "author": "Joy",
                "name": "Coding-hacks",
                "description ": "A few coding tricks"
                "body": "This is my blog ",
                "image": "null",
            }
        ```

    ## Media
        'api/medias/'

    ## Certificates
        'api/',include(router.urls)
        ```
        {
            "id": 1,
            "course_name": "Bachelor of Commerce",
            "institute_name": "Technical University of Mombasa",
            "location": "MOMBASA"
        }
        ```

#### Setup Requirements 
- Ensure you have the following installed on your machine
    - python3.7 or later
    - django
    - pip
    - virtual enviroment
    - Postgress database

    ## Dependencies
    All dependencies are listed in the requirements.txt file

    ## Clone
    git clone https://github.com/DenisMuga/ITBrews.git    cd ITBrews_Clone
    Open in your preferred IDE(Vs Code ,Pycharm,atom)

    ## Running the application
    - To run the application, open the cloned file in terminal and run the following commands: * python3 manage.py runserver

    ## Make and Run Migrations

    * python3.8 manage.py check
    * python manage.py makemigrations 
    * python3.8 manage.py sqlmigrate 
    * python3.8 manage.py migrate


#### Test Driven Development
- Test the API endpoints via Postman or Insomnia
- All the tests can be runned by typing the following command on the terminal $Python3 manage.py test

#### Known Bugs

We have no any known bugs.

#### License

This project is open source and available under the [MIT License]