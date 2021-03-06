# Generated by Django 3.2.4 on 2021-06-04 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FactsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='title')),
                ('title_en_us', models.CharField(max_length=20, null=True, verbose_name='title')),
                ('title_uz', models.CharField(max_length=20, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=20, null=True, verbose_name='title')),
                ('number', models.IntegerField(verbose_name='number')),
            ],
            options={
                'verbose_name': 'fact',
                'verbose_name_plural': 'facts',
            },
        ),
        migrations.CreateModel(
            name='TeamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='team', verbose_name='image')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('name_en_us', models.CharField(max_length=30, null=True, verbose_name='name')),
                ('name_uz', models.CharField(max_length=30, null=True, verbose_name='name')),
                ('name_ru', models.CharField(max_length=30, null=True, verbose_name='name')),
                ('job', models.CharField(max_length=30, verbose_name='job')),
                ('job_en_us', models.CharField(max_length=30, null=True, verbose_name='job')),
                ('job_uz', models.CharField(max_length=30, null=True, verbose_name='job')),
                ('job_ru', models.CharField(max_length=30, null=True, verbose_name='job')),
                ('instagram', models.CharField(blank=True, max_length=100, null=True, verbose_name='instagram')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True, verbose_name='facebook')),
                ('twitter', models.CharField(blank=True, max_length=100, null=True, verbose_name='twitter')),
                ('linked', models.CharField(blank=True, max_length=100, null=True, verbose_name='linked')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'team',
                'verbose_name_plural': 'teams',
            },
        ),
    ]
