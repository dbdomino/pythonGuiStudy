from tkinter import *
import tkinter.ttk as ttk # 콤보 박스(Combobox)는 tkinter 와 다른 묘듈에 있어 추가로 선언 필요


root = Tk() # root를 통해 Tk()를 선언해준다.
root.title("GUI test Title") # 제목을 선언
root.geometry("440x350+200+200") # "가로 x 세로 + x좌표 + y좌표"

root.resizable(True, False) #True 허용, 참 False 비허용, 거짓

#-------------------------------------
# 변수(리스트) 선언
# values = [i for i in range(1, 32)] # 1부터 31까지의 숫자 value에 저장
valuesDay = [str(i) +"일" for i in range(1,32)] # 날짜 일 선언

# 콤보 박스(Combobox), 라디오 버튼과 비슷하며, 여러 선택지 중 하나 선택
# 기본적으로 선택된 값 수정 가능, readonly 옵션 지정해야 수정안됨
combobox01=ttk.Combobox(root, height=7, width=12, state="readonly", values=valuesDay)
combobox01.set("날짜 선택") # 기본값, value 리스트에 없는 값도 하드코딩 가능
combobox01.current(0) # 기본값, index = 0 인 첫번째 값 선택
combobox01.pack()


def print_combo01():
    #print("콤보박스 선택 = ",radio_var) # PY_VAR0
    print("날짜 보기 = ", combobox01.get()) # 0 비선택, 1 선택
button01 = Button(root, text="선택한 날짜 확인 = ", command=print_combo01) #값 삭제
button01.pack()




root.mainloop() # 루트에 메인 루프 선언, 루프가 작동되면서 Tk()로 선언된 gui 화면이 동작시작
