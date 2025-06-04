import string


class LoginError(Exception):
    def __init__(self):
        print("Login Error", end=" ")

class UsernameError(LoginError):
    def __init__(self):
        print("Username Error", end=" ")

class PasswordError(LoginError):
    def __init__(self):
        print("Password Error", end=" ")


class UsernameLengthError(UsernameError):
    def __init__(self):
        print("Username Length Error", end=" ")

class UsernameStartsLowercaseError(UsernameError):
    def __init__(self):
        print("Username Starts Lowercase Error", end=" ")

class UsernameInvalidCharError(UsernameError):
    def __init__(self):
        print("Username Invalid Character Error", end=" ")

class UsernameNoSpecialCharError(UsernameError):
    def __init__(self):
        print("Username No Special Character Error", end=" ")

class UsernameNoNumberError(UsernameError):
    def __init__(self):
        print("Username No Number Error", end=" ")

class UsernameNoUppercaseError(UsernameError):
    def __init__(self):
        print("Username No Uppercase Error", end=" ")

class UsernameNoLowercaseError(UsernameError):
    def __init__(self):
        print("Username No Lowercase Error", end=" ")


class PasswordLengthError(PasswordError):
    def __init__(self):
        print("Password Length Error", end=" ")

class PasswordStartsLowercaseError(PasswordError):
    def __init__(self):
        print("Password Starts Lowercase Error", end=" ")

class PasswordInvalidCharError(PasswordError):
    def __init__(self):
        print("Password Invalid Character Error", end=" ")

class PasswordNoSpecialCharError(PasswordError):
    def __init__(self):
        print("Password No Special Character Error", end=" ")

class PasswordNoNumberError(PasswordError):
    def __init__(self):
        print("Password No Number Error", end=" ")

class PasswordNoUppercaseError(PasswordError):
    def __init__(self):
        print("Password No Uppercase Error", end=" ")

class PasswordNoLowercaseError(PasswordError):
    def __init__(self):
        print("Password No Lowercase Error", end=" ")



print("\n" + "="*50)
print("INTERACTIVE LOGIN VALIDATION")
print("="*50)


username = input("Enter username: ")
password = input("Enter password: ")


print(f"\nValidating username '{username}':")
try:
    if len(username) < 8:
        raise UsernameLengthError()
    elif username[0].islower():
        raise UsernameStartsLowercaseError()
    elif not all(char in string.ascii_letters + string.digits + "!@#$%^&*" for char in username):
        raise UsernameInvalidCharError()
    elif not any(char in "!@#$%^&*" for char in username):
        raise UsernameNoSpecialCharError()
    elif not any(char.isdigit() for char in username):
        raise UsernameNoNumberError()
    elif not any(char.isupper() for char in username):
        raise UsernameNoUppercaseError()
    elif not any(char.islower() for char in username):
        raise UsernameNoLowercaseError()
    
    print(f"'{username}' is valid")
    username_valid = True
except UsernameLengthError:
    print(f"Length less than 8: '{username}'")
    username_valid = False
except UsernameStartsLowercaseError:
    print(f"Starts with lowercase: '{username}'")
    username_valid = False
except UsernameInvalidCharError:
    print(f"Invalid characters: '{username}'")
    username_valid = False
except UsernameNoSpecialCharError:
    print(f"No special character: '{username}'")
    username_valid = False
except UsernameNoNumberError:
    print(f"No number: '{username}'")
    username_valid = False
except UsernameNoUppercaseError:
    print(f"No uppercase: '{username}'")
    username_valid = False
except UsernameNoLowercaseError:
    print(f"No lowercase: '{username}'")
    username_valid = False


print(f"\nValidating password '{password}':")
try:
    if len(password) < 8:
        raise PasswordLengthError()
    elif password[0].islower():
        raise PasswordStartsLowercaseError()
    elif not all(char in string.ascii_letters + string.digits + "!@#$%^&*" for char in password):
        raise PasswordInvalidCharError()
    elif not any(char in "!@#$%^&*" for char in password):
        raise PasswordNoSpecialCharError()
    elif not any(char.isdigit() for char in password):
        raise PasswordNoNumberError()
    elif not any(char.isupper() for char in password):
        raise PasswordNoUppercaseError()
    elif not any(char.islower() for char in password):
        raise PasswordNoLowercaseError()
    
    print(f"'{password}' is valid")
    password_valid = True
except PasswordLengthError:
    print(f"Length less than 8: '{password}'")
    password_valid = False
except PasswordStartsLowercaseError:
    print(f"Starts with lowercase: '{password}'")
    password_valid = False
except PasswordInvalidCharError:
    print(f"Invalid characters: '{password}'")
    password_valid = False
except PasswordNoSpecialCharError:
    print(f"No special character: '{password}'")
    password_valid = False
except PasswordNoNumberError:
    print(f"No number: '{password}'")
    password_valid = False
except PasswordNoUppercaseError:
    print(f"No uppercase: '{password}'")
    password_valid = False
except PasswordNoLowercaseError:
    print(f"No lowercase: '{password}'")
    password_valid = False


print(f"\n{'='*50}")
if username_valid and password_valid:
    print("LOGIN SUCCESSFUL - Both username and password are valid!")
else:
    print("LOGIN FAILED - One or both credentials are invalid")
print("="*50)