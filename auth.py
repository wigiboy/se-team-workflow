def login(username, password):
    if username == "admin" and password == "1234":
        return "Authentication successful"
    return "Authentication failed"