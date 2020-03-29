from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.
from django.db.models import Choices


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

INSTITUTIONS = (
        ("FUNDACJA", 'Fundacja'),
        ("ORGANIZACJA POZARZĄDOWA", 'Organizacja pozarządowa'),
        ("ZBIÓRKA LOKALNA", 'Zbiórka lokalna'),
)



class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=264)
    type = models.CharField(max_length=64, choices=INSTITUTIONS, default='FUNDACJA')
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.name}, typu {self.get_type_inst_display()}'

class Donation(models.Model):

    quantity = models.IntegerField(default=0, )
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    phone_number = models.IntegerField(default=None)
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=12)
    pick_up_date = models.CharField(max_length=32)
    pick_up_time = models.CharField(max_length=32)
    pick_up_comment = models.CharField(max_length=128)
    user = models.ForeignKey(User, null=True, default=0, on_delete=models.CASCADE)





