import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://iloveminor2-3ae9f-default-rtdb.firebaseio.com"
})

ref = db.reference('Students')

data = {
    "123":
        {
            "name": "Atin",
            "major": "CCVT",
            "starting_year": 2021,
            "total_attendance": 1,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1223":
        {
            "name": "Rudraksh Bhatnagar",
            "major": "CCVT",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1235":
        {
            "name": "Shubham Jaiswal",
            "major": "CCVT",
            "starting_year": 2021,
            "total_attendance": 8,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"12466":
        {
            "name": "Parth ",
            "major": "CCVT",
            "starting_year": 2021,
            "total_attendance": 9,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)

