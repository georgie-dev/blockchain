import django_filters
from .models import CryptoData

class CryptoFilterSet(django_filters.FilterSet):
    class Meta:
        model = CryptoData
        fields = ['user']