# Acessing Dataset file pointer	
def AccessingDataset():
	import xlrd
	workbook=xlrd.open_workbook('dataset/data.xlsx')
	FileObj=workbook.sheet_by_name("Sheet1")
	return FileObj

def Extract_MachineData(FileObj):
	Machines=[]
	for i in range(1,FileObj.nrows):
		Machines.append(FileObj.cell_value(i,0))
	return Machines

"""Extracting Data from dataset Neglecting Non selective units"""
def ExtractRegionalCost(FileObj,col):
	Costs,regionName=[],FileObj.cell_value(0,col)
	Costs.append(int(FileObj.cell_value(1,col)))
	for j in range(2,FileObj.nrows):
		if FileObj.cell_value(j,col) is not '':
			if FileObj.cell_value(j-1,col) is not '':
				if FileObj.cell_value(j-1,col)*2 < FileObj.cell_value(j,col):
					Costs.append(None)
				else:		
					Costs.append(int(FileObj.cell_value(j,col)))
			else:
				Costs.append(int(FileObj.cell_value(j,col)))
		else:
			Costs.append(None)
	return Costs
