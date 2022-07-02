from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import login
from django.views import generic
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from .models import Announcement, Categorie, Profil
from .forms import AnnouncementForm, NewUserForm, EditProfileForm, EditProfilePassword, LoginForm, ProfileForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from allauth.account.adapter import DefaultAccountAdapter

ACCOUNT_ADAPTER = 'kvizmaster.adapter.MyAccountAdapter'

class MyAccountAdapter(DefaultAccountAdapter):
    
    def get_login_redirect_url(self, request):
        print("in code")
        redirect_to = request.GET.get('next', '')
        print(redirect_to)
        return redirect(redirect_to)

class PasswordsChangeView(PasswordChangeView):
    form_class = EditProfilePassword
    success_url = reverse_lazy('password_success')
    
def password_success(request):
    messages.info(request, "Hasło zmienione pomyslnie") 
    return redirect('edit_password')
   
def password_succes(request):
    messages.info(request, "Hasło zmienione pomyslnie") 
    return HttpResponseRedirect('/home')
   
def edit_profile(request):
    profil = Profil.objects.get(pk=request.user.id)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profil)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect("edit_success")
    return render(request, 'edit_profile.html', {'profil':profil,'form':form})

def edit_success(request):
    messages.info(request, "Informacje zmienione pomyslnie") 
    return redirect('edit_profile')

def add_event_view(request, *args, **kwargs):
    submitted = False
    
    if request.method == "POST":
        form = AnnouncementForm(request.POST, request.FILES, initial={'avatar': request.user})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dodaj_ogłoszenie?submitted=True')
    else:
        form = AnnouncementForm(initial={'avatar': request.user})
        if 'submitted' in request.GET:
            submitted = True
            
    return render(request, 'dodaj_ogłoszenie.html', {'avatar': request.user, 'form':form, 'submitted':submitted})

def home_view(request, *args, **kwargsuest):
    categorie_list = Categorie.objects.all()
    p = Paginator(Categorie.objects.all(), 8)
    page = request.GET.get('page')
    categories = p.get_page(page)
    nums = "a" * categories.paginator.num_pages
    
    announcement_list = Announcement.objects.all().order_by('-event_date')[:12:1]
    return render(request, 'home.html', {"name": request.user.username, 'announcement_list':announcement_list,'categorie_list':categorie_list, 'categories':categories, 'nums':nums})

def o_nas_view(request, *args):
    return render(request, 'o_nas.html', {})

def homepage_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'homepage.html', {"name": request.user.username})

def category_view(request, *args, **kwargs):
    categorie_list = Categorie.objects.all()
    
    p = Paginator(Categorie.objects.all(),7)
    page = request.GET.get('page')
    categories = p.get_page(page)
    nums = "a" * categories.paginator.num_pages
    
    return render(request, 'kategorie.html', {'categorie_list':categorie_list, 'categories':categories, 'nums':nums})

def items_view(request):
    announcement_list = Announcement.objects.all()
    
    p = Paginator(Announcement.objects.all().order_by('-event_date'),7)
    page = request.GET.get('page')
    events = p.get_page(page)
    nums = "a" * events.paginator.num_pages
    
    return render(request, 'ogłoszenia.html', {'announcement_list':announcement_list, 'events':events, 'nums':nums})

def profile_items_view(request, profile_id):
    profile = User.objects.get(pk=profile_id)
    
    announcement_list = Announcement.objects.all().order_by('-event_date')
    
    p = Paginator(Announcement.objects.all().order_by('-event_date'), 7)
    page = request.GET.get('page')
    announcements = p.get_page(page)
    
    return render(request, 'show_profile_items.html', {'profile': profile, 'announcement_list':announcement_list, 'announcements':announcements})

def search_view(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        announcements = Announcement.objects.filter(name__contains=searched)
        return render(request, 'search.html',{'searched':searched, 'announcements':announcements})
    else:
        return render(request, 'search.html',{})

def update_event_view(request, announcement_id):
    announcement = Announcement.objects.get(pk=announcement_id)
    form = AnnouncementForm(request.POST or None, request.FILES or None, instance=announcement)
    if form.is_valid():
        form.save()
        messages.info(request, "Pomyslnie zmodyfikowałes ogłoszenie") 
        return redirect("ogłoszenia")
    return render(request, 'zmodyfikuj_ogłoszenie.html', {'announcement':announcement,'form':form})

def delete_event_view(request, announcement_id):
    announcement = Announcement.objects.get(pk=announcement_id)
    announcement.delete()
    return redirect('ogłoszenia')
 
def show_item_view(request, announcement_id):
    announcement = Announcement.objects.get(pk=announcement_id)
    return render(request, 'ogłoszenie.html', {'announcement': announcement})

def show_category_view(request, category_id):
    announcement_list = Announcement.objects.all().order_by('-event_date')

    return render(request, 'kategoria.html', {'announcement_list':announcement_list})

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
			#login(request, user)
            messages.success(request, "Rejestracja pomyslna")
            return redirect("home")
    else:
        form = NewUserForm()
    return render (request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = LoginForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Jestes teraz zalogowany jako {username}.")
				return redirect("/home")
			else:
				messages.error(request,"Nieprawidłowy nick lub hasło")
		else:
			messages.error(request,"Nieprawidłowy nick lub hasło")
	form = LoginForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Pomyslnie się wylogowałes") 
	return redirect("home")

def dashboard(request):
    return render(request, 'accounts/dashboard.html', {"name": request.user.first_name})

class ShowProfile(DetailView):
    model = Profil
    template_name = 'show_profile.html'

    def get_context_data(self, **kwargs):
        context = super(ShowProfile, self).get_context_data(**kwargs) 

        user = Profil.objects.get(id=self.request.user.id)
        context["page_user"] = user
        return context