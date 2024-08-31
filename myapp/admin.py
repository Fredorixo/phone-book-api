from django.contrib import admin
from myapp.models import User, Contact

# Register your models here.
admin.site.register([User, Contact])