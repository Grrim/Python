# Generated by Django 3.2.3 on 2021-09-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='static'),
        ),
    ]