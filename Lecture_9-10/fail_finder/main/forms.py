from django import forms

from main.models import Student

class LoginForm(forms.Form):
    username = forms.CharField()
    # <input type="text" name="username" />
    password = forms.CharField(widget = forms.PasswordInput(
        attrs= {
            'placeholder': 'password'
        }
    ))
    # <input type = "password" name = "password" placeholder = "password" />
    email = forms.EmailField()
    # <input type = "email" name = "email" />

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = ('name', 'age', 'branch')
        fields = '__all__'