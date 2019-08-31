# Bookstore Project

Following the Bookstore Project in Django for Professionals
Completed up to Chapter 7 - waiting for rest of chapters to be published!

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

# Commencing again from Chapter 8

Need to look at updating Django to 2.2.4 due to vulnerabilities - need to update docker images
Note - issue with Secret Key if is contains "$"

Chapter 8 - complete
Chapter 9 - complete - need to sign up for e-mail, and configure to use e-mail back end.
Chapter 10 - complete - uuid option is useful to know
Chapter 11 - complete - need to explore more use of Bootstrap content to jazz up the look & feel 
Chapter 12 - pretty basic model for upload and storage of files
Chapter 13 - simple example of using Django customer permissions
Chapter 14 - adding Stripe - pretty basic introduction, quite a bit of functionality missing, think this is a cop-out from the Author TBH!

