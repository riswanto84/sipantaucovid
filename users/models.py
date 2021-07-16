from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=300)
    email = models.EmailField()
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    nomor_hp = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    nomor_sk = models.CharField(max_length=300, blank=True, null=True)
    tanggal_sk = models.DateField(blank=True, null=True)
    foto = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


