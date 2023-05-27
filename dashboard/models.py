from django.db import models

# Create your models here.
class pegawai(models.Model):
    nama = models.CharField(max_length=225)
    alamat  = models.CharField(max_length=225)
    JENIS_KELAMIN   = (
        ('Laki-laki', 'laki-laki'),
        ('Perempuan', 'perempuan')
    )
    jenis_kelamin = models.CharField(max_length=225,choices=JENIS_KELAMIN)

    GOLONGAN_PEGAWAI = (
        ('Pembina 1', 'Pembina 1'),
        ('Pembina 2', 'Pembina 2'),
        ('Pembina 3', 'Pembina 3')
    )
    golongan = models.CharField(max_length=225, choices=GOLONGAN_PEGAWAI)

    def __str__(self):
        return self.nama

class dokumen(models.Model):
    no = models.CharField('Enter of Number',max_length=225)
    date  = models.DateTimeField(auto_now_add = True)
    name = models.CharField('Enter full name',max_length=225)
    activity = models.CharField('Enter detail activity',max_length=225)
    quantity = models.IntegerField('Enter of Quantity',max_length=25)
    img_file = models.FileField(upload_to='images/')

    def __str__(self):
        return self.no
