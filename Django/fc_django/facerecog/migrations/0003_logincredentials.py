# Generated by Django 3.0 on 2020-01-24 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facerecog', '0002_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginCredentials',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=256)),
                ('lastname', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'LoginCredentials',
            },
        ),
    ]
