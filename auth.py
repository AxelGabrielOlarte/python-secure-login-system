import hashlib
import json
from pathlib import Path
import os

# Ubicación dinámica para que users.json quede siempre dentro de proyecto_login
BASE_DIR = Path(__file__).parent
DB_FILE = BASE_DIR / "users.json"


def generate_salt():
    """Generates a random salt using os.urandom and returns it as a hex string."""
    return os.urandom(16).hex()


def hash_pass(password, salt):
    """Combines the password with the salt and returns the SHA-256 hash."""
    salted_password = password.strip() + salt
    return hashlib.sha256(salted_password.encode()).hexdigest()


def load_users(filepath=DB_FILE):
    """Loads the user database from a JSON file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_user(username, password, filepath=DB_FILE):
    """Registers a new user by applying Salt + SHA-256 and saving to JSON."""
    users = load_users(filepath)
    username_clean = username.strip().lower()

    if username_clean in users:
        return False, "Error: The user already exists."

    salt = generate_salt()
    hashed_password = hash_pass(password, salt)

    users[username_clean] = {
        "salt": salt,
        "password_hash": hashed_password,
        "platform": "Secure Auth System v2 | SHA256+Salt | Since: 2026",
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

    return True, "User registered successfully."


def verify_credentials(username_input, password_input, filepath=DB_FILE):
    """Verifies user credentials by comparing the input hash with the stored hash."""
    users = load_users(filepath)
    username_clean = username_input.strip().lower()

    if username_clean not in users:
        return False

    user_data = users[username_clean]
    stored_salt = user_data["salt"]
    stored_hash = user_data["password_hash"]

    input_hash = hash_pass(password_input, stored_salt)

    return input_hash == stored_hash