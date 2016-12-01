try:
    import tkinter as tk
    from tkinter.constants import TOP, BOTTOM, LEFT, RIGHT, X, Y, BOTH
except ImportError:
    import Tkinter as tk
    from Tkinter import TOP, BOTTOM, LEFT, RIGHT, X, Y, BOTH
    
import random

def run():
    calcGUI = CalculatorGUI()

'''
('','','',''),
                 ('','','',''),
                 ('','','',''),
                 ('','','','')
'''

class CalculatorGUI():
    # _palette item: display_bg, display_fg, button_bg, button_fg
    _palettes = [('#dd4b39','#010a7c','#3b5998','#91cfff'),
                 ('#03315c','#007dff','#ff3232','#03315c'),
                 ('#00a1f1','#581a69','#f65314','#ffbb00'),
                 ('#ff0000','#fff400','#7400b6','#00f2f9'),
                 ('#001eff','#fff400','#ff0000','#001eff'),

                 ]

    def __init__(self):
        master = tk.Tk()
        master.resizable(width=False, height=False)
        master.wm_title('Calculator')

        self._current_palette=('','','','')
        button_height = 64
        button_width = 52
        row_h = button_height
        row_w = 4 * button_width
        num_display_ipady=10
        num_display_ipadx=10

        '''
        # options to remove border -- Window becomes immovable, and turns off key bindings
        # Pack self.num_display and buttons_frame in win if you decide to use this
        master.attributes('-alpha', 0.0)
        master.iconify()
        win = tk.Toplevel(master)
        win.overrideredirect(True)
        '''

        self.plus = False
        self.minus = False
        self.div = False
        self.mult = False
        self.decimal_place=0

        #num_disp_bg = '#dd4b39'
        #num_disp_fg = '#010a7c'

        #button_bg = '#3b5998'
        #button_fg = '#91cfff'

        #num_disp_bg, num_disp_fg, button_bg, button_fg = self._palettes[0]

        self.running_num = 0
        self.new_num = 0

        self.num_display_frame = tk.Frame(master)
        buttons_frame = tk.Frame(master)
        self.num_display_frame.pack(side=TOP, fill=X)
        buttons_frame.pack(side=BOTTOM)

        self.num_display = tk.Label(self.num_display_frame, text='0')
        self.num_display.pack(side=RIGHT, ipady=num_display_ipady, ipadx=num_display_ipadx)

        button_row_1 = tk.Frame(buttons_frame, height=row_h, width=row_w, bg='yellow')        # TODO remove color
        button_row_2 = tk.Frame(buttons_frame, height=row_h, width=row_w, bg='orange')        # TODO remove color
        button_row_3 = tk.Frame(buttons_frame, height=row_h, width=row_w, bg='blue')
        button_row_4 = tk.Frame(buttons_frame, height=row_h, width=row_w, bg='green')

        button_row_1.pack_propagate(0)
        button_row_2.pack_propagate(0)
        button_row_3.pack_propagate(0)
        button_row_4.pack_propagate(0)

        button_row_1.pack(side=TOP, fill=X)
        button_row_2.pack(side=TOP, fill=X)
        button_row_3.pack(side=TOP, fill=X)
        button_row_4.pack(side=TOP, fill=X)

        # FRAMES FOR BUTTONS (to control size in pixels)
        # 1, 2, 3, ce
        button_1_frame = tk.Frame(button_row_3, width=button_width)
        button_2_frame = tk.Frame(button_row_3, width=button_width)
        button_3_frame = tk.Frame(button_row_3, width=button_width)
        button_ce_frame = tk.Frame(button_row_3, width=button_width)

        button_1_frame.pack_propagate(0)
        button_2_frame.pack_propagate(0)
        button_3_frame.pack_propagate(0)
        button_ce_frame.pack_propagate(0)

        button_1_frame.pack(side=LEFT, fill=Y)
        button_2_frame.pack(side=LEFT, fill=Y)
        button_3_frame.pack(side=LEFT, fill=Y)
        button_ce_frame.pack(side=LEFT, fill=Y)

        # 4, 5, 6, +, -
        button_4_frame = tk.Frame(button_row_2, width=button_width)
        button_5_frame = tk.Frame(button_row_2, width=button_width)
        button_6_frame = tk.Frame(button_row_2, width=button_width)
        button_minus_frame = tk.Frame(button_row_2, width=button_width)
        button_plus_frame = tk.Frame(button_row_2, width=button_width)

        button_4_frame.pack_propagate(0)
        button_5_frame.pack_propagate(0)
        button_6_frame.pack_propagate(0)
        button_minus_frame.pack_propagate(0)
        button_plus_frame.pack_propagate(0)

        button_4_frame.pack(side=LEFT, fill=Y)
        button_5_frame.pack(side=LEFT, fill=Y)
        button_6_frame.pack(side=LEFT, fill=Y)
        button_minus_frame.pack(side=TOP, fill=Y, expand=1)
        button_plus_frame.pack(side=BOTTOM, fill=Y, expand=1)

        # 7, 8, 9, x, /
        button_7_frame = tk.Frame(button_row_1, width=button_width)
        button_8_frame = tk.Frame(button_row_1, width=button_width)
        button_9_frame = tk.Frame(button_row_1, width=button_width)
        button_mult_frame = tk.Frame(button_row_1, width=button_width, bg='violet')
        button_div_frame = tk.Frame(button_row_1, width=button_width)

        button_7_frame.pack_propagate(0)
        button_8_frame.pack_propagate(0)
        button_9_frame.pack_propagate(0)
        button_mult_frame.pack_propagate(0)
        button_div_frame.pack_propagate(0)

        button_7_frame.pack(side=LEFT, fill=Y)
        button_8_frame.pack(side=LEFT, fill=Y)
        button_9_frame.pack(side=LEFT, fill=Y)
        button_mult_frame.pack(side=TOP, fill=Y, expand=1)
        button_div_frame.pack(side=BOTTOM, fill=Y, expand=1)

        button_0_frame = tk.Frame(button_row_4, width=button_width)
        button_decimal_frame = tk.Frame(button_row_4, width=int(2*button_width))
        button_eq_frame = tk.Frame(button_row_4, width=button_width)

        button_0_frame.pack_propagate(0)
        button_decimal_frame.pack_propagate(0)
        button_eq_frame.pack_propagate(0)

        button_0_frame.pack(side=LEFT, fill=Y)
        button_decimal_frame.pack(side=LEFT, fill=Y)
        button_eq_frame.pack(side=LEFT, fill=Y)

        # BUTTON WIDGETS
        button_1 = tk.Button(button_1_frame, text='1', command=lambda:self.app_num(1))
        button_2 = tk.Button(button_2_frame, text='2', command=lambda:self.app_num(2))
        button_3 = tk.Button(button_3_frame, text='3', command=lambda:self.app_num(3))
        button_ce = tk.Button(button_ce_frame, text='CE', command=self.ce)

        master.bind('1', lambda event: self.app_num(1, event))
        master.bind('2', lambda event: self.app_num(2, event))
        master.bind('3', lambda event: self.app_num(3, event))
        master.bind('<Escape>', lambda event: self.ce(event))

        button_4 = tk.Button(button_4_frame, text='4', command=lambda:self.app_num(4))
        button_5 = tk.Button(button_5_frame, text='5', command=lambda:self.app_num(5))
        button_6 = tk.Button(button_6_frame, text='6', command=lambda:self.app_num(6))
        button_minus = tk.Button(button_minus_frame, text='-', command=self.set_minus)
        button_plus = tk.Button(button_plus_frame, text='+', command=self.set_plus)

        master.bind('4', lambda event: self.app_num(4, event))
        master.bind('5', lambda event: self.app_num(5, event))
        master.bind('6', lambda event: self.app_num(6, event))
        master.bind('-', lambda event: self.set_minus(event))
        master.bind('+', lambda event: self.set_plus(event))

        button_7 = tk.Button(button_7_frame, text='7', command=lambda:self.app_num(7))
        button_8 = tk.Button(button_8_frame, text='8', command=lambda:self.app_num(8))
        button_9 = tk.Button(button_9_frame, text='9', command=lambda:self.app_num(9))
        button_mult = tk.Button(button_mult_frame, text='x', command=self.set_mult)
        button_div = tk.Button(button_div_frame, text='/', command=self.set_div )

        master.bind('7', lambda event: self.app_num(7, event))
        master.bind('8', lambda event: self.app_num(8, event))
        master.bind('9', lambda event: self.app_num(9, event))
        master.bind('/', lambda event: self.set_div(event))
        master.bind('*', lambda event: self.set_mult(event))

        button_0 = tk.Button(button_0_frame, text='0', command=lambda:self.app_num(0))
        button_decimal = tk.Button(button_decimal_frame, text='.', command=lambda:self.set_decimal())
        button_eq = tk.Button(button_eq_frame, text='=', command=self.eq)

        self._all_buttons = [button_0, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_minus, button_plus, button_mult, button_div, button_eq, button_ce, button_decimal]

        master.bind('0', lambda event: self.app_num(0, event))
        master.bind('.', lambda event: self.set_decimal(event))
        master.bind('<Return>', lambda event:self.eq(event))


        button_0.pack(fill=BOTH, expand=1)
        button_decimal.pack(fill=BOTH, expand=1)
        button_eq.pack(fill=BOTH, expand=1)

        button_1.pack(fill=BOTH, expand=1)
        button_2.pack(fill=BOTH, expand=1)
        button_3.pack(fill=BOTH, expand=1)
        button_ce.pack(fill=BOTH, expand=1)

        button_4.pack(fill=BOTH, expand=1)
        button_5.pack(fill=BOTH, expand=1)
        button_6.pack(fill=BOTH, expand=1)
        button_minus.pack(fill=BOTH, expand=1)
        button_plus.pack(fill=BOTH, expand=1)

        button_7.pack(fill=BOTH, expand=1)
        button_8.pack(fill=BOTH, expand=1)
        button_9.pack(fill=BOTH, expand=1)
        button_div.pack(fill=BOTH, expand=1)
        button_mult.pack(fill=BOTH, expand=1)

        self.load_palette(palette=self._palettes[0])
        master.bind("<space>", self.load_palette)

        master.mainloop()

    def load_palette(self, event=None, palette=None):
        different_palette = False
        proposed_palette = (None, None, None, None)
        while not different_palette:
            #display_bg, display_fg, button_bg, button_fg
            proposed_palette = random.choice(self._palettes)
            if proposed_palette != self._current_palette:
                different_palette = True
                self._current_palette = proposed_palette

        display_bg, display_fg, button_bg, button_fg = proposed_palette

        for button in self._all_buttons:
                button.configure(bg=button_bg, fg=button_fg)
        self.num_display.configure(bg=display_bg, fg=display_fg)
        self.num_display_frame.configure(bg=display_bg)


    def app_num(self, num, event=None):
        precision = self.decimal_place
        if not self.new_num:
            self.new_num = 0
        if self.decimal_place > 0:
            self.new_num = self.new_num + (num / (10**self.decimal_place))
            self.decimal_place += 1
        else:
            self.new_num = self.new_num*10 + num
        if self.decimal_place > 0:
            self.num_display['text'] = "{:.{prec}f}".format(self.new_num, prec=precision)
        else:
            self.num_display['text'] = "{}".format(int(self.new_num))

    def eq(self, event=None):

        if self.minus:
            self.running_num = self.running_num - self.new_num
        elif self.plus:
            self.running_num = self.running_num + self.new_num
        elif self.div:
            self.running_num = self.running_num / self.new_num
        elif self.mult:
            self.running_num = self.running_num * self.new_num
        else:
            self.running_num = self.new_num

        self.new_num = None

        self.decimal_place = 0
        if int(self.running_num) == float(self.running_num):
            self.num_display['text'] = str(int(self.running_num))
        else:
            self.num_display['text'] = '{:f}'.format(self.running_num).strip('0')
        self.plus = False
        self.minus = False
        self.div = False
        self.mult = False

    def ce(self, event=None):
        self.running_num = 0
        self.new_num = 0
        self.num_display['text'] = str(self.running_num)
        self.decimal_place = 0
        self.plus = False
        self.minus = False
        self.div = False
        self.mult = False

    def set_decimal(self, event=None):
        if self.decimal_place > 0:
            pass
        else:
            self.decimal_place = 1

    def set_plus(self, event=None):
        if self.plus or self.minus or self.mult or self.div:
            self.eq()
        elif self.new_num:
            self.running_num = self.new_num
            self.new_num = None

        self.decimal_place = 0

        self.plus = True
        self.minus = False
        self.div = False
        self.mult = False

    def set_minus(self, event=None):
        if self.plus or self.minus or self.mult or self.div:
            self.eq()
        elif self.new_num:
            self.running_num = self.new_num
            self.new_num = None

        self.decimal_place = 0

        self.plus = False
        self.minus = True
        self.div = False
        self.mult = False

    def set_div(self, event=None):
        if self.plus or self.minus or self.mult or self.div:
            self.eq()
        elif self.new_num:
            self.running_num = self.new_num
            self.new_num = None

        self.decimal_place = 0

        self.plus = False
        self.minus = False
        self.div = True
        self.mult = False

    def set_mult(self, event=None):
        if self.plus or self.minus or self.mult or self.div:
            self.eq()
        elif self.new_num:
            self.running_num = self.new_num
            self.new_num = None

        self.decimal_place = 0

        self.plus = False
        self.minus = False
        self.div = False
        self.mult = True


run()