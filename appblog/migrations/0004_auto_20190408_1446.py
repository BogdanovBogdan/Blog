# Generated by Django 2.2 on 2019-04-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0003_auto_20190408_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='appblog.Tag'),
        ),
    ]
