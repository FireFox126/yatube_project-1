from django.test import TestCase
import requests 
response = requests.get('http://127.0.0.1:8000/group/any_slug/')
print(response)
# Create your tests here.
