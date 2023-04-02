"""
Goal: 가장 많이 팔린 제품 리뷰 중 유용한 투표를 많이 받은 상위 5개를 출력(구매한 사람들)
"""

from circulardoublylinkedlist import CircularDoublyLinkedList, CircularDoublyLinkedListFilter, CATEGORY_NUM, NUM_OF_CATEGORY
from itertools import groupby
from operator import itemgetter
from pprint import pprint

def load_data(dataset: CircularDoublyLinkedList):
    t = {}
    with open('test.tsv', 'r', encoding='utf-8') as file:
        next(file)
        for line in file:
            fields = line.split('\t')
            if fields[CATEGORY_NUM["product_title"]] not in t:
                t[fields[CATEGORY_NUM["product_title"]]] = 1
            else:
                t[fields[CATEGORY_NUM["product_title"]]] += 1
            for i in range(NUM_OF_CATEGORY):
                dataset.append(fields[i], i)

def get_data(dataset: CircularDoublyLinkedList, filter_str, group_by, top):
    res_dict = {}
    filtered = dataset.filter(CircularDoublyLinkedListFilter(filter_str))
    print(filtered)
    filtered = sorted(filtered, key=(itemgetter(CATEGORY_NUM[group_by])))
    group_data = groupby(filtered, key=itemgetter(CATEGORY_NUM[group_by]))
    for key, group_data in group_data:
        res_dict[key] = list(group_data)
    group_sorted = sorted(res_dict.items(), key=lambda x: len(x[1]), reverse=True)
    for ind in range(top):
        group_name = group_sorted[ind][0]
        product_group = group_sorted[ind][1]
        product_group.sort(key=lambda x: int(x[CATEGORY_NUM['helpful_votes']]), reverse=True)
        print(f"-------- {group_by} : {group_name} --------")
        for j in range(top):
            review_title = product_group[j][CATEGORY_NUM['review_headline']]
            review_body = product_group[j][CATEGORY_NUM['review_body']]
            helpful = product_group[j][CATEGORY_NUM['helpful_votes']]
            print(f"<{j+1}th Review : {review_title}>\n* {review_body}\n- helpful_votes : {helpful}")

if __name__ == '__main__':
    dataset = CircularDoublyLinkedList()
    load_data(dataset)
    #get_data(dataset, "verified_purchase == Y", "product_title", 5)
    get_data(dataset, "helpful_votes > 10", "product_id", 5)