from django.db import models

# Create your models here.

class FYI(models.Model):
    head = models.CharField(max_length=50,default='')
    title = models.CharField(max_length=100)
    link = models.URLField()
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.head


class DIY(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='extras/diy/img')
    desc = models.CharField(max_length=1000)
    mentor = models.CharField(max_length=50)
    members = models.CharField(max_length=200)
    file = models.FileField(upload_to='extras/diy/docs',default='')

    def __str__(self):

        return self.title


class Sponsors(models.Model):
    name = models.CharField(max_length= 150, null= True, blank= True)
    sponsor_type = models.CharField(max_length= 150, null= True, blank= True)
    website = models.CharField(max_length= 150, null= True, blank= True)
    phone_number = models.IntegerField(null= True, blank= True)
    logo = models.FileField(null= True, blank= True,upload_to='extras/sponsors')

    def __str__(self):
        return self.name


class Web(models.Model):
    img = models.ImageField(upload_to='extras/webteam',default='')
    name = models.CharField(max_length=200)
    branch = models.CharField(max_length=50)
    linkedin = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class Emails(models.Model):
    email = models.EmailField(max_length=254)
    verified = models.BooleanField(default=False)


class Gallery(models.Model):
    photo = models.ImageField(upload_to='extras/gallery')
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=110)
    email = models.EmailField()
    message = models.CharField(max_length=5000)
    time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name