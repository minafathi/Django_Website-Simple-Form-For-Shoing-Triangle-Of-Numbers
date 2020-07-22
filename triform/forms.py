from django import forms

class TrianForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=9)