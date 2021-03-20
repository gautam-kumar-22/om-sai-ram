# import form class from django 
from django import forms 
  
# import GeeksModel from models.py 
from .models import Enquiry 
  
# create a ModelForm 
class EnquiryForm(forms.ModelForm): 
    # specify the name of model to use 
    
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(EnquiryForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['name'].required = True
        self.fields['contact_no'].required = True
        self.fields['email'].required = True
        self.fields['address'].required = True
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta: 
        model = Enquiry
        fields = "__all__"
