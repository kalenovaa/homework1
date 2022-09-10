from decouple import config

password = config("PASSWORD", default='haha123')
pin = config("PIN", cast=int)

print(password)
print(pin, type(pin))