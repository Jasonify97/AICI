# Generated by Django 4.2.2 on 2023-06-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0002_remove_boardtb_id_alter_boardtb_brd_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="boardtb",
            name="brd_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
