response = [
    {
            'objectName': 'employee',
            'columns': [
                {'hasSensitiveData': False, 'name': 'employee_number','IsProcessed': True},
                {'hasSensitiveData': True, 'name': 'employee_name', 'IsProcessed': True},
                {'hasSensitiveData': True, 'name': 'location', 'IsProcessed': False},
                {'hasSensitiveData': False, 'name': 'ETLDate', 'IsProcessed': False}
                        ]
    },
    {
            'objectName': 'Department',
            'columns': [
                {'hasSensitiveData': True, 'name': 'dept_Number','IsProcessed': False},
                {'hasSensitiveData': True, 'name': 'dept_Name', 'IsProcessed': False},
                {'hasSensitiveData': False, 'name': 'dept_location', 'IsProcessed': True},
                {'hasSensitiveData': False, 'name': 'ETLDate', 'IsProcessed': True}
                    ]
    }
]
dict1={}
for item in response:
    key=item['objectName']
    cols_lst=item['columns']
    res=[]
    for col1 in cols_lst:
        if col1['hasSensitiveData']==True:
            res.append(col1['name'])
    dict1[key]=res
print(dict1,end="\n")
