# Generated by Django 4.0.3 on 2022-03-13 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_cafemenu_cafe_alter_hotelmenu_hotel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelmenu',
            name='hotel',
        ),
        migrations.AddField(
            model_name='hotelmenu',
            name='hotel',
            field=models.ManyToManyField(to='app.hotel'),
        ),
    ]
