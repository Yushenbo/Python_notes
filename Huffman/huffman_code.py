#-*- coding:utf-8 -*-
#########################################################################
# File Name: huffman_code.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/python

import sys
import six

class HuffNode(object):
    """
    define a HufffNode Abstract class within 2 method
    1, get the node wieght
    2, get the node weather is the function of leaf node
    """
    
    def get_wieght(self):
        raise NotImplementedError(
                "The Abstract Node Class doesn't define 'get_wieght'")


    def isleaf(self):
        raise NotImplementedError(
                "The Abstract Node Class doesn't define 'isleaf'")

class LeafNode(HuffNode):
    """
    Leaf node class
    """

    def __init__(self, value=0, freq=0):
        """
        Initialize the parameters of leaf node : value & frequence of apparence
        """
        super(LeafNode, self).__init__()
        #Node value
        self.value = value
        self.wieght = freq

    def isleaf(self):
        """
        Method based on calss, Leafnode if return True
        """
        return True

    def get_wieght(self):
        """
        Method based on calss, return the object's wieght
        """
        return self.value

    def get_value(self):
        """
        Method to get leafnode value of character
        """
        return self.value

class IntlNode(HuffNode):
    """
    Middle Node class
    """
    def __init__(self, left_child=None, right_child=None):
        """
        Initilize the parameters of Middle Node: left_child, right_child, wieght
        """
        super(IntlNode, self).__init__()

        #Value of Node
        self.wieght = left_child.get_wieght() + right_child.get_wieght()
        #The left & right child node of this node
        self.left_child = left_child
        self.right_child = right_child

        def isleaf(self):
            """
            Method of base class, is the Middle Node if return False
            """
            return False

        def get_wieght(self):
            """
            Method of base class, return the object's wieght
            """
            return self.wieght

        def get_left(self):
            """
            Get the left child Node
            """
            return self.left_child

        def get_right(self):
            """
            Get the right child Node
            """
            return self.right_child

class HuffTree(object):
    """
    huffTreee
    """
    def __init__(self, flag, value =0, freq =0, left_tree=None,
            right_tree=None):
        super(HuffTree, self).__init__()

        if flag == 0:
            self.root = LeafNode(value, freq)
        else:
            self.root = IntlNode(left_tree.get_root(), right_tree.get_root())

    def get_root(self):
        """
        Get huffman tree root Node
        """
        return self.root

    def get_wieght(self):
        """
        Get huffman tree root Node wieght
        """
        return self.root.get_wieght()

    def traverse_huffman_tree(self, root, code, char_freq):
        """
        Traverse the Huffman Tree by Recursion Algorithm, so we can get the
        huffman code of each character, & store them in dictionary char_freq.
        """
        if root.isleaf():
            char_freq[root.get_value()] == code
            print ("it = %d%c and frequence = %d code = %s") %(root.get_value(),
                    chr(root.get_value()), root.get_wieght(), code)
            return None
        else:
            self.traverse_huffman_tree(root.get_left(), code+'0', char_freq)
            self.traverse_huffman_tree(root.get_right(), code+'1', char_freq)


##########################
#Method build huffman tree
###########################
def buildHuffmanTree(list_hufftrees):
    """
    Construct huffman tree
    """
    while len(list_hufftrees) > 1:
        # 1, Sort flow the wieght ascending sequene of huffman tree
        list_hufftrees.sort(key=lambda x: x.get_wieght())

        # 2, Find the 2 smallest wieght huffman tree
        temp1 = list_hufftrees[0]
        temp2 = list_hufftrees[1]
        list_hufftrees = list_hufftrees[2:]

        # 3, Make a new huffman tree
        newed_hufftree = HuffTree(1, 0, 0, temp1, temp2)

        # 4, Put the new huffman tree into array
        list_hufftrees.append(newed_hufftree)

    return list_hufftrees[0]


if __name__ == '__main__':
    #Get user input
    if len(sys.argv) != 2:
        print "please input inputfilename"
        exit(0)
    else:
        INPUTFILE = sys.argv[1]

    #1. Open the file with binary format
    f = open(INPUTFILE, 'rb')
    filedata = f.read()
    # Get the how many bytes of file
    filesize = f.tell()


    #2. Stats the frequence of value byte which in [0 - 255]
    #store the result in char_freq dictionary
    char_freq = {}
    for x in range(filesize):
        tem = six.byte2int(filedata[x])
        if tem in char_freq.keys():
            char_freq[tem] = char_freq[tem] + 1
        else:
            char_freq[tem] = 1

    # Print the statistics result
    for tem in char_freq.keys():
        print tem, ' : ', char_freq[tem]


    #3. Ready to construct the original huffman code tree array that use for
    #huffman tree
    list_hufftrees = []
    for x in char_freq.keys():
        # Define a huffman tree that have only 1 leaf node by using HuffTree
        # construct Method
        tem = HuffTree(0, x, char_freq[x], None, None)
        # Add this HuffTree to list_hufftrees array
        list_hufftrees.append(tem)

    #4. Construct huffman code tree & get the encode value of each character
    tem = buildHuffmanTree(list_hufftrees)
    tem.traverse_huffman_tree(tem.get_root(), '', char_freq)
