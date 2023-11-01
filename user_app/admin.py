from django.contrib import admin
from .models import UserInformation, PaymentGatewaySettings

# Register your models here.
admin.site.register(UserInformation)
admin.site.register(PaymentGatewaySettings)