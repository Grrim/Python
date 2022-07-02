from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Announcement, Profil

# Create your forms here.

class NewUserForm(UserCreationForm):
    username = forms.CharField(label="Nazwa użytkownika", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args,**kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nazwa użytkownika", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username','password')
        
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(label="E-mail", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'type':'hidden'}))
    
    class Meta:
        model = Profil
        fields = ('email', 'prof_picture')
        
        labels = {
            'email': '',
            'zdjecie': 'Zdjęcie',
            }
        
class EditProfilePassword(PasswordChangeForm):
    old_password = forms.CharField(label="Podaj stare hasło", widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(label="Podaj nowe hasło", max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label="Powtórz nowe hasło", max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
            
            
class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ('name', 'venue', 'manager', 'cost', 'image', 'description', 'avatar')
        
        labels = {
            'name': '',
            'event_date':'YYYY-MM-DD HH:MM:SS',
            'venue': 'Kategoria',
            'manager': '',
            'cost': '',
            'image': 'Zdjęcie',
            'description': '',
            'avatar': '',
            }
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nazwa'}),
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event date'}),
            'venue': forms.Select(attrs={'class':'form-select'}),
            'manager':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            'cost': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cena'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Opis'}),
            'avatar':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            }    
        
class UserForm(forms.ModelForm):
    zdjęcie = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'zdjęcie')
        
        
class ProfileForm(ModelForm):
    
    class Meta: 
        model = Profil
        fields = ('prof_picture',)
        
        labels = {
            'prof_picture': 'Zdjęcie',
            }

    
