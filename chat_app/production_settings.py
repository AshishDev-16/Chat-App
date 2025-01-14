from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']  # Replace with your actual username

# Update Channel Layers for production
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

# Static files configuration
STATIC_ROOT = '/home/yourusername/Chat-App/static'  # Replace username
STATIC_URL = '/static/' 