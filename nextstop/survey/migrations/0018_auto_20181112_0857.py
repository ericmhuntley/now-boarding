# Generated by Django 2.1.2 on 2018-11-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0017_auto_20181112_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='gender',
            field=models.CharField(choices=[(None, 'Not specified'), ('male', 'Male'), ('female', 'Female'), ('nonbinary', 'Nonbinary')], default='nonbinary', help_text='Gender identity.', max_length=200, null=True),
        ),
    ]
