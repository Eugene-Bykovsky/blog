# Generated by Django 4.1.13 on 2023-12-11 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('slug', 'publish')},
        ),
    ]
