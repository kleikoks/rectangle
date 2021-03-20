from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user doesnt exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorect password')
            if not user.is_active:
                raise forms.ValidationError('User is not active')
            return super(UserLoginForm, self).clean(*args, **kwargs)



class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email field')
    email2 = forms.EmailField(label='Confirm email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            forms.ValidationError('Emails doesnt match')
        emails_qs = User.objects.filter(email=email)
        if emails_qs.exists():
            raise forms.ValidationError('This Email already used')
        return email

