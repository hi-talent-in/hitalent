from django.db import models

# Create your models here.
class Intern(models.Model):
    first_name = models.CharField(max_length=1000, null=True, blank=True)
    last_name = models.CharField(max_length=1000, null=True, blank=True)
    email = models.EmailField(max_length=1000, null=True, blank=True)
    phone_number = models.PositiveBigIntegerField(null=True, blank=True)
    address = models.CharField(max_length=3000, null=True, blank=True)

    class Meta:
        db_table = "interns"

    def __str__(self):
        return self.email
