import pandas as pd
import math


class Model:
    def __init__(self):
        self.latcity_dataframe = pd.read_csv(
            'cidades lat.csv', sep=';', usecols=['id_cidade', 'nome', 'LATITUDE', 'LONGITUDE'], index_col=[0]
            )
        self.rt_dataframe = pd.read_csv('radiacao solar x lat.csv', sep=';', index_col=[0])
        self.cidade = ''
        self.rt = ''
        self.latitude = ''
        self.mes = ''
        self.eto = ''

    def get_latitude(self, cidade, estado):
        cidade_index = self.latcity_dataframe.nome[self.latcity_dataframe.nome == cidade].index.tolist()
        dict_lat = self.latcity_dataframe['LATITUDE'].to_dict()
        self.latitude = dict_lat.get(cidade_index[0])

    def get_mes(self, data):
        data = data.split('/')
        self.mes = data[1]

    def get_rt(self, latitude, mes):
        self.rt_dataframe.columns = ['01','02','03','04','05','06','07','08','09','10','11','12']
        latitude = latitude.replace(',', '.')
        latitude = math.fabs(float(latitude))
        if latitude >= 0 and latitude <2:
            rt_index = 0
        elif latitude >= 2 and latitude < 4:
            rt_index = 2
        elif latitude >= 4 and latitude < 6:
            rt_index = 4
        elif latitude >= 6 and latitude < 8:
            rt_index = 6
        elif latitude >= 8 and latitude < 10:
            rt_index = 8
        elif latitude >= 10 and latitude < 12:
            rt_index = 10
        elif latitude >= 12 and latitude < 14:
            rt_index = 12
        elif latitude >= 14 and latitude < 16:
            rt_index = 14
        elif latitude >= 16 and latitude < 18:
            rt_index = 16
        elif latitude >= 18 and latitude < 20:
            rt_index = 18
        elif latitude >= 20 and latitude < 22:
            rt_index = 20
        elif latitude >= 22 and latitude < 24:
            rt_index = 22
        elif latitude >= 24 and latitude < 26:
            rt_index = 24
        elif latitude >= 26 and latitude < 28:
            rt_index = 26
        elif latitude >= 28 and latitude < 30:
            rt_index = 28
        else:
            rt_index = 30
        dict_rt = self.rt_dataframe[mes].to_dict()
        self.rt = dict_rt.get(rt_index)

    def calculate(self, t_max, t_min, rt):
        rt = rt.replace(',','.')
        rt = float(rt)
        t_max = float(t_max)
        t_min = float(t_min)
        self.eto = (0.0023*rt*((t_max-t_min)**(1/2))*(((t_max+t_min)/2)+17.8))
        print('A evapotranspiração diária é ' + '%.2f' % self.eto + ' mm.')
        return self.eto

    def get_counties_name(self):
        counties_list = []
        for entrada in self.latcity_dataframe['nome']:
            counties_list.append(entrada)
        return counties_list


