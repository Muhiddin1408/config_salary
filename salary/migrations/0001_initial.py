# Generated by Django 4.0.3 on 2022-03-09 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=125)),
                ('phone', models.CharField(max_length=12)),
                ('age', models.IntegerField(default=0)),
                ('job', models.CharField(max_length=125)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('salary', models.IntegerField(default=0)),
                ('telegram_id', models.CharField(max_length=125)),
                ('bons', models.IntegerField(default=0)),
                ('fine', models.IntegerField(default=0)),
                ('give', models.IntegerField(default=0)),
                ('residue', models.IntegerField(default=0)),
                ('step', models.IntegerField(default=0)),
                ('clock_in', models.TimeField(blank=True, null=True)),
                ('clock_out', models.TimeField(blank=True, null=True)),
                ('month', models.CharField(blank=True, max_length=125, null=True)),
                ('image', models.CharField(blank=True, max_length=125, null=True)),
                ('type', models.CharField(blank=True, max_length=12, null=True)),
                ('status', models.CharField(blank=True, choices=[('true', 'TRUE'), ('false', 'FALSE')], default='true', max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clock_in', models.TimeField(blank=True, null=True)),
                ('clock_out', models.TimeField(blank=True, null=True)),
                ('work', models.IntegerField(blank=True, null=True)),
                ('month', models.CharField(blank=True, max_length=125, null=True)),
                ('worker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='salary.workers')),
            ],
        ),
    ]