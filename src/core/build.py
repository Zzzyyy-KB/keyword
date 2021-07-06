# 基于annoy二叉树的近邻搜索版本 构建

import json
import numpy as np
from collections import OrderedDict
from annoy import AnnoyIndex


def build(word_path='../../res/res/word1.txt', vec_path='../../res/res/vector1.npy', build_trees=1, annoy_deep=200):
    keywords = getKeyword(word_path)
    vectors = getVectors(vec_path)
    word_index = OrderedDict()
    for count, word in enumerate(keywords):
        word_index[word] = count
    with open('../../res/tc_word_index.json', 'w') as fp:
        json.dump(word_index, fp)
    del keywords
    tc_index = AnnoyIndex(annoy_deep)
    for count, vector in enumerate(vectors):
        tc_index.add_item(count, vector)
    tc_index.build(build_trees)
    tc_index.save('../../res/tc_index_build.index')


def getKeyword(path):
    with open(path, 'r', encoding='utf8') as f:
        keywords = f.readlines()
        return keywords


def getVectors(path):
    vectors = np.load(path)
    return vectors

build()