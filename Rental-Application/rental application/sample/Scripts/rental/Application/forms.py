from django import forms 
from phonenumber_field.formfields import PhoneNumberField
from django.forms import modelformset_factory
from .models import Property,PropertyImage

class register_form(forms.Form):
    username = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'ENTER YOUR USERNAME'}))
    first_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'ENTER YOUR FIRSTNAME'}))
    last_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'ENTER YOUR LASTNAME'}))
   
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'ENTER YOUR PASSWORD'}))
    Email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'placeholder': 'ENTER YOUR EMAIL'}))
    phone_no = PhoneNumberField(label="Phone Number",widget=forms.TextInput(attrs={'placeholder': 'ENTER YOUR PHONE NUMBER'}))


class login_form(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name','place', 'area', 'bedrooms', 'bathrooms', 'nearby_landmark', 'property_type','price']

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['image']

PropertyImageFormSet = modelformset_factory(PropertyImage, form=PropertyImageForm, extra=4)


class PropertyUpdateForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name','place', 'area', 'bedrooms', 'bathrooms', 'nearby_landmark', 'property_type', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'bathrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'nearby_landmark': forms.TextInput(attrs={'class': 'form-control'}),
            'property_type': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }