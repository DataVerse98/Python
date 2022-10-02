thisisalist = [0] * 10

#ask for user input for how many station and leg
totStation = int(input("Insert Total Station: "))
leg = int(input("Insert Legs(How Far one station can go): "))

#list1 = []
stationList = [] * totStation
#function that will insert the data/element of the dictionary to the list
def insertInput(stLen):
    sList = [] * stLen
    for i in range(0,stLen):
        ArrDeparList = [] * 10
        station = {
            'statNum' : 0,
            'destination' : 0,
            'ArrivalDepartureStation' : thisisalist
        }
        station['statNum'] = (i+1)
        ArrDeparList.insert(0,(i+1))
        
        station['ArrivalDepartureStation'] = ArrDeparList
        print('Insert The Next Station After Station ' + str((i+1)))
        nxtStation = int(input())
        station['destination'] = nxtStation
        sList.insert(i,station)

    return sList
#assign function call insertInput to the stationList
stationList = insertInput(totStation)


#function that will update the value of the ArrivalDepartureStation in the dictionary based on the leg
def updateADS(st1,stList):
    stNum = st1['statNum']
    d = st1['destination']
    thisisalist = [0] * 10
    k = 0;
    while k<leg:
        station2 = {
            'statNum' : 0,
            'destination' : 0,
            'ArrivalDepartureStation' : thisisalist
        }
        stn2 = stList[d-1]['statNum']
        dtn2 = stList[d-1]['destination']
        ads2 = stList[d-1]['ArrivalDepartureStation']
        station2.update({'statNum':stn2})
        station2.update({'destination':dtn2})
        station2.update({'ArrivalDepartureStation':ads2})
        s2ADS = [] * 10
        value = station2['ArrivalDepartureStation']        
        size = len(station2['ArrivalDepartureStation'])
        if size == 1:
            s2ADS.insert(0,value[0])
        elif size > 1:
            for l in range(0,size):
               s2ADS.append(value[l]) 
        s2ADS.append(stNum)
        station3 = {
            'statNum' : 0,
            'destination' : 0,
            'ArrivalDepartureStation' : thisisalist
        }
        stn3 = station2['statNum']
        dtn3  = station2['destination']
        station3.update({'statNum':stn3})
        station3.update({'destination':dtn3})
        station3.update({'ArrivalDepartureStation':s2ADS})
        stList[d-1] = station3
        d = station3['destination']        
        k+=1
    return stList


for j in range(0,totStation):
    station = {
        'statNum' : 0,
        'destination' : 0,
        'ArrivalDepartureStation' : thisisalist
    }
    stn = stationList[j]['statNum']
    dtn = stationList[j]['destination']
    ads = stationList[j]['ArrivalDepartureStation']
    station.update({'statNum':stn})
    station.update({'destination':dtn})
    station.update({'ArrivalDepartureStation':ads})

    #assign function call updateADS to the stationList 
    stationList = updateADS(station,stationList)


counter = [0] * totStation
#function that will simplify the same number of station in the list
def simplify(stationList,lenSt):
    ctr = [0] * totStation
    for m in range(0,lenSt):
        size = len(stationList[m]['ArrivalDepartureStation'])
        count = 0
        setter = [0] * lenSt
        getList = []
        n = 0
        while n < size :
            for p in range(0,lenSt):
                getList = stationList[m]['ArrivalDepartureStation']
                if getList[n] == stationList[p]['statNum']:
                    if setter[p] != 1:
                        setter[p] = 1
                        count+=1
                
            n+=1
        ctr[m] = count
    return ctr

#assign function call simplify to a list named counter
counter = simplify(stationList,totStation)

#function to display output
def displayOutput(ctr,length):
    for x in range(0,length):
        print(ctr[x])

#function call to display output
print("________________________________")
displayOutput(counter,totStation)





