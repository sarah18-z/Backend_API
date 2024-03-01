# Generated by Django 5.0.2 on 2024-03-01 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_remove_book_category_remove_book_language_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('Phone_number', models.CharField(max_length=10)),
                ('user_email', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='is_borrowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Library.user'),
        ),
    ]