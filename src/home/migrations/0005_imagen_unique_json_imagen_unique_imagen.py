# Generated by Django 5.1.5 on 2025-02-03 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_imagen_table'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='imagen',
            constraint=models.UniqueConstraint(fields=('json',), name='unique_json'),
        ),
        migrations.AddConstraint(
            model_name='imagen',
            constraint=models.UniqueConstraint(fields=('imagen',), name='unique_imagen'),
        ),
    ]
