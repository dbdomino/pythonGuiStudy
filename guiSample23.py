from tkinter import *

root = Tk() # root를 통해 Tk()를 선언해준다.
root.title("GUI test Title") # 제목을 선언
root.geometry("440x350+200+200") # "가로 x 세로 + x좌표 + y좌표"

root.resizable(True, False) #True 허용, 참 False 비허용, 거짓

#-------------------------------------
# 체크박스, 여러 선택지를 원하는만큼 선택가능
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


# 라디오 버튼, 값 텍스트로 저장
radio_var02 = StringVar() # 여기에 라디오버튼 값 저장
button_burger06 = Radiobutton(root, text="데리버거", value="데리버거", variable=radio_var02)
button_burger06.select()
button_burger07 = Radiobutton(root, text="치킨버거", value="치킨버거", variable=radio_var02)
button_burger08 = Radiobutton(root, text="새우버거", value="새우버거", variable=radio_var02)
button_burger09 = Radiobutton(root, text="불고기버거", value="불고기버거", variable=radio_var02)
button_burger10 = Radiobutton(root, text="라이스버거", value="라이스버거", variable=radio_var02)
button_burger06.pack()
button_burger07.pack()
button_burger08.pack()
button_burger09.pack()
button_burger10.pack()

def print_radio02():
    #print("라디오 버튼 선택 = ",radio_var) # PY_VAR0
    print("주문한 값 = ", radio_var02.get()) # 0 비선택, 1 선택
button03 = Button(root, text="한글 주문하기", command=print_radio02) #값 삭제
button03.pack()




root.mainloop() # 루트에 메인 루프 선언, 루프가 작동되면서 Tk()로 선언된 gui 화면이 동작시작
