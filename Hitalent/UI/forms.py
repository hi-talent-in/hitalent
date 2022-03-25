from logging import exception
from django import forms
from .models import Profile
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
    # avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    # bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']



















































































# from allauth.account.forms import SignupForm
# from django import forms
# from django.contrib.auth.models import Group
 
# class CustomSignupForm(SignupForm):
#     first_name = forms.CharField(max_length=30, label='First Name')
#     last_name = forms.CharField(max_length=30, label='Last Name')
#     #phone_number = forms.IntegerField(max_value=15,label='Phone Number')
 
#     def save(self, request):
#         user = super(CustomSignupForm, self).save(request)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         #user.phone_number = self.cleaned_data['phone_number']
#         user.save()
# class CustomSignupForm(SignupForm):
#     user_group = forms.ModelChoiceField(queryset=Group.objects.get('INTERN'),
#                                         widget=forms.RadioSelect,
#                                         initial=('particulier')
#                                         )
#     first_name = forms.CharField(max_length=30, label='First Name')
#     last_name = forms.CharField(max_length=30, label='Last Name')

#     fields = ('user_group')

#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         role = self.cleaned_data['user_group']
#         group = role or None
#         g = Group.objects.get(name=group)
#         user.groups.add(g)
#         user.save()
#         return user