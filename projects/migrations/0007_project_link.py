# Generated by Django 2.2.5 on 2019-09-15 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20190914_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(default='https://github.com/TR-1000', max_length=250),
        ),
    ]
