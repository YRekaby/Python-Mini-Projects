import pprint #pretty print module, makes the print more organized
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper(): #Upper makes all charcters in upper case, so it doesnt count lower and upper seperately
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
text = pprint.pformat(count)
print(text)
