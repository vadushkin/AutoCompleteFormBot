# Generated by Django 4.1.7 on 2023-03-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedtaskpicture',
            name='status',
            field=models.CharField(choices=[(0, 'Executed'), (1, 'Done')], default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='completedtaskpicture',
            name='path_for_picture',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='completedtaskpicture',
            name='user_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
