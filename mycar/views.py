from django.shortcuts import render
from mycar.models import Car
from django.db.models import Q
from django.views.generic.base import TemplateView

class CarView(TemplateView):
    
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filterparams = self.request.GET # получаем параметры гет запроса
        print(filterparams)
        query = Q()
        for key, value in filterparams.items():
            if value and key in vars(Car):
                query = query & Q(**{key: value})
        return {"my_car": Car.objects.filter(query)}