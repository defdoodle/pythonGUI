from tkinter import * 
import tkinter.messagebox as msgbox

root = Tk() 
root.title("Nado GUI") 
root.geometry("640x480") 

def info() :
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn() :
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다")

def error() :
    msgbox.showerror("애러", "결제 오류 발생")

def okcancel() :
    msgbox.askokcancel("확인 / 취소", "유야동반석 결제하시겠습니까")

def retrycancel() :
    response = msgbox.askretrycancel("확인 / 취소", "다시 결제하시겠습니까")

    if response == 1 :
        print("retry")
    elif response == 0 :
        print("cancel")

def yesno() :
    msgbox.askyesno("yes / no", "역방향 괜찮아요?")

def yesnocancel() :
    response = msgbox.askyesnocancel(title=None, message="예매내역이 저장되지 않았습니다\n 계속 하시겠습니까?")
    print("answer :", response)
    if response == 1 :
        print("yes")
    elif response == 0 :
        print("No")
    else :
        print("cancel")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="애러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()