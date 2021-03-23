# Generated by Django 3.1.7 on 2021-03-23 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion_cliente', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id_etapa', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'etapa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Experto',
            fields=[
                ('id_experto', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo_experto', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion_experto', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'experto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inversion',
            fields=[
                ('id_inversion', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'inversion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inversionista',
            fields=[
                ('id_inversionista', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo_inversionista', models.CharField(blank=True, max_length=45, null=True)),
                ('empresa_inversionista', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'inversionista',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id_persona', models.IntegerField(primary_key=True, serialize=False)),
                ('numero_documento_persona', models.CharField(blank=True, max_length=45, null=True)),
                ('direccion_persona', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id_proyecto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_proyecto', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion_proyecto', models.CharField(blank=True, max_length=200, null=True)),
                ('financiamiento_proyecto', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'proyecto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id_tipo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_tabla', models.CharField(blank=True, max_length=45, null=True)),
                ('nombre_tipo', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion_tipo', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tipo',
                'managed': False,
            },
        ),
    ]
