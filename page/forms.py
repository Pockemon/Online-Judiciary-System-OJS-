from django import forms
from django.contrib.auth.models import User
from page.models import Victim,Lawyer,Police
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#from page.models import UserProfile

class VictimSignUpForm(UserCreationForm):
    
    class Meta:
        model = Victim
        fields = [
            'phone',
            'address',
            'username',
            'password1',
            'password2',
            'email'
        ]

class LawyerSignUpForm(UserCreationForm):
    
    class Meta:
        model = Lawyer
        fields = [
            'phone',
            'address',
            'username',
            'password1',
            'password2',
            'email',
            'previous_cases',
            'fees',
        ]

class PoliceSignUpForm(UserCreationForm):
    
    class Meta:
        model = Police
        fields = [
            'phone',
            'address',
            'username',
            'password1',
            'password2',
            'email',
            'cases_registered',
        ]





class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            #'grp_id'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):
    

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )