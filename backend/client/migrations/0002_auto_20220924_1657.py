# Generated by Django 3.2.12 on 2022-09-24 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='message',
        ),
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.CharField(default='9683c2a0-1b48-4c4e-82da-6ac47a391b52', help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True),
        ),
    ]
