from distutils.command.upload import upload
from email.policy import default

from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import models
from django.db.models.signals import post_save

#Group Added To New Users: "Can Add Pattern, Symbol, Broker"

@receiver(user_signed_up)
def user_signed_up_signal_handler(request,user,**kwargs):
    group = Group.objects.get(name='INTERN')
    user.groups.add(group)
    user.save()
    
class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(default='default.jpg',upload_to='avatars')
    bio = models.TextField()
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    educational_details = models.TextField()
    git_profile = models.CharField(max_length=200)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username
