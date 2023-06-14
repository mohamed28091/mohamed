from django.db import models


class Patient(models.Model):
    choices_gender = [("male", "male"), ("female", "female")]
    patientID = models.CharField(max_length=50, primary_key=True)
    patientName = models.CharField(max_length=300)
    patientAddress = models.CharField(max_length=500)
    patientPhone = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50,choices=choices_gender)
    medical_history = models.CharField(max_length=500)


    def __str__(self):
        return self.patientName

class Doctor(models.Model):
    doctorID = models.CharField(max_length=50, primary_key=True)
    doctorName = models.CharField(max_length=300)
    doctorAddress = models.CharField(max_length=500)
    doctorPhone = models.CharField(max_length=50)
    specialisation = models.CharField(max_length=300)
    certification = models.CharField(max_length=300)


    def __str__(self):
        return self.doctorName

class Appointment(models.Model):
    choices_Status = [("Scheduled", "Scheduled"), ("Canceled", "Canceled")]
    appointmentID = models.CharField(max_length=50, primary_key=True)
    appointmentDate = models.DateField(verbose_name='appointment Date', auto_now_add=True, null=False)
    appointmentTime = models.TimeField(verbose_name='appointment Time', auto_now_add=True)
    appointmentStatus = models.CharField(max_length=100,default="Scheduled", choices=choices_Status)
    reason = models.CharField(max_length=500)
    doctor_id = models.ForeignKey("Doctor", on_delete=models.PROTECT)
    patient_id = models.ForeignKey("Patient", on_delete=models.PROTECT)

    def __str__(self):
        return self.appointmentID

class Prescription(models.Model):
    PrescriptionID = models.CharField(max_length=50, primary_key=True)
    # prescriptionDate= models.DateField(verbose_name='prescription Date', auto_now_add=True, null=False)
    appointment_id = models.ForeignKey("Appointment", on_delete=models.PROTECT)
    # patient_id = models.ForeignKey("Patient", on_delete=models.PROTECT)
    medicationName = models.CharField(max_length=300)
    dosage = models.CharField(max_length=300)
    frequency = models.CharField(max_length=300)

    def __str__(self):
        return self.PrescriptionID
