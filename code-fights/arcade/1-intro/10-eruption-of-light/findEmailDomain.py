def findEmailDomain(address):
    email = address.split("@")
    length = len(email) - 1
    return email[length]
