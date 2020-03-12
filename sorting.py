import csv

f = open('../words/words.csv','r', encoding='utf8')
rdr = csv.reader(f)

after = [[[''for q in range(2)]for w in range(30) ] for i in range(80)]


i = 0
j = 0
k = 4
after[0][0][0]= 'yee'

for line in rdr:
    if (line[0] == 'Vocabulary Test') or (line[0] =='Book') or (line[0] =='This is vocabulary 중급') or (line[0] =='No.'):
        k -= 1
    elif k == 1:
        after[i][j][0]= line[1]
        after[i][j][1]= line[2]
        j += 1
        after[i][j][0]= line[4]
        after[i][j][1]= line[5]
        j += 1
    if j > 28:
        k = 13
        j = 0
        i += 1

x = input("원하는 날짜의 단어 : ")

for line in range(30):
    print(after[int(x)-1][line])

f.close