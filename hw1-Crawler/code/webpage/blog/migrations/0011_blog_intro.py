# Generated by Django 4.2.4 on 2023-09-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0010_word_doc"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="intro",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]