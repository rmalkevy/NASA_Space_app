from .query import *
from .clients import Clients
from django.views import View
from collections import OrderedDict
from django.http import JsonResponse, HttpResponse, HttpResponseServerError

import logging
import copy

class getMaps(View):
    def get(self, request):
        maps = {}
        response = requestServer.query.cmx("https://cisco-cmx.unit.ua/api/config/v1/maps/floor/list")
        listMaps = response.json()
        for map in range(len(listMaps)):
            campus, claster, nameFloor = listMaps[map].split(">")
            mapInfo = requestServer.query.cmx("https://cisco-cmx.unit.ua/api/config/v1/maps/info/" + campus + "/" + claster + "/" + nameFloor)
            maps[nameFloor] = {'dimension': mapInfo.json()['dimension']}
            maps[nameFloor]['img'] = mapInfo.json()['image']
            maps[nameFloor]['img']['url'] = "queries/getImageFloor?nameImage=" + mapInfo.json()['image']['imageName']
            Clients.clients[nameFloor] = {'clients': {}, 'countClients': ""}
        return JsonResponse(OrderedDict(sorted(maps.items())))


class getUsersByFloor(View):
    def __init__(self):
        self.retClients = {'clients': {}, 'countClients': ""}
    def get(self, request):
        self.data = request.GET
        if 'nameFloor' in self.data:
            listMaps = requestServer.query.cmx("https://cisco-cmx.unit.ua/api/config/v1/maps/floor/list").json()
            for map in range(len(listMaps)):
                campus, claster, nameFloor = listMaps[map].split(">")
                if (self.data['nameFloor'] == nameFloor):
                    listAllClients = requestServer.query.cmx("https://cisco-cmx.unit.ua/api/location/v2/clients").json()
                    for client in listAllClients:
                        if (client['mapInfo']['mapHierarchyString'].find(listMaps[map]) != -1):
                            macAddress = client['macAddress']
                            if macAddress in Clients.clients[nameFloor]['clients']:
                                self.retClients['clients'][macAddress] = {'mapCoordinate': client['mapCoordinate']}
                                self.retClients['clients'][macAddress]['new'] = False
                            else:
                                self.retClients['clients'][macAddress] = {'mapCoordinate': client['mapCoordinate']}
                                self.retClients['clients'][macAddress]['new'] = True
                            self.retClients['clients'][macAddress]['ipAddress'] = client['ipAddress']
                            self.retClients['clients'][macAddress]['ssId'] = client['ssId']
                    self.retClients['countClients'] = len(self.retClients['clients'])
                    self.retClients['clients'] = OrderedDict(sorted(self.retClients['clients'].items(), key=lambda t: t[1]['new'], reverse=True))
                    Clients.clients[nameFloor] = self.retClients
                    return JsonResponse(self.retClients)
        else:
            logging.error("Wrong Data recived in getUsersByFloor query!!! Data = %s", self.data)
            return HttpResponseServerError()

class getImageFloor(View):
    def get(self, request):
        if 'nameImage' in request.GET:
            self.img = request.GET['nameImage']
            return HttpResponse(requestServer.query.cmx("https://cisco-cmx.unit.ua/api/config/v1/maps/imagesource/" + self.img).content, content_type="image/jpeg")
        else:
            logging.error("getImageFloor get data = %s ! This data have wrong patern", request.GET)
            return HttpResponseServerError()
