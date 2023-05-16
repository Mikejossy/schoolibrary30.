from django.contrib import admin

from Library.models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(IssuedBook)