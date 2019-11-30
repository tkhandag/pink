from django.contrib.auth.models import User as User1





from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as User1

from healthcare.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(max_length=254, required=True,help_text='Required. Inform a valid email address.')

    class Meta:
        model = User1
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        def save(self,commit=True):
            user=super(SignUpForm,self).save(commit=False)
            user.first_name=self.cleaned_data['first_name']
            user.last_name=self.cleaned_data['last_name']
            user.email=self.cleaned_data['email']    
            if commit:
                user.save()
            return user