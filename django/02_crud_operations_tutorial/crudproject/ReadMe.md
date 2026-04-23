cd crudproject 

pip install -r requirements.txt

py manage.py makemigrations
#If above query is not working then, py manage.py makemigrations crudapp


py manage.py migrate 

py manage.py runserver