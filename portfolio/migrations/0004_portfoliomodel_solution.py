# Generated by Django 3.2.4 on 2021-06-04 05:27

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20210603_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliomodel',
            name='solution',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='solution'),
        ),
    ]
