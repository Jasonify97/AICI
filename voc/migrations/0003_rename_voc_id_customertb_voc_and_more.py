# Generated by Django 4.2.2 on 2023-06-27 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("voc", "0002_alter_centertb_cent_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customertb",
            old_name="voc_id",
            new_name="voc",
        ),
        migrations.RenameField(
            model_name="voctb",
            old_name="cent_id",
            new_name="cent",
        ),
    ]
