# Generated by Django 4.1.7 on 2023-03-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedTaskPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('path_for_picture', models.CharField(max_length=200)),
            ],
        ),
    ]
