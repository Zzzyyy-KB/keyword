import json
import numpy as np
from collections import OrderedDict
from annoy import AnnoyIndex
from build import build,getKeyword,getVectors

def main():
    with open('./res/three_fourth_tc_word_index.json', 'r') as fp:
        word_index = json.load(fp)
    tc_index = AnnoyIndex(200)
    tc_index.load('./res/three_fourth_tc_index_build.index')
    reverse_word_index = dict([(index,word) for (word,index) in word_index.items()])

    keyword = input("Keyword（输入end结束）:")
    while(True):
        if(keyword=='end'):
            break
        else:
            index=word_index.get(keyword+'\n')
            if(index):
                result= tc_index.get_nns_by_item(index,5,include_distances=True)
                sim_keywords = [(str(reverse_word_index[idx]).strip(), distance) for idx, distance in zip(result[0], result[1]) if
                            distance < 0.9]
                
                print(sim_keywords)
            else:
                print('关键词不在词典中！')
        keyword = input("Keyword（输入end结束）:")


#build()
main()
