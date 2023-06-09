# Generated by Django 4.2 on 2023-05-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProtocolDataAddLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.TextField(blank=True, max_length=40, null=True, verbose_name='No')),
                ('item', models.TextField(max_length=1000, verbose_name='Item')),
                ('responsible', models.TextField(blank=True, max_length=100, null=True, verbose_name='Responsible')),
                ('deadline', models.TextField(blank=True, max_length=100, null=True, verbose_name='Deadline')),
                ('status', models.TextField(blank=True, max_length=100, null=True, verbose_name='Status')),
            ],
        ),
    ]
