from django.contrib.auth.models import User
from django import forms
from .models import Order



class Order_Form(forms.ModelForm):
    class Meta :
        model=Order
        fields="__all__"
        exclude=("user",)
        