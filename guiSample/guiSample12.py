from tkinter import *

root = Tk() # root를 통해 Tk()를 선언해준다.
root.title("GUI test Title") # 제목을 선언
root.geometry("440x350+200+200") # "가로 x 세로 + x좌표 + y좌표"

root.resizable(True, False) #True 허용, 참 False 비허용, 거짓

#-------------------------------------
#command 속성, 버튼 동작시키기
def change01():
    label01.config(text="글자가 바뀌었습니다.")

def change02():
    global photo1 #photo 전역변수 설정, 함수가 끝나도 그림 변경이 유지되기 위해 설정

    photo1 = PhotoImage(file="../include/picture01.png")
    label02.config(image=photo1)

button01 = Button(root, text="글자변경", command=change01) # 버튼01
button01.pack() # 버튼01 출력
button02 = Button(root, text="그림변경", command=change02) # 버튼02
button02.pack() # 버튼01 출력

#레이블(Label) 사용하기
label01 = Label(root, text="레이블01 글상자") # 레이블01 선언
label01.pack() # 레이블01 출력

#레이블에 이미지 넣기
photo02 = PhotoImage(file="../include/picture02.png")
label02 = Label(root, image = photo02) # 레이블01 선언
label02.pack() # 레이블01 출력



root.mainloop() # 루트에 메인 루프 선언, 루프가 작동되면서 Tk()로 선언된 gui 화면이 동작시작
