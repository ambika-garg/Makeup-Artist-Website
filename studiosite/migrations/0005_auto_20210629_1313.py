# Generated by Django 3.2.4 on 2021-06-29 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studiosite', '0004_auto_20210628_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reveiw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Makeup_reveiw', models.CharField(choices=[('BRIDAL MAKEUP', 'BRIDAL MAKEUP'), ('SKIN CONSULTANCY', 'SKIN CONSULTANCY'), ('PARTY MAKEUP', 'PARTY MAKEUP'), ('SELF GROOMING', 'SELF GROOMING'), ('PROFESSIONAL MAKEUP COURSE', 'PROFESSIONAL MAKEUP CLASS'), ('EVENT MAKEUP', 'EVENT MAKEUP')], max_length=100)),
                ('Reveiw_field', models.TextField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Enquiry',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='Contact_no',
        ),
        migrations.AddField(
            model_name='feedback',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Feedback',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]