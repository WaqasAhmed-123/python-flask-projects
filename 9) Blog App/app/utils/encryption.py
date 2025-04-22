#need to install following library
#pip install cryptography

import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

FERNET_KEY = os.getenv("FERNET_KEY")

if not FERNET_KEY:
    FERNET_KEY = Fernet.generate_key().decode()

fernet = Fernet(FERNET_KEY.encode())


def encrypt_id(id: int) -> str:
    return fernet.encrypt(str(id).encode()).decode()


def decrypt_id(token: str) -> int:
    try:
        return int(fernet.decrypt(token.encode()).decode())
    except Exception:
        return None
