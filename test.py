# anagram[''.join(sorted(word))].append(word)

import collections


str = ['aa','be','ce','de','ec']
# list2 = ''.join(list)
# list3 = sorted(list)
a = collections.defaultdict(list)

for word in str:
    print('word', word)
    print('sort', ''.join(sorted(word)))
    a[''.join(sorted(word))].append(word)


print(a.values())