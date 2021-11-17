# 簡易プログラム 

from kivy.app import App

# 日本語を適用
# import japanize_kivy

# from kivy.uix ~ : ウジェット(ボタンとかラベルなど)をプログラム上で使えるようにする
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
# ------------------------

# Windowの背景色を変更 (黒 → 白) : デフォルトは黒です。
Window.clearcolor = (1, 1, 1, 1)

# 画面を作る
class Sample(App):
    def build(self):
        # - 画面の設定 -------------
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}
        # ------------------------
        
# 以下、ウィジェット(ラベルとかボタンなどの部品)の追加

# 画像を表示するためのウィジェット : Image
# kivy_sampleディレクトリ内に好きな画像を配置し、その画像のファイル名を書いてあげる
        self.window.add_widget(Image(source="licensed-image.jpg"))

# ラベルウィジェット(テキスト) : Label
        self.Test = Label(
    # テキストの設定
         text="kivy_practice",
    # フォントのサイズを40で指定
         font_size = 40,
    # 文字色を青に指定
         color="blue"
)
# ラベルを画面上に追加
        self.window.add_widget(self.Test)

# ボタンウィジェット : Button
        self.button = Button(
    # ボタン上に表示させるテキストを設定
        text="CLICK!!",
    # 背景色を青に設定
        background_color="blue",
    # サイズの設定
        size_hint = (1,0.5),
    # 文字色を白に設定
        color = "white",
    # フォントサイズを30に設定
        font_size = 30,
    # ボタンの背景は、灰色がデフォルトのため、""にする事で背景色を思い通りに反映させる事ができる
        background_normal = ""
)

# ボタンをクリックした際の処理 : on_press
        self.button.bind(on_press=self.callback)
# ボタンを画面上に追加
        self.window.add_widget(self.button)

# レイアウトを返す
        return self.window

# 関数を準備 : ボタンがクリックされた際に呼び出される
    def callback(self, instance):
    # ラベルのテキストを更新する
        self.Test.text = "kivy : basic_learning"
    
# アプリを起動する
if __name__ == "__main__":
    Sample().run()
