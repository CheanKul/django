# Generated by Django 2.1.7 on 2019-03-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_auto_20190319_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('Address', models.TextField()),
                ('Posts', models.ManyToManyField(to='Posts.Post')),
            ],
        ),
    ]
