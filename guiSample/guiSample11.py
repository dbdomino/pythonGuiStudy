from tkinter import *

root = Tk() # root를 통해 Tk()를 선언해준다.
root.title("GUI test Title") # 제목을 선언
root.geometry("440x350+200+200") # "가로 x 세로 + x좌표 + y좌표"

root.resizable(True, False) #True 허용, 참 False 비허용, 거짓

#-------------------------------------
#버튼 만들기
button01 = Button(root, text="버튼01") # 버튼01 구성
button01.pack() # 버튼01 출력

#command 속성, 버튼 동작시키기
def func01():  # 함수
    print("버튼을 클릭했습니다.")

button06 = Button(root, text="버튼06", command=func01) # 버튼06
button06.pack() # 버튼06 출력

#레이블(Label) 사용하기
label01 = Label(root, text="라벨01 글상자") # 레이블01 선언
label01.pack() # 레이블01 출력

#레이블에 이미지 넣기
photo02 = PhotoImage(file="../include/picture02.png")
label02 = Label(root, image = photo02) # 레이블01 선언
label02.pack() # 레이블01 출력



root.mainloop() # 루트에 메인 루프 선언, 루프가 작동되면서 Tk()로 선언된 gui 화면이 동작시작
