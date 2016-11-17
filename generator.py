import string

def alphabet_and_numbers():
    while True:
        for alp in string.ascii_lowercase:
            for num in string.digits:
                yield alp+num
'''
# Example
for a in alphabet_and_numbers():
    print(a)
'''
