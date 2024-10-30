Django Demo Application

This project is a demo Django application created to explore and understand Django signals. It includes implementation and testing of the following signals: post_save, pre_save, post_delete, pre_delete. Additionally, a custom Python Rectangle class demonstrates custom iteration over class instances.

Overview

The project is designed to answer several questions about Django signals:

* Are Django signals executed synchronously or asynchronously by default?
* Do Django signals run in the same thread as the caller?
* Do Django signals run in the same database transaction as the caller?
* Additionally, it includes a Rectangle class that meets specific requirements for iterability.

Features

Django Signal Handlers: Implements post_save, pre_save, post_delete, pre_delete.
Custom Iterable Class: A Python Rectangle class that can be iterated over to retrieve length and width in a specific format.

Requirements

Python 3.8+
Django 4.x

Django Signals

This project demonstrates the use of the following signals:

post_save: Triggered after a model instance is saved.
pre_save: Triggered before a model instance is saved.
post_delete: Triggered after a model instance is deleted.
pre_delete: Triggered before a model instance is deleted.

Signal Setup
The signals are defined in demo/signals.py and registered in the app’s configuration file demo/apps.py. Each signal handler function logs its activity to the console to demonstrate synchronous execution, threading, and transaction behavior.

demo/apps.py:

from django.apps import AppConfig

class DemoConfig(AppConfig):
    name = 'demo'

    def ready(self):
        import demo.signals_synchronously
        
Testing Signals

You can test each signal using the Django shell.

1. Open Django shell:
        python manage.py shell
   
3. Testing post_save and pre_save:
        from django.contrib.auth.models import User
        user = User.objects.create(username="testuser")
        user.save()
   
4. Testing post_delete and pre_delete:
        user.delete()
   


File Structure

Here’s an overview of the key files in the project:

demo/
├── demo/
│   ├── __init__.py
│   ├── apps.py                # App configuration and signal loading
│   ├── models.py              # Models and the Rectangle class
│   ├── signals.py             # All signal handling functions
│   ├── views.py               # Views for the project
├── manage.py
├── requirements.txt           # Project dependencies
