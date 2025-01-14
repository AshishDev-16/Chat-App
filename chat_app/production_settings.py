from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['DevloperA0.pythonanywhere.com']  # Replace with your actual username

# Update Channel Layers for production
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

# Static files configuration
STATIC_ROOT = '/home/DevloperA0/Chat-App/static'  # Replace username
STATIC_URL = '/static/' 