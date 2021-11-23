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