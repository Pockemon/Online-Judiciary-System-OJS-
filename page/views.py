from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from page.forms import RegistrationForm,VictimSignUpForm,LawyerSignUpForm,PoliceSignUpForm
from page.forms import UserLoginForm,EditProfileFormLawyer,EditProfileFormPolice,EditProfileFormVictim
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,AuthenticationForm
from django.contrib.auth import authenticate, login,get_user_model,logout
from page.models import Lawyer,Police,VictimCase,Victim,Case
from django.views.generic import CreateView,DeleteView,DetailView,UpdateView
from django.contrib import messages
from page.forms import LawyerForm, PoliceForm
#from django.core.context_processors import csrf

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
        return redirect('page:add_case')


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
        items = Case.objects.filter(victim_name__startswith = username)
        #print(request.user.is_authenticated)
        return render(request, 'accounts3/victim_home.html')
    return render(request,"accounts3/login_victim.html",{"form":form,"title":title,})


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
    return render(request,"accounts3/login_police.html",{"form":form,"title":title})


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
    return render(request,"accounts3/login_lawyer.html",{"form":form,"title":title})


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

def lawyer_case_details(request):
    if request.method =='POST':
        form = LawyerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts3/victim_home.html')
    else:
        form = LawyerForm()
        return render(request, 'accounts3/lawyer_case_details.html', {'form': form})

def police_case_details(request):
    if request.method =='POST':
        form = PoliceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'accounts3/victim_home.html')
    else:
        form = PoliceForm()
        return render(request, 'accounts3/police_case_details.html', {'form': form})


def victim_case(request):
    username = None
    #if request.user.is_authenticated():
    username = request.user.username
    items = Case.objects.filter(victim_name__startswith = username)
    return render(request, 'accounts3/victim_case.html', {'items':items})

def lawyer_case(request):
    username = None
    #if request.user.is_authenticated():
    username = request.user.username
    items = Case.objects.filter(lawyer_name__startswith = username)
    return render(request, 'accounts3/lawyer_case.html', {'items':items})

def police_case(request):
    username = None
    #if request.user.is_authenticated():
    username = request.user.username
    items = Case.objects.filter(police_name__startswith = username)
    return render(request, 'accounts3/police_case.html', {'items':items})

def edit_profile_victim(request):
    if request.method == 'POST':
        form = EditProfileFormVictim(request.POST, instance=request.user)
        #return redirect('victim_home')
        if form.is_valid():
            form.save()
            return render(request, 'accounts3/victim_home.html')
    else:
        form = EditProfileFormVictim(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts3/edit_profile_victim.html', {'form': form})

def edit_profile_lawyer(request):
    if request.method == 'POST':
        form = EditProfileFormLawyer(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'accounts3/lawyer_home.html')
    else:
        form = EditProfileFormLawyer(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts3/edit_profile_lawyer.html', {'form': form})

def edit_profile_police(request):
    if request.method == 'POST':
        form = EditProfileFormPolice(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'accounts3/police_home.html')
    else:
        form = EditProfileFormPolice(instance=request.user)
        #args = {'form': form}
    return render(request, 'accounts3/edit_profile_police.html', {'form': form})


'''class EditLawyer(UpdateView):
    model = Lawyer
    form_class = LawyerForm
    template_name = "accounts3/lawyer_case_details.html"

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user.userprofile

    def get_success_url(self, *args, **kwargs):
        return reverse("accounts3/lawyer_case_details.html")
'''

'''def lawyer_create(request, template_name="accounts3/lawyer_case_details.html"):
    if request.method == 'POST':
        form = LawyerForm(data=request.POST)
        if form.is_valid():
             lawyer = form.save(commit=False)
             user.save()
             return HttpResponseRedirect('login_victim/')#change this url and put url to victim homepage
    #if there is  nothing in the post array then we are creating the form
    else:
        form = LawyerForm()
    args = {}
        #args.update(csrf(request))
    args['form'] = form
    return render(request,'accounts3/lawyer_case_details.html',args)

def police_create(request):
    if request.method == 'POST':
        form = PoliceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('login_victim/') #Change this url and put url to victim homepage
    else:
        form = PoliceForm()
    args = {}
        #args.update(csrf(request))
    #args['form'] = form
    return render(request,'accounts3/police_case_details.html',{'form':form})
'''





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