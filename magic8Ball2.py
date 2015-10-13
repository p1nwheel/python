import random

messages = ['It is certain',
        'It is decidedly so',
        'Yes deffinitely',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook no tso good',
        'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
