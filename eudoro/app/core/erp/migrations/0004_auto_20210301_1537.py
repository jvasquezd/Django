# Generated by Django 3.1.7 on 2021-03-01 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_auto_20210228_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='igv',
            field=models.DecimalField(db_column='sal_igv', decimal_places=2, default=0.0, max_digits=9),
        ),
    ]