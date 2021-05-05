from model import Model
from view import View

class Controller:


    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def button_pressed(self):
        cidade = self.view.city_entry.get()
        estado = self.view.state_combobox.get()
        data = self.view.de.get()
        temp_max = str(self.view.temp_max_entry.get())
        temp_min = str(self.view.temp_min_entry.get())
        self.model.get_latitude(cidade, estado)
        self.model.get_mes(data)
        self.model.get_rt(self.model.latitude, self.model.mes)
        self.view.eto_var.set(str('%.2f' % self.model.calculate(temp_max, temp_min, self.model.rt)))
        self.view.make_result()

    def return_counties_name(self, eventObject):
        lista_cidades = self.model.get_counties_name()
        print(len(lista_cidades))
        for i in lista_cidades:
            self.view.COUNTIES_LIST.append(i)
            print(i)

    def CitySelect(self):
        self.view.make_toplevel_cityentry()

if __name__ == '__main__':
    app = Controller()
    app.main()   