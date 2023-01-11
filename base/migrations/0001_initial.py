# Generated by Django 4.1.4 on 2022-12-15 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=255)),
                ('license_number', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=256)),
                ('role', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
