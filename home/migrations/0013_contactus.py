# Generated by Django 4.2.3 on 2023-12-04 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
