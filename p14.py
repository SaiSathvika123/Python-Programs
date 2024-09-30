state_details={
                    'AndhraPradesh':{
                                        'capitalcity':'Amaravathi',
                                        'Districts':26
                                    },
                    'Tamilnadu':{
                                    'capitalcity':'Chennai',
                                    'Districts':38
                                },
                    'Karnataka':{
                                    'capitalcity':'Banglore',
                                    'Districts':31
                                }
                }
state=input("Enter the state\n")
values=state_details[state]
print("Capital is",values['capitalcity'])
print("Number of districts are",values['Districts'])
