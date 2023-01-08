static:
	python manage.py collectstatic

migrations:
	python manage.py makemigrations
	python manage.py migrate