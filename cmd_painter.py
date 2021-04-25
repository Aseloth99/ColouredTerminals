import os

def cmd_painter(msg,fore="White",back="Black"):
    """
    Normally white foreground with black background

    -ForegroundColor and BackgroundColor

    Black
    DarkBlue
    DarkGreen
    DarkCyan
    DarkRed
    DarkMagenta
    DarkYellow
    Gray
    DarkGray
    Blue
    Green
    Cyan
    Red
    Magenta
    Yellow
    White
    """
    os.system(f"powershell write-host -fore {fore} {msg} -back {back}")
