# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Mmeasure_mem='G'# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, ScratchPad, DropDown
from libqtile.scripts.main import VERSION
from libqtile.lazy import lazy

from subprocess import run

mod = 'mod4'
terminal = 'alacritty'
opaque_config = '--config-file /home/roland/.config/alacritty/alacritty-opaque.yml'
terminal_opaque = f'alacritty {opaque_config}'
qtile_config = f'alacritty {opaque_config} -e vim /home/roland/.config/qtile/config.py'
ipython = f'alacritty {opaque_config} -e ipython'
python = f'alacritty {opaque_config} -e python'
vpn_vta = 'alacritty -e /home/roland/.local/bin/vpn'
rdp = 'alacritty -e /home/roland/.local/bin/bjendal'
rofi = 'rofi -combi-modi window,drun,ssh -theme nord -font "hack 12" -show drun -icon-theme "Papirus" -show-icons'
qtile_dir = '/home/roland/.config/qtile/'

flameshot = '#8800aa'
nord = {
        'nord0':'#2E3440',
        'nord1':'#3B4252',
        'nord2':'#434C5E',
        'nord3':'#4C566A',
        'nord4':'#D8DEE9',
        'nord5':'#E5E9F0',
        'nord6':'#ECEFF4',
        'nord7':'#8FBCBB',
        'nord8':'#88C0D0',
        'nord9':'#81A1C1',
        'nord10':'#5E81AC',
        'nord11':'#BF616A',
        'nord12':'#D08770',
        'nord13':'#EBCB8B',
        'nord14':'#A3BE8C',
        'nord15':'#B48EAD',
       }

# Keys
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    #Key(
        #[mod, "shift"],
        #"Return",
        #lazy.layout.toggle_split(),
        #desc="Toggle between split and unsplit sides of stack",
    #),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn(rofi), desc="Launch rofi"),
    Key([mod], "z", lazy.run_extension(extension.WindowList()), desc="Launch window list"),
    # LAUNCH chord
    KeyChord([mod], "e", [
        Key([], "e", lazy.group['scratchpad'].dropdown_toggle('term'), desc="Launch Scratchpad Terminal"),
        Key([], "i", lazy.group['scratchpad'].dropdown_toggle('ipython'), desc="Launch IPython"),
        Key([], "p", lazy.group['scratchpad'].dropdown_toggle('python'), desc="Launch python"),
        Key([], "q", lazy.group['scratchpad'].dropdown_toggle('qtile-config'), desc="Launch qtile config"),
        Key([], "v", lazy.group['scratchpad'].dropdown_toggle('vpn'), desc="Launch vpn"),
        Key([], "x", lazy.group['scratchpad'].dropdown_toggle('xrdp'), desc="Launch xrdp: bjendal"),
        Key([], "s", lazy.spawn('passmenu'), desc="Launch pass"),
        Key([], "r", lazy.run_extension(extension.DmenuRun(dmenu_prompt = "\uf101")), desc="Launch dmenu"),
        # FLAMESHOT chord
        KeyChord([], "f", [
            Key([], "f", lazy.spawn('flameshot'), desc="Launch flameshot"),
            Key([], "s", lazy.spawn('flameshot gui'), desc="Take screenshot"),
            Key([], "a", lazy.spawn('flameshot full'), desc="Take screenshot"),
            Key([], "c", lazy.spawn('flameshot full --clipboard'), desc="Take screenshot"),
            Key([], "l", lazy.spawn('flameshot launcher'), desc="Take screenshot"),
            ],
            name='flameshot',
        )
        ],
        #mode=True,
        name="launch",
    ),
    # TOGGLE chord
    KeyChord([mod], "d", [
        Key([], "s", lazy.hide_show_bar(), desc="Toggle show bar"),
        # BOXES chord
        KeyChord([], "t", [
                Key([], "1", lazy.widget['widget_box_1'].toggle(), desc="Toggle Widget Box 1"),
                Key([], "2", lazy.widget['widget_box_2'].toggle(), desc="Toggle Widget Box 2"),
                Key([], "3", lazy.widget['widget_box_3'].toggle(), desc="Toggle Widget Box 3"),
                Key([], "t", lazy.widget['widget_box_1'].toggle(),
                             lazy.widget['widget_box_2'].toggle(),
                             lazy.widget['widget_box_3'].toggle(),
                             lazy.widget['media_box_1'].toggle(),
                             lazy.widget['media_box_2'].toggle(),
                             lazy.widget['media_box_3'].toggle(), desc="Toggle Widget Boxes"),
                ],
            name="boxes",
            ),
        ],
        name="toggle",
    ),
    # MEDIA chord
    KeyChord([mod], "s", [
            Key([], "s", lazy.widget['spotifyd'].play_pause(), desc="Play - Pause"),
            Key([], "h", lazy.widget['spotifyd'].previous(), desc="Previous"),
            Key([], "l", lazy.widget['spotifyd'].next(), desc="Next"),
        ],
        name="media",
    ),
    Key([mod, "shift"], "u", lazy.group['scratchpad'].dropdown_toggle('hotkeys'), desc="Show Hot Keys"),
]

