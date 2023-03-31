"""
Git Repo: https://github.com/eunjicious/ds_2023
Document: https://docs.google.com/document/d/1irCSyXrV5c-3ILwiZLjVdHW6ionR0e4kuo506ZYbaJA/edit
"""

"""
Goal: 제품별로 리뷰에서 가장 많이 나온 단어들중 상위 10개를 출력한다.
p1 : 파인드 함수를 가진 객체를 어떻게 활용해 필터를 할 것인가.
"""

from circulardoublylinkedlist import CircularDoublyLinkedList
import collections

CATEGORY_NUM = {
    "marketplace" : 0,
    "customer_id" : 1,
    "review_id"	: 2,
    "product_id" : 3,
    "product_parent" : 4,
    "product_title" : 5,
    "product_category" : 6,
    "star_rating" : 7,
    "helpful_votes" : 8,
    "total_votes" : 9,
    "vine" : 10,
    "verified_purchase" : 11,
    "review_headline" : 12,
    "review_body" : 13,
    "review_date" : 14
}

def load_data(dataset: CircularDoublyLinkedList):
    title_dict = dict()
    with open('amazon_reviews_us_Shoes_v1_00_40k.tsv', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.split('\t')
            if fields[CATEGORY_NUM["product_title"]] not in title_dict:
                title_dict[fields[CATEGORY_NUM["product_title"]]] = 1
            else:
                title_dict[fields[CATEGORY_NUM["product_title"]]] += 1
        
        print(sorted(title_dict.items(), key=lambda x:x[1],reverse=True)[:10])
# def get_data(dataset: CircularDoublyLinkedList):
#     filtered = dataset.filter(CircularDoublyLinkedListFilter()) 
# 저 클래스는 Find 함수를 가졌음. 특정 조건 노드를 찾아 리스트로 만들어 리턴함

if __name__ == '__main__':
    dataset = CircularDoublyLinkedList()
    load_data(dataset)
    #get_data(dataset)