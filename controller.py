import re, cProfile,pstats

from trie import Trie


class ControlIt:
    def __init__(self):
        self.the_trie = Trie()

    def file_grab(self):
        log = open("content/words1.txt", 'r')
        loglist = log.readlines()
        log.close()
        cl = []
        sendc = []
        pattern = '^\w+-\s'
        for index, line in enumerate(loglist, 0):
            if re.search(pattern, line) is not None:
                test = re.search(pattern, line)
                firstFound = test.string.split(' ', 1)[0]
                secondFound = loglist[index + 1]
                if not secondFound.split(' ', 1)[0] == "ship":
                    sendc.append(secondFound.split(' ', 1)[0].lower())
                cl.append(firstFound.__add__(secondFound.split(' ', 1)[0]).lower())
        try:
            with open("content/words1.txt", encoding='UTF-8') as f:
                lines = f.read().translate({ord(i): None for i in ';:*.,[]|"�<>()!°&¶/'}).lower().split()
                f.close()
        except:
            with open("content/words1.txt", encoding='latin_1') as f:
                lines = f.read().translate({ord(i): None for i in ';:*.,[]|"�<>()!°&¶/'}).lower().split()
                f.close()
        for index, i in enumerate(lines):
            if i.count('-') >= 3 or i == re.search('\w+-\n', i):
                lines[index] = None
        [lines.append(i) for i in cl]
        for i in sendc:
            lines = list((x for x in lines if re.sub(i, "", str(x))))
        return lines

    def grab_file(self):
        start_list = self.file_grab()
        for i in start_list:
            self.the_trie.add(self.the_trie.trie, str(i))
        mytrie = self.the_trie.get_trie()
        self.the_trie.trie_pickle(mytrie)
        # self.ct = self.the_trie
        print(mytrie)

    def main(self):
        self.grab_file()
        self.the_trie.create_binary_tree()
        self.the_trie.create_avl_tree()

if __name__ == '__main__':
    ct = ControlIt()
    ct.main()
    cProfile.run('ct.file_grab()')

