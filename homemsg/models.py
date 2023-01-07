from django.db import models
from mdeditor.fields import MDTextField
def autogetuuid():
    from uuid import uuid4
    return str(uuid4())
# Create your models here.
class filelist(models.Model):
	id=models.AutoField(primary_key=True,verbose_name='id')
	time=models.DateField(auto_now_add=True,verbose_name='创建时间')
	file=models.FileField(upload_to='upload_file/',verbose_name="文件",null=True, blank=True)
	class Meta:
		verbose_name='文件列表'
		verbose_name_plural=verbose_name

class articlePags(models.Model):
	id=models.AutoField(primary_key=True,verbose_name='id')
	time=models.DateField(auto_now_add=True,verbose_name='创建时间')
	uuids=models.UUIDField(verbose_name='UUID',auto_created=True,default=autogetuuid)
	articletype=models.CharField(choices=(('m',"md"),('r',"href")),max_length=49,verbose_name="记录类型",default="md")
	urlshref=models.CharField(max_length=999,verbose_name="链接",null=True, blank=True)
	mdtext=MDTextField(verbose_name="内容",default="",editable=True,null=True, blank=True)
	text=models.TextField(verbose_name='简介')
	title=models.CharField(max_length=100,verbose_name='标题')
	ifok=models.BooleanField(default=True,verbose_name="是否显示")
	class Meta:
		verbose_name='文章列表'
		verbose_name_plural=verbose_name
		ordering = ['-time']
    