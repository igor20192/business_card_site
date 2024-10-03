# Generated by Django 5.1.1 on 2024-10-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_card_app', '0008_eventblock_button_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventblock',
            name='button_text',
        ),
        migrations.AddField(
            model_name='eventblock',
            name='title_mobile',
            field=models.CharField(default='EVENT', max_length=50, verbose_name='Заголовок мобильной (version)'),
        ),
    ]
