from tkinter import *

root = Tk() # root를 통해 Tk()를 선언해준다.
root.title("GUI test Title") # 제목을 선언
root.geometry("440x350+200+200") # "가로 x 세로 + x좌표 + y좌표"

root.resizable(True, False) #True 허용, 참 False 비허용, 거짓

#-------------------------------------
#listbox 목록 보여주기
listbox01 = Listbox(root, selectmode="extended", height=0) # height=0 모두 보여주기, height=2 2개 보여주기

#listbox 목록에 값 추가하기
listbox01.insert(0, "0. 양천구")
listbox01.insert(1, "1. 신월동")
listbox01.insert(2, "2. 신정동")
listbox01.insert(3,"3. 목동")
listbox01.pack()


def delete_list():
    #리스트의 항목 하나씩 삭제
    #listbox01.delete(END) # 마지막 위치의 리스트 값 삭제, END 대신 원하는 index값 넣을수있음
    listbox01.delete(0) # 처음 값부터 삭제
def get_list():
    listbox01.get(0, 2)
    print("첫번째부터 세번째 값은 ",listbox01.get(0, 2))
def curselection_list():
    listbox01.curselection()
    print("현재 선택된 값의 index는 ",listbox01.curselection())
def size_list():
    listbox01.size()
    print("리스트의 크기는 ",listbox01.size())


button01 = Button(root, text="리스트 삭제 delete", command=delete_list) #값 삭제
button01.pack()

button02 = Button(root, text="리스트 가져오기 get", command=get_list) #값 가져오기
button02.pack()

button03 = Button(root, text="리스트 선택확인 curselection", command=curselection_list)
button03.pack()

button04 = Button(root, text="리스트 크기 size", command=size_list)
button04.pack()

root.mainloop() # 루트에 메인 루프 선언, 루프가 작동되면서 Tk()로 선언된 gui 화면이 동작시작
