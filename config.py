# ********************************                          IMPORTS                                ********************************
import os
import colors
import subprocess
from libqtile import hook, qtile, extension
from colors import gruvbox, nord_fox, gruvbox2
from libqtile.lazy import lazy
from libqtile.core.manager import Qtile
from libqtile import bar, layout, widget
from libqtile.backend.base import Window
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from MyBars import mera_bar1
# from Colours_Decor import *

# Additional Functions -------------***********-----------

# Brightness Up 
def brightup():
  qtile.cmd_spawn('brightnessctl set +1%')
  

# Brightness Down
def brightdown():
  qtile.cmd_spawn('brightnessctl set 1%-')


# ********************************-------------------------------Key_bidings-------------------------------********************************

mod = "mod4"
mod1 = "mod1"
trml = "terminator"

keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(trml),
             desc='Launches My Terminal'
             ),
         Key([mod1, "shift"], "c",
             lazy.spawn("google-chrome-stable"),
             desc='Launches My Chrome'
             ),
         Key([mod1, "shift"], "n",
             lazy.spawn("terminator -e nmtui"),
             desc='NetworkManager Tools'
             ),
        #  Key([mod1], "s",
        #      lazy.spawn("spotify"),
        #      desc='Launches My Spotify'
        #      ),
         Key([mod, "shift"], "Return",
             lazy.spawn("/home/abhi/.config/rofi/launchers/type-1/launcher.sh"),
             desc='Run Launcher Menu'
             ),

         Key([mod1], "f",
             lazy.spawn("firefox"),
             desc='Firefox'
             ),
         Key([mod1], "d",
             lazy.spawn("discord"),
             desc='Discord'
             ),
         Key([mod1], "t",
             lazy.spawn("telegram-desktop"),
             desc='Telegram'
             ),
         Key([mod1], "c",
             lazy.spawn("code"),
             desc='VS Code'
             ),
         Key([mod1], "n",
             lazy.spawn("pcmanfm"),
             desc='File Manager'
             ),
         Key([mod1], "b",
             lazy.spawn("blueman-manager"),
             desc='blueman-manager'
             ),         
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod1], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             ),
         Key([mod, "shift"], "x",
             lazy.spawn("shutdown -P now"),
             desc='Shut Down'
             ),
         Key([mod, "shift"], "r",
             lazy.spawn("reboot"),
             desc='Reboot'
             ),
         Key([mod], "l",
             lazy.spawn("betterlockscreen -l"),
             desc='Shut Down'
             ),
         Key([mod], "s",
             lazy.spawn("systemctl suspend"),
             desc='Shut Down'
             ),


         ### Window controls           
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod, "shift"], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),

         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod1], "Tab",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc ='Toggle between split and unsplit sides of stack'
             ),
         
         # Sound
         Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse sset Master toggle")),
         Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 1%-")),
         Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 1%+")),
         
         # Brightness
         Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl set +5%')),
         Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl set 5%-')),
        
         # ScreenShots
         Key([], "Print", lazy.spawn("scrot -q 100 -e 'mv $f /home/abhi/Pictures'")),
         Key(["control"], "Print", lazy.spawn('xfce4-screenshooter')),
         Key(["control", "shift"], "Print", lazy.spawn("scrot -q 100 -s -e 'mv $f /home/abhi/Pictures'")),


         Key([mod, "control"], 'r', lazy.run_extension(extension.DmenuRun(
                dmenu_prompt=">",
                dmenu_font="Andika-8",
                background="#15181a",
                foreground="#00ff00",
                selected_background="#079822",
                selected_foreground="#fff",
                dmenu_height=24,  # Only supported by some dmenu forks
    ))),

]

# Drag floating layouts.
my_mouse = [Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
            Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
            Click([mod], "Button2", lazy.window.bring_to_front())]


# Grouping I created -*-

