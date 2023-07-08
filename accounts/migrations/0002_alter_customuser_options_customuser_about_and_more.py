# Generated by Django 4.2.3 on 2023-07-07 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={"verbose_name_plural": "Users"},
        ),
        migrations.AddField(
            model_name="customuser",
            name="about",
            field=models.CharField(default="Available", max_length=200),
        ),
        migrations.AddField(
            model_name="customuser",
            name="profile_picture",
            field=models.ImageField(blank=True, null=True, upload_to="profiles/"),
        ),
    ]
