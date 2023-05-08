"""                               """                               """
-----------------------------------------------------------------------
  #    ###  ## ##       ####  ##### #   #       #   # #####  ###  #  ##
 ##   #   #  # #        #   # #     #   #       ##  #   #   #   # # ##
# #   #   #   #         #   # ##### ## ##       # # #   #   #     ###
  #   #   #  # #        #   # #      # #        #  ##   #   #   # # ##
#####  ###  ## ##       ####  #####  ###        #   # #####  ###  #  ##
-----------------------------------------------------------------------
"""                               """                               """

import os, socket
from libqtile import qtile, extension
from libqtile.config import Click, Drag, Key, Screen, Group, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget
from libqtile.lazy import lazy
from typing import List 

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

mod = "mod4"
terminal = "alacritty"

keys = [
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
    Key([mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", 
        lazy.run_extension(extension.DmenuRun(fontsize=13, dmenu_ignorecase=True)), 
        desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
            Key([mod], i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key([mod, "shift"], i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": "e1acff",
    "border_normal": "1D2330"
}

layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Stack(stacks=2, **layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
        font = "Monospace Bold",
        fontsize = 12,
        sections = ["First", "Second", "Third", "Fourth"],
        section_fontsize = 18,
        border_width = 2,
        bg_color = "1c1f24",
        active_bg = "c678dd",
        active_fg = "000000",
        inactive_bg = "a9a1e1",
        inactive_fg = "1c1f24",
        padding_left = 2,
        padding_x = 0,
        padding_y = 5,
        section_top = 10,
        section_bottom = 20,
        level_shift = 8,
        vspace = 2,
        panel_width = 200
    ),
    layout.Floating(**layout_theme)
]

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

widget_defaults = dict(
    font = "Monospace Bold",
    fontsize = 18,
    padding = 2,
    background = colors[2]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top = bar.Bar(
            [
                widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                    ),
                widget.Image(
                        filename = "~/.config/qtile/icons/python-white.png",
                        scale = "False",
                        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(terminal)}
                    ),
                widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                    ),
                widget.GroupBox(
                        font = "Monospace Bold",
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 3,
                        borderwidth = 3,
                        active = colors[2],
                        inactive = colors[7],
                        rounded = False,
                        highlight_color = colors[1],
                        highlight_method = "line",
                        this_current_screen_border = colors[6],
                        this_screen_border = colors [4],
                        other_current_screen_border = colors[6],
                        other_screen_border = colors[4],
                        foreground = colors[2],
                        background = colors[0]
                    ),
                widget.TextBox(
                        text = "|",
                        font = "Monospace",
                        background = colors[0],
                        foreground = "474747",
                        padding = 2,
                        fontsize = 14
                    ),
                widget.CurrentLayoutIcon(
                        custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                        foreground = colors[2],
                        background = colors[0],
                        padding = 0,
                        scale = 0.7
                    ),
                widget.CurrentLayout(
                        foreground = colors[2],
                        background = colors[0],
                        padding = 5
                    ),
                widget.TextBox(
                        text = "|",
                        font = "Monospace",
                        background = colors[0],
                        foreground = "474747",
                        padding = 2,
                        fontsize = 14
                    ),
                widget.WindowName(
                        foreground = colors[6],
                        background = colors[0],
                        padding = 0,
                        max_chars = 50
                    ),
                widget.Systray(
                        background = colors[0],
                        padding = 5
                    ),
                widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[0],
                        background = colors[0]
                    ),
                widget.Memory(
                        foreground = colors[9],
                        background = colors[0],
                        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(terminal + " -e htop")},
                        fmt = "Mem:{}",
                        padding = 5,
                        decorations=[
                            BorderDecoration(
                                colour = colors[9],
                                border_width = [0, 0, 2, 0],
                                padding_x = 5,
                                padding_y = None,
                            )
                        ],
                    ),
                widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[0],
                        background = colors[0]
                    ),
                widget.PulseVolume(
                        foreground = colors[7],
                        background = colors[0],
                        fmt = "Vol: {}",
                        padding = 5,
                        decorations=[
                            BorderDecoration(
                                colour = colors[7],
                                border_width = [0, 0, 2, 0],
                                padding_x = 5,
                                padding_y = None,
                            )
                        ],
                    ),
                widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[0],
                        background = colors[0]
                    ),
                widget.Battery(
                        foreground = colors[4],
                        background = colors[0],
                        format = "Bat: {percent:2.0%}",
                        padding = 5,
                        decorations=[
                            BorderDecoration(
                                colour = colors[4],
                                border_width = [0, 0, 2, 0],
                                padding_x = 5,
                                padding_y = None,
                            )
                        ],
                ),
                widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[0],
                        background = colors[0]
                    ),
                widget.KeyboardLayout(
                        foreground = colors[8],
                        background = colors[0],
                        fmt = "{}",
                        padding = 5,
                        decorations=[
                            BorderDecoration(
                                colour = colors[8],
                                border_width = [0, 0, 2, 0],
                                padding_x = 5,
                                padding_y = None,
                            )
                        ],
                    ),
                widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[0],
                        background = colors[0]
                    ),
                widget.AnalogueClock(
                        background = colors[0],
                        face_shape = "square",
                        face_background = colors[6],
                        face_border_colour = colors[6],
                        face_border_width = 4,
                        padding = 5
                    ),
                widget.Clock(
                        foreground = colors[6],
                        background = colors[0],
                        format = " %d %a | %I:%M:%S %p ",
                        decorations=[
                            BorderDecoration(
                                colour = colors[6],
                                border_width = [0, 0, 2, 0],
                                padding_x = 5,
                                padding_y = None,
                            )
                        ],
                    ),
                widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[0],
                        background = colors[0]
                    ),
            ],
            24,
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start = lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start = lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class = "confirmreset"),  # gitk
        Match(wm_class = "makebranch"),    # gitk
        Match(wm_class = "maketag"),       # gitk
        Match(wm_class = "ssh-askpass"),   # ssh-askpass
        Match(title = "branchdialog"),     # gitk
        Match(title = "pinentry"),         # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"
