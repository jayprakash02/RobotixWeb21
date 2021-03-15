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
    photo = models.ImageField(upload_to='img/team',null=True)
    name = models.CharField(max_length=50,null=True)
    branch = models.CharField(max_length=50,null=True)
    domain_assign  = models.CharField(choices=DOMAIN_CHOICE,max_length=2,null=True)
    post_assign = models.CharField(choices=POST_CHOICES,max_length=2,null=True)
    fb_id = models.URLField(null=True)
    email_id = models.EmailField(null=True)
    phone = models.CharField(max_length=100,null=True)
    joining = models.DateField(auto_created=False,null=True)
