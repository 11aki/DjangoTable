import django_filters

from .models import *

class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = '__all__'