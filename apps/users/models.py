from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
from phone_field import PhoneField
from .managers import CustomUserManager

import uuid

# Create your models here.
GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Prefer not to say'),
)
POSITION = (
    ('CO','Converners'),
    ('MA','Managers'),
    ('CD','Coordinator'),
)
DOMIAN = (
    ('PR','Public Relations & Marketing'),
    ('SP','Sponsorship'),
    ('DO','Documentation'),
    ('WA','Web & APP'),
    ('DD','Design'),
)
YEAR = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    id = models.AutoField(primary_key=True)
    user_id = models.UUIDField(default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=50,unique=True,db_index=True)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    phone_number = PhoneField(blank=True)
    domain = models.CharField(choices=DOMIAN,max_length=2)
    gender = models.CharField(max_length=32, choices=GENDER, default='N')
    profile = models.ImageField(upload_to='members/',blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    year = models.CharField(choices=YEAR,max_length=1)
    passout = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email_verified = models.BooleanField(default=False)
    mobile_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }