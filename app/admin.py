from django.contrib import admin
from .models import Gallery,Product
# Register your models here.


admin.site.register(Gallery)
admin.site.register(Product)


admin.site.site_header = "AA Plastics Admin"
admin.site.site_title = "AA Plastics Admin Portal"  
admin.site.index_title = "Welcome to AA Plastics Admin Portal"