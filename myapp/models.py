from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 200)
    phone_number = models.CharField(primary_key = True, max_length = 15)
    email = models.EmailField(blank = True)

    class Meta:
        managed = False
        db_table = "users"

class Contact(models.Model):
    user_details = models.CharField(max_length = 15)
    contact_number = models.CharField(max_length = 15)
    alias = models.CharField(max_length = 200)
    # is_spam = models.BooleanField(default = False)

    class Meta:
        managed = False
        db_table = "contacts"