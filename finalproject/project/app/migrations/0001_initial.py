# Generated by Django 4.2.1 on 2023-07-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('fprice', models.IntegerField()),
                ('fdetails', models.CharField(max_length=50)),
                ('fimg', models.ImageField(upload_to='')),
            ],
        ),
    ]
