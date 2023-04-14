r'''
               _                           _   _ _
 _ __ ___  ___| |__   __ _ _ __       __ _| |_(_) | ___
| '__/ _ \/ __| '_ \ / _` | '__|____ / _` | __| | |/ _ \
| | | (_) \__ \ | | | (_| | | |_____| (_| | |_| | |  __/
|_|  \___/|___/_| |_|\__,_|_|        \__, |\__|_|_|\___|
                                        |_|
'''

from subprocess import run, CalledProcessError
from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, ScratchPad, DropDown
from libqtile.scripts.main import VERSION
from libqtile.lazy import lazy

mod = 'mod4'
terminal = 'alacritty'
opaque_config = '--config-file /home/roland/.config/alacritty/alacritty-opaque.yml'
terminal_opaque = f'alacritty {opaque_config}'
qtile_config = f'alacritty {opaque_config} -e vim /home/roland/.config/qtile/config.py'
ipython = f'alacritty {opaque_config} -e ipython'
python = f'alacritty {opaque_config} -e python'
vpn_vta = 'alacritty -e /home/roland/.local/bin/vpn'
bjendal = 'alacritty -e /home/roland/.local/bin/bjendal'
lumar = 'alacritty -e /home/roland/.local/bin/lumar'
cmatrix = 'alacritty -e cmatrix'
rofi = 'rofi -combi-modi window,drun,ssh -theme nord -font "hack 12" -show drun -icon-theme "Papirus" -show-icons'
qtile_dir = '/home/roland/.config/qtile/'
wallpaper_dir = '/home/roland/.config/qtile/wallpaper/'
hotkeys = '/home/roland/.config/qtile/dhk'
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


def parse_task_text(text):
  '''
  Removes unwanted text from a given task string.

  Args:
      text (str): The text to be cleaned.

  Returns:
      str: The cleaned text.
  '''
  text = text.replace(' \u2014 Mozilla Firefox', '')
  text = text.replace(' - qutebrowser', '')
  text = text.replace(' - Discord', '')
  return text


def get_wallpaper(screen_number):
  '''
  Returns the wallpaper path based on the size of the screen.

  Args:
      screen_number (int): Index of the screen to get the wallpaper for.

  Returns:
      str: The wallpaper path for the specified screen size.

  Raises:
      IndexError: If the specified screen number is out of bounds.
  '''
  try:
    screens_ = run(
      ["xrandr | grep '*' | awk '{ print $1 }'"],
      shell=True,
      capture_output=True,
      encoding='utf-8',
      check=True,
    )
  except CalledProcessError:
    screens_ = '1920x1080'

  try:
    size = screens_.stdout.split()[screen_number]
  except IndexError:
    size = screens_.stdout.split()[0]

  match size:
    case '3440x1440':
      wallpaper = f'{wallpaper_dir}p3_3440x1440.png'
    case '1920x1080':
      wallpaper = f'{wallpaper_dir}p2_1920x1080.png'
    case '3840x1080':
      wallpaper = f'{wallpaper_dir}gunter_throne.png'
    case '5120x1440':
      wallpaper = f'{wallpaper_dir}p4_5120x1440.png'
    case '5760x1080':
      wallpaper = f'{wallpaper_dir}gunter_throne.png'
    case '1760x1262':
      wallpaper = f'{wallpaper_dir}gunter_throne_1760x1262.png'
    case _:
      wallpaper = f'{wallpaper_dir}not_supported.png'

  return wallpaper


