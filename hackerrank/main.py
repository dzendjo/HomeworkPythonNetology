# from kivy.app import App
# from kivy.base import runTouchApp
# from kivy.lang import Builder
#
# runTouchApp(Builder.load_string("""
#
# BoxLayout:
#     Button:
#         text: 'B1'
#
#
#
# """))

s = 'TestCaseTestCase'
fs = 'CaseT'

count = set()
for i in range(len(s)):
    print(s.find(fs, i, len(s)))
    count.add(s.find(fs, i, len(s)))
count.remove((-1))
print(count)
print(len(count))
