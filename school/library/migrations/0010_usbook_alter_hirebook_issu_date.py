# Generated by Django 4.0.3 on 2022-04-21 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_alter_record_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='usbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=150)),
                ('book_name', models.CharField(max_length=100)),
                ('book_id', models.IntegerField()),
                ('issue_date', models.DateField()),
                ('due', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='hirebook',
            name='issu_date',
            field=models.DateField(max_length=100),
        ),
    ]
