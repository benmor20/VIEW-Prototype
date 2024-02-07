from django.shortcuts import render


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
