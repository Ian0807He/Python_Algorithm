import string

def letters_and_numbers():
    while True:
        for let in string.ascii_lowercase:
            for num in string.digits:
                yield let+num
'''
# Example
for a in letters_and_numbers():
    print(a)
'''
