# Generated by Django 3.2.3 on 2021-09-18 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_profile_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='prof_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
    ]
