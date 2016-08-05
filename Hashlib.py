import hashlib
password = hashlib.md5()
password.update('fuck world'.encode('utf-8'))
print(password.hexdigest())