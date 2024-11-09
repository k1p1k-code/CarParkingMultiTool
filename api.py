import requests
from .utils import get_headers
from .exception import AuthError
from .utils import result
from .cptypes import Url_send, Noneheaders
import json


car_ids=[5, 133, 132, 13, 53, 99, 100, 102, 37, 21, 48, 77, 74, 2, 23, 51, 163, 186, 158, 55, 39, 181, 196, 39, 160, 220, 197, 47, 66, 1, 106, 76, 0, 43, 152, 108, 82, 81, 146, 204, 147, 210, 148, 149, 49, 112, 29, 20, 88, 137, 139, 176, 180, 179, 185, 54, 60, 85, 45, 190, 6, 57, 219, 209, 30, 56, 145, 214, 218, 213, 156, 11, 128, 177, 129, 131, 140, 187, 184, 134, 89, 12, 9, 31, 120, 4, 8, 62, 17, 175, 157, 113, 86, 217, 168, 200, 215, 5, 127, 117, 15, 35, 206, 3, 28, 151, 110, 87, 103, 19, 24, 116, 121, 123, 58, 22, 205, 109, 138, 130, 70, 170, 171, 195, 101, 7, 118, 135, 193, 150, 153, 104, 114, 105, 208, 154, 126, 189, 192, 212, 61, 107, 111, 221, 199, 40, 166, 141, 14, 188, 136, 115, 10, 194, 172, 124, 169, 142, 161, 143, 144, 164, 41, 162, 201, 27, 178, 32, 216, 198, 202, 207, 155, 165, 182, 183]

