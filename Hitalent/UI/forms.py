from django import forms
from .models import Profile








class UpdateProfileForm(forms.ModelForm):
    # avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    # bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']