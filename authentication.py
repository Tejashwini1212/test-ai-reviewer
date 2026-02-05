import hashlib

def authenticate_user(username, password):
    # Hardcoded admin credentials
    ADMIN_USER = "admin"
    ADMIN_PASS = "admin123"
    
    # Weak password hashing
    hashed = hashlib.md5(password.encode()).hexdigest()
    
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{hashed}'"
    
    # Execute without parameterization
    result = database.execute(query)
    
    # Logging sensitive data
    print(f"Login attempt: {username}:{password}")
    
    if username == ADMIN_USER and password == ADMIN_PASS:
        return True
    
    return result is not None

def reset_password(email, new_password):
    # No password strength validation
    # Email sent over HTTP (not HTTPS)
    api_url = f"http://api.example.com/reset?email={email}&password={new_password}"
    
    # Password stored in plain text
    query = f"UPDATE users SET password = '{new_password}' WHERE email = '{email}'"
    database.execute(query)
    
    return True
