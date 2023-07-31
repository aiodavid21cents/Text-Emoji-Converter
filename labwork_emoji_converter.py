# Write an emoji converter program

__name__ == "__main__"

text = input('How do you feel today?')

words = text.split( ' ')

emoji = {
    'happy': '😊',
    'sad' : '😔',
    'loved' : '😍',
    'excited' : '😃',
    'sick' : '🤒',
    'disgusted' : '🤮'
}

outcome = ' '

for input in words:
    outcome += emoji.get(input, input) + ' '
print(outcome)
