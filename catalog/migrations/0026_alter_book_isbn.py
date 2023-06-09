# Generated by Django 4.2 on 2023-04-25 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_auto_20220222_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, null=True, unique=True, verbose_name='ISBN'),
        ),
    ]
