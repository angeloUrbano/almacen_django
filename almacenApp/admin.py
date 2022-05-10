from django.contrib import admin
from django.contrib.auth.models import Permission


from almacenApp.models import *

# Register your models here.




admin.site.register(Misil)
admin.site.register(Lote)
admin.site.register(DetallesExtras)
admin.site.register(User)
admin.site.register(Condicion)
admin.site.register(Permission)