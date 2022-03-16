# Generated by Django 4.0.3 on 2022-03-16 19:33

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('goodreads_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(max_length=255)),
                ('on_sale_date', models.DateField(blank=True, null=True)),
                ('flat_cover_image', models.CharField(blank=True, max_length=255, null=True)),
                ('book_mockup', models.CharField(blank=True, max_length=255, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.publisher')),
                ('territory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.territory')),
            ],
        ),
        migrations.CreateModel(
            name='BuyLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retailer_name', models.CharField(blank=True, max_length=255)),
                ('retailer_url', models.URLField(blank=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_links', to='books.book')),
            ],
        ),
        migrations.CreateModel(
            name='Blurb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribution_name', models.CharField(blank=True, max_length=255)),
                ('attribution_description', ckeditor.fields.RichTextField(blank=True)),
                ('blurb_content', ckeditor.fields.RichTextField(blank=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blurbs', to='books.book')),
            ],
        ),
    ]
