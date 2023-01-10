from .base import *
from os import environ

DEBUG = False

SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ['brandont.dev']
