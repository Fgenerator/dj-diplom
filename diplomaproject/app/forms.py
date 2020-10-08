from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)