from django import forms


class ScanForm(forms.Form):
    vehicle_make = forms.CharField(max_length=50, label='Enter the make of the vehicle')
    vehicle_model = forms.CharField(max_length=50, label='Enter the model of the vehicle')
    vehicle_year = forms.IntegerField(label='Enter the year of the vehicle')
    driver_side_start = forms.ChoiceField(label='What side did you start the scan?', choices=["Driver's side", "Passenger's side"], widget=forms.RadioSelect)
    eye_x_ft = forms.IntegerField(label='Enter the X coordinate of the eye position', label_suffix='ft')
    eye_x_in = forms.FloatField(label_suffix='in')
    eye_y_ft = forms.IntegerField(label='Enter the Y coordinate of the eye position', label_suffix='ft')
    eye_y_in = forms.FloatField(label_suffix='in')
    eye_z_ft = forms.IntegerField(label='Enter the Z coordinate of the eye position', label_suffix='ft')
    eye_z_in = forms.FloatField(label_suffix='in')
    lidar_scan = forms.FileField()
