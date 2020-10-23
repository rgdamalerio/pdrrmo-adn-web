from django.contrib.gis import admin
from .models import Magallenes

admin.site.register(Magallenes, admin.GeoModelAdmin)
