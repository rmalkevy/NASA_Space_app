from django.views import View
from collections import OrderedDict
from django.http import JsonResponse, HttpResponse, HttpResponseServerError

import logging
import copy
import array as arr

class getData(View):
    def __init__(self):
        self.chlorine = list()
        self.water = list()
        self.pottasium = list()
        self.silicon = list()
        self.ferum = list()
        self.retInfo = {}
        self.retInfo["mixed_values"] = list()
        self.retInfo["gradient"] = {}
        self.retInfo["gradient"]["min"] = 1;
        self.retInfo["gradient"]["averange"] = 0;
        self.retInfo["gradient"]["max"] = 0;
        self.cell = {"latitude": "", "longtitude": "", "value": ""}
        self.max_chlorine = 0.797
        self.max_water = 7.398
        self.max_pottasium = 0.561
        self.max_silicon = 22.113
        self.max_ferum = 19.301
    def get(self, request): 
        if 'chlorine' in request.GET:
            self.koef_chlorine = float(request.GET['chlorine'])
            with open("cl_sr_5x5.tab") as f:
                content = f.readlines()
            list_string = list()
            for member in content:
                list_string.append([s.strip() for s in member.splitlines()][0])
            list_data = list()
            for member in list_string:
                list_data.append(member.split())
            for member in list_data:
                if (member[2] != '9999.999'):
                    self.cell_chlorine = copy.deepcopy(self.cell)
                    self.cell_chlorine["longtitude"] = member[1]
                    self.cell_chlorine["latitude"] = member[0]
                    self.cell_chlorine["value"] = (float(member[2]) / self.max_chlorine) * self.koef_chlorine
                    self.chlorine.append(self.cell_chlorine)
        if 'water' in request.GET:
            self.koef_water = float(request.GET['water'])
            with open("h2o_sr_5x5.tab") as f:
                content = f.readlines()
            list_string = list()
            for member in content:
                list_string.append([s.strip() for s in member.splitlines()][0])
            list_data = list()
            for member in list_string:
                list_data.append(member.split())
            for member in list_data:
                if (member[2] != '9999.999'):
                    self.cell_water = copy.deepcopy(self.cell)
                    self.cell_water["longtitude"] = member[1]
                    self.cell_water["latitude"] = member[0]
                    self.cell_water["value"] = (float(member[2]) / self.max_water) * self.koef_water
                    self.water.append(self.cell_water)
        if 'pottasium' in request.GET:
            self.koef_pottasium = float(request.GET['pottasium'])
            with open("k_sr_5x5.tab") as f:
                content = f.readlines()
            list_string = list()
            for member in content:
                list_string.append([s.strip() for s in member.splitlines()][0])
            list_data = list()
            for member in list_string:
                list_data.append(member.split())
            for member in list_data:
                if (member[2] != '9999.999'):
                    self.cell_pottasium = copy.deepcopy(self.cell)
                    self.cell_pottasium["longtitude"] = member[1]
                    self.cell_pottasium["latitude"] = member[0]
                    self.cell_pottasium["value"] = (float(member[2]) / self.max_pottasium) * self.koef_pottasium
                    self.pottasium.append(self.cell_pottasium)
        if 'silicon' in request.GET:
            self.koef_silicon = float(request.GET['silicon'])
            with open("si_sr_5x5.tab") as f:
                content = f.readlines()
            list_string = list()
            for member in content:
                list_string.append([s.strip() for s in member.splitlines()][0])
            list_data = list()
            for member in list_string:
                list_data.append(member.split())
            for member in list_data:
                if (member[2] != '9999.999'):
                    self.cell_silicon = copy.deepcopy(self.cell)
                    self.cell_silicon["longtitude"] = member[1]
                    self.cell_silicon["latitude"] = member[0]
                    self.cell_silicon["value"] = (float(member[2]) / self.max_silicon) * self.koef_silicon
                    self.silicon.append(self.cell_silicon)
        if 'ferum' in request.GET:
            self.koef_ferum = float(request.GET['ferum'])
            with open("fe_sr_5x5.tab") as f:
                content = f.readlines()
            list_string = list()
            for member in content:
                list_string.append([s.strip() for s in member.splitlines()][0])
            list_data = list()
            for member in list_string:
                list_data.append(member.split())
            for member in list_data:
                if (member[2] != '9999.999'):
                    self.cell_ferum = copy.deepcopy(self.cell)
                    self.cell_ferum["longtitude"] = member[1]
                    self.cell_ferum["latitude"] = member[0]
                    self.cell_ferum["value"] = (float(member[2]) / self.max_ferum) * self.koef_ferum
                    self.ferum.append(self.cell_ferum)
        for chlorine in self.chlorine:
            for water in self.water:
                if (water["longtitude"] == chlorine["longtitude"] and water["latitude"] == chlorine["latitude"]):
                    for pottasium in self.pottasium:
                        if (pottasium["longtitude"] == chlorine["longtitude"] and pottasium["latitude"] == chlorine["latitude"]):
                            for silicon in self.silicon:
                                if (silicon["longtitude"] == chlorine["longtitude"] and silicon["latitude"] == chlorine["latitude"]):
                                    for ferum in self.ferum:
                                        if (ferum["longtitude"] == chlorine["longtitude"] and ferum["latitude"] == chlorine["latitude"]):
                                            self.cell_new = copy.deepcopy(self.cell)
                                            self.cell_new["longtitude"] = chlorine["longtitude"]
                                            self.cell_new["latitude"] = chlorine["latitude"]
                                            self.mixed_value = round(chlorine["value"] + water["value"] + pottasium["value"] + silicon["value"] + ferum["value"], 3)
                                            self.cell_new["value"] = self.mixed_value;
                                            if (self.mixed_value > self.retInfo["gradient"]["max"]):
                                                self.retInfo["gradient"]["max"] = self.mixed_value
                                            if (self.mixed_value < self.retInfo["gradient"]["min"]):
                                                self.retInfo["gradient"]["min"] = self.mixed_value                                                
                                            self.retInfo["mixed_values"].append(self.cell_new)
        self.retInfo["gradient"]["averange"] = round((self.retInfo["gradient"]["min"] + self.retInfo["gradient"]["max"]) / 2, 3)
        return JsonResponse(OrderedDict(self.retInfo))
