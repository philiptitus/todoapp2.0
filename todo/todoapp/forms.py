from  .models import User_info,Tlist
from django.contrib.auth.models import User
from django import forms


class New_User(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')



class UserProfileInfoform(forms.ModelForm):
    class Meta():
        model = User_info
        fields = ('instagram',)



class Task(forms.ModelForm):
    class Meta():
        model = Tlist
        fields = ('item','description')
        
