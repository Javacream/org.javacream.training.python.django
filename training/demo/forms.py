from django import forms

class NameForm(forms.Form):
    first_name = forms.CharField(
        label="First name",
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter first name"
        })
    )
    last_name = forms.CharField(
        label="Last name",
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter last name"
        })
    )
