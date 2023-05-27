from django.db import models

# Create your models here.
# class Register(models.Model):
#     username    = models.CharField(max_length=255)
#     email       = models.CharField(max_length=255)
#     password    = models.CharField(max_length=255)

#     def __str__(self):
#         return self.username

class Register(models.Model):
    
    email       = models.CharField(max_length=100)
    password    = models.CharField(max_length=100)
    first_name  = models.CharField(max_length=100)
    last_name   = models.CharField(max_length=100)
    username    = models.CharField(max_length=100)
    # GENDER = [
    #     ('p', 'Pria'),
    #     ('w', 'Wanita'),
    # ]
    # jenis_kelamin = models.CharField(choices=GENDER, max_length=10)
    # alamat = models.TextField()
    # agree = models.BooleanField(default=False)

    def __str__(self):
        return self.username