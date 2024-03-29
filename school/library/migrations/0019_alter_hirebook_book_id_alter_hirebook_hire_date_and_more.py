# Generated by Django 4.0.3 on 2022-05-25 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_alter_hirebook_due2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hirebook',
            name='book_id',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='hirebook',
            name='hire_date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='hirebook',
            name='issu_date',
            field=models.DateField(blank=True, max_length=100),
        ),
    ]
