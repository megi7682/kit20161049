print("게임 시작 ")
my = 1

def gogo(my):
    if my == 1:
        print("간다")
    else :
        print("안간다")

#돈을 넣으면 2배가 뻥튀기
def ck_idpw(ret):
    #if id == 'asd' and pw == '123':
    if ret != None :
        return '로그인 성공'
    else:
        return '로그인 실패'
 
