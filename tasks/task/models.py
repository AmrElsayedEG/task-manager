from django.db import models

# Create your models here.
class task(models.Model):
    cat_list = (("university","university"),("School","School"),("Home","Home"))
    description = models.CharField(max_length=100)
    category = models.CharField(choices=cat_list,max_length=15)
    date = models.DateField()

    def __str__(self):
        return self.description