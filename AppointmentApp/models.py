from django.db import models

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    service = models.CharField(max_length=100)
    appointment_status = models.CharField(max_length=50)

    def __str__(self):
        return self.client_name
