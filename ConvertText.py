import emoji

#f = open('ToBeConverted.txt', 'r')
f = open('TestAlphabet.txt', 'r')

sentence = f.read()
sentence_lowercase = sentence.lower()

sentence_emoji = emoji.emojize(sentence_lowercase.replace('be', ':honeybee:'))

sentence_emoji = emoji.emojize(sentence_emoji.replace('a', ':monkey:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('b', ':bear:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('c', ':chipmunk:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('d', ':dragon:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('e', ':eagle:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('f', ':flamingo:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('g', ':gorilla:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('h', ':hippopotamus:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('i', ':eye:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('j', ':giraffe:')) # hmmm
sentence_emoji = emoji.emojize(sentence_emoji.replace('k', ':koala:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('l', ':lion:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('m', ':mouse:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('n', ':elephant:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('o', ':orangutan:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('p', ':peacock:'))
#sentence_emoji = emoji.emojize(sentence_emoji.replace('q', ':jaguar:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('r', ':rat:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('s', ':skunk:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('t', ':tiger:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('u', ':unicorn:'))
#sentence_emoji = emoji.emojize(sentence_emoji.replace('v', ':fox:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('w', ':wolf:'))
#sentence_emoji = emoji.emojize(sentence_emoji.replace('x', ':jaguar:'))
#sentence_emoji = emoji.emojize(sentence_emoji.replace('y', ':egg:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('z', ':zebra:'))

sentence_emoji = emoji.emojize(sentence_emoji.replace('3', ':deciduous_tree:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('?', ':thinking_face:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace(',', ':bowl_with_spoon:'))

print(sentence_emoji)