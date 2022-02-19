from django.contrib import admin
from . models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name_of_customer', 'phone_number', 'test_provided', 'price',
        'referral_name', 'discount', 'amount_given', 'provided_test_results',
        'date_of_arrival', 'user'
    )
    
    def save_model(self, request, obj, form, change):
        '''Automatically generate registry number'''
        if getattr(obj, 'id', True) is not None:
            self.user = request.user
            obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(Client, ClientAdmin)