from django import forms
from .models import User
from .models import TeamMember
from django.contrib.admin import widgets 
from.models import Contact,Admission
class InputForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('__all__')

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ('__all__')
        
        


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')
        
class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'contactnumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your contact number'}),
            'dateOfAdmission': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }