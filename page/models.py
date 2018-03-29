from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.forms import ModelForm
import django_tables2 as tables
from django_tables2 import SingleTableView

class Victim(User):
    #grp_id = 1
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=100)

class Lawyer(User):

    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=100)

    previous_cases = models.CharField(max_length=200)
    #case_status = models.BooleanField(initial=False)
    fees = models.IntegerField(default=0)
    #case_details = models.CharField(max_length=1000)

    def __unicode__(self):
        return u"%s" % self.user

class Police(User):

    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=100)

    cases_registered = models.CharField(max_length=100)
    #case_status = models.BooleanField(initial=False)
    #case_details = models.TextField(max_length=1000)

class VictimCase(models.Model):
    victim = models.ForeignKey(User,on_delete=models.CASCADE,related_name="victims")
    #lawyer = models.ForeignKey(User,on_delete=models.CASCADE,related_name="lawyers",default='')
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class Case(models.Model):
    text = models.CharField(max_length = 1000)
    victim_name = models.CharField(max_length = 100)
    lawyer_name = models.CharField(max_length = 100)
    police_name = models.CharField(max_length = 100)

""""
class LawyerTable(tables.Table):
    class Meta:
        model = Lawyer


class LawyerList(SingleTableView):
    model = Lawyer
    table_class = LawyerTable

class VictimForm(ModelForm):
    class Meta:
        model = Victim
        fields = ['username', 'phone', 'address','password']

class LawyerForm(ModelForm):
    class Meta:
        model = Lawyer
        fields = ['username', 'phone', 'address','password','previous_cases','fees']

class PoliceForm(ModelForm):
    class Meta:
        model = Police
        fields = ['username', 'phone', 'address','password','case_registered']


# Create your models here.
class User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=100,default='')
    phone = models.IntegerField(default=0)
    #grp_id = models.IntegerField(default=1)

    #enter the user profile only after it login the system
    def create_profile(sender,**kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile,sender=User)


"""
    