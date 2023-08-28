# Generated by Django 4.2.2 on 2023-06-30 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("voc", "0008_alter_customertb_tm_judge"),
        (
            "construction",
            "0003_constructiontb_cstrcall_constructiontb_receipt_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="constructiontb",
            name="cent",
        ),
        migrations.AddField(
            model_name="constructioncalltb",
            name="cent",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="voc.centertb",
            ),
            preserve_default=False,
        ),
    ]