from django.contrib import admin
from .models import Questions, Options, CustomerFeedback, CustomerResponse

admin.site.register(Questions)
admin.site.register(Options)
admin.site.register(CustomerFeedback)
admin.site.register(CustomerResponse)

