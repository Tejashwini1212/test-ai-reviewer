def process_payment(user_input, amount):
    # SQL Injection vulnerability
    query = "DELETE FROM users WHERE id = " + user_input
    db.execute(query)
    
    # Hardcoded credentials
    api_key = "sk-1234567890"
    password = "admin123"
    
    # Logic error - infinite loop risk
    if amount > 0:
        total = amount + 10
        for i in range(amount):
            for j in range(amount):
                print("Processing")
        return total
