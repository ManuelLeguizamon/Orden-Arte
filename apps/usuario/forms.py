from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-input",
            "placeholder": "Ingresá tu email"
        })
    )

    name = forms.CharField(
        required=True,
        label="Nombre",
        widget=forms.TextInput(attrs={
            "class": "form-input",
            "placeholder": "Ingresá tu nombre"
        })
    )

    class Meta:
        model = User
        fields = ["email", "name", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update({
            "class": "form-input",
        })
        self.fields["name"].widget.attrs.update({
            "class": "form-input",
        })
        self.fields["password1"].widget.attrs.update({
            "class": "form-input",
            "placeholder": "Contraseña"
        })
        self.fields["password2"].widget.attrs.update({
            "class": "form-input",
            "placeholder": "Repetí tu contraseña"
        })

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya fue registrado.")
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if not password1 or not password2:
            return password2
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return password2



    def save(self, commit=True):
        user = super().save(commit=False)
        email = self.cleaned_data["email"]
        name = self.cleaned_data["name"]
        user.username = email
        user.email = email   
        user.first_name = name
        if commit:
            user.save()
        return user

