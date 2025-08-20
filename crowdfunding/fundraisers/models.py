from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Fundraiser(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, null=True, blank=True, related_name='owned_fundraisers')
    

class Pledge(models.Model):
    amount = models.IntegerField(default=0)
    comment = models.CharField(max_length=200, blank=True, null=True)
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        'Fundraiser',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='pledges'
    )
    