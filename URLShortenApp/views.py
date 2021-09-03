from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .models import URLShortenModel
from .forms import URLShortenForm

# Create your views here.

class HomePage(View):
    def get(self, request, *args, **kwargs):
        my_form = URLShortenForm()
        context = {
            'form': my_form,
        }
        return render(request, 'URLShortenApp/home2.html', context)

    def post(self, request, *args, **kwargs):
        my_form = URLShortenForm(request.POST)
        context = {
            'form': my_form
        }
        # print(request.POST) returns a query dict {'csrfmiddlewaretoken' : ['....'], 'field_name' : ['value']}
        if my_form.is_valid():
            data = my_form.cleaned_data # returns a dictionary with field_name as key and form input as value
            link = data['url']
            obj,created = URLShortenModel.objects.get_or_create(original_url = link)
            context = {
                'obj': obj,
            }
            if created:
                return render(request, 'URLShortenApp/success.html', context)
            else:
                return render(request, 'URLShortenApp/base.html', context)     

        return render(request, 'URLShortenApp/home2.html', context)

class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = URLShortenModel.objects.filter(short_code = shortcode) # returns a queryset
        if qs.exists():
            obj = qs.get() # get method returns an object from the queryset
            return HttpResponseRedirect(obj.original_url)
        else:
            raise Http404


