from django import forms


class RegForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username:',
        max_length=32
    )
    roll_no = forms.CharField(
        required=True,
        label='RollNo :',
        max_length=32
    )
    email = forms.CharField(
        required=True,
        label='Email   :',
        max_length=32,
    )
    password = forms.CharField(
        required=True,
        label='Password :',
        max_length=32,
        widget=forms.PasswordInput()
    )
    rpassword = forms.CharField(
        required=True,
        label='Re-enter Password :',
        max_length=32,
        widget=forms.PasswordInput()
    )
    phno = forms.CharField(
        required=True,
        label='Mobile:',
        max_length=32,
    )


#CHOICES = [('student', 'examiner', 'admin')]
CHOICES = [('c1', 'Student'), ('c2', 'Examiner'), ('c3', 'Admin')]


class LoginForm(forms.Form):
    rollno = forms.CharField(
        required=True,
        label='User Id',
        max_length=32
    )
    password = forms.CharField(
        required=True,
        label='Password :',
        max_length=500,
        widget=forms.PasswordInput()
    )
    user = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(),
    )




