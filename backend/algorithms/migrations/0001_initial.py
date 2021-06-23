# Generated by Django 3.2.4 on 2021-06-20 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Preset',
                'verbose_name_plural': 'Presets',
            },
        ),
        migrations.CreateModel(
            name='RequestSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField()),
                ('seniority_level', models.IntegerField()),
                ('preset_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='algorithms.preset', verbose_name='preset')),
                ('skill_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='skills.skill', verbose_name='skill')),
            ],
            options={
                'verbose_name': 'EmployeeSkill',
                'verbose_name_plural': 'EmployeeSkills',
            },
        ),
    ]
