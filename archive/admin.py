from django.contrib import admin
from .models import Club, Request, Budget, Funding

admin.site.register(Club)
admin.site.register(Request)
admin.site.register(Budget)
admin.site.register(Funding)