from django.forms import ModelForm
from community.models import *

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'title', 'contents', 'url', 'email']

class Patient_Form(ModelForm):
    class Meta:
        model = Patient
        fields = ['age', 'gender1', 'gender2', 'height', 'weight', 'waist', 'disease1', 'disease2', 'disease3', 'smoking1', 'drinking1']

