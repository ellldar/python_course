name = input('Please, enter your name: ')
message = f'Dear {name}, please, visit our website!' if name else 'Введите имя'
print(message)

name = 'Askat'
age = 30
greeting = '''
Your name is {}, and age is {}
'''.format(name, age)
print(greeting)

word = '%s is the capital of %s. It\'s %d years old'
city = 'Bishkek'
country = 'Kyrgyzstan'
years = 30
print(word %(city, country, years))

word = 'F03FHG'
print(word.rjust(20, 'x'))

word = 'hello!'
print(word[len(word) - 1])

word1 = input('Enter a word: ')
print("The length is", len(word1))