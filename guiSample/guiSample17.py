from tkinter import *

root = Tk() # root를 통해 Tk()를 선언해준다.
root.title("GUI test Title") # 제목을 선언
root.geometry("440x350+200+200") # "가로 x 세로 + x좌표 + y좌표"

root.resizable(True, False) #True 허용, 참 False 비허용, 거짓

#-------------------------------------
#listbox 목록 보여주기
listbox01 = Listbox(root, selectmode="extended", height=0) # height=0 모두 보여주기, height=2 2개 보여주기

#listbox 목록에 값 추가하기
listbox01.insert(0, "양천구")
listbox01.insert(1, "신월동")
listbox01.insert(2, "신정동")
listbox01.insert(3,"목동")
listbox01.pack()

#listbox 목록 보여주기
listbox02 = Listbox(root, selectmode="single", height=0) # selectmode="single" 리스트에서 하나만 선택 가능

#listbox 목록에 값 추가하기
listbox02.insert(END, "양천구") # index에 END를 넣으면 마지막 위치에 추가됨
listbox02.insert(END, "신월동")
listbox02.insert(END, "신정동")
listbox02.insert(END,"목동")
listbox02.pack()



root.mainloop() # 루트에 메인 루프 선언, 루프가 작동되면서 Tk()로 선언된 gui 화면이 동작시작
