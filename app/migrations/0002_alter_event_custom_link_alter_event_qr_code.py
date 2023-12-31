# Generated by Django 4.2.4 on 2023-08-19 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='custom_link',
            field=models.CharField(help_text='Choose a memorable link name, e.g. mywedding, giftbirthday', max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='qr_code',
            field=models.CharField(editable=False, max_length=255, unique=True),
        ),
    ]
