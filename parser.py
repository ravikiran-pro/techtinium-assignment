import json 

def ParsingRegionalData(machine_data,totalcost,Machines,RegionName):
	"""Formatting regional result"""
	machine_count=[]
	for i in range(len(machine_data)-1,-1,-1):
		if machine_data[i] is not 0:
			machine_count.append((Machines[i],machine_data[i]))

	RegionalOutput={"region":RegionName}
	RegionalOutput["totalcost"],RegionalOutput["Machines"]=totalcost,machine_count
	return(json.dumps(RegionalOutput, indent=4))


def ParsingOutputData(Output):
	"""Formatting output to match sample output format"""
	Output="{"+'"output"'+":["+Output[:-1]+"]}"
	Output=json.loads(Output)
	Output=json.dumps(Output, indent=4)
	print(Output)
	#Writting Results to file
	with open("results.json","w") as Obj:
		Obj.write(Output)
	Obj.close()
