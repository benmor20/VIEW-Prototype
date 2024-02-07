from django import forms
from .models import Scan


class ScanForm(forms.ModelForm):
    class Meta:
        model = Scan
        fields = ['vehicle', 'driver_side_start', 'eye_x_ft', 'eye_x_in', 'eye_y_ft', 'eye_y_in', 'eye_z_ft', 'eye_z_in', 'lidar_scan']
