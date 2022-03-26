from django.db import models
from django.dispatch import receiver
from allauth.account.signals import user_signed_up,user_logged_in
from django.contrib.auth.models import Group,User

#Below function is to add new signed up user to group intern
@receiver(user_signed_up)
def user_signed_up_signal_handler(request,user,**kwargs):
    group = Group.objects.get(name='INTERN')
    user.groups.add(group)
    user.save()
#function for profile 
class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(default='default.png',upload_to='avatars')
    bio = models.TextField()
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    educational_details = models.TextField()
    git_profile = models.CharField(max_length=200)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username
# @receiver(post_save,sender=User)
# def created_or_update_profile(sender,instance,created,**kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()