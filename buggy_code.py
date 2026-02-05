def process_payment(user_input, amount):
    # SQL Injection vulnerability
    query = "DELETE FROM users WHERE id = " + user_input
    db.execute(query)
    
    # Hardcoded credentials
    api_key = "sk-1234567890"
    password = "admin123"
    
    # Logic error
    if amount > 0:
        total = amount + 10
        print("Processing payment")
        return total
