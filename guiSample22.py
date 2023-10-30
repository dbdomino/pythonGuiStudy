from tkinter import *

root = Tk() # root를 통해 Tk()를 선언해준다.
root.title("GUI test Title") # 제목을 선언
root.geometry("440x350+200+200") # "가로 x 세로 + x좌표 + y좌표"

root.resizable(True, False) #True 허용, 참 False 비허용, 거짓

#-------------------------------------
# checkbox = Checkbutton(root, text="    ", variable = 변수     )
# variable을 넣어서 체크 박스 선택 유무 값을 저장해 줘야 함.
checkbox01value = IntVar()
checkbox02value = IntVar()
checkbox01 = Checkbutton(root, text="오늘 하루 그만 보기", variable=checkbox01value)
checkbox01.pack()

checkbox02 = Checkbutton(root, text="1주일 동안 그만 보기")
checkbox02.deselect()
#checkbox02.select()
checkbox02.pack()

def value_checkbox():
    #print("체스박스선택 = ",checkbox01value) # PY_VAR0
    print("오늘 하루 그만 보기 = ", checkbox01value.get()) # 0 비선택, 1 선택

button01 = Button(root, text="checkbox01value", command=value_checkbox) #값 삭제
button01.pack()

root.mainloop() # 루트에 메인 루프 선언, 루프가 작동되면서 Tk()로 선언된 gui 화면이 동작시작
