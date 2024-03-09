from django import forms
from .models import CustomUser


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'number']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        username = cleaned_data.get("username")

        # Check if password is too similar to the username
        if username and password.lower().startswith(username.lower()):
            raise forms.ValidationError("Password is too similar to the username.")

        # Check if password is common
        common_passwords = ["password", "123456", "qwerty", "abc123"]  # Add more common passwords
        if password.lower() in common_passwords:
            raise forms.ValidationError("Password is too common.")

        # Check if password is at least 8 characters
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters.")

        # Check if password is not full of numbers
        if password.isdigit():
            raise forms.ValidationError("Password should not be all numeric.")

        return cleaned_data
    



    

