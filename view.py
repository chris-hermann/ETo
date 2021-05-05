import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date


class View(tk.Tk):

    PAD = 10

    LABELS_LIST = [
        'Selecione o estado: ',
        'Digite o municipio: ', 
        'Selecione o dia: ',
        'Digite a temperatura máxima: ',
        'Digite a temperatura minima: '
    ]

    STATE_LIST = [
        'AC',
        'AL',
        'AP',
        'AM',
        'BA',
        'CE',
        'DF',
        'ES',
        'GO',
        'MA',
        'MT',
        'MS',
        'MG',
        'PA',
        'PB',
        'PR',
        'PE',
        'PI',
        'RJ',
        'RN',
        'RS',
        'RO',
        'RR',
        'SC',
        'SP',
        'SE',
        'TO'
    ]

    COUNTIES_LIST = []

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title('EToCalc1.0')
        self.eto_var = tk.StringVar()
        self._change_style()
        self._make_main_frm()
        self._make_labels()
        self._make_calendar()
        self._make_max_temp_entry()
        self._make_button()
        self._make_topmenus()

    def main(self):
        self.mainloop()

    def _make_main_frm(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_calendar(self):
        self.outer_frm = ttk.Frame(self.main_frm)
        self.outer_frm.grid(row=0, column=1)
        frm = ttk.Frame(self.outer_frm)
        frm.grid()
        self.de = MyDateEntry(frm)
        self.de.pack(pady=self.PAD, padx=self.PAD)

    def _change_style(self):
        style = ttk.Style(self)
        style.theme_use('clam')

    def _make_labels(self):
        frm = ttk.Frame(self.main_frm)
        frm.grid(row=0,column=0)
        i = 0
        for item in self.LABELS_LIST:
            label = ttk.Label(frm, text=item)
            label.grid(row=i, column=0, padx=self.PAD,pady=self.PAD)
            i += 1

    def _make_max_temp_entry(self):
        frm = ttk.Frame(self.outer_frm)
        frm.grid()
        self.temp_max_entry = ttk.Entry(frm)
        self.temp_min_entry = ttk.Entry(frm)
        self.temp_max_entry.pack(padx=self.PAD, pady=self.PAD)
        self.temp_min_entry.pack(padx=self.PAD, pady=self.PAD)

    def _make_button(self):
        frm = ttk.Frame(self.main_frm)
        frm.grid(row=1, column=0, columnspan=2, padx=self.PAD, pady=self.PAD)
        btn = ttk.Button(frm, text='Calcular ETo', command=self.controller.button_pressed)
        btn.pack(padx=self.PAD, pady=self.PAD, fill='x', expand=True)

    def make_result(self):
        frm = ttk.Frame(self.main_frm)
        frm.grid(row=2, column=0, columnspan=2, pady=self.PAD)
        lbl = ttk.Label(frm, text='A evapotranspiração diária é ')
        lbl.pack(side='left')
        eto_result = ttk.Entry(frm, textvariable=self.eto_var, state='readonly', width=8)
        eto_result.pack()

    def _make_topmenus(self):
        self.MenuFather = tk.Menu(self)
        self.config(menu=self.MenuFather)
        MenuCity = tk.Menu(self.MenuFather, tearoff=False)
        self.MenuFather.add_cascade(label='Cidade', menu=MenuCity)
        MenuCity.add_command(label='Definir cidade', command=self.controller.CitySelect)

    def make_toplevel_cityentry(self):
        toplevel = CityEntry()



class MyDateEntry(DateEntry):
    def __init__(self, master):
        DateEntry.__init__(self, master)
        # add black border around drop-down calendar
        self._top_cal.configure(bg='black', bd=1)
        # add label displaying today's date below
        tk.Label(self._top_cal, bg='gray90', anchor='w',
            text='Hoje: %s' % date.today().strftime('%d/%m/%Y')).pack(fill='x')
        self.configure(width=18, locale='pt_BR')
        self.configure(date_pattern='dd/mm/yyyy')

class CityEntry(tk.Toplevel):
    def __init__(self, master):
        self.master = master
        self.main_frm = ttk.Frame(self.master)
        self.main_frm.pack()

