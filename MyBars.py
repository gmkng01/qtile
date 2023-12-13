import colors
from libqtile import qtile
from libqtile import widget
from libqtile.bar import Bar
from libqtile.lazy import lazy
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
                        text='ё',
                        background = rand_,
                        # foreground = ,
                        fontsize = 25,
                        mouse_callbacks = {'Button1': menu,},
                        padding = 4,  
                        font = "NFS font"                      
                        ),
               
                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = background,
                        foreground = rand_,
                        padding = 0,
                        fontsize = 19
                        ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = background,
                        foreground = menuback,
                        padding = 0,
                        fontsize = 22
                        ),


                widget.AGroupBox(
                        font = "NFS font",
                        fontsize = 18,
                        background = menuback,
                        foreground = background,
                        border = trn,
                        scroll = True,
                        scroll_clear = True,
                        width = 30,
                        mouse_callbacks = {'Button1': lazy.screen.next_group(),
                                           'Button2':lazy.screen.toggle_group(), 
                                           'Button3':lazy.screen.prev_group()}
                ),


                # widget.GroupBox(
                #         active=colors.changable['active'],
                #         inactive=colors.draculla['cl'],
                #         highlight_method='line',
                #         block_highlight_text_color=colors.changable['highlight'],
                #         borderwidth=0,
                #         highlight_color=menuback,
                #         background=menuback,
                #         foreground = rand_,
                #         fontsize = 18,
                #         # margin_y = 1,
                #         # margin_x = 1,
                #         # padding_y = 10,
                #         # padding_x = 0,
                #         font = "Speedeasy Speedy"
                #         ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = background,
                        foreground = menuback,
                        padding = 0,
                        fontsize = 22
                        ),
                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = background,
                        foreground = background,
                        padding = 0,
                        fontsize = 22
                        ),
                    
                widget.CurrentLayout(
                        fmt = '{} ',
                        # background=gruvbox['fg0'],
                        foreground=gruvbox['fg9'],
                        font = "NFS font",
                        fontsize = 19
                        ),

                widget.WindowCount(
                        text_format=' {num}  ',
                        # background=gruvbox['fg0'],
                        foreground=gruvbox['fg9'],
                        show_zero=True,
                        font = "NFS font"
                        ),                    
                   
                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 22
                        ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 22
                        ),

                widget.TextBox(
                        text = '',
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
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 22
                        ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 22
                        ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 19
                        ),

                widget.Net(
                        format = '« {down} » {up} ',
                        #     background=netback,
                        foreground=netback,
                        font = "NFS font",
                        fontsize = 19
                        ), 

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = menuback,
                        foreground = background,
                        padding = 0,
                        fontsize = 22
                        ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = menuback,
                        foreground = background,
                        padding = 0,
                        fontsize = 22
                        ),

                widget.TextBox(
                  text = "Ë ",
                  foreground = timeback,
                  font = "Dodger Super-Italic",
                  fontsize = 22
                ),

                widget.Clock(
                        font = "NFS font",
                        foreground = timeback,
                        #     background = ,
                        fontsize = 18,
                        format=' %d %b %a - %H:%M ',
                        mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn("korganizer")}                            
                        ),

                widget.TextBox(
                        text = '',
                        font = "JetBrainsMono Nerd Font Mono",
                        background = trn,
                        foreground = background,
                        padding = 0,
                        fontsize = 22
                        ),

                # widget.TextBox(
                #         text = '',
                #         font = "JetBrainsMono Nerd Font Mono",
                #         background = trn,
                #         foreground = trn,
                #         padding = 0,
                #         fontsize = 22
                #         ),

                #     widget.ALSAWidget(
                        # text='',
                        # background = colors[0],
                        # foreground = colors[2],
                        # fontsize = 18,
                        # mouse_callbacks = {'Button1': brightup, 'Button3': brightdown},
                        # padding = 0
                        # ),

               

                # widget.Systray(
                #         background="#000000",
                #         foreground = "#000000",
                #         icon_size = 22,
                        
                #         )
                                       
            ],
               background=trn, size=26, margin=[0, 0, 0, 0],
        )