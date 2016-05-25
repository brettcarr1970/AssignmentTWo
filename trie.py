from pythonds.trees import BinarySearchTree, AVLTree
import pickle, re


class Trie:
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
        self.bint = self.trie
        self.binaryList = ""

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
            temp_trie =  temp_trie[letter]

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
    def list(self, newList):
        my_list = []
        if type(newList) == AVLTree:
            pass
        for k, v in newList.items():
            if k != '_':
                for el in self.list(v):
                    my_list.append(k + el)
            else:
                my_list.append('')
        return my_list

    def get_trie(self):
        return self.trie

    def get_bint(self):
        return self.trie

    def trie_pickle(self, lines):
        pickle.dump(self, open("pickletree", "wb"))
        self.trie = pickle.load(open("pickletree", "rb"))

    def create_binary_tree(self):
        bst = BinarySearchTree()
        self.binaryList = self.list(self.trie.trie)
        for word in self.binaryList:
            bst.put(word, word)
        # print("Binary Tree", {x for x in bst if not x.__len__() < 1})

    def create_avl_tree(self):
        avlt = AVLTree()
        for newWord in self.binaryList:
            avlt.put(newWord,newWord)

        # print("AVLTree",{x for x in avlt if not x.__len__() < 1})