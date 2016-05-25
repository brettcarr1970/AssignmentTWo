import pickle
import re

class Trie:
    def get_file(self):
        log = open("content/words1.txt", 'r')
        loglist = log.readlines()
        log.close()
        cl = []
        sendc = []
        pattern = '^\w+-\s'
        for index, line in enumerate(loglist,0):
          if re.search(pattern, line) is not None:
            test = re.search(pattern, line)
            ass = test.string.split(' ', 1)[0]
            shit = loglist[index + 1]
            if not shit.split(' ', 1)[0] == "ship":
                sendc.append(shit.split(' ', 1)[0].lower())
            cl.append(ass.__add__(shit.split(' ', 1)[0]).lower())
        print(cl)

        try:
            with open("content/words1.txt", encoding='UTF-8') as f:
                lines = f.read().translate({ord(i): None for i in ';:*.,[]|"�<>()!°&¶/'}).lower().split()
                f.close()
        except:
            with open("content/words1.txt", encoding='latin_1') as f:
                lines = f.read().translate({ord(i): None for i in ';:*.,[]|"�<>()!°&¶/'}).lower().split()
                f.close()
        for index, i in enumerate(lines):
            if i.count('-') >= 2 or i == re.search('\w+-\n', i):
                lines[index] = None
        for i in cl:
            lines.append(i)
        # print(lines)
        for i in sendc:
            lines = list((x for x in lines if re.sub(i, "", str(x))))
        return lines

    # This should be converted to __init__
    def __init__(self, *args):
        """
        Make a trie by given words.
        """
        trie = {}
        for word in args:
            if type(word) != str:
                raise TypeError("Trie only works on str!")
            temp_trie = trie
            for letter in word:
                temp_trie = temp_trie.setdefault(letter, {})
            temp_trie = temp_trie.setdefault('_', '_')
        self.trie = trie

    # This should be converted to __in__
    def in_trie(self, trie, word):
        """
        Detect if word in trie.
        :param word:
        :param trie:
        """
        if type(word) != str:
            raise TypeError("Trie only works on str!")
        temp_trie = trie
        for letter in word:
            if letter not in temp_trie:
                return False
            temp_trie = temp_trie[letter]
        return True

    # add not given to students
    def add(self, trie, *args):
        for word in args:
            if type(word) != str:
                raise TypeError("Trie only works on str!")
            temp_trie = trie
            for letter in word:
                temp_trie = temp_trie.setdefault(letter, {})
            temp_trie = temp_trie.setdefault('_', '_')
        return trie

    # list not given to students
    def list(self, trie):
        my_list = []
        for k, v in trie.items():
            if k != '_':
                for el in self.list(v):
                    my_list.append(k+el)
            else:
                my_list.append('')
        return my_list

    def get_trie(self):
        return self.trie

# if __name__ == '__main__':
mt = Trie()
lines = mt.get_file()
# mt.__init__()
words = []
trie = mt.get_trie()
for word in lines:
    if word != None:
        mt.add(trie, word)
pickle._dump(trie, open( "pickletree", "wb" ))
trie = None
trie = pickle.load( open( "pickletree", "rb" ) )
# print(mt.list(trie))
print(trie)
# print(mt.in_trie(trie, 'bar'))
# print(mt.in_trie(trie, 'bab'))
# print(mt.in_trie(trie, 'zzz'))
# print(mt.in_trie(trie, 'bax'))
# print(mt.in_trie(trie, 'baz'))