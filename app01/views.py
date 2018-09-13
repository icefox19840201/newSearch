from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import GoodsInfo as gf
# Create your views here.
from haystack.generic_views import SearchView
class GoodInfo(View):
    def get(self,request):
        keyswords = request.GET.get('keywords')
        if keyswords:
            data = gf.objects.filter(goodsName__contains=keyswords)
        else:
            data=gf.objects.all()
        paginator = Paginator(data, 2)
        currentPage = request.GET.get('page', 1)  # GET方法获得url参数
        page_data = paginator.page(currentPage)
        return render(request, 'app01/search.html', {'data': page_data})







