# Generated by Django 4.2.2 on 2023-06-27 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("voc", "0002_alter_centertb_cent_name"),
        ("users", "0002_remove_engineertb_phonenum"),
    ]

    operations = [
        migrations.AddField(
            model_name="uidtb",
            name="cent_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="voc.centertb",
            ),
        ),
    ]
