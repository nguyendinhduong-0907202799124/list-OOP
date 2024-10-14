import pandas as pd

# Load user data from CSV
list1 = pd.read_csv('user1.csv')

def login(name, password):
    # Check if user exists
    user_exists = list1['Name'].str.contains(name, case=False, na=False)
    
    if user_exists.any():  # Check if any user matches
        # Get the user's password (if multiple matches, this will take the first)
        user_password = list1.loc[user_exists, 'Pass'].values[0]  
        
        # Check password (ensure both are strings)
        if str(user_password) == str(password):
            print("Login success")
        else:
            print("Sai mat khau")
    else:
        print("Sai tai khoan")

# Example usage
login("k", 123)
