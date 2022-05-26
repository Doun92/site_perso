from django.contrib import admin

# Register your models here.
from .models import Citation, Certification, Experience

admin.site.register(Citation)
admin.site.register(Certification)
admin.site.register(Experience)
