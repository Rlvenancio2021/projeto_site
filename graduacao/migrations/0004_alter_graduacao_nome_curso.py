# Generated by Django 4.1.1 on 2022-09-12 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduacao', '0003_alter_graduacao_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduacao',
            name='nome_curso',
            field=models.CharField(max_length=50),
        ),
    ]
