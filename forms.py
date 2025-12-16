from django.forms import ModelForm
from .models import Bb
from django import forms
from django.forms import inlineformset_factory
from .models import Product, ProductMeta

class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image')

class ProductMetaForm(forms.ModelForm):
    class Meta:
        model = ProductMeta
        fields = ('name', 'value')

ProductMetaFormSet = inlineformset_factory(
    Product,
    ProductMeta,
    form=ProductMetaForm,
    extra=1,
    can_delete=True,
)