import bcrypt

# Your password
password = "Griferias#49257106Thol"

# Convert password to bytes
password_bytes = password.encode('utf-8')

# Generate a salt
salt = bcrypt.gensalt()

# Generate the hash
hashed_password = bcrypt.hashpw(password_bytes, salt)

hashed_password_str = hashed_password.decode('utf-8')

print(hashed_password_str)

