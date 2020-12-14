from django.contrib import admin
from myboard.models import BoardTab

# Register your models here.
class BoardTabAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'passwd', 'mail', 'title', 'cont',
                    'bip', 'bdate', 'readcnt', 'gnum', 'onum', 'nested')
    
admin.site.register(BoardTab, BoardTabAdmin)