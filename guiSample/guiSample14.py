from tkinter import *

root = Tk() # root를 통해 Tk()를 선언해준다.
root.title("GUI test Title") # 제목을 선언
root.geometry("440x350+200+200") # "가로 x 세로 + x좌표 + y좌표"

root.resizable(True, False) #True 허용, 참 False 비허용, 거짓

#-------------------------------------
#버튼 만들기
button01 = Button(root, text="버튼01") # 버튼01 구성
button01.pack() # 버튼01 출력

#레이블(Label) 사용하기
label01 = Label(root, text="레이블01 글상자") # 레이블01 선언
label01.pack() # 레이블01 출력

#텍스트상자 사용하기(글자입력, 수정 가능)
text01 = Text(root, width=30, height=7) # 텍스트상자 너비, 높이 조절가능
text01.pack()

#엔트리(Entry) 텍스트 상자와 비슷하나 한줄만 입력가능
ent01 = Entry(root, width=20) # id나 비밀번호 처럼 한줄만 입력시 사용
ent01.insert(0,"예시 미리입력") # 샘플
ent01.pack()


root.mainloop() # 루트에 메인 루프 선언, 루프가 작동되면서 Tk()로 선언된 gui 화면이 동작시작
