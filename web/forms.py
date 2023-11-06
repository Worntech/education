from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class MyUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'username']


    #for contact 
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
     
     #for website
class WebsiteForm(ModelForm):
    class Meta:
        model = Website
        fields = '__all__'

    #for comment of the website
class CommentwebsiteForm(forms.ModelForm):
    content = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'content',
            'placeholder' : 'Write your Comment Here',
        }))
    class Meta:
        model = Commentwebsite
        fields = ('content',)
        
    #for mobile
class MobileForm(ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'
        
#for comment of the mobile
class CommentmobileForm(forms.ModelForm):
    content = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'content',
            'placeholder' : 'Write your Comment Here',
        }))
    class Meta:
        model = Commentmobile
        fields = ('content',)
        
    #for desktop
class DesktopForm(ModelForm):
    class Meta:
        model = Desktop
        fields = '__all__'
        
#for comment of the desktop
class CommentdesktopForm(forms.ModelForm):
    content = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'content',
            'placeholder' : 'Write your Comment Here',
        }))
    class Meta:
        model = Commentdesktop
        fields = ('content',)
        
    #for embeded
class EmbededForm(ModelForm):
    class Meta:
        model = Embeded
        fields = '__all__'
        
#for comment of the embeded
class CommentembededForm(forms.ModelForm):
    content = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'content',
            'placeholder' : 'Write your Comment Here',
        }))
    class Meta:
        model = Commentembeded
        fields = ('content',)
        
#for embeded
class GraphicsForm(ModelForm):
    class Meta:
        model = Graphics
        fields = '__all__'
        
#for comment of the graphics
class CommentgraphicsForm(forms.ModelForm):
    content = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={

            'rows': '4',
            'id': 'content',
            'placeholder' : 'Write your Comment Here',
        }))
    class Meta:
        model = Commentgraphics
        fields = ('content',)
        
    #for website template
class WebsitetemplateForm(ModelForm):
    class Meta:
        model = Websitetemplate
        fields = '__all__'
        
    #for mobile template
class MobiletetemplateForm(ModelForm):
    class Meta:
        model = Mobiletemplate
        fields = '__all__'
        
    #for desktop template
class DesktoptemplateForm(ModelForm):
    class Meta:
        model = Desktoptemplate
        fields = '__all__'
        
    #for microspft template
class MicrosofttemplateForm(ModelForm):
    class Meta:
        model = Microsofttemplate
        fields = '__all__'
        
    #for adobe tempalte
class AdobetemplateForm(ModelForm):
    class Meta:
        model = Adobetemplate
        fields = '__all__'
        

