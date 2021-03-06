from django.shortcuts import render
from django.http import HttpResponseRedirect
from page.forms import RegistrationForm,VictimSignUpForm,LawyerSignUpForm,PoliceSignUpForm
from page.forms import EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'accounts3/home.html')

def add_case(request):
    return render(request,'accounts3/add_case.html')


# def register(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/login')
#         else:
#             return render(request, 'accounts3/reg_form.html',{'form': form})
#     else:
#         form = RegistrationForm()

#         args = {'form':form}
#         return render(request,'accounts3/reg_form.html',args)


def victim_signup(request):
    if request.method == 'POST':
        form = VictimSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts3/login_victim.html')
    else:
        form = VictimSignUpForm()
    return render(request, 'accounts3/victim_signup.html', {'form': form})

def lawyer_signup(request):
    if request.method == 'POST':
        form = LawyerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts3/login_lawyer.html')
    else:
        form = LawyerSignUpForm()
    return render(request, 'accounts3/lawyer_signup.html', {'form': form})

def police_signup(request):
    if request.method == 'POST':
        form = PoliceSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts3/login_police.html')
    else:
        form = PoliceSignUpForm()
    return render(request, 'accounts3/police_signup.html', {'form': form})




"""
def organizer_signup(request):
    if request.method=='POST':
        form=OrganizerSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizer:home')
        else:
            return render(request, 'cricket/organizer_signup.html', {'form': form,'errors':form.errors})
    else:
         form=OrganizerSignupForm()
    return render(request, 'cricket/organizer_signup.html', {'form':form})
"""

def login_victim(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            return render(request,'accounts3/victim_home.html',{'form': form})
        else:
            return redirect(request,'accounts3/victim_home.html',{'form': form})                         ####error in login module
            #return render(request,'accounts3/victim_signup.html',{'form':form}
    else:
        form = AuthenticationForm()
        args = {'form':form}        
        return render(request,'accounts3/login_victim.html',args)

def login_lawyer(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            return render(request,'accounts3/lawyer_home.html',{'form': form})
        else:
            return redirect(request,'accounts3/lawyer_home.html',{'form': form})                          ####error in login module
            #return render(request,'accounts3/lawyer_home.html',{'form':form})
    else:
        form = AuthenticationForm()
        args = {'form':form}        
        return render(request,'accounts3/login_lawyer.html',args)

def login_police(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            return render(request,'accounts3/police_home.html',{'form': form})
        else:
            return redirect(request,'accounts3/police_home.html',{'form': form})                             ####error in login module
         #   return render(request,'accounts3/police_home.html',{'form':form})
    else:
        form = AuthenticationForm()
        args = {'form':form}        
        return render(request,'accounts3/login_police.html',args)

'''
def view_profile(request):
    args = {'user':request.user}
    return render(request,'accounts3/profile.html',args)
'''

def profile_victim(request):
    args = {'user':request.user}
    return render(request,'accounts3/profile_victim.html',args)

def profile_lawyer(request):
    args = {'user':request.user}
    return render(request,'accounts3/profile_lawyer.html',args)

def profile_police(request):
    args = {'user':request.user}
    return render(request,'accounts3/profile_police.html',args)

def choice_home(request):
    args = {'user':request.user}
    return render(request,'accounts3/choice_home.html',args)

"""
def login_victim(request):
    args = {'user':request.user}
    return render(request,'accounts3/login_victim.html',args)

def login_lawyer(request):
    args = {'user':request.user}
    return render(request,'accounts3/login_lawyer.html',args)

def login_police(request):
    args = {'user':request.user}
    return render(request,'accounts3/login_police.html',args)

"""

"""

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('profile/'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts3/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('profile/'))

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts3/change_password.html', args)   
"""
