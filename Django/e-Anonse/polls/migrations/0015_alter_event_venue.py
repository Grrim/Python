# -*- coding: utf-8 -*-

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_alter_event_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='polls.models.Kategorie'),
        ),
    ]
