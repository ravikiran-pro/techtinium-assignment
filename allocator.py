from parser import *
from extractor import *
"""
	tallying to production hours
	[0, 1, 0, 1, 0, 0] -->2hours
	[2, 0, 0, 1, 0, 0] -->3hours
	
"""
def Maximizing_production(marker,Costs,units,totalcost,machine_data,machinehours,expected_hours):
	while(marker<len(machine_data)):
		if(machine_data[marker]!=0):
			break
		marker+=1
	else:
		return machine_data
	totalcost-=Costs[marker]
	machinehours-=1
	machine_data[marker]-=1
	add=0
	while(marker>-1):
		marker-=1
		add+=2
		if(Costs[marker] is not None):
			break
	machine_data[marker]+=add
	machinehours+=add
	totalcost+=Costs[marker]*2
	if(machinehours<expected_hours):
		Maximizing_production(1,Costs,units,totalcost,machine_data,machinehours,expected_hours)
	return machine_data

""" 
	Calculating individual regional data(most minimum cost)
	As cost is sorted proportionally, more the highest unit the cost is less

	for i in range(6,0,-1):
		machine.append(totalunit//units[i]  )
		totalunit/=units[i]

	output << 	machines    m1,m2,m3,m4,m5,m6
				count= 		[1,  1, 1, 0, 1 ,0]

"""
def RegionalResult(capacity,expected_hours,regionName,Machines,Cost,units):
	machine_data=Machines[:]	
	machinehours=0
	totalcost=0
	#Selecting the machines Based on minimal cost
	k=len(units)-1
	for i in range(len(units)-1,-1,-1):
		if (capacity//units[i] is not 0 and Cost[i] is not None):
			machine_data[k]=capacity//units[i]
			machinehours+=(capacity//units[i])
			totalcost+=Cost[i]*(capacity//units[i])
			capacity=capacity%units[i]
		else:
			machine_data[k]=0
		k-=1

	#if production faster than expected
	if machinehours<expected_hours:
		Maximizing_production(1,Costs,units,totalcost,machine_data,machinehours,expected_hours)
	return ParsingRegionalData(machine_data,totalcost,Machines,regionName)


units=(10,20,40,80,160,320)
FileObj=AccessingDataset()
capacity=int(input("enter capacity"))
expected_hours=int(input("enter hours"))
Machines=Extract_MachineData(FileObj)
Output=''
for col in range(1,FileObj.ncols):
	RegionName=FileObj.cell_value(0,col)
	Costs=ExtractRegionalCost(FileObj,col)
	#passing out individual cost to get base cost
	Output+=str(RegionalResult(capacity,expected_hours,RegionName,Machines,Costs,units))+','

ParsingOutputData(Output)

