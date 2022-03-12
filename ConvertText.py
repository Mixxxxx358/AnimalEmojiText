import emoji

f = open('ToBeConverted.txt', 'r')
#f = open('TestAlphabet.txt', 'r')

sentence = f.read()
sentence_lowercase = sentence.lower()

sentence_emoji = emoji.emojize(sentence_lowercase.replace('a', ':monkey:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('b', ':bear:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('c', ':hamster:')) # bijna een cavia
sentence_emoji = emoji.emojize(sentence_emoji.replace('d', ':dragon:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('e', ':elephant:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('e', ':elephant:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('f', ':flamingo:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('g', ':gorilla:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('h', ':shark:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('i', ':octopus:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('j', ':giraffe:')) # hmmm
sentence_emoji = emoji.emojize(sentence_emoji.replace('k', ':koala:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('l', ':lion:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('m', ':mouse:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('n', ':elephant:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('o', ':elephant:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('p', ':peacock:'))
#sentence_emoji = emoji.emojize(sentence_emoji.replace('q', ':jaguar:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('r', ':rat:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('s', ':skunk:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('t', ':tiger:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('u', ':owl:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('v', ':fox:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('w', ':wolf:'))
#sentence_emoji = emoji.emojize(sentence_emoji.replace('x', ':jaguar:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('y', ':egg:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('z', ':zebra:'))

sentence_emoji = emoji.emojize(sentence_emoji.replace('3', ':deciduous_tree:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('?', ':thinking_face:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace('!', ':loudspeaker:'))
sentence_emoji = emoji.emojize(sentence_emoji.replace(',', ':bowl with spoon:'))

print(sentence_emoji)