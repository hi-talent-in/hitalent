from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

#Group Added To New Users: "Can Add Pattern, Symbol, Broker"

@receiver(user_signed_up)
def user_signed_up_signal_handler(request,user,**kwargs):
    group = Group.objects.get(name='INTERN')
    user.groups.add(group)
    user.save()