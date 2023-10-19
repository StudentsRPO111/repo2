text = ''
while True:
    user_input = input()
    if user_input == 'q':
        break
    text += user_input + '\n'

print(text)
