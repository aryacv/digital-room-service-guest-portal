from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Amenity, RoomRequest

def check_in(request):
    if request.method == "POST":
        name = request.POST.get("guest_name")
        room = request.POST.get("room_number")
        
        # Clear out historical simulation data for this specific room setup instantly
        RoomRequest.objects.filter(guest_name=name, room_number=room).delete()
        
        # Initialize session storage keys securely
        request.session['guest_name'] = name
        request.session['room_number'] = room
        request.session['total_bill'] = 0 # Starts at $0 and goes up with resource selection
        
        return redirect('menu')
    return render(request, 'kiosk/check_in.html')

def menu(request):
    if 'guest_name' not in request.session:
        return redirect('check_in')
        
    amenities = Amenity.objects.all()
    return render(request, 'kiosk/menu.html', {'amenities': amenities})

def request_item(request, item_id):
    if 'guest_name' not in request.session:
        return redirect('check_in')

    amenity = Amenity.objects.get(id=item_id)

    if amenity.stock <= 0:
        messages.error(request, f"Sorry, {amenity.name} is currently out of stock.")
    else:
        # Deduct available warehouse stock
        amenity.stock -= 1
        amenity.save()
        
        # Increase the guest's running session bill as resource selection expands
        request.session['total_bill'] += amenity.price
        
        # Record transaction log row
        RoomRequest.objects.create(
            guest_name=request.session['guest_name'],
            room_number=request.session['room_number'],
            amenity=amenity
        )
        messages.success(request, f"{amenity.name} successfully ordered to your room!")

    return redirect('menu')

def room_ledger(request):
    if 'guest_name' not in request.session:
        return redirect('check_in')

    raw_requests = RoomRequest.objects.filter(
        guest_name=request.session['guest_name'],
        room_number=request.session['room_number']
    ).select_related('amenity')

    grouped_items = {}
    total_spent = 0
    
    for req in raw_requests:
        item_id = req.amenity.id
        total_spent += req.amenity.price
        if item_id in grouped_items:
            grouped_items[item_id]['quantity'] += 1
            grouped_items[item_id]['subtotal'] += req.amenity.price
        else:
            grouped_items[item_id] = {
                'name': req.amenity.name,
                'category': req.amenity.category,
                'price': req.amenity.price,
                'quantity': 1,
                'subtotal': req.amenity.price
            }

    # Keep session data synced with total bill calculations
    request.session['total_bill'] = total_spent

    context = {
        'ledger_items': grouped_items.values(),
        'total_spent': total_spent
    }
    return render(request, 'kiosk/ledger.html', context)

def check_out(request):
    request.session.flush() 
    return redirect('check_in')