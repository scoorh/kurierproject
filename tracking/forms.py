from django import forms

class NewEntryForm(forms.Form):
    '''form for creating new entry in database with POST'''
    package_id = forms.IntegerField(required=True)
    change_date = forms.DateTimeField(required=True, widget=forms.DateTimeInput)
    place = forms.CharField(max_length=100, required=True)
    message = forms.CharField(max_length=255, required=True)
