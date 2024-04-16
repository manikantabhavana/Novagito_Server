from django.contrib import admin
from .models import Customer,Testinominal,Query

@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'mail', 'location', 'rating','photo_url'] 

@admin.register(Testinominal)
class TestinominalsAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'review', 'rating','photo_url'] 


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'mobile','message','date'] 

