# Custom Token Authentication Example Easiest Way to understand

1. First see the custom_project code to understand the way of logic step by step

2. ( auth_token ) app name is for the custom token to generate automatically 
    when we create api's in postman/swaggers...

3. ( cutom exceptions ) are very useful for future projects to get response 
    when client give mistake like token/endpoints/Authentication credentials. 
    See in ( utils.py ) file ( under auth_token app folder )

    1. Change Authentication credentials were not provided message to NotAuthourized.

    2. status code can be added in exception handlers to get response.

    3. added Custom 404 json response and 

    4. added Custom 500 view handler ( in JSON not HTML ).

4. ( custom renderers ) uses to get response like success/failure ( JSONRender ).

# Installation steps :-

1. Firstly you need to have python3 installed

2. Then clone the repository

3. create a virtual environment using cmd: ( virtualenv env )

4. Activate the virtual environment by running source :- ( env/bin/activate )
   
   On Windows use source :- ( env\Scripts\activate )
   
5. Install the dependencies using ( pip install -r requirements.txt )

6. Migrate existing db tables by running ( python manage.py migrate )

7. Run the django development server using ( python manage.py runserver )
