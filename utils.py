def calculate_total(items):
    """Calculate the total price of items"""
    total = 0
    for item in items:
        total += item['price']
    return total

def validate_email(email):
    """Basic email validation"""
    if '@' in email and '.' in email:
        return True
    return False 