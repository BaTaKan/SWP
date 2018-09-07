import pickle

dbfilename = 'assignment3_20181672.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))

        if inputstr == "": continue
        parse = inputstr.split(" ")

        if parse[0] == 'add':
            try :
                parse[1] == '' , parse[2] == '' , parse[3] == ''
            except IndexError:
                print('add뒤에 필요한 조건을 다 입력하지 않았습니다')
            else:
                record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                scdb += [record]


        elif parse[0] == 'del':
            try :
                parse [1] == ''
            except IndexError:
                print('del 뒤에 필요한 조건을 다 입력하지 않았습니다')
            else:
                scdb2 = []
                for p in scdb:
                    if p['Name'] != parse[1]:
                        scdb2.append(p)
                scdb=scdb2
                
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'quit':
            break

        elif parse[0] == 'find':
            try :
                parse [1] == ''
            except IndexError:
                print('find 뒤에 필요한 조건을 다 입력하지 않았습니다')
            else:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        print(p)

        elif parse[0] == 'inc' :
            try :
                parse [1] == '' , parse [2] == ''
            except IndexError:
                print('inc 뒤에 필요한 조건을 다 입력하지 않았습니다')
            else :
                for p in scdb:
                    if p['Name'] == parse[1]:
                        Skey = int(p['Score']) + int(parse[2])
                        p['Score'] = str(Skey)

        else:
            print("Invalid command: " + parse[0])

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
