from django.contrib import admin

from api.models import *

# Register your models here.
admin.site.register(Request)
admin.site.register(Message)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Rate)
