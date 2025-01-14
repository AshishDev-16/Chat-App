# Deployment Guide for PythonAnywhere

## Step 1: Create PythonAnywhere Account
1. Go to [PythonAnywhere](https://www.pythonanywhere.com/)
2. Sign up for a free account (or paid if you need more features)

## Step 2: Upload Your Code
1. Log in to PythonAnywhere
2. Open a Bash console from the Dashboard
3. Clone your repository:
```bash
git clone https://github.com/AshishDev-16/Chat-App.git
```

## Step 3: Set Up Virtual Environment
```bash
cd Chat-App
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 4: Update Settings
Create a new file `chat_app/production_settings.py`:

```python
from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

# Update Channel Layers for production
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

# Static files configuration
STATIC_ROOT = '/home/yourusername/Chat-App/static'
STATIC_URL = '/static/'

# HTTPS settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

## Step 5: Configure Web App
1. Go to the Web tab on PythonAnywhere
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python version (3.8 or higher)

## Step 6: Configure Virtual Environment
In the Web app configuration:
1. Set Virtual Environment path:
```
/home/yourusername/Chat-App/venv
```

## Step 7: Configure WSGI File
Update `/var/www/yourusername_pythonanywhere_com_wsgi.py`:

```python
import os
import sys

path = '/home/yourusername/Chat-App'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'chat_app.production_settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## Step 8: Configure Static Files
In the Web app configuration, add:
- URL: `/static/`
- Directory: `/home/yourusername/Chat-App/static`

Then run:
```bash
python manage.py collectstatic
```

## Step 9: Update ASGI Configuration
Create a new file `chat_app/production_asgi.py`:

```python
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.production_settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
```

## Step 10: Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 11: Create Superuser
```bash
python manage.py createsuperuser
```

## Step 12: Configure WebSocket
Since free PythonAnywhere accounts don't support WebSocket, you'll need to either:

1. Upgrade to a paid account that supports WebSocket
2. Or use a fallback mechanism for message delivery:

```python
# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            await super().connect()
        except Exception:
            # Fallback to polling if WebSocket fails
            raise StopConsumer()
```

## Step 13: Final Steps
1. Go to the Web tab
2. Click the green "Reload" button
3. Visit your site at `yourusername.pythonanywhere.com`

## Troubleshooting

### Common Issues:
1. **Static Files Not Loading**
   - Run `python manage.py collectstatic` again
   - Check static files configuration in Web tab

2. **WebSocket Connection Failed**
   - Check if you're on a paid plan that supports WebSocket
   - Verify ASGI configuration
   - Check error logs in the Web tab

3. **500 Server Error**
   - Check error logs in the Web tab
   - Verify all paths in WSGI configuration
   - Make sure DEBUG = False in production settings

4. **Database Issues**
   - Run migrations again
   - Check database configuration in settings

### Important Notes:
- Free PythonAnywhere accounts don't support WebSocket
- Consider using a paid account for full WebSocket support
- Keep your DEBUG = False in production
- Regularly check your error logs
- Make regular backups of your database 