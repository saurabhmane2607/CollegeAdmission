from django import forms

class StudForm(forms.Form):
    student_name = forms.CharField(max_length=30)
    class_year = forms.CharField(max_length=30)
    address = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)