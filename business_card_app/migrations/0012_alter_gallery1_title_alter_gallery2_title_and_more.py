# Generated by Django 5.1.1 on 2024-10-06 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_card_app', '0011_alter_gallery1_description_alter_gallery1_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery1',
            name='title',
            field=models.CharField(default='Callery', max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='gallery2',
            name='title',
            field=models.CharField(default='Callery', max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='gallery3',
            name='title',
            field=models.CharField(default='Callery', max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='gallery4',
            name='title',
            field=models.CharField(default='Callery', max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='gallery5',
            name='title',
            field=models.CharField(default='Callery', max_length=255, verbose_name='Заголовок'),
        ),
    ]
