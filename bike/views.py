from http.client import HTTPResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models import (State, Bike, BikeBooking)
from django.db.models import Q
from .utils import send_mail_to_client
from .forms import ContactUsForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail


def home(request):
    bikes_objs = Bike.objects.all()
    context = {'bikes_obj':bikes_objs}

    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')
    if sort_by:
        if sort_by == 'ASC':
            bikes_objs = bikes_objs.order_by('bike_price')
        elif sort_by == 'DSC':
            bikes_objs = bikes_objs.order_by('-bike_price')

    if search:
        bikes_objs = bikes_objs.filter(
            Q(brand__icontains = search) |
            Q(description__icontains = search) )






    context = {'bike_objs' : bikes_objs , 'sort_by' : sort_by
    , 'search' : search}
    return render(request , 'home.html' ,context)




def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username)

        if not user_obj.exists():
            messages.warning(request, 'Account not found ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user_obj = authenticate(username = username , password = password)
        if not user_obj:
            messages.warning(request, 'Invalid password ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        login(request , user_obj)
        return redirect('/')


    return render(request ,'login.html')


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username)

        if user_obj.exists():
            messages.warning(request, 'Username already exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user = User.objects.create(username = username)
        user.set_password(password)
        user.save()
        return redirect('/')

    return render(request , 'register.html')


def home(request):
    bikes_objs = Bike.objects.all()

    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')
    if sort_by:
        if sort_by == 'ASC':
            bikes_objs = bikes_objs.order_by('bike_price')
        elif sort_by == 'DSC':
            bikes_objs = bikes_objs.order_by('-bike_price')

    if search:
        bikes_objs = bikes_objs.filter(
            Q(brand__icontains = search) |
            Q(description__icontains = search) )






    context = {'bike_objs' : bikes_objs , 'sort_by' : sort_by
    , 'search' : search}
    return render(request , 'home.html' ,context)


def check_booking(start_date  , end_date ,uid , bike_count):
    qs = BikeBooking.objects.filter(
        start_date__lte=start_date,
        end_date__gte=end_date,
        bike__uid = uid
        )

    if len(qs) >= bike_count:
        return False

    return True

def bike_detail(request,uid):
    try:
        bike_obj = Bike.objects.get(uid=uid)
    except Bike.DoesNotExist:
        return HTTPResponse("Bike not found", status=404)
    bike_obj = Bike.objects.get(uid = uid)

    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout= request.POST.get('checkout')
        bike = Bike.objects.get(uid = uid)
        if not check_booking(checkin ,checkout  , uid , bike.bike_count):
            messages.warning(request, 'bike is already booked in these dates ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        BikeBooking.objects.create(bike=bike , user = request.user , start_date=checkin
        , end_date = checkout , booking_type  = 'Pre Paid')

        messages.success(request, 'Your booking has been saved')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




    return render(request , 'bike_detail.html' ,{
        'bike_obj' :bike_obj
    })


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            send_mail_to_client(subject, message, email)
        return redirect('/')
    else:
        form = ContactUsForm()
    return render(request, 'FormContact.html', {'form': form})
