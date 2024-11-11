import json

class account_data():
    def __init__(self, data: dict):
        self.data=data
        data=(json.loads(data['result']))
        self.json=data
        self.localID=data.get('localID')
        self.Name=data.get('Name')
        self.money=data.get('money')
        self.coin=data.get('coin')
        self.flags=data.get('flags')
        self.FriendsID=data.get('FriendsID')
        self.fcar=data.get('fcar')
        self.boughtFsos=data.get('boughtFsos')
        self.floats=data.get('floats')
        self.animations=data.get('animations')
        self.carIDnStatus=self.carGeneratedIDsObj(data=data)
        self.personEquipmentsMale=self.personEquipmentsMaleObj(data=data)
        self.personEquipmentsFemal=self.personEquipmentsFemaleObj(data=data)
        self.platesData=self.platesDataObj(data=data)

    def __str__(self):
        return str(json.loads(self.data['result']))

    class personEquipmentsMaleObj():
        def __init__(self, data: dict):
            data=data.get('personEquipmentsMale')
            self.data=data
            self.json=data
            self.Gender=data.get('Gender')
            self.bag=data.get('bag')
            self.beard=data.get('beard')
            self.cap=data.get('cap')
            self.face=data.get('face')
            self.glasses=data.get('glasses')
            self.gloves=data.get('gloves')
            self.hair=data.get('hair')
            self.mask=data.get('mask')
            self.pants=data.get('pants')
            self.shoes=data.get('shoes')
            self.top=data.get('top')
            self.SelectedEquipments=data.get('SelectedEquipments')

        def __str__(self):
            return str(self.data)

    class personEquipmentsFemaleObj():
        def __init__(self, data: dict):
            data=data.get('personEquipmentsFemale')
            self.data=data
            self.json=data
            self.Gender=data.get('Gender')
            self.bag=data.get('bag')
            self.beard=data.get('beard')
            self.cap=data.get('cap')
            self.face=data.get('face')
            self.glasses=data.get('glasses')
            self.gloves=data.get('gloves')
            self.hair=data.get('hair')
            self.mask=data.get('mask')
            self.pants=data.get('pants')
            self.shoes=data.get('shoes')
            self.top=data.get('top')
            self.SelectedEquipments=data.get('SelectedEquipments')

        def __str__(self):
            return str(self.data)

    class platesDataObj(): 
        def __init__(self, data: dict):
            data=data.get('platesData')
            self.data=data
            self.json=data
            self.allPlates=self.allPlatesObj()
            data_allPlates=data.get('allPlates')
            count=int()

            self.allPlates.append(vinyls=data_allPlates[count].get('vinyls'), plateId=data_allPlates[count].get('plateId'), frontCarId=data_allPlates[count].get("frontCarId"), rearCarId=data_allPlates[count].get('rearCarId'))

        def __str__(self):
            return str(self.data)

        class allPlatesObj():
            def __init__(self):
                self.data=list()
            
            def append(self, vinyls, plateId, frontCarId, rearCarId):
                self.data.append([vinyls, plateId, frontCarId, rearCarId])

            def get(self):
                return self.data

    class carGeneratedIDsObj():
        def __init__(self, data: dict):
            data=data.get('carIDnStatus')
            self.data=data
            self.data=data
            self.carGeneratedIDs=data.get('carGeneratedIDs')
            self.carStatus=data.get('carStatus')
        def __str__(self):
            return str(self.data)

class save_result():
    def __init__(self, data):
        self.result=json.loads(data['result'])['result']
