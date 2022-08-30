from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Poll)
admin.site.register(Count_total_poll)
admin.site.register(Poll_statistics)