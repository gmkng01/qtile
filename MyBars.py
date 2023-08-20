import colors
from libqtile import qtile
from libqtile import widget
from libqtile.bar import Bar
from colors import gruvbox, gruvbox2
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration, BorderDecoration


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
trn = colors.changable['trn']

# powerline = {
#     "decorations": [
#         PowerLineDecoration()
#     ]
# }

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
                        background = trn,
                        foreground = rand_,
                        padding = 0,
                        fontsize = 19
                        ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = menuback,
                        padding = 0,
                        fontsize = 22
                        ),

                widget.GroupBox(
                        active=colors.changable['active'],
                        inactive=colors.draculla['cl'],
                        highlight_method='line',
                        block_highlight_text_color=colors.changable['highlight'],
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
                        background = trn,
                        foreground = menuback,
                        padding = 0,
                        fontsize = 19
                        ),
                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 22
                        ),
                    
                widget.CurrentLayout(
                        # background=gruvbox['fg0'],
                        foreground=gruvbox['fg9']
                        ),

                widget.WindowCount(
                        text_format=' {num}',
                        # background=gruvbox['fg0'],
                        foreground=gruvbox['fg9'],
                        show_zero=True,
                        ),                    
                   
                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 19
                        ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 22
                        ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 19
                        ),

                widget.Spacer(
                        background = trn,
                        ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 22
                        ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 19
                        ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 22
                        ),

                widget.Net(
                        format = ' {down}  {up}',
                        #     background=netback,
                        foreground=netback
                        ), 

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 19
                        ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
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
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 19
                        ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = rand_,
                        padding = 0,
                        fontsize = 22
                        ),

                #     widget.ALSAWidget(
                        # text='',
                        # background = colors[0],
                        # foreground = colors[2],
                        # fontsize = 18,
                        # mouse_callbacks = {'Button1': brightup, 'Button3': brightdown},
                        # padding = 0
                        # ),

               

                # widget.Systray(
                #         # background="#000000",
                #         # foreground = "#000000",
                #         icon_size = 22,
                #         decorations = [
                #             BorderDecoration (
                #                 colour = slide1,
                #                 # padding = 200,
                #                 radius = 20,
                #                 filled = True
                #             ),
                #         ],
                #         )
                                       
            ],
               background=trn, size=26, margin=[0, 0, 0, 0],
        )