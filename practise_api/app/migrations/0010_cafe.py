# Generated by Django 4.0.3 on 2022-03-13 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0009_alter_restourant_dostavka'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.TextField(null=True)),
                ('rate', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=50)),
                ('adress', models.CharField(max_length=100)),
                ('chances', models.CharField(choices=[('NETWORK', 'Network'), ('EAT', 'Eat'), ('SWIM', 'Swim'), ('FITNESS', 'Fitness')], max_length=50)),
                ('photo1', models.ImageField(upload_to='hotel_photos/')),
                ('photo2', models.ImageField(upload_to='re_photos/')),
                ('photo3', models.ImageField(upload_to='cafe_photos/')),
                ('cost', models.IntegerField(default=0)),
                ('phone_num', models.BigIntegerField(null=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Activ'), ('NOT_ACTIVE', 'Not_Active')], default='Active', max_length=50)),
                ('ig', models.CharField(max_length=100, null=True)),
                ('tg', models.CharField(max_length=100, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
