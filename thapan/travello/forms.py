from django import forms
from .models import destination


class destinationform(forms.ModelForm):
    class Meta:
        model = destination
        fields  = ['name','img','desc','price','offer']