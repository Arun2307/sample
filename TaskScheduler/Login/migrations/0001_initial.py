# Generated by Django 4.2.4 on 2023-08-06 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=100)),
                ('UserName', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('Created_date', models.DateField()),
            ],
        ),
    ]
