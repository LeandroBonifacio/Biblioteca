# Generated by Django 3.1.7 on 2021-05-25 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0007_autor_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
