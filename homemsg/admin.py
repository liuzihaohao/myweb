from django.contrib import admin
from .models import articlePags,filelist

# Register your models here.

class filelistAdmin(admin.ModelAdmin):
	list_display = ['id','time','file']
	list_display_links = ['id']
	search_fields = ['file']
admin.site.register(filelist,filelistAdmin)

class articlePagsAdmin(admin.ModelAdmin):
	list_display = ['id','uuids','title','text','time','urlshref','articletype','ifok']
	list_display_links = ['id','uuids']
	search_fields = ['time','id','text','title','mdtext','urlshref','uuids']
	list_filter=['articletype','ifok']
admin.site.register(articlePags,articlePagsAdmin)

admin.site.site_title="myweb"
admin.site.site_header="myweb"

from django.contrib.admin.models import LogEntry
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
class LogEntryAdmin(admin.ModelAdmin):
	list_display = ['action_time','user','content_type','object_id','object_repr','action_flag','change_message']
admin.site.register(LogEntry,LogEntryAdmin)
class SessionAdmin(admin.ModelAdmin):
	list_display = ['session_key','session_data','expire_date']
admin.site.register(Session,SessionAdmin)
class ContentTypeAdmin(admin.ModelAdmin):
	list_display = ['app_label','model']
admin.site.register(ContentType,ContentTypeAdmin)