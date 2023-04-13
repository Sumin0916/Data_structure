def is_included(word, sentence):
    sen_lst = list(sentence.split(' '))
    if word in sen_lst:
        return 'Yes'
    return 'No'

def do_sum():
    res = 0
    for _ in range(5):
        res += int(input("Type the number: "))
    print(res)

if __name__ == "__main__":
    print(is_included("love", "I love you"))
    print(is_included("me", "I love you"))
    print(is_included("you", "I love you"))
    do_sum()

    
    