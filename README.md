# URL-Shortening-Service


An URL shortening service application written in Python and Django involves the following components:

- The Django Superuser (127.0.0.1:8000/login) database to store the original URLs and their corresponding shortened versions.
- A backend API written in Python using Django's web framework to handle incoming requests, validate input, and generate the shortened URLs.
- A frontend interface for users to enter long URLs and receive their shortened versions.
- A redirection mechanism to send users to the original URL when they click on the shortened version.

The application works by taking a long URL input from a user, generating a unique short code using an algorithm that is one-hot encoding, storing the mapping between the short code and original URL in the database, and returning the shortened URL to the user. When a user clicks on the shortened URL, the application looks up the original URL in the database and redirects the user to the appropriate webpage. It also stores the number of URLs shortened and the number of times the shortener is used. The application also handles edge cases such as checking for duplicate URLs, validating the format of the input URLs, and preventing malicious use such as URL phishing.



### Getting Started:

- Clone the repo.

- Install Django (pip install django).

- Install virtualenv (pip install virtualenv).

- In the terminal, go to the source folder and run, 
            virutalenv .
            
- Then, run,
            source bin/activate
            
- Lastly, to start the Django project, 
            django-admin startproject [Name of the project]
            
- To migrate the changes, run,
            manage.py makemigrations
            manage.py migrate
            
- To create superuser,
            python manage.py createsuperuser
            
- To start the server, that is a emulating a production & development environment.
            python manage.py runserver
