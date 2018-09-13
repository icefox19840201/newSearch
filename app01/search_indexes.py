from haystack import indexes
from .models import GoodsInfo

class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    goodsName=indexes.CharField(model_attr='goodsName')
    goodsDesc = indexes.CharField(model_attr='goodsDesc')

    def get_model(self):
        return GoodsInfo

    def index_queryset(self, using=None):
        a=1
        return self.get_model().objects.all()