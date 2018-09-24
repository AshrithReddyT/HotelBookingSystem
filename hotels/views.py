from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Hotel , Location

# Create your views here.

def search(request):
    locations = Location.objects.all().order_by('location_name')
    if not request.GET.get('location', 'none') == 'none':
        location = request.GET['location']
        location = Location.objects.filter(location_name=location[0])
        hotels = Hotel.objects.filter(location=location[0])

        return render(request, 'hotels/search.html', {'hotels': hotels, 'locations': locations, 'location': location})

    return render(request, 'hotels/search.html', {'locations': locations})

class HotelList(ListView):
    model = Hotel
    context_object_name = 'hotels_list'
    template_name='hotels/hotel_list.html'

class HotelDetail(DetailView):
    model = Hotel
    template_name='hotels/hotel_detail.html'


