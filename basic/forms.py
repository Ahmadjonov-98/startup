from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import *


class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control mt-2', 'name': 'password1', 'placeholder': 'enter the password...'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control mt-2', 'name': 'password2', 'placeholder': 'Repeat the password...'}))

    class Meta:
        model = CustomUser
        fields = ('full_name', 'email', 'user_type', 'phone', 'password1', 'password2', 'username')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control mt-2', 'name': 'full_name'}),
            'username': forms.TextInput(attrs={'class': 'form-control mt-2', 'name': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-2', 'name': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mt-2', 'name': 'phone'}),
            'user_type': forms.Select(attrs={'class': 'form-control mt-2', 'name': 'user_type'}),
        }


class AllUserAccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        #         fields = '__all__'
        fields = ('full_name', 'email', 'user_type', 'phone', 'username')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control mt-2', 'name': 'full_name'}),
            'username': forms.TextInput(attrs={'class': 'form-control mt-2', 'name': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-2', 'name': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mt-2', 'name': 'phone'}),
            'user_type': forms.Select(attrs={'class': 'form-control mt-2', 'name': 'user_type'}),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(label=("Login"), widget=forms.TextInput(
        attrs={'class': 'form-control text-dark', 'placeholder': 'loginni kiriting...', 'autofocus': True}))
    password = forms.CharField(label=("Parol"), strip=False, widget=forms.PasswordInput(
        attrs={'autofocus': 'current-password', 'class': 'form-control text-dark',
               'placeholder': 'parolni kiriting...'}))

    class Meta:
        model = login
        fields = "__all__"


class SimpleCustomForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'email', 'user_type', 'phone')
        labels = {'username': 'Username', 'full_name': 'full_name', 'email': 'email', 'user_type': 'user_type',
                  'phone': 'phone'}
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control mt-2 disabled', 'name': 'username', 'disabled': 'username'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control mt-2', 'name': 'full_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-2', 'name': 'email'}),
            'user_type': forms.Select(
                attrs={'class': 'form-control mt-2', 'name': 'user_type', 'disabled': 'user_type'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mt-2', 'name': 'phone'}),
        }


class StartapperAccountForm(forms.ModelForm):
    class Meta:
        model = Startapper
        fields = ['bio', 'country', 'image', ]
        labels = {'user': 'Full name', 'bio': 'Bio', 'country': 'Country', 'image': 'image'}
        widgets = {'user': forms.TextInput(attrs={'class': 'form-control'}),
                   'bio': forms.Textarea(attrs={'class': 'form-control'}),
                   'country': forms.Select(attrs={'class': 'form-control mt-2', 'name': 'country'}),
                   'image': forms.FileInput(attrs={})
                   }


class DeveloperAccountorm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['bio', 'country', 'image', ]
        labels = {'user': 'Full name', 'bio': 'Bio', 'country': 'Country', 'image': 'image'}
        widgets = {'user': forms.TextInput(attrs={'class': 'form-control'}),
                   'bio': forms.Textarea(attrs={'class': 'form-control'}),
                   'country': forms.Select(attrs={'class': 'form-control mt-2', 'name': 'country'}),
                   'image': forms.FileInput(attrs={})
                   }


class IdeaStartApperForm(forms.ModelForm):
    class Meta:
        model = IdeaStartapper
        fields = ['title', 'description', 'file']
        labels = {'title': 'Title', 'description': 'Description', 'file': 'file'}


class ApplicationDeveloperForm(forms.ModelForm):
    class Meta:
        file = forms.FileField()
        model = ApplicationStaff
        fields = ['title', 'description', 'resume', 'work_type']

        widgets = {
            'work_type': forms.Select(
                attrs={'class': "form-control"}
            )
        }
        labels = {'title': 'Title', 'description': 'description', 'resume': 'resume'}


class ApplicationPractitionerForm(forms.ModelForm):
    class Meta:
        model = ApplicationStaff
        fiele = forms.FileField()
        fields = ['title', 'description', 'resume', 'work_type']

        widgets = {
            'work_type': forms.Select(
                attrs={'class': "form-control"}
            )
        }
        labels = {'title': 'Title', 'description': 'description', 'resume': 'resume'}


class AllUserIdeaForm(forms.ModelForm):
    class Meta:
        model = AllUsersIdea
        exclude = ('user', 'created_at')




# class DeveloperApplicationForm(forms.ModelForm):
#     class Meta:
#         model = ApplicationStaff
#         fields = ['title', 'description', 'resume', 'work_type']
#         labels = {'title': 'Title', 'description': 'Description', 'resume': 'Resume', 'work_type': 'Work_type'}
#         widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
#                    'description': forms.Textarea(attrs={'class': 'form-control'}),
#                    'resume': forms.FileInput(attrs={'class': 'form-control'}),
#                    'work_type': forms.Select(attrs={'class': 'form-control mt-2', 'name': 'work_type'}),
#
#                    }

# class CustomUserForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('full_name', 'email', 'user_type','phone', 'password1', 'password2','username')
#         widgets = { 
#             'user_type':forms.Select(attrs={'class': 'form-control mt-2'}), 
#         }

# class CustomUserForm(forms.Form):
#     full_name = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(attrs={
#             'name':'full_name',
#             'class':'form-control',
#             'required':'required'
#         })
#     )

#     user_type = forms.Select(
#     )

#     email = forms.EmailField(
#         max_length=40,
#         widget=forms.EmailInput(attrs={
#             'name':'email',
#             'class':'form-control',
#             'placeholder':'elektronpochta@gmail.com',
#             'required':'required'
#         })
#     )

#     username = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(attrs={
#             'name':'username',
#             'class':'form-control',
#             'id':'usernameInput',
#             'placeholder':'Loginni kiriting va eslab qoling..',
#             'required':'required'
#         })
#     )

#     phone = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(attrs={
#             'name':'phone',
#             'class':'form-control',
#             'id':'usernameInput',
#             'placeholder':'Loginni kiriting va eslab qoling..',
#             'required':'required'
#         })
#     )

#     password1 = forms.CharField(
#         max_length=30,
#         widget=forms.PasswordInput(attrs={
#             'name':'password1',
#             'class':'form-control',
#             'id':'InputPassword',
#             'placeholder':'Parolni kiriting va eslab qoling..',
#             'required':'required'
#         })
#     )

#     password2 = forms.CharField(
#         max_length=30,
#         widget=forms.PasswordInput(attrs={
#             'name':'password2',
#             'class':'form-control',
#             'id':'InputPassword',
#             'placeholder':'Parolni qayta kiriting..',
#             'required':'required'
#         })
#     )
