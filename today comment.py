# ウィンドウ立ち上げ
# -----------------------------------------------------------

# Tkinterモジュールのimport
import tkinter
import csv
import datetime

# ウィンドウ（フレーム）作成
root = tkinter.Tk()

# ウィンドウの名前を設定
root.title("今日の進捗")

# ウィンドウの大きさを設定
root.geometry("400x400")

# コンソールに"Button is clicked"を出力する関数
def clicked():
    now = datetime.datetime.now()
    filename = now.strftime("%Y%m%d") + ".txt"
    comment = txt.get()
    with open(filename, "w") as f:
        print(comment, file=f)
    print("今日の一言",comment)
    root.destroy()

# ボタンの作成
button = tkinter.Button(root, text="保存！" , command=clicked)

# ボタンの表示
button.grid()

# ボタンの位置
button.place(x=160, y=200)

# ラベルの作成
label = tkinter.Label(root, text="今日の一言？")

# ラベルの表示
label.grid()

#ラベルの位置
label.place(x=120, y=100)

# テキストボックスの作成
txt = tkinter.Entry(width=30)

# テキストボックスの位置
txt.place(x=100, y=150)

# イベントループ (TK上のイベントを捕捉し，適切な処理を呼び出す)
root.mainloop()