# Groups
groups = [Group(i) for i in "123456"]

discord_match = Match(wm_class="discord")
obsidian_match = Match(wm_class="obsidian")
xrdp_match = Match(wm_class="xfreerdp")
vm_match = Match(wm_class="VirtualBox Machine")
groups.extend([Group("7", label='\ue007')])
groups.extend([Group("8", matches=[obsidian_match], label='\ue13a')])
groups.extend([Group("9", matches=[discord_match], label='\uf392')])
groups.extend([Group("0", matches=[xrdp_match], label='\uf512', init=False, persist=False)])
groups.extend([Group("o", matches=[vm_match], label='\uf511', init=False, persist=False)])

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            # toggle=True switches current group to last group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(toggle=True),
                desc=f"Switch to group {i.name}",
            ),
            # mod1 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc=f"Move focused window to group {i.name}",
            ),
        ]
    )

def get_hot_keys():
    mod_keys = {
            'mod4':'Super',
            'shift':'Shift',
            'control':'Control',
            'space':'Space',
           }

    hot_keys = []

    for key in keys:
        if isinstance(key, Key):
            key_modifiers = ' + '.join([mod_keys[modifier] for modifier in key.modifiers])
            if len(key.key) == 1:
                hot_keys.append(f"{key_modifiers} + {key.key}: {key.desc}\n")
            elif len(key.key) > 1:
                hot_keys.append(f"{key_modifiers} + {key.key.title()}: {key.desc}\n")
    for key in keys:
        if isinstance(key, KeyChord):
            key_modifiers = ' + '.join([mod_keys[modifier] for modifier in key.modifiers])
            hot_keys.append(f"{key_modifiers} + {key.key}: {key.name.upper()}\n")
            for sub in key.submappings:
                if isinstance(sub, Key):
                    hot_keys.append(f"  {sub.key}: {sub.desc}\n")
                elif isinstance(key, KeyChord):
                    hot_keys.append(f"  {sub.key}: {sub.name.upper()}\n")
                    for map in sub.submappings:
                        hot_keys.append(f"    {map.key}: {map.desc}\n")

    return ''.join(hot_keys)

hot_key_text = get_hot_keys()

hotkeys = f'yad --title "Hotkeys" --text-info --scroll --text="{hot_key_text}"'