groups = [
    Group('1', label="WEB. ", matches = [Match(wm_class = "firefox")], layout='bsp'),
    Group('2', label="CODE. ", matches = [Match(wm_class = "Code")], layout='max'),
    Group('3', label="TERM. ", layout='bsp'),
    Group('4', label="FILES. ", matches = [Match(wm_class = "pcmanfm")], layout='bsp'),
    Group('5', label="SOCIAL. ", matches = [Match(wm_class = "discord"), Match(wm_class="TelegramDesktop")], layout='bsp'),
    Group('6', label="Ж ", matches = [Match(wm_class = "vysor")], layout='bsp'),
    Group('7', label="Ж ", layout='bsp'),
    Group('8', label="Ж ", layout='bsp'),
    ]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# layout_theme = {"border_width": 0,
#                 "margin": [10, 10, 10, 10],
#                 "border_focus": colors.changable['trn'],
#                 "border_normal": "ffffff00"
#                 }
# floating_layout = {"border_width":0,}

layouts = [
    layout.MonadWide(
    #    **layout_theme
       border_width = 0,
       fullscreen_border_width = 0,
       max_border_width = 0,   
       margin =  [10, 10, 10, 10],
    ),
    # layout.Bsp(
    # #    **layout_theme
    #    border_width = 0,
    #    fullscreen_border_width = 0,
    #    max_border_width = 0,
    #    border_focus = colors.changable['trn'],
    #    margin =  [10, 10, 10, 10],
    # ),

    layout.Bsp(margin=10, border_focus=colors.changable['menuback'],border_width = 0, fair=False, border_on_single=True),

    layout.Columns(
    #    **layout_theme
       border_width = 0,
       fullscreen_border_width = 0,
       max_border_width = 0,
       margin =  [10, 10, 10, 10],
    ),
    layout.Zoomy(
    #    **layout_theme
       border_width = 0,
       fullscreen_border_width = 0,
       max_border_width = 0,
       margin =  [10, 10, 10, 10],
    ),
    layout.MonadTall(
    #    **layout_theme
       border_width = 0,
       fullscreen_border_width = 0,
       max_border_width = 0,
       margin =  [10, 10, 10, 10],
    ),
    layout.Max(
    #    **layout_theme
       border_width = 0,
       fullscreen_border_width = 0,
       max_border_width = 0,
       margin =  [10, 10, 10, 10],
    ),
    layout.Floating(
    #    **layout_theme,
       border_width = 0,
       border_focus=colors.changable['menuback'],
       fullscreen_border_width = 0,
       max_border_width = 0,
       margin =  [10, 10, 10, 10],
    )
]

## Layouts ------------------------------
var_bg_color = '#2e3440'
var_active_bg_color = '#81A1C1'
var_active_fg_color = '#2e3440'
var_inactive_bg_color = '#3d4555'
var_inactive_fg_color = '#D8DEE9'
var_urgent_bg_color = '#BF616A'
var_urgent_fg_color = '#D8DEE9'
var_section_fg_color = '#EBCB8B'
var_active_color = '#81A1C1'
var_normal_color = '#3d4555'
var_border_width = 2
var_margin = [5,5,5,5]
var_gap_top = 45
var_gap_bottom = 5
var_gap_left = 5
var_gap_right = 5 

#  The default floating layout to use. This allows you to set custom floating rules among other things if you wish.
floating_layout = layout.Floating(
	border_focus=var_active_color,
	border_normal=var_normal_color,
	border_width=var_border_width,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="alacritty-float|Music"),
        Match(wm_class="Lxappearance|Nitrogen"),
        Match(wm_class="Pavucontrol|Xfce4-power-manager-settings|Nm-connection-editor"),
        Match(wm_class="feh|Viewnior|Gpicview|Gimp|MPlayer|Vlc|Spotify"),
        Match(wm_class="Kvantum Manager|qt5ct"),
        Match(wm_class="VirtualBox Manager|qemu|Qemu-system-x86_64"),
        Match(title="branchdialog"),
    ]
)

widget_defaults = dict(
    background = colors.gruvbox['bg'],
    font="JetBrainsMono Nerd Font",
    fontsize=16,
    padding=0,
)
extension_defaults = widget_defaults.copy()


# ********************************                          BAR                               ********************************


screens = [ Screen(
   wallpaper = '~/Pictures/Wall/image_2023-05-11_10-40-12.png',
   wallpaper_mode = 'fill',
   top=mera_bar1
   )]

dgroups_key_binder = None
dgroups_app_rules = []  
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True



# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "Saitama"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])