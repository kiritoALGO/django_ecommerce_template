from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # ROLE_CHOICES = [
    #     ('admin', 'Admin'),
    #     ('vendor', 'Vendor'),
    #     ('customer', 'Customer'),
    # ]

    # role = models.CharField(
    #     max_length=20,
    #     choices=ROLE_CHOICES,
    #     default='user',
    #     help_text='Designates the role of the user in the system.'
    # )

    def __str__(self):
        return self.username
    
