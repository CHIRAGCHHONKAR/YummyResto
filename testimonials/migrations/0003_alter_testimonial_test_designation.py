# Generated by Django 4.2.3 on 2023-09-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_alter_testimonial_test_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='test_designation',
            field=models.TextField(),
        ),
    ]
