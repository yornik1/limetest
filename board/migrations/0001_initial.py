# Generated by Django 2.2.2 on 2019-06-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('status', models.IntegerField(choices=[(0, 'TO DO'), (1, 'In Progress'), (2, 'Done')], default=0)),
            ],
        ),
    ]
