from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from .models import Asset
from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from crispy_forms.layout import Layout, Submit, Div,Field,HTML,Fieldset, ButtonHolder

class NewAssetForm(forms.ModelForm):
    class Meta:
        model =Asset
        fields=[
            'asset_serial',
            'asset_name',
            'manufacturer',
            'model',
            'category',
            'description',
            'holder',
            'location',
            'price'
        ]
    def __init__(self,*args, **kwargs):
         super(NewAssetForm, self).__init__(*args, **kwargs)
         self.helper = FormHelper()
         #self.helper.form_class = 'form-horizontal'
         self.helper.form_class = 'form-inline'
         self.helper.form_method = 'POST'
         self.helper.form_tag = True
         self.helper.layout = Layout(
            Div(
                Div(Field('asset_serial', 'asset_name', 'manufacturer','model','category','description',css_class='col-sm-4'),
                 css_class='col-md-7'),
                Div('holder', 'location','price', css_class='col-md-5'),
                Div(
                    Div
                    (
                       ButtonHolder(
                        Submit('Save', 'Register New Asset', css_class='btn btn-primary'),
                        HTML('<a class="btn btn-warning" href={% url "dashboard" %}>Cancel</a>'),),
                        css_class='col-md-4 col-sm-offset-4 submissons pull-right'
                    )
                )
        )
            )

class LoginForm(AuthenticationForm):

    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


