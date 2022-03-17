# Generated by Django 4.0.3 on 2022-03-16 20:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='hero_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hero',
            name='hero_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]