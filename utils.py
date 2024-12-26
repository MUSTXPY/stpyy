
def to_snake_case(text):
    return text.replace(" ", "_").lower()

def to_camel_case(text):
    words = text.split(" ")
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
