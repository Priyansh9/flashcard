import random
mydict = {
' BEST PHONE' : ['ONE PLUS', 'VIVO', 'MI', 0]
}
keyword_list = list(mydict.keys())
print('Pick the right color:')
for keyword in keyword_list:
    sf = '''\
{}
A) {}
B) {}
C) {}
'''
    print(sf.format(keyword, mydict[keyword][0],
                    mydict[keyword][1],mydict[keyword][2]))
    letter = input("Enter letter of your choice (A B C): ").upper()
    if letter == 'ABC'[mydict[keyword][3]]:
        print('correct')
    else:
        print('wrong')
