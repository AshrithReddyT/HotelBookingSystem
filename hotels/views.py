from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hotel,Room
from .forms import BookingForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

def search(request):
    locations = Hotel.objects.all().values_list('location', flat=True).distinct()
    if not request.GET.get('location', 'none') == 'none':
        location = request.GET['location']
        hotels = Hotel.objects.filter(location=location)
        return render(request, 'hotels/search.html', {'hotels': hotels, 'locations': locations, 'location': location})

    return render(request, 'hotels/search.html', {'locations': locations})


def Booking(request):
    if request.GET.get('hotel_id'):
        return render(request, 'hotels/booking.html', {'hotel': Hotel.objects.get(id=request.GET['hotel_id'])})

    return render(request, 'hotels/search.html')

@method_decorator(login_required, name='dispatch')
class booking(CreateView):
    form_class = BookingForm
    model = Room
    template_name = 'hotels/booking.html'

    def get_initial(self):
        if self.request.GET.get('hotel_id'):
            return { 'hotel': Hotel.objects.get(id=self.request.GET['hotel_id'])}


class HotelList(ListView):
    model = Hotel
    context_object_name = 'hotels_list'
    template_name='hotels/hotel_list.html'

class HotelDetail(DetailView):
    model = Hotel
    template_name='hotels/hotel_detail.html'


