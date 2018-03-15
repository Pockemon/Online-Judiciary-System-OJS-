from django.urls import path
from . import views
from django.contrib.auth.views import login,logout,password_reset,password_reset_done,password_reset_confirm,password_reset_complete
from django.views.generic import ListView, DetailView
from page.models import Lawyer,Police


app_name = 'page'

urlpatterns = [
   
   #for home page
   path('',views.home),
   
   #just for debugging
   #path('accounts3/home',views.home),

   path('victim_signup/', views.victim_signup, name='victim_signup'),
   path('lawyer_signup/', views.lawyer_signup, name='lawyer_signup'),
   path('police_signup/', views.police_signup, name='police_signup'),

   #homepage/login will open the login page for user
   #path('login1',views.login1,name='login1'),
   #path('login',login,{'template_name' : 'accounts3/login1.html'}),

   #just for debugging
   #path('login',login,{'template_name': 'accounts3/login.html'}),

   #homepage/logout will open the logout page 
   path('logout',logout,{'template_name': 'accounts3/logout.html'}),

   #homepage/register will open the signup page
#    path('register',views.register,name='register'),

   #just for debugging
   #path('add_case',add_case,{'template_name':'accounts3/add_case.html'}),

   #this will for displaying the profile of user
   #path('profile',views.view_profile,name='view_profile'),

   path('profile_victim',views.profile_victim,name='profile_victim'),
 
   path('profile_lawyer',views.profile_lawyer,name='profile_lawyer'),

   path('profile_police',views.profile_police,name='profile_police'),

   path('choice_home',views.choice_home,name='choice_home'),

   path('login_victim',views.login_victim,name='login_victim'),

   path('login_lawyer',views.login_lawyer,name='login_lawyer'),

   path('login_police',views.login_police,name='login_police'),

   #this will for victim 
   path('add_case',views.add_case,name='add_case'),

   #path('list_lawyer',views.list_lawyer,name='list_lawyer'),
   path('list_lawyer/',ListView.as_view(queryset=Lawyer.objects.all(),template_name="accounts3/list_lawyer.html")),

   path('list_police/',ListView.as_view(queryset=Police.objects.all(),template_name="accounts3/list_police.html")),

   path('victim_home',views.victim_home,name='victim_home'),

   path('lawyer_home',views.lawyer_home,name='lawyer_home'),

   path('police_home',views.police_home,name='victim_home'),

   path('case_victim',views.CaseCreateView.as_view(),name='case_victim'),

   #"just for debugging"
   #path('profile/edit',views.edit_profile,name="edit_profile"),
   #path('profile/change_password',views.change_password,name="change_password"),
   #path('profile/reset_password',password_reset,name='reset_password'),
   #path('profile/reset_password/done',password_reset_done,name='password_reset_done'),
   #path('profile/reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)',password_reset_confirm,name='password_reset_confirm'),
   #path('profile/reset_password/complete',password_reset_complete,name='password_reset_comlete'),
]

