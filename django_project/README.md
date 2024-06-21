# Django

Create a virtual environment using venv or pipenv
> python -m venv {virtual_name}

Activate the venv
> source myenv/bin/activate

Install Django
> pip install django

Using the django-admin to create project 
> django-admin createproject {project_name}


### Django Template Language

Variables -> {{ blog_title }}

Tags -> { % if has_title % }

Filters -> {{ blog_title|title }}

### Movies app

Display your favorite movies

#### Template format for any app
> app/templates/app/{function_name}.html

Migrations:

    Django’s migration system tracks changes to your models and applies them to your database. You can create and apply migrations with simple commands.

Admin Interface:

    The Django admin interface is automatically generated from your models, providing a ready-made interface for managing your application’s data.

Middlewares:

    Middleware in Django is a way to process requests globally before they reach the view or after the view has processed them. You can create custom middleware to handle various tasks.

Using Django for API Development

 Install Django and Django REST Framework
`pip install django djangorestframework`

