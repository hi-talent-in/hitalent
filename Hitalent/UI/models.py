from django.db import models
from django.dispatch import receiver
from allauth.account.signals import user_signed_up, user_logged_in
from django.contrib.auth.models import Group, User

# Below function is to add new signed up user to group intern


@receiver(user_signed_up)
def user_signed_up_signal_handler(request, user, **kwargs):
    group = Group.objects.get(name='INTERN')
    user.groups.add(group)
    user.save()
# function for profile


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    LANGUAGE_CHOICES = (
        ('CHOOSE','Choose'),
        ('JAVA', 'Java'),
        ('JAVASCRIPT', 'Javascript'),
        ('PYTHON', 'Python'),
        ('.NET', '.Net'),
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, null=True)
    # username=models.CharField(null=True,max_length=100)
    language = models.CharField(
        null=True, max_length=200, default="", choices=LANGUAGE_CHOICES)

    avatar = models.ImageField(default='avatar.svg', upload_to='avatars')
    bio = models.TextField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    educational_details = models.TextField(null=True)
    git_profile = models.CharField(max_length=200, null=True, unique=True)
    phone = models.IntegerField(null=True, unique=True)

    def __str__(self):
        return str(self.user.username)
# @receiver(post_save,sender=User)
# def created_or_update_profile(sender,instance,created,**kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
