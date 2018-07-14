# Generated by Django 2.0.6 on 2018-06-28 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookOrderSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=880)),
                ('author', models.CharField(blank=True, max_length=512)),
                ('keyword', models.CharField(blank=True, max_length=512)),
                ('isbn', models.PositiveIntegerField(blank=True)),
            ],
        ),
    ]
