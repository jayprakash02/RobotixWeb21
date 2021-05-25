from django.db import models

POST_CHOICES = (
    ("AA","Alumini"),
    ("CC","Convenor"),
    ("HC","HeadCoordinator"),
    ("MM","Manager"),
    ("CO","Coordinator"),
)

DOMAIN_CHOICE = (
    ("WA","WEB & APP"),
    ("PM","PR MARKETING"),
    ("DD","DOCUMENTATION"),
    ("SS","SPONSERSHIP"),
    ("DD","DESIGN"),
    ("TT","TECHNICAL"),
)
# Create your models here.

class Team(models.Model):
    photo = models.ImageField(upload_to='about/team',null=True)
    name = models.CharField(max_length=250,null=True)
    branch = models.CharField(max_length=250,null=True)
    domain_assign  = models.CharField(choices=DOMAIN_CHOICE,max_length=50,null=True)
    post_assign = models.CharField(choices=POST_CHOICES,max_length=50,null=True)
    fb_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    email_id = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    joining = models.DateField(auto_created=False, blank=True, null=True)

class Achievements(models.Model):

    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
