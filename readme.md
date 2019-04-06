# Bookstore Project

Following the Bookstore Project in Django for Professionals

# Docker for Windows Issues

1.  Port Binding for the 'web' service is causing problems.  Occasionally only way to fix is to remove the images and start afresh.
2.  Alterative way to ensure containers all stopped `docker stop $(docker ps -a -q)`
3. Find that I have to remove the images from time to time, to do this use : `docker rmi $(docker images -q)`
4. Then is is a case of bulding the images again 
```
docker build . 
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```


