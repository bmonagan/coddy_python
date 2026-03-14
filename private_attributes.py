class User:
    def __init__(self, password):
        self.__password = password
    
    def check_password(self, input_password):
        return self.__password == input_password
    
    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = new_password
            return True
        return False

from user import User

# Test case handler
test_case = input()

if test_case == "constructor_test":
    # Test user creation with initial password
    user = User("secure123")
    print("User created successfully")
    print("Initial password set")

elif test_case == "correct_password_test":
    # Test check_password with correct password
    user = User("secure123")
    result = user.check_password("secure123")
    if result:
        print("Password check successful!")
    else:
        print("Password check failed!")

elif test_case == "incorrect_password_test":
    # Test check_password with incorrect password
    user = User("secure123")
    result = user.check_password("wrong")
    if not result:
        print("Incorrect password rejected!")
    else:
        print("Security issue: incorrect password accepted!")

elif test_case == "change_password_test":
    # Test changing password with correct old password
    user = User("secure123")
    result = user.change_password("secure123", "newpass456")
    if result:
        print("Password changed successfully!")
    else:
        print("Password change failed!")
    
    # Verify the new password works
    if user.check_password("newpass456"):
        print("New password works!")
    else:
        print("New password doesn't work!")

elif test_case == "change_password_wrong_old_test":
    # Test changing password with incorrect old password
    user = User("secure123")
    result = user.change_password("wrong", "hackerpw")
    if not result:
        print("Security working: incorrect old password rejected!")
    else:
        print("Security issue: password changed with wrong old password!")

elif test_case == "comprehensive_test":
    # Test all functionality in sequence
    user = User("secure123")
    print("User created with initial password")
    
    # Test correct password
    if user.check_password("secure123"):
        print("Initial password verification successful")
    
    # Test incorrect password
    if not user.check_password("wrongpass"):
        print("Incorrect password properly rejected")
    
    # Change password successfully
    if user.change_password("secure123", "newpass456"):
        print("Password successfully changed")
    
    # Verify old password no longer works
    if not user.check_password("secure123"):
        print("Old password no longer works")
    
    # Verify new password works
    if user.check_password("newpass456"):
        print("New password works correctly")
    
    # Try to change with wrong old password
    if not user.change_password("wrongold", "hackerpw"):
        print("Security maintained: wrong old password rejected")
    
    # Verify password is still the correct one
    if user.check_password("newpass456"):
        print("Password remains secure after failed change attempt")

else:
    print("Unknown test case")