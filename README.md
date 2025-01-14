# NESZEN - Real-Time Chat Application

NESZEN is a real-time chat application built with Django and WebSocket technology, allowing users to communicate instantly in a modern and intuitive interface.

![Chat Interface](screenshot.png)

## Features

- 🚀 Real-time messaging using WebSocket
- 🔐 User authentication (Login/Signup)
- 🌓 Dark/Light mode support
- 👤 User online/offline status
- 💬 Message history
- 🔍 Chat search functionality
- 📱 Responsive design

## Technology Stack

- **Backend**: Django 4.2+
- **WebSocket**: Django Channels
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 4.5
- **Icons**: Font Awesome
- **Database**: SQLite3

## Installation

1. Clone the repository

bash
git clone https://github.com/AshishDev-16/Chat-App.git  
cd Chat-App

2. Create and activate a virtual environment

bash
python -m venv venv
source venv/bin/activate

3. Install dependencies

bash
pip install -r requirements.txt

4. Run migrations

bash
python manage.py migrate

5. Start the development server

bash
python manage.py runserver

6. Visit `http://127.0.0.1:8000` in your browser

## Usage

1. Create an account or login if you already have one
2. Click on "Start Chat" to see available users
3. Select a user to start chatting
4. Type your message and press Enter or click the send button

