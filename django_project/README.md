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

