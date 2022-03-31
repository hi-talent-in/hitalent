from dataclasses import field
from pyexpat import model
from django import forms
from .models import Profile








class UpdateProfileForm(forms.ModelForm):
    # avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    # bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
LANGUAGE_CHOICES=(
        ('JAVA','Java'),
        ('JAVASCRIPT','Javascript'),
        ('PYTHON','Python'),
        ('.NET','.Net'),
    )
class LanguageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ['language']
        #field = forms.ChoiceField(choices=LANGUAGE_CHOICES, widget=forms.Select(attrs={'onchange': 'submit();'}))
    
    # class Meta:
    #     model = Profile
    #     fields = ['language']
