from django import forms
from page.models import Victim,Lawyer,Police
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login,get_user_model,logout

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


#class VictimCaseForm(UserCreationForm):
User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        #user = authenticate(username=username,password=password)
        #user_qs = User.objects.filter(username=username)
        #if user_qs.count() == 1:
           # user = user_qs.first()
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("This User does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active")
        return super(UserLoginForm,self).clean(*args,**kwargs)


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
