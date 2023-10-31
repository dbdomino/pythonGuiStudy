from tkinter import *
import tkinter.ttk as ttk # 콤보 박스(Combobox)는 tkinter 와 다른 묘듈에 있어 추가로 선언 필요
import time # time 함수 쓰기위해 추가

root = Tk() # root를 통해 Tk()를 선언해준다.
root.title("GUI test Title") # 제목을 선언
root.geometry("440x350+200+200") # "가로 x 세로 + x좌표 + y좌표"

root.resizable(True, False) #True 허용, 참 False 비허용, 거짓

#-------------------------------------
# 변수(리스트) 선언
# values = [i for i in range(1, 32)] # 1부터 31까지의 숫자 value에 저장
valuesDay = [str(i) +"일" for i in range(1,32)] # 날짜 일 선언

# 프로그레스 바(Progressbar), 진행도나 상태를 나타낼 때 사용
# mode 옵션으로 구분됨 (indeterminate 좌우로 계속움직임, determinate 좌측부터 우측으로 채워짐)
#progressbar01 = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar01 = ttk.Progressbar(root, maximum=100, mode="determinate")
# start 명령 안주면 가만히 멈춰있음. ms단위로 입력 10 = 10ms
progressbar01.start(10)
# stop 명령 주면 바로 멈춤
progressbar01.stop()
progressbar01.pack()

# 프로그래스바 0%부터 100% 까지 가면 멈추게 하기
progress_var02 = DoubleVar() # 소수점이 있는 실수 사용하기 위해 Double 선언
progressbar02 = ttk.Progressbar(root, maximum=100, length=150, variable=progress_var02)
progressbar02.pack()
def button_command02():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기, 진행속도 조절위해 사용

        progress_var02.set(i)  # progressbar의 값을 설정,
        progressbar02.update() # 설정된 값대로 update

button02 = Button(root, text="시작", command=button_command02)
button02.pack()








root.mainloop() # 루트에 메인 루프 선언, 루프가 작동되면서 Tk()로 선언된 gui 화면이 동작시작
