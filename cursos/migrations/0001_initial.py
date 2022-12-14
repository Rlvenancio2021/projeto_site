# Generated by Django 4.1.1 on 2022-09-12 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_instituicao', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('C', 'Concluído'), ('E', 'Estudando'), ('S', 'Suspenso')], default='E', max_length=1)),
                ('categoria', models.CharField(choices=[('P', 'Presencial'), ('D', 'Distância')], default='D', max_length=1)),
                ('area_estudo', models.CharField(choices=[('F', 'Finanças'), ('T', 'Tecnologia da Informação'), ('O', 'Outros')], max_length=1)),
                ('linguagem', models.CharField(default='Não se aplica', max_length=50)),
                ('nome_curso', models.CharField(max_length=50)),
                ('nome_extenso', models.TextField()),
                ('tecnologia', models.TextField()),
                ('inicio', models.DateField()),
                ('conclusao', models.DateField()),
                ('carga_horaria', models.IntegerField()),
                ('url_certificado', models.URLField()),
            ],
        ),
    ]