# Keys
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], 'h', lazy.layout.left(), desc='Move focus to left'),
    Key([mod], 'l', lazy.layout.right(), desc='Move focus to right'),
    Key([mod], 'j', lazy.layout.down(), desc='Move focus down'),
    Key([mod], 'k', lazy.layout.up(), desc='Move focus up'),
    Key([mod], 'space', lazy.layout.next(), desc='Move window focus to other window'),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, 'shift'], 'h', lazy.layout.shuffle_left(), desc='Move window to the left'),
    Key([mod, 'shift'], 'l', lazy.layout.shuffle_right(), desc='Move window to the right'),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down(), desc='Move window down'),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up(), desc='Move window up'),
    Key([mod, 'shift'], 'space', lazy.layout.flip(), desc='Flip Layout'),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, 'control'], 'h', lazy.layout.grow_left(), desc='Grow window to the left'),
    Key([mod, 'control'], 'l', lazy.layout.grow_right(), desc='Grow window to the right'),
    Key([mod, 'control'], 'j', lazy.layout.grow_down(), desc='Grow window down'),
    Key([mod, 'control'], 'k', lazy.layout.grow_up(), desc='Grow window up'),
    Key([mod], 's', lazy.layout.normalize(), desc='Reset all window sizes'),
    Key([mod], "a", lazy.run_extension(extension.WindowList()), desc="Launch window list"),
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
    Key([mod, "shift"], "u", lazy.spawn(hotkeys), desc="Show Hotkeys"),
    Key([mod], "n", lazy.screen.next_group(skip_empty=True), desc="Switch to next group"),
    Key([mod, "shift"], "n", lazy.screen.prev_group(skip_empty=True), desc="Switch to previous group"),

    # LAUNCH chord
    KeyChord([mod], "e", [
        Key([], "e", lazy.group['scratchpad'].dropdown_toggle('term'), desc="Launch Scratchpad Terminal"),
        Key([], "i", lazy.group['scratchpad'].dropdown_toggle('ipython'), desc="Launch IPython"),
        Key([], "p", lazy.group['scratchpad'].dropdown_toggle('python'), desc="Launch python"),
        Key([], "q", lazy.group['scratchpad'].dropdown_toggle('qtile-config'), desc="Launch qtile config"),
        Key([], "v", lazy.group['scratchpad'].dropdown_toggle('vpn'), desc="Launch vpn"),
        Key([], "b", lazy.group['scratchpad'].dropdown_toggle('bjendal'), desc="Launch xrdp: bjendal"),
        Key([], "l", lazy.group['scratchpad'].dropdown_toggle('lumar'), desc="Launch xrdp: lumar"),
        Key([], "s", lazy.spawn('passmenu'), desc="Launch pass"),
        Key([], "r", lazy.run_extension(extension.DmenuRun(dmenu_prompt = "\uf101")), desc="Launch dmenu"),
        Key([], "m", lazy.spawn(cmatrix), desc="Launch matrix"),
        ],
        #mode=True,
        name="launch",
    ),
    # TOGGLE chord
    KeyChord([mod], "d", [
        Key([], "s", lazy.hide_show_bar(), desc="Toggle show bar"),
        Key([], "f", lazy.window.toggle_floating(), desc="Toggle floating mode"),
        Key([], "z", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen mode"),
        Key([], "e", lazy.widget['media_box_1'].toggle(),
                     lazy.widget['media_box_2'].toggle(),
                     lazy.widget['media_box_3'].toggle(), desc="Toggle Media Boxes"),
        Key([], "t", lazy.widget['widget_box_1'].toggle(),
                     lazy.widget['widget_box_2'].toggle(),
                     lazy.widget['widget_box_3'].toggle(), desc="Toggle Widget Boxes"),
        Key([], "1", lazy.widget['widget_box_1'].toggle(), desc="Toggle Widget Box 1"),
        Key([], "2", lazy.widget['widget_box_2'].toggle(), desc="Toggle Widget Box 2"),
        Key([], "3", lazy.widget['widget_box_3'].toggle(), desc="Toggle Widget Box 3"),
        ],
        name="toggle",
    ),
    # MEDIA chord
    KeyChord([mod], "v", [
        Key([], "v", lazy.widget['spotifyd'].play_pause(), desc="Play - Pause"),
        Key([], "h", lazy.widget['spotifyd'].previous(), desc="Previous"),
        Key([], "l", lazy.widget['spotifyd'].next(), desc="Next"),
        ],
        name="media",
    ),
    # FLAMESHOT chord
    KeyChord([mod], "f", [
        Key([], "f", lazy.spawn('flameshot'), desc="Launch flameshot"),
        Key([], "s", lazy.spawn('flameshot gui'), desc="Launch gui with option to select region"),
        Key([], "a", lazy.spawn('flameshot full'), desc="Screenshot all monitors"),
        Key([], "c", lazy.spawn('flameshot full --clipboard'), desc="Save capture to clipboard"),
        Key([], "l", lazy.spawn('flameshot launcher'), desc="Launch launcher"),
        ],
        name='flameshot',
    ),
]

