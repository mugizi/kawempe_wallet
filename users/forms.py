from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile

class UserProfileForm(UserCreationForm):  
    email = forms.EmailField(required=True)  
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)  
    profile_image = forms.ImageField(required=False)  

    class Meta:  
        model = User  
        fields = ['username', 'email', 'password1', 'password2', 'role', 'profile_image']  

    def save(self, commit=True):  
        user = super().save(commit=False)  
        user.email = self.cleaned_data['email']  
        if commit:  
            user.save()  
            Profile.objects.create(  
                user=user,  
                role=self.cleaned_data['role'],  
                profile_image=self.cleaned_data.get('profile_image')  
            )  
        return user  
    


class ProfileForm(forms.ModelForm):  
    class Meta:  
        model = Profile  
        fields = ['role','profile_image']  
