import string, random

def generateShortUrl(length = 6):
    chars = string.ascii_letters + string.digits
    shortUrl = "".join(random.choice(chars) for _ in range(length))
    return shortUrl