# Groups
groups = [Group(i) for i in '123456']

discord_match = Match(wm_class='discord')
obsidian_match = Match(wm_class='obsidian')
xrdp_match = Match(wm_class='xfreerdp')
vm_match = Match(wm_class='VirtualBox Machine')
groups.extend([Group('7', label='\ue007'),
               Group('8', matches=[obsidian_match], label='\ue13a'),
               Group('9', matches=[discord_match], label='\uf392'),
               Group('0', matches=[xrdp_match], label='\uf512', init=False, persist=False),
               Group('o', matches=[vm_match], label='\uf511', init=False, persist=False)])

for i in groups:
  keys.extend(
    [
      # mod1 + letter of group = switch to group
      # toggle=True switches current group to last group
      Key(
        [mod],
        i.name,
        lazy.group[i.name].toscreen(toggle=True),
        desc=f'Switch to group {i.name}',
      ),
      # mod1 + shift + letter of group = move focused window to group
      # switch_group=False stays with current group
      Key(
        [mod, 'shift'],
        i.name,
        lazy.window.togroup(i.name, switch_group=False),
        desc=f'Move focused window to group {i.name}',
      ),
    ]
  )

groups.extend(
        [ScratchPad('scratchpad', [
            DropDown(
                'term',
                terminal_opaque,
                on_focus_lost_hide=False,
                opacity=.9,
                height=0.8,
                y=0.1,
                ),
            DropDown(
                'ipython',
                ipython,
                on_focus_lost_hide=False,
                opacity=.9,
                height=0.8,
                y=0.1,
                ),
            DropDown(
                'python',
                python,
                on_focus_lost_hide=False,
                opacity=.9,
                height=0.8,
                y=0.1,
                ),
            DropDown(
                'qtile-config',
                qtile_config,
                on_focus_lost_hide=False,
                opacity=1.0,
                height=0.9,
                y=0.05,
                ),
            DropDown(
                'vpn',
                vpn_vta,
                on_focus_lost_hide=True,
                opacity=1.0,
                height=0.5,
                y=0.1,
                ),
            DropDown(
                'bjendal',
                bjendal,
                on_focus_lost_hide=True,
                opacity=1.0,
                height=0.5,
                y=0.1,
                ),
            DropDown(
                'lumar',
                lumar,
                on_focus_lost_hide=True,
                opacity=1.0,
                height=0.5,
                y=0.1,
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
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
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

widget_defaults = {
        'font':"FontAwesome",
        'fontsize':18,
        'padding':2,
    }
extension_defaults = widget_defaults.copy()

# Mirrored widgets
chord = widget.Chord(
            chords_colors={
                'launch': (nord['nord13'], nord['nord0']),
                'flameshot': (nord['nord15'], nord['nord0']),
                'toggle': (nord['nord11'], nord['nord0']),
                'boxes': (nord['nord12'], nord['nord0']),
                'media': (nord['nord14'], nord['nord0']),
                },
                name_transform=lambda name: name.upper())

clock = widget.Clock(
            background=nord['nord11'],
            foreground=nord['nord0'],
            padding=4,
            format='%Y-%m-%d %a %H:%M')

screens = [
    Screen( #Screen1
        bottom=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    background=nord['nord10'],
                    foreground=nord['nord4'],
                ),
                widget.GroupBox(
                    font='Font Awesome 6 Brands',
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
                    font='Font Awesome 6 Brands',
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
    				        format = '{xesam:title} - ({xesam:artist})',
    				        playing_text = ' 契 {track}',
    				        paused_text  = '  {track}',
    				        width = 400,
    				        scroll_delay = 5,
    				        scroll_interval = 0.25,
    				        scroll_step = 15,
                            background=nord['nord10'],
    				        foreground=nord['nord0'],
				        ),
                        widget.PulseVolume(
                            font='FontAwesome',
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
                    font='Font Awesome 6 Brands',
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
                    font='Font Awesome 6 Brands',
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
    				        format = '{xesam:title} - ({xesam:artist})',
    				        playing_text = ' 契 {track}',
    				        paused_text  = '  {track}',
    				        width = 400,
    				        scroll_delay = 5,
    				        scroll_interval = 0.25,
    				        scroll_step = 15,
                            background=nord['nord10'],
    				        foreground=nord['nord0'],
				        ),
                        widget.PulseVolume(
                            font='FontAwesome',
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
                    font='Font Awesome 6 Brands',
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
                    font='Font Awesome 6 Brands',
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
    				        format = '{xesam:title} - ({xesam:artist})',
    				        playing_text = ' 契 {track}',
    				        paused_text  = '  {track}',
    				        width = 400,
    				        scroll_delay = 5,
    				        scroll_interval = 0.25,
    				        scroll_step = 15,
                            background=nord['nord10'],
    				        foreground=nord['nord0'],
				        ),
                        widget.PulseVolume(
                            font='FontAwesome',
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
    Drag([mod], 'Button1', lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], 'Button2', lazy.window.bring_to_front()),
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
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(wm_class='display_hotkeys'),
        Match(wm_class='dhk'),
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ],
    border_width=4,
    border_focus=nord['nord11'],
    border_normal=nord['nord10'],
)
auto_fullscreen = False
focus_on_window_activation = 'smart'
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
wmname = f'qtile {VERSION}'


def write_hot_keys():
  '''
  Generates two text files containing the list of hot keys and key chords.

  Writes the list of hot keys and key chords to two separate text files
  named "hotkeys.txt" and "keychords.txt", respectively. The text files are
  saved in the directory specified by the qtile_dir variable.
  '''
  mod_keys = {
      'mod4': 'Super',
      'shift': 'Shift',
      'control': 'Control',
      'space': 'Space',
  }

  hot_keys = []
  key_chords = []

  for key in keys:
    if isinstance(key, Key):
      if key.desc == 'Launch terminal':
        hot_keys.append('0000\n')
      if key.desc == 'Switch to group 1':
        hot_keys.append('0000\n')
      key_modifiers = ' + '.join([mod_keys[modifier] for modifier in key.modifiers])
      if len(key.key) == 1:
        hot_keys.append(f'{key_modifiers} + {key.key}: {key.desc}\n')
      elif len(key.key) > 1:
        hot_keys.append(f'{key_modifiers} + {key.key.title()}: {key.desc}\n')

  for key in keys:
    if isinstance(key, KeyChord):
      key_modifiers = ' + '.join([mod_keys[modifier] for modifier in key.modifiers])
      key_chords.append(f'{key_modifiers} + {key.key}: {key.name.upper()}\n')
      for sub in key.submappings:
        if isinstance(sub, Key):
          key_chords.append(f'    {sub.key}: {sub.desc}\n')
        elif isinstance(key, KeyChord):
          key_chords.append(f'    {sub.key}: {sub.name.upper()}\n')
          for map_ in sub.submappings:
            key_chords.append(f'        {map_.key}: {map_.desc}\n')
      key_chords.append('0000\n')

  with open(f'{qtile_dir}hotkeys.txt', 'w', encoding='utf-8') as file:
    file.write(''.join(hot_keys))
  with open(f'{qtile_dir}keychords.txt', 'w', encoding='utf-8') as file:
    file.write(''.join(key_chords))


write_hot_keys()
