#dat파일
##assignment3_20181672.dat파일을 읽기 위해 pickle.load를 이용             


#find 함수
##find 기능을 넣기위해 scdb에 포함된 이름이  입력한 이름인 parse[1]와 같다면 이에 해당되는 이름을 프린트함
                for p in scdb:
                    if p['Name'] == parse[1]:
                        print(p)

#del 함수
##del 기능에서 1번 입력할 때 1명만 삭제되는 것을 개선하기 위해서 원래 소스코드에 존재하던 break를 삭제하고 새로운 리스트를 만들어 입력한 이름과 같지않은 이름들을 새로운 리스트에 넣어 따로 저장한 후 새로운 리스트를 원래 리스트로 옮겨 출력함

                scdb2 = []
                for p in scdb:
                    if p['Name'] != parse[1]:
                        scdb2.append(p)
                scdb=scdb2

#inc 함수
##inc 기능을 넣기위해 점수를 올리고자 하는 이름인 parse[1]과 scdb에 포함된 이름이 같다면 그 이름에 해당되는 점수에 parse[2]만큼의 점수를 더해줌(현재 scdb에 들어가있는 Score는 str형태이고 parse[2]도 str형태이므로 int로 변환해준후 다시 str로 바꿔줌)
                for p in scdb:
                    if p['Name'] == parse[1]:
                        Skey = int(p['Score']) + int(parse[2])
                        p['Score'] = str(Skey)

#add함수
##add함수에서 이름이나 나이나 점수를 넣지않았을 때 작동하는 에러를 예외처리해주기 위해서 밑과 같이 바
            try :
                parse[1] == '' , parse[2] == '' , parse[3] == ''
            except IndexError:
                print('add뒤에 필요한 조건을 다 입력하지 않았습니다')
            else:
                record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                scdb += [record]


#del함수
            try :
                parse [1] == ''
            except IndexError:
                print('del 뒤에 필요한 조건을 다 입력하지 않았습니다')
            else:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
#find함수

            try :
                parse [1] == ''
            except IndexError:
                print('find 뒤에 필요한 조건을 다 입력하지 않았습니다')
            else:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        print(p)

#inc함수
            try :
                parse [1] == '' , parse [2] == ''
            except IndexError:
                print('inc 뒤에 필요한 조건을 다 입력하지 않았습니다')
            else :
                for p in scdb:
                    if p['Name'] == parse[1]:
                        Skey = int(p['Score']) + int(parse[2])
                        p['Score'] = str(Skey)

