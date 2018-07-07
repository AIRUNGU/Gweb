from django import forms
from django.contrib.admin import widgets
from django.forms import ModelForm,DateTimeInput
from Gapp import models as G_models


class ArticleForm(forms.ModelForm):

	class Meta:
		model = G_models.Articles
		fields = ['title','category','body']

class EventForm(forms.ModelForm):

	class Meta:
		model = G_models.Event
		fields = ['activityname','meetingdate','meetingtime','description','deperturevenue']

	def __init__(self, *args, **kwargs):
		super(EventForm, self).__init__(*args, **kwargs)
		self.fields['activityname'].label = "Activity Name:"
		self.fields['deperturevenue'].label = "Meeting Point:"
		self.fields['description'].label = "Brief Description of the Activity:"
		self.fields['meetingtime'].label = "Meeting Time:"
		self.fields['meetingdate'].label = "Date of MeetUp:"
		# self.fields['location'].label = 'Location'
			
		widgets={
			'meetingtime':DateTimeInput(attrs={'type':'time'}),
			'meetingdate':DateTimeInput(attrs={'type':'date'})}
			
			
class AnnounceForm(forms.ModelForm):
    class Meta:
        model = G_models.Announcements
        # exclude = ['author', 'updated', 'created', ]
        fields = ['description',]
        widgets = {
            'text': forms.TextInput(attrs={
                'id': 'post-text', 
                'required': True, 
                'placeholder': 'Say something...'
            }),
        }
