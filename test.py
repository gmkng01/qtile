import colors
from libqtile import qtile
from libqtile import widget
from libqtile.bar import Bar
from libqtile.lazy import lazy
from colors import gruvbox, gruvbox2
from qtile_extras import widget


me = Bar([
     widget.AGroupBox()
],background=colors.gruvbox("bg"), size=26, margin=[0, 0, 0, 0],)

print(me)