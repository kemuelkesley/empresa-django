# Generated by Django 4.2.5 on 2023-09-23 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='empresa.pessoa')),
                ('matricula', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            bases=('empresa.pessoa',),
        ),
    ]
