# Generated by Django 3.2.4 on 2021-06-03 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('subject', models.CharField(blank=True, max_length=30, null=True, verbose_name='subject')),
                ('message', models.TextField(verbose_name='message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contact',
            },
        ),
    ]