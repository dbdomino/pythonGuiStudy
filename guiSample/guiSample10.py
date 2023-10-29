from tkinter import *

root = Tk() # root를 통해 Tk()를 선언해준다.
root.title("GUI test Title") # 제목을 선언
root.geometry("440x350+200+200") # "가로 x 세로 + x좌표 + y좌표"

root.resizable(True, False) #True 허용, 참 False 비허용, 거짓

#-------------------------------------
#버튼 만들기
button01 = Button(root, text="버튼01") # 버튼01 구성
button01.pack() # 버튼01 출력

#너비(width) 와 높이(height): 버튼 텍스트 내의 상하좌우 넓이 조절
button02 = Button(root, width=8, height=5, text="버튼02") # 버튼02 구성
button02.pack() # 버튼02 출력

#padx, pady: 버튼 텍스트 내의 상하좌우 공백(여백) 조절
button03 = Button(root, width=8, height=5, padx=6, pady=10, text="버튼03") # 버튼03 구성
button03.pack() # 버튼03 출력

#fg="green"(글자색깔), bg="yellow"(배경색깔)  red, orange, yellow, green, blue, violet, black, white, gray
button04 = Button(root, width=6, fg="orange", bg="blue", height=3, text="버튼04") # 버튼04 구성
button04.pack() # 버튼04 출력

#이미지를 이용해 버튼 만들기
photo01 = PhotoImage(file="../include/picture01.png") #그림 선언
button05 = Button(root, image=photo01) # 버튼05 photo01 이미지 넣기
button05.pack() # 버튼05 출력

root.mainloop() # 루트에 메인 루프 선언, 루프가 작동되면서 Tk()로 선언된 gui 화면이 동작시작
