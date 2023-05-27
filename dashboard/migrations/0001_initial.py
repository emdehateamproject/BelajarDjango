# Generated by Django 4.2.1 on 2023-05-21 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pegawai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=225)),
                ('alamat', models.CharField(max_length=225)),
                ('jenis_kelamin', models.CharField(choices=[('Laki-laki', 'laki-laki'), ('Perempuan', 'perempuan')], max_length=225)),
                ('golongan', models.CharField(choices=[('Pembina 1', 'Pembina 1'), ('Pembina 2', 'Pembina 2'), ('Pembina 3', 'Pembina 3')], max_length=225)),
            ],
        ),
    ]
