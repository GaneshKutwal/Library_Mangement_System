# Generated by Django 4.0.3 on 2022-04-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_hirebook_hire_date_alter_hirebook_issu_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hirebook',
            name='hire_date',
        ),
        migrations.AlterField(
            model_name='hirebook',
            name='issu_date',
            field=models.DateField(),
        ),
    ]