class LoginCarParking():
    def __init__(self, email, password, base_url='https://us-central1-cp-multiplayer.cloudfunctions.net'):
        self.base_url=base_url
        req=self.requests_post(url='/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM',
                                json={"email":email,"password":password,"returnSecureToken":"true"},     
                                base_url='https://www.googleapis.com',
                                headers=Noneheaders
                      )
        
        self.data_auth=req.json()
        if 'error' in dict(req.json()).keys():
            raise AuthError('Login&Password Invalid')
        self.idToken=str(self.data_auth['idToken'])
        self.localId=str(self.data_auth['localId'])
        self.refreshToken=str(self.data_auth['refreshToken'])

        jsonn={"data" : None}
        req=self.requests_post(Url_send.GetPlayerRecords, json=jsonn)
        
        self.json_account=req.json()
        self.data_account=result.account_data(data=req.json())
    
    def requests_post(self, url, json, base_url='', headers=dict()) -> requests.post:
        if not base_url:
            base_url=self.base_url
        if Noneheaders == headers:
            headers=dict()
        elif not headers:
            headers=get_headers(self.idToken, json)

        return requests.post(url=base_url+url,headers=headers,json=json)

    def update(self):
        jsonn={"data" : None}
        req=self.requests_post(Url_send.GetPlayerRecords, json=jsonn)
        self.json_account=req.json()
        self.data_account=result.account_data(data=req.json())

    def delete_account(self):
        jsonn={'data' : None}
        req=self.requests_post(Url_send.deleteAccountOne, jsonn)
        return True

    def get_cars(self):
        jsonn ={"data":None}
        req=self.requests_post(Url_send.TestGetAllCars, json=jsonn)
        car=list()
        req=json.loads(req.json()['result'])
        for i in req:
            car.append(i['CarID'])
        return car

    def hack_money(self, money: int):
        jsonn ={"data":"{\"money\":replace}".replace('replace', str(money))}
        req=self.requests_post(Url_send.SavePlayerRecordsPartially, json=jsonn)
        return result.save_result(data=req.json())

    def hack_coin(self, coin: int):
        jsonn ={"data":"{\"coin\":replace}".replace('replace', str(coin))}
        req=self.requests_post(Url_send.SavePlayerRecordsPartially, json=jsonn)
        return result.save_result(data=req.json())
    

    def unlock_animations(self):
        jsonn ={"data":"{\"animations\":[1,2,3,4,33,34,6,7,13,15,16,27,30,32,35,36,25,26,29,11,12,14,18,24,31,28,37,8,9,10,17,19,20,22,5,21,23,38,39,40,41,42]}"}
        req=self.requests_post(Url_send.SavePlayerRecordsPartially, jsonn)
        return result.save_result(data=req.json())
    
    def unlock_all_cosmetic(self):
        jsonn ={"data":"{\"personEquipmentsMale.Gender\":1,\"personEquipmentsMale.bag\":[0,1,2,3,4],\"personEquipmentsMale.beard\":[6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],\"personEquipmentsMale.cap\":[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35],\"personEquipmentsMale.face\":[2,5],\"personEquipmentsMale.glasses\":[0,1,2,3,4,5,6,7,8,9],\"personEquipmentsMale.gloves\":[0,1,2,3,4,5],\"personEquipmentsMale.hair\":[1,2,6,7,8,9,10,11,12,13,14,15,16,17,18,19],\"personEquipmentsMale.mask\":[3,4,5,6,7,8],\"personEquipmentsMale.pants\":[0,1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],\"personEquipmentsMale.shoes\":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],\"personEquipmentsMale.top\":[2,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67],\"personEquipmentsMale.SelectedEquipments\":[-1,5,20,-1,-1,66,4,2,21,-1,-1],\"personEquipmentsFemale.Gender\":1,\"personEquipmentsFemale.bag\":[0,1,2,3,4],\"personEquipmentsFemale.beard\":[],\"personEquipmentsFemale.cap\":[3,4,5,6,7,8,9,10,11,12,13],\"personEquipmentsFemale.face\":[0],\"personEquipmentsFemale.glasses\":[0,1,2,3,4,5,6,7,8,9],\"personEquipmentsFemale.gloves\":[1],\"personEquipmentsFemale.hair\":[4,7,8,9,10],\"personEquipmentsFemale.mask\":[3,4,5,6],\"personEquipmentsFemale.pants\":[0,2,3,4,5,6,7],\"personEquipmentsFemale.shoes\":[0,3,4,5],\"personEquipmentsFemale.top\":[0,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],\"personEquipmentsFemale.SelectedEquipments\":[10,0,-1,-1,6,0,1,4,6,4,9]}"}
        req=self.requests_post(Url_send.SavePlayerRecordsPartially, jsonn)
        return result.save_result(data=req.json())
    
    def unlock_all_flags(self):
        jsonn ={"data":"{\"flags\":{\"-1\":1,\"0\":1,\"1\":1,\"2\":1,\"3\":1,\"4\":1,\"5\":1,\"6\":1,\"7\":1,\"8\":1,\"9\":1,\"10\":1,\"11\":1,\"12\":1,\"13\":1,\"14\":1,\"15\":1,\"16\":1,\"17\":1,\"18\":1,\"19\":1,\"20\":1,\"21\":1,\"22\":1,\"23\":1,\"24\":1,\"25\":1,\"26\":1,\"27\":1,\"28\":1,\"29\":1,\"30\":1,\"31\":1,\"32\":1,\"33\":1,\"34\":1,\"35\":1,\"36\":1,\"37\":1,\"38\":1,\"39\":1,\"40\":1,\"41\":1,\"42\":1,\"43\":1,\"44\":1,\"45\":1,\"46\":1,\"47\":1,\"48\":1,\"49\":1,\"50\":1,\"51\":1,\"52\":1,\"53\":1,\"54\":1,\"55\":1,\"56\":1,\"57\":1,\"58\":1,\"59\":1,\"60\":1,\"61\":1,\"62\":1,\"63\":1,\"64\":1,\"65\":1,\"66\":1,\"67\":1,\"68\":1,\"69\":1,\"70\":1,\"71\":1,\"72\":1,\"73\":1,\"74\":1}}"}
        req=self.requests_post(Url_send.SavePlayerRecordsPartially, jsonn)
        return result.save_result(data=req.json())
    
    def unlock_all_wheels(self):
        jsonn ={"data":"{\"wheels\":[118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210]}"}
        req=self.requests_post(Url_send.SavePlayerRecordsPartially, jsonn)
        return result.save_result(data=req.json())
    
    def unlock_fcos(self):
        jsonn={"data" : "{\"boughtFsos\": [-1,1,2,3,4]}"}
        req=self.requests.post(Url_send.SavePlayerRecordsPartially, json=jsonn)
        return result.save_result(data=req.json())

    def unlock_car(self, id_car: str):
        jsonn ={"data":"{\"CarID\":replacecar,\"dataVersion\":2,\"vectors\":[{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0},{\"x\":2.0,\"y\":2.0,\"z\":2.0}],\"floats\":[0.0,816.0,5500.0,260.0,1400.0,0.0,0.0,1.0,1.0,68.0,0.22,0.22,40000.0,40000.0,0.0,0.0,0.0,0.0,0.0,0.0,33.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.0,2.0,0.5,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1500.0,1.0,0.0,0.0,68.0,0.0,0.0,0.0,0.0,0.0,0.0],\"gears\":[3.2,1.91,1.53,1.27,0.9,0.6,0.45,5.0],\"typeToInstall\":[-2,-2,-2,-2,-2,-2,-2,-2],\"BoughtParts\":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\"texts\":[\"\",\"\",\"replaceid_replacecarJX335\",\"\"],\"flagID\":-1,\"fsoData\":[-1,0,255,255,255,255,255,255],\"installedPoliceLights\":[-1,-1,-1,-1,-1],\"Vynils\":{\"allVynils\":[],\"CarID\":replacecar}}".replace('replaceid', self.data_account.localID).replace('replacecar', id_car)}
        req=self.requests_post(Url_send.SaveCarsPartially,
                        json=jsonn
                        )
    
    def unlock_all_car(self):
        for i in car_ids:
            self.unlock_car(str(i))



    