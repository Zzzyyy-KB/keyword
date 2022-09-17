import json
import numpy as np
from collections import OrderedDict
from annoy import AnnoyIndex
import os


def build(word_path='D:\Pyproject\keyword\word1.txt', vec_path='D:/Pyproject/keyword/vector1.npy', build_trees=10, annoy_deep=200):
    '''
    keywords = getKeyword(word_path)
    keywords += getKeyword('D:\Pyproject\keyword\word2.txt')
    keywords+=getKeyword('D:\Pyproject\keyword\word3.txt')
    #keywords+=getKeyword('D:\Pyproject\keyword\word4.txt')
    total= len(keywords)
    print(total)
    word_index = OrderedDict()
    for count, word in enumerate(keywords):
        word_index[word] = count
        temp=word.strip()
        print('\r第%-7d个词: %-20s' % (count, temp), end='')
    print('完成%-7d词' % (count), end='')
    with open('./res/three_fourth_tc_word_index.json', 'w') as fp:
        json.dump(word_index, fp)
    del keywords
    '''
    vectors = getVectors(vec_path)
    vectors = vectors + getVectors('D:/Pyproject/keyword/vector2.npy')
    vectors = vectors + getVectors('D:/Pyproject/keyword/vector3.npy')
    print("Vectors start processing!")
    #vectors = vectors + getVectors('D:/Pyproject/keyword/vector4.npy')

    tc_index = AnnoyIndex(annoy_deep)
    for count, vector in enumerate(vectors):
        tc_index.add_item(count, vector)
        print('\r第%-7d个向量' % (count), end='')
    print('\r%-7d' % (count), end='')
    tc_index.build(build_trees)
    print('Vectors are saving!')
    tc_index.save('./res/three_fourth_tc_index_build.index')

def getKeyword(path):
    with open(path, 'r', encoding='utf8') as f:
        keywords = f.readlines()
        return keywords


def getVectors(path):
    vectors = np.load(path)
    return list(vectors)

#build()