groups.extend(
        [ScratchPad("scratchpad", [
            DropDown(
                "term",
                terminal_opaque,
                config = {
                    'on_focus_lost_hide':False,
                    'opacity':1.0,
                    'height':0.5,
                    'y':0.1,
                    },
                ),
            DropDown(
                "ipython",
                ipython,
                config = {
                    'on_focus_lost_hide':False,
                    'opacity':1.0,
                    'height':0.9,
                    'y':0.05,
                    },
                ),
            DropDown(
                "python",
                python,
                config = {
                    'on_focus_lost_hide':False,
                    'opacity':1.0,
                    'height':0.9,
                    'y':0.05,
                    },
                ),
            DropDown(
                "qtile-config",
                qtile_config,
                config = {
                    'on_focus_lost_hide':False,
                    'opacity':1.0,
                    'height':0.9,
                    'y':0.05,
                    },
                ),
            DropDown(
                "vpn",
                vpn_vta,
                config = {
                    'on_focus_lost_hide':True,
                    'opacity':1.0,
                    'height':0.5,
                    'y':0.1,
                    },
                ),
            DropDown(
                "xrdp",
                rdp,
                config = {
                    'on_focus_lost_hide':True,
                    'opacity':1.0,
                    'height':0.5,
                    'y':0.1,
                    },
                ),
            DropDown(
                "hotkeys",
                hotkeys,
                config = {
                    'on_focus_lost_hide':True,
                    'opacity':1.0,
                    'height':0.5,
                    'y':0.1,
                    },
                ),
            ])
        ])

layouts = [
    #layout.Columns(
    #    #border_focus_stack=[nord['nord11'], "#8f3d3d"],
    #    border_focus_stack=nord['nord11'],
    #    border_focus=nord['nord11'],
    #    border_normal_stack=nord['nord10'],
    #    border_normal=nord['nord10'],
    #    border_width=4,
    #    margin=[4,2,4,2],
    # ),
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    layout.MonadTall(
        border_focus=nord['nord11'],
        border_normal=nord['nord10'],
        border_width=4,
        margin=4
    ),
    layout.Max(),
    layout.MonadThreeCol(
        main_centered=True,
        new_client_position='after_current',
        border_focus=nord['nord11'],
        border_normal=nord['nord10'],
        border_width=4,
        margin=4
        ),
    #layout.MonadWide(),
    #layout.RatioTile(),
    #layout.Spiral(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font="FontAwesome",
    fontsize=18,
    padding=2,
)
extension_defaults = widget_defaults.copy()

# Mirrored widgets
chord = widget.Chord(
            chords_colors={
                "launch": (nord['nord13'], nord['nord0']),
                "flameshot": (nord['nord15'], nord['nord0']),
                "toggle": (nord['nord11'], nord['nord0']),
                "boxes": (nord['nord12'], nord['nord0']),
                "media": (nord['nord14'], nord['nord0']),
                },
                name_transform=lambda name: name.upper())

clock = widget.Clock(
            background=nord['nord11'],
            foreground=nord['nord0'],
            padding=4,
            format="%Y-%m-%d %a %H:%M")


def parse_task_text(text):
    text = text.replace(' \u2014 Mozilla Firefox','')
    text = text.replace(' - qutebrowser','')
    text = text.replace(' - Discord','')
    return text


def get_wallpaper(screen_number):
    screens = run(["xrandr | grep '*' | awk '{ print $1 }'"],
               shell=True, 
               capture_output=True,
               encoding='utf-8')
    try:
        size = screens.stdout.split()[screen_number]
    except IndexError:
        size = screens.stdout.split()[0]

    match size:
        case '3440x1440':
            wallpaper = f'{qtile_dir}gunter_wallpaper3440x1440_fill.png'
        case '1920x1080':
            wallpaper = f'{qtile_dir}gunter_throne.png'
        case '3840x1080':
            wallpaper = f'{qtile_dir}gunter_throne.png'
        case '5760x1080':
            wallpaper = f'{qtile_dir}gunter_throne.png'
        case '1760x1262':
            wallpaper = f'{qtile_dir}gunter_throne_1760x1262.png'
        case _:
            wallpaper = f'{qtile_dir}not_supported.png'

    return wallpaper

