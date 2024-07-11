# from django.test import TestCase

import firebase_admin
from firebase_admin import credentials, firestore
import json
import requests
# Create your tests here.

def downloadDataFromFirestore(firebase_credentials_path: str) -> dict:
    cred = credentials.Certificate(firebase_credentials_path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    collections = db.collections()
    data_dict = {}
    for collection in collections:
        collection_data = {}
        print("Collection ID:", collection.id)
        documents = collection.stream()
        for doc in documents:
            print(f"\t - Document ID: {doc.id}")
            doc_data = {}
            doc_data = doc.to_dict()
            subcollections = doc.reference.collections()
            for subcollection in subcollections:
                print(f"\t\t - SubCollection ID: {subcollection.id}")
                docs_in_subcollection = subcollection.stream()
                subcollection_docs_data = {}
                for sub_doc in docs_in_subcollection:
                    print(f"\t\t\t - SubCollection Document ID: {sub_doc.id}")
                    subcollection_docs_data[sub_doc.id] = sub_doc.to_dict()
                doc_data[subcollection.id] = subcollection_docs_data
            collection_data[doc.id] = doc_data
        data_dict[collection.id] = collection_data
    return data_dict

def uploadDataToFirestore(firebase_credentials_path: str, data_dict: str) -> None:
    cred = credentials.Certificate(firebase_credentials_path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    for collection_id, collection_data in data_dict.items():
        print("Collection ID:", collection_id)
        collection_ref = db.collection(collection_id)
        for doc_id, doc_data in collection_data.items():
            print(f"\t - Document ID: {doc_id}")
            doc_ref = collection_ref.document(doc_id)
            doc_ref.set(doc_data)
            for subcollection_id, subcollection_data in doc_data.items():
                if isinstance(subcollection_data, dict):
                    print(f"\t\t - SubCollection ID: {subcollection_id}")
                    subcollection_ref = doc_ref.collection(subcollection_id)
                    for sub_doc_id, sub_doc_data in subcollection_data.items():
                        print(f"\t\t\t - SubCollection Document ID: {sub_doc_id}")
                        sub_doc_ref = subcollection_ref.document(sub_doc_id)
                        sub_doc_ref.set(sub_doc_data)

def getData(firebase_credentials_path: str, data_path: str) -> dict: # e.g. data_path : "collection/document/sub_collection/sub_collection_document + /field_name"
    is_content = False
    cred = credentials.Certificate(firebase_credentials_path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    tmp = data_path.split('/')
    while "" in tmp: tmp.remove("")
    if len(tmp) % 2 == 1:
        is_content = True
        content_path = tmp[-1]
        tmp = tmp[:-1]
    doc_path = "/".join(tmp)
    print(doc_path)
    doc_ref = db.document(doc_path)
    doc = doc_ref.get()
    if is_content:
        print(doc.to_dict())
        content = doc.to_dict().get(content_path)
        return {'content': content}
    else:
        return doc.to_dict()
    
FIREBASE_CREDENTIALS_PATH = "./serviceAccountKey.json"   

# with open("./backup.json", 'w') as json_file:
#     json.dump(downloadDataFromFirestore(FIREBASE_CREDENTIALS_PATH), json_file)
with open("./backup.json", 'r') as json_file:
    data_dict = json.load(json_file)

user_path = 'http://127.0.0.1:8000/api/user/'
approveusers = data_dict['ApprovedUsers']
kakao = data_dict['KAKAO']
users = data_dict['Users']
pendingusers = data_dict['PendingUsers']
usercollections = data_dict['UserCollection']

uid_dict = {
    '3277957562': '2021040031',
    '3330817225': '2017037015',
    '3331519082': '2020038043',
    '3332230053': '2021084050',
    '3341293504': '2019037023',
    '3351288104': '2020038016',
    '3385482930': '2021040039',
}

# for user in kakao:
#     user_data = kakao[user]
#     for usercollection in usercollections:
#         if usercollections[usercollection]["name"] == user:
#             user_data['birth_date'] = usercollections[usercollection]['birth']
#     for approveuser in approveusers:
#         if "name" in approveusers[approveuser].keys() and "studentId" in approveusers[approveuser].keys():
#             if approveusers[approveuser]['name'] == user_data['nickname']:
#                 user_data['student_id'] = approveusers[approveuser]['studentId']
#     # if 'birth_date' not in user_data.keys():
#     user_data['birth_date'] = "2000-01-01"
#     if user_data['fcmToken'] == None:  user_data['fcmToken'] = "None"
#     user_model = {
#         "student_id":user_data['student_id'],
#         "name":user_data['nickname'],
#         "fcm_token":user_data['fcmToken'],
#         "birth_date":user_data['birth_date']
#     }
#     print(user_model)
#     response = requests.post(url = user_path, json=user_model)
#     print(response.text)

attendance_path = 'http://127.0.0.1:8000/api/attendancelist/'

def timeParsing(time: str):
    if time[-2] == 'P':
        timelist = time[:-3].split(':')
        timelist[0] = str(int(timelist[0]) + 12)
        time = timelist[0] + ':' + timelist[1]
    return time

# for uid in users:
#     attendancelist = {
#         'student_id' : uid_dict[uid],
#         'date': '',
#         'time': ''
#     }
#     attendance = users[uid]['attendanceList']
#     for date in attendance:
#         data = attendance[date]
#         attendancelist['date'] = data['date']
#         if 'time' in data.keys():
#             attendancelist['time'] = timeParsing(data['time'])
#         else:
#             attendancelist['time'] = None
#         print(attendancelist)
#         response = requests.post(url = attendance_path, json=attendancelist)
#         print(response)

#### Header -> access Token ####
# Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
