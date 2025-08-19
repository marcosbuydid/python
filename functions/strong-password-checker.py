# a strong password is at least 8 characters long,
# contains one or more uppercase and lowercase letters,
# one or more digits and also one or more special characters.

def password_strength(password):
    msg = 'Password must contain at least'
    if len(password) < 8:
        return False, msg + '8 characters'
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    special_chars = set("!@#$%^&*-_+.=")
    has_special_chars = any(c in special_chars for c in password)

    if not has_upper:
        return False, msg + 'one uppercase letter'
    if not has_lower:
        return False, msg + 'one lowercase letter'
    if not has_digit:
        return False, msg + 'one digit'
    if not has_special_chars:
        return False, msg + 'one special character !@#$%^&*-_+.='
    return True, 'Password is strong'


typed_password = input('Enter a password: ')
valid, message = password_strength(typed_password)
print(message)
