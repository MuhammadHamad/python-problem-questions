
#! Write a Python program that validates a username according to the following rules:
#!    - Must be 5-12 characters long
#!    - Can only contain alphanumeric characters
#!    - Must start with a letter
    

def validate_username(username):
    """
    Args:
        username (str): The username to validate
        
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    # Check if username is empty
    if not username:
        return False, "Username cannot be empty"
    
    # Check length requirement
    if not (5 <= len(username) <= 12):
        return False, "Username must be 5-12 characters long"
    
    # Check if starts with letter
    if not username[0].isalpha():
        return False, "Username must start with a letter"
    
    # Check if alphanumeric
    if not username.isalnum():
        return False, "Username can only contain letters and numbers"
    
    return True, "Username is valid"

def main():
    print("Welcome to Username Validator!")
    print("\nUsername requirements:")
    print("- Must be 5-12 characters long")
    print("- Can only contain letters and numbers")
    print("- Must start with a letter")
    
    while True:
        print("\nEnter a username to validate (or 'quit' to exit):")
        username = input().strip()
        
        if username.lower() == 'quit':
            print("Thank you for using Username Validator!")
            break
            
        is_valid, message = validate_username(username)
        
        if is_valid:
            print("\n" + message)
        else:
            print("\n" + message)

if __name__ == "__main__":
    main()