# Python Data Structure Extraction Assignment

## Task 1: Nested List Extraction

# List of data
L = ['A', ['BB', ['CCC', 'DDD'], 'EE', ("IIII", "JJJJ", ("KKKKK", "LLLLL")), 'FF'], 'G', 'H']

# Extract BB:
print(L[1][0])

# Extract G:
print(L[2])

# Extract CCC:
print(L[1][1][0])

# Extract ['CCC', 'DDD']:
print(L[1][1])

# Extract IIII:
print(L[1][3][0])

# Extract LLLLL:
print(L[1][3][2][1])

# Extract ("IIII", "JJJJ", ("KKKKK", "LLLLL")):
print(L[1][3])

# Extract ['CCC', 'DDD'], 'EE':
print(L[1][1:3])

# Extract [['CCC', 'DDD'], ("IIII", "JJJJ", ("KKKKK", "LLLLL"))]:
print(L[1][1:4:2])


## Task 2: Dictionary List Extraction

# List of data
listData = [
    {"A": [
        {"1": "a"},
        {"2": "aa"},
        {"3": "aaa"},
        {"3": "aaaa"}
    ]},

    {"B": [
        {"1": "b"},
        {"2": "bb"},
        {"3": "bbb"},
        {"4": "bbbb"}
    ]},

    {"C": [
        {"1": "c"},
        {"2": "cc"},
        {"3": "ccc"},
        {"4": "cccc"}
    ]},

    {"info": {
        "country": "Jordan",
        "city": "Amman",
        "phoneNo": [
            "+962111111111",
            "02123456",
            "12343456"
        ],
        "address": {
            "address1": "Jordan-Amman-str1",
            "address2": "Jordan-Irbid-str5"
        }
    }}
]

# Extract ['A', 'B', 'C']:
print(list(listData[0].keys())[0] + "," + list(listData[1].keys())[0] + "," + list(listData[2].keys())[0])

# Extract 'bbbb':
print(listData[1]["B"][3]["4"])

# Extract [{'1': 'c'}, {'2': 'cc'}, {'3': 'ccc'}]:
print(listData[2]["C"][:3])

# Extract 'Amman':
print(listData[3]["info"]["city"])

# Extract '12343456':
print(listData[3]["info"]["phoneNo"][2])

# Extract ['+962111111111', '02123456']:
print(listData[3]["info"]["phoneNo"][:2])

# Extract 'Jordan-Irbid-str5':
print(listData[3]["info"]["address"]["address2"])


## Task 3: Complex Medical Data Extraction

# List of data
dictPatientsData = {
    "timelines": [
        {
            "date": "2022-08-07T00:00:00",
            "doctorName": "Dr Mahmoud",
            "doctorId": 101034,
            "encounterNumber": 10443,
            "doctorImage": "medical-icon-registration",
            "projectID": 70,
            "projectName": "WebEMR UAT Hospital",
            "clinicId": 1,
            "clinicName": "INTERNAL MEDICINE CLINIC",
            "timeLineEvents": [
                {
                    "eventId": 1,
                    "iconClass": "fa fa-lg fa-stethoscope",
                    "colorClass": "bg-green",
                    "toolTip": "OPD Consultation detail",
                    "isDisabled": False,
                    "consulations": [
                        {
                            "dispalyName": "Episode",
                            "doctorID": 101034,
                            "patientID": 123456,
                            "doctorName": "Dr Mahmoud Hammouri",
                            "appointmentNo": 10443,
                            "episodeID": 220011080,
                            "admissionNo": 0,
                            "appointmentDate": "2022-08-07T00:00:00",
                            "episodeDate": "2022-08-07T00:00:00"
                        }
                    ]
                }
            ]
        },
        {
            "date": "2022-07-31T00:00:00",
            "doctorName": "Dr Mahmoud",
            "doctorId": 101044,
            "encounterNumber": 10424,
            "doctorImage": "medical-icon-registration",
            "projectID": 70,
            "projectName": "WebEMR UAT Hospital",
            "clinicId": 31,
            "clinicName": "PSYCHIATRY",
            "timeLineEvents": [
                {
                    "eventId": 1,
                    "iconClass": "fa fa-lg fa-stethoscope",
                    "colorClass": "bg-green",
                    "toolTip": "OPD Consultation detail",
                    "isDisabled": False,
                    "consulations": [
                        {
                            "dispalyName": "Episode",
                            "doctorID": 101044,
                            "patientID": 123456,
                            "doctorName": "Dr Mahmoud",
                            "appointmentNo": 10424,
                            "episodeID": 220011072,
                            "admissionNo": 0,
                            "appointmentDate": "2022-07-31T00:00:00",
                            "episodeDate": "2022-07-31T00:00:00"
                        }
                    ]
                }
            ]
        },
        {
            "date": "2022-07-28T00:00:00",
            "doctorName": "Dr Bahaa",
            "doctorId": 101044,
            "encounterNumber": 10423,
            "doctorImage": "medical-icon-registration",
            "projectID": 70,
            "projectName": "WebEMR UAT Hospital",
            "clinicId": 31,
            "clinicName": "PSYCHIATRY",
            "timeLineEvents": [
                {
                    "eventId": 1,
                    "iconClass": "fa fa-lg fa-stethoscope",
                    "colorClass": "bg-green",
                    "toolTip": "OPD Consultation detail",
                    "isDisabled": False,
                    "consulations": [
                        {
                            "dispalyName": "Episode",
                            "doctorID": 101044,
                            "patientID": 123456,
                            "doctorName": "Dr Bahaa",
                            "appointmentNo": 10423,
                            "episodeID": 220011072,
                            "admissionNo": 0,
                            "appointmentDate": "2022-07-28T00:00:00",
                            "episodeDate": "2022-07-28T00:00:00"
                        }
                    ]
                }
            ]
        },
        {
            "date": "2022-06-02T00:00:00",
            "doctorName": "Dr Mahmoud",
            "doctorId": 101034,
            "encounterNumber": 10057,
            "doctorImage": "medical-icon-registration",
            "projectID": 70,
            "projectName": "WebEMR UAT Hospital",
            "clinicId": 1,
            "clinicName": "INTERNAL MEDICINE CLINIC",
            "timeLineEvents": [
                {
                    "eventId": 1,
                    "iconClass": "fa fa-lg fa-stethoscope",
                    "colorClass": "bg-green",
                    "toolTip": "OPD Consultation detail",
                    "isDisabled": False,
                    "consulations": [
                        {
                            "dispalyName": "Episode",
                            "doctorID": 101034,
                            "patientID": 123456,
                            "doctorName": "Dr Mahmoud",
                            "appointmentNo": 10057,
                            "episodeID": 220011057,
                            "admissionNo": 0,
                            "appointmentDate": "2022-06-02T00:00:00",
                            "episodeDate": "2022-06-02T00:00:00"
                        }
                    ]
                }
            ]
        }
    ]
}

# Extract ['date', 'doctorName', 'doctorId', 'encounterNumber', 'doctorImage']:
print(list(dictPatientsData["timelines"][0].keys())[:5])

# Extract Dr Mahmoud Hammouri:
print(dictPatientsData["timelines"][0]["timeLineEvents"][0]["consulations"][0]["doctorName"])