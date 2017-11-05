#import json
#from pyfcm import FCMNotification
#from firebase import firebase

#firebase = firebase.FirebaseApplication('https://healthhacks2017-ec6bf.firebaseio.com/', None)
#result = firebase.get('/Clinic', None)
#print (json.dumps(result, indent=2))
#for _, d in result.items():
#        for room_num, values in d.items():
#                if values["temperature"] < 97.4 or values["temperature"] > 99.6:
#                        print("Temperature: " + str(values["temperature"]))
#                        push_service = FCMNotification(api_key="AAAA_RINJFk:APA91bF4wqCoC-rvQ01XXedftgncrjw2RaqbQL9iWIwBhNr948KjQ02flNn5Gud49eOfnuGgQcNR2rH6XnhD1EllE-GpWnT-7DicLVoq2b0xynCFZwVBE0m7IP0I4ItaBlntZL70kUsI")
#                        registration_id = "crWV01AoxHk:APA91bGftkZ70ZPZqaL7yK_lkYMWPHGhSPrZOc9kwvlMSDUk7f4BQ4UV4gRTE7o2fhdaTafgQ745RdcGZpx_djC7GDq9M6MHgQg_Hhx6op4Bq5Ar5wtooblrgj2h6AuZ15xw5GNXacfn"
#                        message_title = "Patient in CRITICAL CONDITION"
#                        message_body = "Patient 1 has an EXTREME Temperature"
#                        rest = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)




#///////////////////////////////////////////////////////

 import json
 from pyfcm import FCMNotification
 from firebase import firebase

 firebase = firebase.FirebaseApplication('https://healthhacks2017-ec6bf.firebaseio.com/', None)
 result = firebase.get('/Clinic', None)
 #print (json.dumps(result, indent=2))
 push_service = FCMNotification(api_key="AAAA_RINJFk:APA91bF4wqCoC-rvQ01XXedftgncrjw2RaqbQL9iWIwBhNr948KjQ02flNn5Gud49eOfnuGgQcNR2rH6XnhD1EllE- \
 GpWnT-7DicLVoq2b0xynCFZwVBE0m7IP0I4ItaBlntZL70kUsI")
 registration_id = "eR55rA8Qb9o:APA91bGomZun8agNZfs2cpgHgR_5VGISxDtW9Mi_T18qMZS7VfkhfUcG6lKItd7LnPxvk3zSIuQ6a-tAtgNw1vSgonKY6ViMum-vxM5m7gteF2qp1KN4a5wRqzqByxizLgWj-A-i_Qwi"

if values["SpO2"] > 0.94:
        print("SpO2: " + str(values["SpO2"]))
        message_title = "Patient 1 in CRITICAL CONDITION"
        message_body = "Patient 1 has high SpO2 levels"

if 0 == values["age"] and  (120 > values["HR"] < 160 or 50 < values["systolic BP"] > 70):
        print("SpO2: " + str(values["SpO2"]))
        message_title = "Patient 1 in CRITICAL CONDITION"
        message_body = "Patient 1 has high SpO2 levels"

elif 0 < values["age"] < 1 and  (80 > values["HR"] < 140 or 70 < values["systolic BP"] > 100):
        print("SpO2: " + str(values["SpO2"]))
        message_title = "Patient 1 in CRITICAL CONDITION"
        message_body = "Patient 1 has high SpO2 levels"

elif 1 <= values["age"] < 3 and  (80 > values["HR"] < 130 or 80 < values["systolic BP"] > 110):
        print("SpO2: " + str(values["SpO2"]))
        message_title = "Patient 1 in CRITICAL CONDITION"
        message_body = "Patient 1 has high SpO2 levels"

elif 3 <= values["age"] <= 5 and (80 > values["HR"] < 120 or 90 < values["systolic BP"] > 110):
        print("SpO2: " + str(values["SpO2"]))
        message_title = "Patient 1 in CRITICAL CONDITION"
        message_body = "Patient 1 has high SpO2 levels"


elif  6 <= values["age"] <= 12 and  (70 > values["HR"] < 110 or 80 <values["systolic BP"]>120):
        print("SpO2: " + str(values["SpO2"]))
        message_title = "Patient 1 in CRITICAL CONDITION"
        message_body = "Patient 1 has high SpO2 levels"


elif 12 < values["age"] and  (55 > values["HR"] < 105 or 110 <values["systolic BP"]>120):
        if 55 > values["HR"] < 105:
            print("Heart Rate: " + str(values["HR"]))
        if 110 < values["systolic BP"] >120:
            print ("Blood Pressure: " + str(values["systolic BP"]))
        message_title = "Patient 1 in CRITICAL CONDITION"
        message_body = "Patient 1 has high SpO2 levels"

rest = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
