# Generated by Django 3.2.4 on 2021-06-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210603_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='image'),
        ),
    ]
