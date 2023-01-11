from .models import Tech, Shop, Manufacturer
from django.forms import ModelForm, TextInput, NumberInput


class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'address', 'status']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название магазина'
            }),
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес'
            }),
            'status': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите статус магазина'
            })
        }


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country', 'CEO']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите производителя'
            }),
            'country': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите страну производства'
            }),
            'CEO': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя и фамилию директора'
            })
        }

class TechForm(ModelForm):
    class Meta:
        model = Tech
        fields = ['name', 'model', 'address', 'price']
        widgets = {
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите модель'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену товара'
            })
        }
