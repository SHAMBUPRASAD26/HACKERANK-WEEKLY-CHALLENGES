def minion_game(string):
    # your code goes here
    stuart, kevin = 0, 0
    lens = len(string)
    for i in range(lens):
        if string[i] in 'AEIOU':
            kevin = kevin + lens - i
        else:
            stuart = stuart + lens - i
    if kevin > stuart:
        print('Kevin ' + str(kevin))
    elif kevin < stuart:
        print('Stuart ' + str(stuart))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)