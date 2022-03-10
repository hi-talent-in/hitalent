
# from allauth.account.adapter import DefaultAccountAdapter
# from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
# class UserAccountAdapter(DefaultAccountAdapter):
#     def save_user(self, request, user, form, commit=True):

#         user = super(UserAccountAdapter, self).save_user(request, user, form, commit=False)
#         user.first_name = form.cleaned_data.get('first_name')
#         user.last_name = form.cleaned_data.get('last_name')
#         user.user_group = form.cleaned_data.get('INTERN')
#         user.save()
#         user.groups.add(user.user_group)
        
#         if user.groups.filter(name='INTERN').exists():
#             user.is_active = False
#         else:
#             user.is_active = True
        
#         return user