screens = [
    Screen( #Screen1
        bottom=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    background=nord['nord10'],
                    foreground=nord['nord4'],
                ),
                widget.GroupBox(
                    font="Font Awesome 6 Brands",
                    background=nord['nord10'],
                    disable_drag=True,
                    block_highlight_text_color=nord['nord8'],
                    this_screen_border=nord['nord13'],
                    this_current_screen_border=nord['nord11'],
                    padding=4,
                    #margin=0,
                ),
                widget.Spacer(
                    background=nord['nord0'],
                    length=4,
                ),
                widget.WindowCount(
                    font="Font Awesome 6 Brands",
                    background=nord['nord0'],
                    foreground=nord['nord4'],
                ),
                widget.TaskList(
                    background=nord['nord0'],
                    foreground=nord['nord4'],
                    border=nord['nord11'],
                    highlight_method='block',
                    markup_focused='<span foreground="#2E3440">{}</span>',
                    parse_text=parse_task_text,
                    margin=2,
                    padding=2,
                ),
                chord,
                widget.Spacer(
                    background=nord['nord0'],
                    length=4,
                ),
                widget.Systray(
                    background=nord['nord0'],
                    icon_size=26,
                    padding=4,
                ),
                widget.Spacer(
                    background=nord['nord0'],
                    length=6,
                ),
                widget.WidgetBox(
                    name='media_box_1',
                    background=nord['nord0'],
                    foreground=nord['nord13'],
                    fontsize=30,
                    close_button_location='right',
                    text_closed='\uf100',
                    text_open='\uf101',
                    padding=15,
                    widgets=[
				        widget.Mpris2(
					        name='spotifyd',
					        #objname=media_player,
    				        format = "{xesam:title} - ({xesam:artist})",
    				        playing_text = " 契 {track}",
    				        paused_text  = "  {track}",
    				        width = 400,
    				        scroll_delay = 5,
    				        scroll_interval = 0.25,
    				        scroll_step = 15,
                            background=nord['nord10'],
    				        foreground=nord['nord0'],
				        ),
                        widget.PulseVolume(     
                            font="FontAwesome",
                            fmt='\uf028 {}',
                            background=nord['nord0'],
                            foreground=nord['nord4'],
                        ),
                    ],
                ),
                widget.Spacer(
                    background=nord['nord0'],
                    length=4,
                ),
                widget.WidgetBox(
                    name='widget_box_1',
                    background=nord['nord0'],
                    foreground=nord['nord13'],
                    fontsize=30,
                    close_button_location='right',
                    text_closed='\uf100',
                    text_open='\uf101',
                    padding=15,
                    widgets=[
                        widget.OpenWeather(
                            background=nord['nord15'],
                            foreground=nord['nord0'],
                            cityid='4198514',
                            app_key='*****',
                            metric=False),
                        widget.Net(
                            background=nord['nord10'],
                            foreground=nord['nord0'],
                            interface='net0'),
                        widget.Memory(
                            background=nord['nord14'],
                            foreground=nord['nord0']),
                        widget.CPU(
                            background=nord['nord13'],
                            foreground=nord['nord0']),
                        widget.ThermalSensor(
                            background=nord['nord13'],
                            foreground=nord['nord0'],
                            tag_sensor='Package id 0',
                            format='{temp:.0f}{unit}'),
                        widget.DF(
                            background=nord['nord12'],
                            foreground=nord['nord0'],
                            warn_space=40,
                            visible_on_warn=True),
                        widget.DF(
                            background=nord['nord12'],
                            foreground=nord['nord0'],
                            partition='/home',
                            warn_space=40,
                            visible_on_warn=True),
                        widget.ThermalSensor(
                            background=nord['nord12'],
                            foreground=nord['nord0'],
                            tag_sensor='Composite',
                            format='NVME: {temp:.0f}{unit}'),
                        widget.Spacer(
                            background=nord['nord0'],
                            length=8
                        ),
                    ]
                ),
                widget.Spacer(
                    background=nord['nord0'],
                    length=6
                ),
                clock,
                widget.WidgetBox(
                    name='shutdown',
                    background=nord['nord11'],
                    foreground=nord['nord0'],
                    fontsize=30,
                    close_button_location='right',
                    text_closed='\uf100',
                    text_open='\uf101',
                    padding=15,
                    widgets=[
                        widget.QuickExit(
                            background=nord['nord11'],
                            foreground=nord['nord0'],
                            fontsize=24,
                            default_text='\uf1e2'
                        ),
                    ],
                ),
                widget.Spacer(
                    background=nord['nord11'],
                    length=4
                ),
            ],
            size=32,
            border_width=[0, 0, 0, 0],
            border_color=[nord['nord10'], nord['nord10'], nord['nord10'], nord['nord10']],
            margin=4,
        ),
        wallpaper = get_wallpaper(0),
        wallpaper_mode='fill',
    ),
    Screen( # Screen2
            bottom=bar.Bar([
                widget.CurrentLayoutIcon(
                    background=nord['nord10'],
                    foreground=nord['nord4'],
                ),
                widget.GroupBox(
                    font="Font Awesome 6 Brands",
                    background=nord['nord10'],
                    disable_drag=True,
                    block_highlight_text_color=nord['nord8'],
                    this_screen_border=nord['nord13'],
                    this_current_screen_border=nord['nord11'],
                    padding=4,
                ),
                widget.Spacer(
                    background=nord['nord0'],
                    length=4,
                ),
                widget.WindowCount(
                    font="Font Awesome 6 Brands",
                    background=nord['nord0'],
                    foreground=nord['nord4'],
                ),
                widget.TaskList(
                    background=nord['nord0'],
                    foreground=nord['nord4'],
                    border=nord['nord11'],
                    highlight_method='block',
                    markup_focused='<span foreground="#2E3440">{}</span>',
                    parse_text=parse_task_text,
                    margin=2,
                    padding=2,
                ),
                chord,
                widget.Spacer(
                    background=nord['nord0'],
                    length=6,
                ),
                widget.WidgetBox(
                    name='media_box_2',
                    background=nord['nord0'],
                    foreground=nord['nord13'],
                    fontsize=30,
                    close_button_location='right',
                    text_closed='\uf100',
                    text_open='\uf101',
                    padding=15,
                    widgets=[
				        widget.Mpris2(
					        name='spotifyd',
					        #objname=media_player,
    				        format = "{xesam:title} - ({xesam:artist})",
    				        playing_text = " 契 {track}",
    				        paused_text  = "  {track}",
    				        width = 400,
    				        scroll_delay = 5,
    				        scroll_interval = 0.25,
    				        scroll_step = 15,
                            background=nord['nord10'],
    				        foreground=nord['nord0'],
				        ),
                        widget.PulseVolume(     
                            font="FontAwesome",
                            fmt='\uf028 {}',
                            background=nord['nord0'],
                            foreground=nord['nord4'],
                        ),
                    ],
                ),
                widget.Spacer(
                    background=nord['nord0'],
                    length=4,
                ),
                widget.WidgetBox(
                    name='widget_box_2',
                    background=nord['nord0'],
                    foreground=nord['nord13'],
                    fontsize=30,
                    close_button_location='right',
                    text_closed='\uf100',
                    text_open='\uf101',
                    padding=15,
                    widgets=[
                        widget.OpenWeather(
                            background=nord['nord15'],
                            foreground=nord['nord0'],
                            cityid='4198514',
                            app_key='*****',
                            metric=False),
                        widget.Net(
                            background=nord['nord10'],
                            foreground=nord['nord0'],
                            interface='net0'),
                        widget.Memory(
                            background=nord['nord14'],
                            foreground=nord['nord0']),
                        widget.CPU(
                            background=nord['nord13'],
                            foreground=nord['nord0']),
                        widget.ThermalSensor(
                            background=nord['nord13'],
                            foreground=nord['nord0'],
                            tag_sensor='Package id 0',
                            format='{temp:.0f}{unit}'),
                        widget.DF(
                            background=nord['nord12'],
                            foreground=nord['nord0'],
                            warn_space=40,
                            visible_on_warn=True),
                        widget.DF(
                            background=nord['nord12'],
                            foreground=nord['nord0'],
                            partition='/home',
                            warn_space=40,
                            visible_on_warn=True),
                        widget.ThermalSensor(
                            background=nord['nord12'],
                            foreground=nord['nord0'],
                            tag_sensor='Composite',
                            format='NVME: {temp:.0f}{unit}'),
                        widget.Spacer(
                            background=nord['nord0'],
                            length=8
                        ),
                    ]
                ),
                widget.Spacer(
                    background=nord['nord0'],
                    length=6
                ),
                clock,
                widget.WidgetBox(
                    name='shutdown',
                    background=nord['nord11'],
                    foreground=nord['nord0'],
                    fontsize=30,
                    close_button_location='right',
                    text_closed='\uf100',
                    text_open='\uf101',
                    padding=15,
                    widgets=[
                        widget.QuickExit(
                            background=nord['nord11'],
                            foreground=nord['nord0'],
                            fontsize=24,
                            default_text='\uf1e2'
                        ),
                    ],
                ),
                widget.Spacer(
                    background=nord['nord11'],
                    length=4
                ),
            ],
            size=32,
            border_width=[0, 0, 0, 0],
            border_color=[nord['nord10'], nord['nord10'], nord['nord10'], nord['nord10']],
            margin=4,
        ),
        wallpaper = get_wallpaper(1),
        wallpaper_mode='fill',
    ),
    Screen( # Screen3
            bottom=bar.Bar([
                widget.CurrentLayoutIcon(
                    background=nord['nord10'],
                    foreground=nord['nord4'],
                ),
                widget.GroupBox(
                    font="Font Awesome 6 Brands",
                    background=nord['nord10'],
                    disable_drag=True,
                    block_highlight_text_color=nord['nord8'],
                    this_screen_border=nord['nord13'],
                    this_current_screen_border=nord['nord11'],
                    padding=4,
                ),
                widget.Spacer(
                    background=nord['nord0'],
                    length=4,
                ),
                widget.WindowCount(
                    font="Font Awesome 6 Brands",
                    background=nord['nord0'],
                    foreground=nord['nord4'],
                ),
                widget.TaskList(
                    background=nord['nord0'],
                    foreground=nord['nord4'],
                    border=nord['nord11'],
                    highlight_method='block',
                    markup_focused='<span foreground="#2E3440">{}</span>',
                    parse_text=parse_task_text,
                    margin=2,
                    padding=2,
                ),
                chord,
                widget.Spacer(
                    background=nord['nord0'],
                    length=6,
                ),
                widget.WidgetBox(
                    name='media_box_3',
                    background=nord['nord0'],
                    foreground=nord['nord13'],
                    fontsize=30,
                    close_button_location='right',
                    text_closed='\uf100',
                    text_open='\uf101',
                    padding=15,
                    widgets=[
				        widget.Mpris2(
					        name='spotifyd',
					        #objname=media_player,
    				        format = "{xesam:title} - ({xesam:artist})",
    				        playing_text = " 契 {track}",
    				        paused_text  = "  {track}",
    				        width = 400,
    				        scroll_delay = 5,
    				        scroll_interval = 0.25,
    				        scroll_step = 15,
                            background=nord['nord10'],
    				        foreground=nord['nord0'],
				        ),
                        widget.PulseVolume(     
                            font="FontAwesome",
                            fmt='\uf028 {}',
                            background=nord['nord0'],
                            foreground=nord['nord4'],
                        ),
                    ],
                ),
                widget.Spacer(
                    background=nord['nord0'],
                    length=4,
                ),
                widget.WidgetBox(
                    name='widget_box_3',
                    background=nord['nord0'],
                    foreground=nord['nord13'],
                    fontsize=30,
                    close_button_location='right',
                    text_closed='\uf100',
                    text_open='\uf101',
                    padding=15,
                    widgets=[
                        widget.OpenWeather(
                            background=nord['nord15'],
                            foreground=nord['nord0'],
                            cityid='4198514',
                            app_key='*****',
                            metric=False),
                        widget.Net(
                            background=nord['nord10'],
                            foreground=nord['nord0'],
                            interface='net0'),
                        widget.Memory(
                            background=nord['nord14'],
                            foreground=nord['nord0']),
                        widget.CPU(
                            background=nord['nord13'],
                            foreground=nord['nord0']),
                        widget.ThermalSensor(
                            background=nord['nord13'],
                            foreground=nord['nord0'],
                            tag_sensor='Package id 0',
                            format='{temp:.0f}{unit}'),
                        widget.DF(
                            background=nord['nord12'],
                            foreground=nord['nord0'],
                            warn_space=40,
                            visible_on_warn=True),
                        widget.DF(
                            background=nord['nord12'],
                            foreground=nord['nord0'],
                            partition='/home',
                            warn_space=40,
                            visible_on_warn=True),
                        widget.ThermalSensor(
                            background=nord['nord12'],
                            foreground=nord['nord0'],
                            tag_sensor='Composite',
                            format='NVME: {temp:.0f}{unit}'),
                        widget.Spacer(
                            background=nord['nord0'],
                            length=8
                        ),
                    ]
                ),
                widget.Spacer(
                    background=nord['nord0'],
                    length=6
                ),
                clock,
                widget.WidgetBox(
                    name='shutdown',
                    background=nord['nord11'],
                    foreground=nord['nord0'],
                    fontsize=30,
                    close_button_location='right',
                    text_closed='\uf100',
                    text_open='\uf101',
                    padding=15,
                    widgets=[
                        widget.QuickExit(
                            background=nord['nord11'],
                            foreground=nord['nord0'],
                            fontsize=24,
                            default_text='\uf1e2'
                        ),
                    ],
                ),
                widget.Spacer(
                    background=nord['nord11'],
                    length=4
                ),
            ],
            size=32,
            border_width=[0, 0, 0, 0],
            border_color=[nord['nord10'], nord['nord10'], nord['nord10'], nord['nord10']],
            margin=4,
        ),
        wallpaper = get_wallpaper(2),
        wallpaper_mode='fill',
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        vm_match,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_width=4,
    border_focus=nord['nord11'],
    border_normal=nord['nord10'],
)
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
# wmname = "LG3D"
wmname = f"qtile {VERSION}"

#mod_keys = {
            #'mod4':'Super',
            #'shift':'Shift',
            #'control':'Control',
            #'space':'Space',
           #}
#
#hot_keys = []
#
#for key in keys:
    #if isinstance(key, Key):
        #key_modifiers = ' + '.join([mod_keys[modifier] for modifier in key.modifiers])
        #if len(key.key) == 1:
            #hot_keys.append(f"{key_modifiers} + {key.key}: {key.desc}\n")
        #elif len(key.key) > 1:
            #hot_keys.append(f"{key_modifiers} + {key.key.title()}: {key.desc}\n")
#for key in keys:
    #if isinstance(key, KeyChord):
        #key_modifiers = ' + '.join([mod_keys[modifier] for modifier in key.modifiers])
        #hot_keys.append(f"{key_modifiers} + {key.key}: {key.name.upper()}\n")
        #for sub in key.submappings:
            #if isinstance(sub, Key):
                #hot_keys.append(f"  {sub.key}: {sub.desc}\n")
            #elif isinstance(key, KeyChord):
                #hot_keys.append(f"  {sub.key}: {sub.name.upper()}\n")
                #for map in sub.submappings:
                    #hot_keys.append(f"    {map.key}: {map.desc}\n")
#
#print(''.join(hot_keys))
