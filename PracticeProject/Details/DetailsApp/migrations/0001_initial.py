# Generated by Django 3.2 on 2021-05-17 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=30)),
                ('Phone_No', models.IntegerField()),
                ('Password', models.CharField(max_length=20)),
            ],
        ),
    ]
