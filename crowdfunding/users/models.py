from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
    
#Add You'll be able to add any extra fields to it that you think you need later on!

