    
from django import forms

class ReservationForm(forms.Form):
    TIME_OF_DAY_CHOICES = (
        ('', 'Time'),
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'p-2 form-control','placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'p-2 form-control','placeholder': 'Your Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'p-2 form-control','placeholder': 'Your Phone'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'p-2 form-control','placeholder': 'Date','type': 'date',}))
    time = forms.ChoiceField(choices=TIME_OF_DAY_CHOICES, widget=forms.Select(attrs={'class': ' p-2 form-control'}))
    people = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'p-2 form-control','placeholder': '# of people'}))
    comments = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': 'p-2 form-control', 'rows': 5, 'cols': 101,'placeholder': 'Message'}))
    
    

class Sendmessage(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'p-2 form-control','placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'p-2 form-control','placeholder': 'Your Email'}))
    subject=forms.CharField(widget=forms.TextInput(attrs={'class': 'p-2 form-control','placeholder': 'Subject'}))
    comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'p-2 form-control', 'rows': 5, 'cols': 101,'placeholder': 'Message'}))
    

    # You can add any additional validation or customization here if needed
 
