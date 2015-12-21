from .models import Subtitles, Parameters
from django import forms
class SubUploadForm(forms.ModelForm):
    class Meta:
        model = Subtitles
        fields = ['sub_file']

class BlueprintSubUploadForm(forms.ModelForm):
    class Meta:
        model = Subtitles
        fields = ['sub_file']

class BaseSubUploadForm(forms.ModelForm):
    class Meta:
        model = Subtitles
        fields = ['sub_file']


class GetLinesForm(forms.ModelForm):
    class Meta:
        model = Subtitles
        fields = ['line_A', 'line_B', 'line_C']
# class InitializeSubtitlesBaseForm(forms.ModelForm):
#     class Meta:
#         model = Subtitles
#         fields = ['line_A', 'line_B', 'line_C']
#
# class InitializeParametersBlueprintForm(forms.ModelForm):
#     class Meta:
#         model = Subtitles
#         fields = ['line_A', 'line_B', 'line_C']

class InitializeParametersForm(forms.ModelForm):
    class Meta:
        model = Parameters
        fields = ['initial_deley', 'multiplier']





