from django.contrib import admin
from .models import Friend
from .models import Friend,ANKENTBL,ICHIRANTBL,USERTBL,HYOKATBL,KOUMOKUM
# Register your models here.
admin.site.register(Friend) 
admin.site.register(ANKENTBL) 
admin.site.register(ICHIRANTBL) 
admin.site.register(USERTBL) 
admin.site.register(HYOKATBL) 
admin.site.register(KOUMOKUM) 