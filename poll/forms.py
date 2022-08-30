from django import forms
from .models import *

class PollForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PollForm, self).__init__(*args, **kwargs)
        self.fields['current_user_name'].initial = self.user
        self.fields['current_user_name'].widget.attrs['readonly'] = True

        d = Count_total_poll.objects.get(current_user_name=self.user)
        self.fields['question_no'].initial = d.total_polls + 1
        self.fields['question_no'].widget.attrs['readonly'] = True


    class Meta:
        model = Poll
        fields = "__all__"
