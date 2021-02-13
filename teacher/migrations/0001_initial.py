# Generated by Django 3.1.6 on 2021-02-13 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('department', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('BBA', 'BBA')], max_length=15)),
                ('designation', models.CharField(max_length=55)),
                ('email', models.EmailField(max_length=60)),
            ],
        ),
    ]
