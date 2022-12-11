from typing import Optional
from libqtile.widget.textbox import TextBox


def left_half_circle(fg_color):
    return TextBox(
        text='\uE0B6',
        fontsize=28,
        foreground=fg_color,
        padding=0)


def right_half_circle(bg_color, fg_color: Optional['str'] = None):
    return TextBox(
        text='\uE0B4',
        fontsize=28,
        background=bg_color,
        foreground=fg_color,
        padding=0)


def lower_left_triangle(bg_color, fg_color):
    return TextBox(
        text='\u25e2',
        padding=0,
        fontsize=50,
        background=bg_color,
        foreground=fg_color)


def left_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B2',
        #text='\ueb6f',
        font='FuraMono NF',
        #text='\ue5b7',
        padding=0,
        fontsize=20,
        background=bg_color,
        foreground=fg_color)


def right_arrow(bg_color, fg_color):
    return TextBox(
        font='FuraMono NF',
        text='\uE0B0',
        #text='\uf44a',
        padding=0,
        fontsize=20,
        background=bg_color,
        foreground=fg_color)
