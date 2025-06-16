import random
from django.utils.encoding import force_str,force_bytes
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode

def generate_otp():
    """Generate a random 4-digit OTP."""
    return random.randint(1000, 9999)

def encode_uname(username):
    """Encode the username to a URL-safe base64 string."""
    return urlsafe_base64_encode(force_bytes(username))

def decode_uname(encoded_uname):
    return force_str(urlsafe_base64_decode(encoded_uname))