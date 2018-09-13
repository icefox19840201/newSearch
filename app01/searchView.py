from haystack.generic_views import SearchView
from .models import GoodsInfo
from django.db.models import Q

class MySearchView(SearchView):
    def get_queryset(self):
        queryset = super(MySearchView, self).get_queryset()
        return queryset.all()

    def get_context_data(self, *args, **kwargs):
        mySearchView = super(MySearchView, self)

        form_data = mySearchView.get_form_kwargs()['data']

        GInfo = GoodsInfo.objects.filter(Q(goodsName__contains=form_data['q'])|Q(goodsDesc__contains=form_data['q']))
        context={}
        print(GInfo.count())
        context['object_list']=GInfo
        return context

