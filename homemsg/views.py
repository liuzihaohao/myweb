from django.shortcuts import render,redirect
from . import models
from django.shortcuts import HttpResponse
import markdown
# Create your views here.

def getpagelist(request):
	obj=models.articlePags.objects.all()
	return render(request,'../template/homepage.html',{'obj':obj,'murl':"/media/"})
def getpages(request,ida):
    obj=None
    try:
    	obj=models.articlePags.objects.get(uuids=ida)
    except Exception:
        return render(request,'../template/404.html')
    article=obj.mdtext
    # article=markdown.markdown(article,extensions=[
	# 	'markdown.extensions.extra',
	# 	'markdown.extensions.codehilite',
	# 	'markdown.extensions.toc',
    #     'mdx_math',
	# ],
    # extension_configs={
    #     'mdx_math': {
    #         'enable_dollar_delimiter': True,  # 是否启用单美元符号（默认只启用双美元）
    #         'add_preview': True  # 在公式加载成功前是否启用预览（默认不启用）
    #     }
    # })
    return render(request,'../template/articlepage.html', {'article': article,"title":obj.title,'time':obj.time})
def getpagesida(request,ida):
    obj=None
    try:
    	obj=models.articlePags.objects.get(id=ida)
    except Exception:
        return render(request,'../template/404.html')
    article=obj.mdtext
    # article=markdown.markdown(article,extensions=[
	# 	'markdown.extensions.extra',
	# 	'markdown.extensions.codehilite',
	# 	'markdown.extensions.toc',
    #     'mdx_math',
	# ],
    # extension_configs={
    #     'mdx_math': {
    #         'enable_dollar_delimiter': True,  # 是否启用单美元符号（默认只启用双美元）
    #         'add_preview': True  # 在公式加载成功前是否启用预览（默认不启用）
    #     }
    # })
    return render(request,'../template/articlepage.html', {'article': article,"title":obj.title,'time':obj.time})