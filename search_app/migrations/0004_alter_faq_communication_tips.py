# Generated by Django 5.0 on 2024-04-02 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("search_app", "0003_alter_faq_communication_tips"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faq",
            name="communication_tips",
            field=models.TextField(),
        ),
    ]
