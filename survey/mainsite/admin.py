from django.contrib import admin
from .models import Fill

# Register your models here.

class FillAdmin(admin.ModelAdmin):
    list_display = ('delivery_date','campaign_id','campaign_name','channel','create_time')

admin.site.register(Fill, FillAdmin)