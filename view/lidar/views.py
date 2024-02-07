from django.shortcuts import render
from .models import Vehicle, Scan


def index(request):
    return render(request, 'lidar/index.html', {})


def add_vehicle(request):
    return render(request, 'lidar/add-vehicle.html', {})


def data_upload(request):
    return render(request, 'lidar/data-upload.html', {})


def faq(request):
    return render(request, 'lidar/faq.html', {})


def vehicle_database_loading(request):
    return render(request, 'lidar/vehicle-database-loading.html', {})


def vehicle_database_table(request):
    return render(request, 'lidar/vehicle-database-table.html', {})


def new_data(request):
    vehicle = Vehicle.objects.get(vehicle_year=2011)
    scan = Scan(
        vehicle=vehicle,
        lidar_scan=request.POST[]
    )
