from django import forms
from .models import Machine


# Create the form class.

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = [
            'machine_id',
            'machine_name',
            'date_of_first_inspection',
            'agent',
            ]


class LeadForm(forms.Form):
    machine_id = forms.CharField()
    machine_name = forms.CharField()
    agent = forms.CharField()
  