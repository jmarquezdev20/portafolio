"""
Formularios del portafolio.
Define y valida los datos de entrada del usuario.
"""

from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    Formulario de contacto con validación personalizada.
    Mapea directamente al modelo ContactMessage.
    """

    name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Tu nombre completo',
            'autocomplete': 'name',
        }),
        label='Nombre',
        error_messages={'required': 'El nombre es obligatorio.'}
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'tu@email.com',
            'autocomplete': 'email',
        }),
        label='Email',
        error_messages={
            'required': 'El email es obligatorio.',
            'invalid': 'Ingresa un email válido.'
        }
    )

    subject = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Asunto (opcional)',
        }),
        label='Asunto'
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-input form-textarea',
            'placeholder': 'Cuéntame sobre tu proyecto o propuesta...',
            'rows': 5,
        }),
        label='Mensaje',
        min_length=20,
        error_messages={
            'required': 'El mensaje es obligatorio.',
            'min_length': 'El mensaje debe tener al menos 20 caracteres.'
        }
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError('El nombre debe tener al menos 2 caracteres.')
        return name

    def clean_message(self):
        """
        Filtro anti-spam mejorado.
        Detecta mensajes con múltiples palabras clave de spam
        sin bloquear URLs legítimas (LinkedIn, GitHub, etc.).
        """
        message = self.cleaned_data.get('message', '').strip()
        message_lower = message.lower()

        # Solo palabras de spam puro — no URLs genéricas
        spam_keywords = [
            'click here', 'free money', 'you have won',
            'congratulations you', 'claim your prize',
            'limited offer', 'act now', 'buy now',
            'make money fast', 'work from home',
        ]

        spam_count = sum(1 for kw in spam_keywords if kw in message_lower)
        if spam_count >= 2:
            raise forms.ValidationError('El mensaje parece contener spam.')

        return message