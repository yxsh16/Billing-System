from django.contrib import admin
from billing_sys.plowing.models import PlowingService, PlowingRequest

# Register your models here.

admin.site.register(PlowingService)
admin.site.register(PlowingRequest)
