from pygame import Color
from gradient_tools import linear_gradient

CGA = [
    Color('#000000'), Color('#0000aa'), Color('#00aa00'), Color('#00aaaa'),
    Color('#aa0000'), Color('#aa00aa'), Color('#aa5500'), Color('#aaaaaa'),
    Color('#555555'), Color('#5555ff'), Color('#55ff55'), Color('#55ffff'),
    Color('#ff5555'), Color('#ff55ff'), Color('#ffff55'), Color('#ffffff')
]

EGA = [
    Color('#000000'), Color('#000040'), Color('#000080'), Color('#0000C0'),
    Color('#004000'), Color('#004040'), Color('#004080'), Color('#0040C0'),
    Color('#008000'), Color('#008040'), Color('#008080'), Color('#0080C0'),
    Color('#00C000'), Color('#00C040'), Color('#00C080'), Color('#00C0C0'),
    Color('#400000'), Color('#400040'), Color('#400080'), Color('#4000C0'),
    Color('#404000'), Color('#404040'), Color('#404080'), Color('#4040C0'),
    Color('#408000'), Color('#408040'), Color('#408080'), Color('#4080C0'),
    Color('#40C000'), Color('#40C040'), Color('#40C080'), Color('#40C0C0'),
    Color('#800000'), Color('#800040'), Color('#800080'), Color('#8000C0'),
    Color('#804000'), Color('#804040'), Color('#804080'), Color('#8040C0'),
    Color('#808000'), Color('#808040'), Color('#808080'), Color('#8080C0'),
    Color('#80C000'), Color('#80C040'), Color('#80C080'), Color('#80C0C0'),
    Color('#C00000'), Color('#C00040'), Color('#C00080'), Color('#C000C0'),
    Color('#C04000'), Color('#C04040'), Color('#C04080'), Color('#C040C0'),
    Color('#C08000'), Color('#C08040'), Color('#C08080'), Color('#C080C0'),
    Color('#C0C000'), Color('#C0C040'), Color('#C0C080'), Color('#C0C0C0')
]

LINEAR_16 = [Color(code) for code in linear_gradient('#000000', '#00FF00', 16)['hex']]
LINEAR_64 = [Color(code) for code in linear_gradient('#000000', '#00FF00', 64)['hex']]
LINEAR_256 = [Color(code) for code in linear_gradient('#000000', '#00FF00', 256)['hex']]

ALL_PALETTES = [
    {'name': 'CGA', 'colors': CGA}, 
    {'name': 'EGA', 'colors': EGA},
    {'name': 'LINEAR_16', 'colors': LINEAR_16},
    {'name': 'LINEAR_64', 'colors': LINEAR_64},
    {'name': 'LINEAR_256', 'colors': LINEAR_256},
]
