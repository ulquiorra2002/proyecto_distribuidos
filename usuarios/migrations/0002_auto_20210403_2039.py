# Generated by Django 3.1.7 on 2021-04-03 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='numero_documento',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]