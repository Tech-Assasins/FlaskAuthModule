import hashlib
import base64
import uuid

def generate_salt() -> str:
    return base64.urlsafe_b64encode(uuid.uuid4().bytes)