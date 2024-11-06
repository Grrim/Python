from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this
    
class Categorie(models.Model):
    name = models.CharField('Category Name', max_length=120)
    image = models.ImageField(upload_to='static', null=True, blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Kategorie"
  
class Profil(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60)
    prof_picture = models.ImageField(upload_to='static', null=True, blank=True)
    def __str__(self):
        return str(self.name)
    
    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
    	if created:
            Profil.objects.create(name=instance)

    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
    	instance.profil.save()
    
class Announcement(models.Model):
    name = models.CharField('Announcement Name', max_length=120)
    event_date = models.DateTimeField('Announcement Date', default=timezone.now, editable=False)
    venue = models.ForeignKey(Categorie, blank=True, null=True, on_delete=models.CASCADE)
    #vanue = models.CharField(max_length=120)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    cost = models.CharField('Cost', max_length=120)
    image = models.ImageField(upload_to='static', null=True, blank=True)
    description = models.TextField(blank=True)
    avatar = models.ForeignKey(Profil, blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Ogłoszenia"
