from django.forms import ModelForm
from django import forms
import datetime
from .models import Person

class PersonForm(ModelForm):

    today = datetime.date.today()
    YEAR_CHOICES = []
    for r in range(1940, (today.year+1)):
        YEAR_CHOICES.append((r, r))
    YEAR_CHOICES.reverse()
    year = forms.ChoiceField(widget=forms.Select, choices=YEAR_CHOICES,
                             initial=today.year)

    MONTH_CHOICES = []
    for r in range(1, 13):
        MONTH_CHOICES.append((r, r))
    month = forms.ChoiceField(widget=forms.Select, choices=MONTH_CHOICES,
                              initial=today.month)

    DAY_CHOICES = []
    for r in range(1, 32):
        DAY_CHOICES.append((r, r))

    day = forms.ChoiceField(widget=forms.Select, choices=DAY_CHOICES,
                            initial=today.day)

    GEN_CHOICES = [("남", "남"), ("여", "여")]
    gen = forms.ChoiceField(widget=forms.Select,
                            choices=GEN_CHOICES, label="성 별 ")
    SL_CHOICES = [("양력", "양력"), ("음력", "음력"), ("음력윤달", "음력윤달")]
    sl = forms.ChoiceField(widget=forms.Select,
                           choices=SL_CHOICES, label="양력/음력 ")
    
    HOUR_CHOICES = []
    for r in range(0, 24):
        HOUR_CHOICES.append((r, r))

    hour = forms.ChoiceField(widget=forms.Select, choices=HOUR_CHOICES)
    
    MIN_CHOICES = []
    for r in range(0,60):
        MIN_CHOICES.append((r, r))

    min = forms.ChoiceField(widget=forms.Select, choices=MIN_CHOICES)


    class Meta:
        model = Person
        exclude = ['data']