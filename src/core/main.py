# 基于annoy二叉树的近邻搜索版本

import json
import numpy as np
from collections import OrderedDict
from annoy import AnnoyIndex

def main():
    with open('../../res/tc_word_index.json', 'r') as fp:
        word_index = json.load(fp)
    tc_index = AnnoyIndex(200)
    tc_index.load('../../res/tc_index_build.index')
    reverse_word_index = dict([(index,word) for (word,index) in word_index.items()])

    tests = [reverse_word_index[5], reverse_word_index[100], reverse_word_index[1000]]
    for word in tests:
        print('keyword: ', word)
        for item in tc_index.get_nns_by_item(word_index[word], 10):
            print(reverse_word_index[item])
        print('ok ')


main()