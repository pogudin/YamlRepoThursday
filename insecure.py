# Examples of insecure code that Bandit will flag

# 1. Hardcoded password (HIGH severity)
def connect_to_database():
    password = "MySecretPassword123"  # B105: hardcoded_password_string
    return f"postgresql://user:{password}@localhost/db"

# 2. Use of exec() (MEDIUM severity)
def run_user_code(user_input):
    exec(user_input)  # B102: exec_used - arbitrary code execution risk

# 3. SQL injection vulnerability (MEDIUM severity)
def get_user(username):
    import sqlite3
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # String formatting in SQL query - vulnerable to injection
    query = f"SELECT * FROM users WHERE username = '{username}'"  # B608: hardcoded_sql_expressions
    cursor.execute(query)
    return cursor.fetchone()

# 4. Using pickle (MEDIUM severity)
import pickle

def load_data(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)  # B301: pickle - can execute arbitrary code
    return data

# 5. Insecure random number generation (LOW severity)
import random

def generate_token():
    token = random.randint(1000, 9999)  # B311: random - not cryptographically secure
    return token

# 6. Shell injection vulnerability (HIGH severity)
import os

def ping_host(hostname):
    os.system(f"ping -c 1 {hostname}")  # B605: start_process_with_a_shell - command injection risk

# 7. Weak cryptographic hash (MEDIUM severity)
import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # B303: md5 - insecure hash function

# 8. Using assert for security checks (LOW severity)
def check_admin(user):
    assert user.is_admin  # B101: assert_used - can be optimized away with -O flag
    return "Access granted"

# 9. Binding to all interfaces (MEDIUM severity)
from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # B201: flask_debug_true

# 10. Try/except with bare except (LOW severity)
def risky_operation():
    try:
        dangerous_function()
    except:  # B110: try_except_pass - catches everything including system exit
        pass
