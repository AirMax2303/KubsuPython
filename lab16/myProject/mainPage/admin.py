from django.contrib import admin
from .models import Tech
from .models import Manufacturer
from .models import Shop

admin.site.register(Tech)
admin.site.register(Manufacturer)
admin.site.register(Shop)
