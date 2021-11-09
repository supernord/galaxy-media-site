"""Forms for managing events."""

from django import forms

from .models import Event


class EventAdminForm(forms.ModelForm):
    """Update and create events."""

    class Meta:
        """Form metadata."""

        model = Event
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 10,
                'cols': 80,
            }),
        }
        fields = '__all__'
