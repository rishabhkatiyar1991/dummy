from django import forms
import datetime

DATE_SELECT = (
    ('2019-2020', '2019-2020'),
    ('2020-2021', '2020-2021')
)
AMT_TYPE = (
    ('cash', 'Cash'),
    ('cheque', 'Cheque'),
    ('drafts', 'Drafts'),
)
COURSE_YEARS = (
    ('1', 'I Year'),
    ('2', 'II Year')
)

class StudentForm(forms.Form):
    sdate = forms.ChoiceField(choices=DATE_SELECT, widget=forms.Select())
    courseYear = forms.ChoiceField(choices=COURSE_YEARS, widget=forms.Select())
    """username = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],
                                widget=forms.DateTimeInput(attrs={ 'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker1' }))"""
    regno = forms.CharField(max_length=20,
                               widget=forms.TextInput(attrs={'size': 35, 'placeholder': ' username'}))

    firstname = forms.CharField(max_length=20,
                                widget=forms.TextInput(attrs={'size': 35,'placeholder':' First name'}))
    lastname = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'size': 35,'placeholder':' Last name', 'required': False}))
    fathername = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'size': 35, 'placeholder': ' Father name'}))
    agentrname = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'size': 35, 'placeholder': ' Agent name'}))
    course = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'size': 35, 'placeholder': ' Course name'}))
    amttype = forms.ChoiceField(choices=AMT_TYPE, widget=forms.Select(attrs={'width': 35}))
    amount = forms.CharField(max_length=20,
                                widget=forms.NumberInput(attrs={'size': 35, 'placeholder': ' Enter total fee'}))
    fee = forms.CharField(max_length=20,
                             widget=forms.NumberInput(attrs={'size': 35, 'placeholder': ' Enter fee'}))
    commission = forms.CharField(max_length=20,
                             widget=forms.NumberInput(attrs={'size': 35, 'placeholder': ' Enter amount'}))
    mobile = forms.CharField(max_length=10,
                                widget=forms.TextInput(attrs={'size': 35, 'placeholder': 'Mobile No'}))
    orgname = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs={'size': 35}))


class EditFee(forms.Form):
    sdate = forms.ChoiceField(choices=DATE_SELECT, widget=forms.Select())
    courseYear = forms.ChoiceField(choices=COURSE_YEARS, widget=forms.Select())
    """username = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'],
                                widget=forms.DateTimeInput(attrs={ 'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker1' }))"""
    regno = forms.CharField(max_length=20,
                               widget=forms.TextInput(attrs={'size': 35, 'placeholder': ' Registration  Number'}))

    firstname = forms.CharField(max_length=20,
                                widget=forms.TextInput(attrs={'size': 35,'placeholder':' First name'}))
    lastname = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={'size': 35,'placeholder':' Last name', 'required': False}))
    fathername = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'size': 35, 'placeholder': ' Father name'}))
    agentrname = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'size': 35, 'placeholder': ' Agent name'}))
    course = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'size': 35, 'placeholder': ' Course name'}))
    amttype = forms.ChoiceField(choices=AMT_TYPE, widget=forms.Select(attrs={'width': 35}))
    amount = forms.CharField(max_length=20,
                                widget=forms.NumberInput(attrs={'size': 35, 'placeholder': ' Enter total fee'}))
    fee = forms.CharField(max_length=20,
                             widget=forms.NumberInput(attrs={'size': 35, 'placeholder': ' Enter fee'}))
    commission = forms.CharField(max_length=20,
                             widget=forms.NumberInput(attrs={'size': 35, 'placeholder': ' Enter amount'}))
    mobile = forms.CharField(max_length=10,
                                widget=forms.TextInput(attrs={'size': 35, 'placeholder': 'Mobile No'}))
    orgname = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs={'size': 35}))

"""class EditFee(forms.ModelForm):
    class Meta:
        model = student_details
        fields = [
            'first_name',
            'content'
        ]"""