# Generated by Django 4.2.3 on 2023-12-02 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliverProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderd_at', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('paymentmod', models.CharField(default='COD', max_length=50)),
                ('total_amount', models.IntegerField()),
                ('Status', models.CharField(default='pending', max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.products')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
