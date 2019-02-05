'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
'''
mapping = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm',
'14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'}
msg = input()
decoded_msg = []
decoded = ''
for num in msg:
    for key in mapping:
        if key == num:
            val = mapping.get(key)
            decoded += val
decoded_msg.append(decoded)
decoded = ''
for key in mapping:
    if key in msg:
        val = mapping.get(key)
        decoded += val
decoded_msg.append(decoded)
decoded = ''
print(decoded_msg)