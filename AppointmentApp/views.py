from django.shortcuts import render, redirect
from .models import Appointment


def index(request):
    return render(request, 'appointment/index.html')


def appointment_list(request):
    appointments = Appointment.objects.all()

    context = {
        'appointments': appointments
    }

    return render(
        request,
        'appointment/appointment_list.html',
        context
    )


def appointment_create(request):
    if request.method == 'POST':
        Appointment.objects.create(
            client_name=request.POST['client_name'],
            contact_number=request.POST['contact_number'],
            appointment_date=request.POST['appointment_date'],
            appointment_time=request.POST['appointment_time'],
            service=request.POST['service'],
            appointment_status=request.POST['appointment_status']
        )

        return redirect('appointment_list')

    return render(request, 'appointment/appointment_form.html')


def appointment_update(request, appointment_id):
    appointment = Appointment.objects.get(
        appointment_id=appointment_id
    )

    if request.method == 'POST':
        appointment.client_name = request.POST['client_name']
        appointment.contact_number = request.POST['contact_number']
        appointment.appointment_date = request.POST['appointment_date']
        appointment.appointment_time = request.POST['appointment_time']
        appointment.service = request.POST['service']
        appointment.appointment_status = request.POST['appointment_status']

        appointment.save()

        return redirect('appointment_list')

    context = {
        'appointment': appointment
    }

    return render(
        request,
        'appointment/appointment_form.html',
        context
    )


def appointment_delete(request, appointment_id):
    appointment = Appointment.objects.get(
        appointment_id=appointment_id
    )

    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')

    context = {
        'appointment': appointment
    }

    return render(
        request,
        'appointment/appointment_confirm_delete.html',
        context
    )
