from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

class Fill(models.Model):

    delivery_date = models.DateField(auto_now_add=True)
    campaign_id = models.CharField(max_length=20)
    campaign_name = models.CharField(max_length=50)
    channel = models.CharField(max_length=10)
    lead_id = models.CharField(max_length=10)
    units = models.CharField(max_length=4)
    PM = models.CharField(max_length=10)
    DA = models.CharField(max_length=10)
    notes = models.TextField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-delivery_date','-campaign_id',)

    def __str__(self):
        return self.campaign_id