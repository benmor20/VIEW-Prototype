from django.db import models


class Vehicle(models.Model):
    vehicle_make = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    vehicle_year = models.IntegerField()


class Scan(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    lidar_scan = models.FileField(upload_to='lidar_scans/')
    eye_x = models.FloatField()
    eye_y = models.FloatField()
    eye_z = models.FloatField()
    driver_side_start = models.BooleanField()
