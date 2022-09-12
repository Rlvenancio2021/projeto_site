# Generated by Django 4.1.1 on 2022-09-12 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carreira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa_fonetico', models.CharField(max_length=20)),
                ('nome_empresa', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=50)),
                ('funcao', models.TextField()),
                ('inicio', models.DateField()),
                ('fim', models.DateField()),
                ('empresa_atual', models.BooleanField(default=True)),
            ],
        ),
    ]