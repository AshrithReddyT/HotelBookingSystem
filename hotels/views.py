from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hotel, Room ,Booking
from .forms import BookingForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import dateutil.parser
# Create your views here.

def search(request):
    locations = Hotel.objects.all().values_list('location', flat=True).distinct()
    if not request.GET.get('location', 'none') == 'none':
        location = request.GET['location']
        hotels = Hotel.objects.filter(location=location)
        return render(request, 'hotels/search.html', {'hotels': hotels, 'locations': locations, 'location': location})

    return render(request, 'hotels/search.html', {'locations': locations})


def availability(request):
    if request.GET.get('hotel_id') and request.GET.get('room_id') and request.GET.get('checkin') and request.GET.get('checkout'):
        hotel_id = request.GET['hotel_id']
        room_id = request.GET['room_id']
        checkin = request.GET['checkin']
        checkin =  dateutil.parser.parse(checkin)
        checkout = request.GET['checkout']
        checkout =  dateutil.parser.parse(checkout)
        error = "Check-Out can not be before Check-In"
        if checkout < checkin:
            return render(request, 'hotels/availability.html', {'hotel_id' : hotel_id, 'room_id': room_id,'error':error} )
        hotel = Hotel.objects.filter(id=hotel_id)
        rooms = Room.objects.filter(id=room_id)
        bookings = Booking.objects.filter(room=rooms[0])
        total = 0
        empty = 0
        for booking in bookings:
            in_time = booking.begin_time
            in_time = str(in_time.strftime("%Y-%m-%d %H:%M:%S"))
            in_time =  dateutil.parser.parse(in_time)
            out_time = booking.end_time
            out_time = str(out_time.strftime("%Y-%m-%d %H:%M:%S"))
            out_time =  dateutil.parser.parse(out_time)
            if in_time > checkout or out_time < checkin:
                empty = empty + booking.num_rooms
            total = total + booking.num_rooms
        non_empty = total - empty
        total = rooms[0].maximum
        empty =  total - non_empty
        return render(request, 'hotels/availability.html', {'hotel_id' : hotel_id, 'room_id': room_id,'empty':empty , 'total': total} )
    elif request.GET.get('hotel_id') and request.GET.get('room_id'):
        hotel_id = request.GET['hotel_id']
        room_id = request.GET['room_id']
        hotel = Hotel.objects.filter(id=hotel_id)
        room = Room.objects.filter(id=room_id)
        hotel_name = hotel[0].name
        room_type = room[0].type_name
        return render(request, 'hotels/availability.html', {'hotel_id' : hotel_id, 'room_id': room_id,'hotel_name' : hotel_name, 'room_type': room_type})
    return render(request, 'hotels/availability.html')
class HotelList(ListView):
    model = Hotel
    context_object_name = 'hotels_list'
    template_name='hotels/hotel_list.html'

class HotelDetail(DetailView):
    model = Hotel
    template_name='hotels/hotel_detail.html'

class RoomList(ListView):
    model = Room
    context_object_name = 'rooms_list'
    template_name='hotels/room_list.html'

    queryset = Room.objects.all()

    def get_queryset(self):
        return Room.objects.filter(hotel=self.kwargs.get('hotel_pk'))

class RoomDetail(DetailView):
    model = Room
    template_name='hotels/room_detail.html'
