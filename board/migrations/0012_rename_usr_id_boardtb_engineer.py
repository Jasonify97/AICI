# Generated by Django 4.2.2 on 2023-07-03 16:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0011_alter_uploadfile_file"),
    ]

    operations = [
        migrations.RenameField(
            model_name="boardtb",
            old_name="usr_id",
            new_name="engineer",
        ),
    ]
