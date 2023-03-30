from listlib import *
def load_data(dataset: CircularDoublyLinkedList):
    with open('amazon_reviews_us_Shoes_v1_00_40k.tsv', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.split('\t')

"""def get_data(dataset: CircularDoublyLinkedList):
    filtered = dataset.filter(CircularDoublyLinkedListFilter())"""

if __name__ == '__main__':
    dataset = CircularDoublyLinkedList()
    load_data(dataset)
    #get_data(dataset)