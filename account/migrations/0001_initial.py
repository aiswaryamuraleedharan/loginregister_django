# Generated by Django 4.0.6 on 2022-08-02 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=50)),
                ('phonenumber', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
