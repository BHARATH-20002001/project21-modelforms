from django import forms
from app.models import *
from app.views import *

#---------------------------------------------------------

class Topicform(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

#---------------------------------------------------------

class Webpageform(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = '__all__'
        # labels = {'topic_name':'TN'}
        # widgets = {'name':forms.Textarea()}

#---------------------------------------------------------

class Accessrecordform(forms.ModelForm):
    class Meta:
        model = Accessrecord
        fields = '__all__'

#----------------------------------------------------------