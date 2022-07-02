"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from polls import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('', views.home_view, name="home"),
    path('home', views.home_view, name="home"),
    path("admin", admin.site.urls, name="admin"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("ogłoszenia", views.items_view, name="ogłoszenia"),
    path("ogłoszenie\<announcement_id>", views.show_item_view, name="ogłoszenie"),
    path("kategoria/<category_id>", views.show_category_view, name="kategoria"),
    path("search", views.search_view, name="search"),
    path("dodaj_ogłoszenie", views.add_event_view, name="dodaj_ogłoszenie"),
    path("zmodyfikuj_ogłoszenie\<announcement_id>", views.update_event_view, name="zmodyfikuj_ogłoszenie"),
    path("usuń_ogłoszenie\<announcement_id>", views.delete_event_view, name="usuń_ogłoszenie"),
    path("kategorie", views.category_view, name='kategorie'),
    path("profile/<int:pk>", views.ShowProfile.as_view(), name='profile'),
    path("profile_items\<profile_id>", views.profile_items_view, name='profile_items'),
    path("edit_profile", views.edit_profile, name="edit_profile"),
    path("password/", views.PasswordsChangeView.as_view(template_name="edit_password.html"), name="edit_password"),
    path("password_success", views.password_success, name="password_success"),
    path("edit_success", views.edit_success, name="edit_success"),
    path('es', TemplateView.as_view(template_name="google.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('messages/', include('postman.urls'), name='postman'),
    path('o_nas', views.o_nas_view, name="o_nas"),
    #path('write/', include('postman.urls'), name="postman"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

