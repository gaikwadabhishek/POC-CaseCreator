from django import forms
from django.core import validators


CHOICES = [
    ('Create','Create Request'),
    ('Submit','Submit Request'),
    ('Documents','Send Documents')]


class FormName(forms.Form):
    RACid = forms.CharField(max_length = 100)
    no_of_req = forms.IntegerField()
    condition = forms.CharField(label = 'till where do you want to perform operation?',widget = forms.Select(choices = CHOICES))

    def clean(self):
        all_clean_data = super().clean()
        no_of_req = all_clean_data['no_of_req']
        
        if no_of_req > 5:
            raise forms.ValidationError("MAKE SURE NUMBER OF REQUESTS <5")
