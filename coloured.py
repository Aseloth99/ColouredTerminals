from term_painter import *
from cmd_painter import *
import os

#1. path (linux ,windows, vscode)
painter("red and underlined text on a gray background", "red", styles=['underline'], backgroundColor="lgrey")
painter("green, bold and underlined text", "green", styles=['underline','bold'])
painter("invisible text", styles=['invisible'])
painter("bold text", styles=['bold'])

#2. path (windows and vscode)
cmd_painter("Hello World!") 
#              message     foreground background
cmd_painter("Hello World!", "Magenta", "Yellow") 
cmd_painter("Hello World!","Blue") 
cmd_painter("Hello World!","White","Green") 
test="345345"
cmd_painter(f"Hello World! {test}","Red") 

#3. path (windows and vscode)
#This is for whole text
#os.system("color 2")  #for green

# 0 = Black # 8 = Gray
# 1 = Blue # 9 = Light Blue
# 2 = Green # A = Light Green
# 3 = Aqua # B = Light Aqua
# 4 = Red # C = Light Red
# 5 = Purple # D = Light Purple
# 6 = Yellow # E = Light Yellow
# 7 = White # F = Bright White