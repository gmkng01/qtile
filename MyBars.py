import colors
from libqtile import qtile
from libqtile import widget
from libqtile.bar import Bar
from colors import gruvbox, gruvbox2
from unicodes import right_arrow, left_arrow, left_half_circle, lower_left_triangle
# from spotify import Spotify

terminal = "terminator"

# Brightness Up 
def brightup():
  qtile.cmd_spawn('brightnessctl set +5%')
# Brightness Down
def brightdown():
  qtile.cmd_spawn('brightnessctl set 5%-')

def menu():
  qtile.cmd_spawn('/home/abhi/.config/rofi/launchers/type-1/launcher.sh')

# COLORS----------------------------*

background = colors.gruvbox['bg']
slide1 = colors.changable['slide1']
slide2 = colors.changable['slide2']
rand_ = colors.changable['rand3']
menuback = colors.changable['menuback']
timeback = colors.changable['timeback']
netback = colors.changable['netback']

mera_bar1 = Bar([
                    widget.TextBox(
                        text='',
                        background = rand_,
                        # foreground = ,
                        fontsize = 25,
                        mouse_callbacks = {'Button1': menu,},
                        padding = 4,
                        ),
               
                   widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide1,
                            foreground = rand_,
                            padding = 0,
                            fontsize = 19
                    ),
                   widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide1,
                            foreground = menuback,
                            padding = 0,
                            fontsize = 22
                    ),

                    widget.GroupBox(
                            active=colors.draculla['cm'],
                            inactive=colors.draculla['cl'],
                            highlight_method='line',
                            block_highlight_text_color=colors.gruvbox['magenta'],
                            borderwidth=0,
                            highlight_color=menuback,
                            background=menuback,
                            fontsize = 25,
                            margin_y = 1,
                            margin_x = 1,
                            padding_y = 0,
                            padding_x = 3,
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide1,
                            foreground = menuback,
                            padding = 0,
                            fontsize = 19
                    ),
                   widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide1,
                            foreground = background,
                            padding = 0,
                            fontsize = 22
                    ),
                    
                    
                    widget.CurrentLayout(
                        #     background=gruvbox['fg0'],
                            foreground=gruvbox['fg9']
                    ),

                    widget.WindowCount(
                            text_format=' {num}',
                        #     background=gruvbox['fg0'],
                            foreground=gruvbox['fg9'],
                            show_zero=True,
                    ),
                    
                   
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide2,
                            foreground = background,
                            padding = 0,
                            fontsize = 19
                    ),
                   widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide2,
                            foreground = background,
                            padding = 0,
                            fontsize = 22
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide2,
                            foreground = background,
                            padding = 0,
                            fontsize = 19
                    ),
                   widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide2,
                            foreground = background,
                            padding = 0,
                            fontsize = 22
                    ),

                    widget.Spacer(),

                    
                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide2,
                            foreground = background,
                            padding = 0,
                            fontsize = 19
                    ),
                   widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide2,
                            foreground = background,
                            padding = 0,
                            fontsize = 22
                    ),

                    widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide2,
                            foreground = background,
                            padding = 0,
                            fontsize = 19
                    ),
                   widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide2,
                            foreground = background,
                            padding = 0,
                            fontsize = 22
                    ),

                    widget.Net(
                            format = ' {down}  {up}',
                        #     background=netback,
                            foreground=netback
                    ), 
                    
                #      widget.TextBox(
                #             text = '',
                #             font = "JetBrainsMono Nerd Font Mono",
                #             background = slide1,
                #             foreground = background,
                #             padding = 0,
                #             fontsize = 19
                #     ),
                #    widget.TextBox(
                #             text = '',
                #             font = "JetBrainsMono Nerd Font Mono",
                #             background = slide1,
                #             foreground = background,
                #             padding = 0,
                #             fontsize = 22
                #     ),

                #     widget.Volume(
                #         #     background=gruvbox['fg0'],
                #             foreground=gruvbox['dark-magenta'],
                #             fmt = 'ﮱ  HI-RES',
                #             mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn("pavucontrol")}
                #     ),

                     widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide1,
                            foreground = background,
                            padding = 0,
                            fontsize = 19
                    ),
                   widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide1,
                            foreground = background,
                            padding = 0,
                            fontsize = 22
                    ),

                    widget.Clock(
                            font = "JetBrainsMono Nerd Font",
                            foreground = timeback,
                        #     background = ,
                            format=' %d%b %a-%H:%M',
                            mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn("korganizer")}                            
                    ),

                   widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide1,
                            foreground = background,
                            padding = 0,
                            fontsize = 19
                    ),
                   widget.TextBox(
                            text = '',
                            font = "JetBrainsMono Nerd Font Mono",
                            background = slide1,
                            foreground = rand_,
                            padding = 0,
                            fontsize = 22
                    ),

                    widget.Systray(
                            background=rand_,
                            foreground = gruvbox['fg0'],
                            icon_size = 22,
                    )
                                       
            ],
               background=background, size=26, margin=[10, 0, 10, 0],
        )