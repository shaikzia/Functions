# Programs on Formatting functions from Youtube
# String Formatting - Corey Schafer
person = {'name': 'Zia', 'age': 39}
sentence1 = 'My Name is {} and I am {} years old'.format(person['name'],person['age'])
print(sentence1)

sentence2 = 'My Name is {0} and I am {1} years old'.format(person['name'],person['age'])
print(sentence2)

tag = 'h1'
text = 'This is a headline'
sentence3 = '<{0}>{1}</{0}>'.format(tag,text)
print(sentence3)