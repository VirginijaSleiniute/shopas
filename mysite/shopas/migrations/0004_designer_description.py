# Generated by Django 4.0.5 on 2022-07-08 09:38

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopas', '0003_order_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='designer',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
