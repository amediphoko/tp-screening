# Generated by Django 2.1.1 on 2018-10-16 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp_screening', '0008_auto_20181016_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantscreening',
            name='guardian',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Does subject have a guardian available?, If minor'),
        ),
    ]
