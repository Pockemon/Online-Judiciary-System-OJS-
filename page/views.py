from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from page.forms import RegistrationForm,VictimSignUpForm,LawyerSignUpForm,PoliceSignUpForm
from page.forms import EditProfileForm,UserLoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,AuthenticationForm
from django.contrib.auth import authenticate, login,get_user_model,logout
from page.models import Lawyer,Police,VictimCase,Victim
from django.views.generic import CreateView,DeleteView,DetailView,UpdateView
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'accounts3/home.html')


class CaseCreateView(CreateView):
    model = VictimCase
    fields = ('text',)
    template_name = 'accounts3/case_victim.html'

    def form_valid(self,form):
        case1 = form.save(commit=False)
        case1.victim = self.request.user
        case1.save()
        messages.success(self.request,'Case details are added successfully')
        return redirect('add_case')


def victim_signup(request):
    if request.method == 'POST':
        form = VictimSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts3/victim_home.html')
    else:
        form = VictimSignUpForm()
    return render(request, 'accounts3/victim_signup.html', {'form': form})

def lawyer_signup(request):
    if request.method == 'POST':
        form = LawyerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts3/lawyer_home.html')
    else:
        form = LawyerSignUpForm()
    return render(request, 'accounts3/lawyer_signup.html', {'form': form})

def police_signup(request):
    if request.method == 'POST':
        form = PoliceSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts3/police_home.html')
    else:
        form = PoliceSignUpForm()
    return render(request, 'accounts3/police_signup.html', {'form': form})


def login_victim(request):
    title = "Login"
    form = UserLoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        #print(request.user.is_authenticated)
        return render(request, 'accounts3/victim_home.html')
    return render(request,"accounts3/form.html",{"form":form,"title":title})


def login_police(request):
    title = "Login"
    form = UserLoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        #print(request.user.is_authenticated)
        return render(request, 'accounts3/police_home.html')
    return render(request,"accounts3/form.html",{"form":form,"title":title})

def login_lawyer(request):
    title = "Login"
    form = UserLoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        #print(request.user.is_authenticated)
        return render(request, 'accounts3/lawyer_home.html')
    return render(request,"accounts3/form.html",{"form":form,"title":title})


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

def victim_home(request):
    args = {'user':request.user}
    return render(request,'accounts3/victim_home.html',args)

def lawyer_home(request):
    args = {'user':request.user}
    return render(request,'accounts3/lawyer_home.html',args)

def police_home(request):
    args = {'user':request.user}
    return render(request,'accounts3/police_home.html',args)

def add_case(request):
    args = {'user':request.user}
    return render(request,'accounts3/add_case.html',args)

"""

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

def login_victim(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            return redirect(request,'accounts3/victim_home.html')
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
        #else:
            #return redirect(request,'accounts3/lawyer_home.html',{'form': form})                          ####error in login module
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
        #else:
            return redirect(request,'accounts3/police_home.html',{'form': form})                             ####error in login module
         #   return render(request,'accounts3/police_home.html',{'form':form})
    else:
        form = AuthenticationForm()
        args = {'form':form}        
        return render(request,'accounts3/login_police.html',args)

def view_profile(request):
    args = {'user':request.user}
    return render(request,'accounts3/profile.html',args)

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

def victim_home(request):
    args = {'user':request.user}
    return render(request,'accounts3/victim_home.html',args)

def lawyer_home(request):
    args = {'user':request.user}
    return render(request,'accounts3/lawyer_home.html',args)

def police_home(request):
    args = {'user':request.user}
    return render(request,'accounts3/police_home.html',args)

def add_case(request):
    args = {'user':request.user}
    return render(request,'accounts3/add_case.html',args)

def list_lawyer(request):
    result = Lawyer.objects.all()
    context = {'result': result}
    return render_to_response('accounts3/list_lawyer.html', context)

def list_lawyer(request):
    istekler = Lawyer.objects.all()
    return render(request, 'accounts3/list_lawyer.html', locals())

def login_victim(request):
    args = {'user':request.user}
    return render(request,'accounts3/login_victim.html',args)

def login_lawyer(request):
    args = {'user':request.user}
    return render(request,'accounts3/login_lawyer.html',args)

def login_police(request):
    args = {'user':request.user}
    return render(request,'accounts3/login_police.html',args)

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
