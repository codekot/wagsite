git pull
docker-compose exec api pip install -r requirements.txt
docker-compose exec api python manage.py migrate
docker-compose restart api