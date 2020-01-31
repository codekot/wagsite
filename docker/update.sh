git pull
docker-compose exec api python manage.py migrate
docker-compose restart api