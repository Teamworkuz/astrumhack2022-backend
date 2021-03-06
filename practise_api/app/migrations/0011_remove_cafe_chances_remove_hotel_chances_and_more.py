# Generated by Django 4.0.3 on 2022-03-13 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_cafe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='chances',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='chances',
        ),
        migrations.RemoveField(
            model_name='restourant',
            name='chances',
        ),
        migrations.AddField(
            model_name='cafe',
            name='t',
            field=models.CharField(choices=[('HOTEL', 'Hotel'), ('RESTOURANT', 'Restourant'), ('CAFE', 'Cafe')], default='Cafe', max_length=50),
        ),
        migrations.AddField(
            model_name='hotel',
            name='t',
            field=models.CharField(choices=[('HOTEL', 'Hotel'), ('RESTOURANT', 'Restourant'), ('CAFE', 'Cafe')], default='Hotel', max_length=50),
        ),
        migrations.AddField(
            model_name='restourant',
            name='t',
            field=models.CharField(choices=[('HOTEL', 'Hotel'), ('RESTOURANT', 'Restourant'), ('CAFE', 'Cafe')], default='Restourant', max_length=50),
        ),
    ]
