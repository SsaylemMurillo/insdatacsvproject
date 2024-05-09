import pandas as pd
from operations.operator import *

# Global variables
#route_to_file = ''
#dane_file = 'C:/Users/sandr/Documents/UPC/8 Semestre/MODSIM/parcial2/departments.csv'
#dane_mapFile = 'C:/Users/sandr/Documents/UPC/8 Semestre/MODSIM/parcial2/daneMapFile.csv'
#dane_depMapFile = 'C:/Users/sandr/Documents/UPC/8 Semestre/MODSIM/parcial2/mun_dept_codes.csv'


file1 = './data/newFile.csv'
#file2 = './data/newdepartments.csv'
#file3 = './data/newDaneMapFile.csv'

# Only for dengue.csv case
columnsToDelete = ['DANE.year.month', 'Codigo.DANE.periodo', 'Codigo.DANE.year']
newColumnsName = ['dane_code', 'year', 'month', 'period', 'cases_lab', 'cases_all']
# For daneMapFile.csv case
    #columnsToDelete3 = ['Nombre Departamento', 'Nombre Municio']
    #newColumnsMAPCSV = ['department_code',  'municipal_code', 'latitude_municipal', 'longitude_municipal']
# For deparmentsFile.csv case
    #newColumnsDepartamentsCSV = ['department_code', 'name_department', 'municipal_code', 'name_municipal']
# For mun_dept_codes.csv
    # columnsToDeleteDeptCodes = ['Nombre']
    # newColumnsDeptCodes = ['id', 'latitude_departament', 'longitude_department']


# Methods
def main_operations(fileRoute):
    route_to_file = fileRoute
    dataFrame1 = pd.read_csv(route_to_file)
    #dataFrame2 = pd.read_csv(dane_file)
    #dataFrame3 = pd.read_csv(dane_mapFile)
    #dataFrame4 = pd.read_csv(dane_depMapFile)
    
    # Removing unnecesary column data
    newDataFrame1 = remove_columns(columnsToDelete=columnsToDelete, dataFrame=dataFrame1)
    
    # Renaming columns of main file
    rename_columns(newColumnsName=newColumnsName, dataFrame=newDataFrame1)
    
    # Adding a unique id for main file
    add_unique_id(dataFrame=newDataFrame1)
    
    # Renaming columns of departments/municipal data
        #rename_columns(newColumnsName=newColumnsDepartamentsCSV, dataFrame=dataFrame2)
    
    # Adding a unique id for departments/municipal data
        #add_unique_id(dataFrame=dataFrame2)
    
    # Creating separate columns for municipal and departament code
    separate_dane_code(newDataFrame1, 'dane_code')
    
    # Removing name of maps data
        #newDataFrame3 = remove_columns(columnsToDelete=columnsToDelete3, dataFrame=dataFrame3)
    
    # Renaming columns of maps data
        #rename_columns(newColumnsName=newColumnsMAPCSV, dataFrame=newDataFrame3)
    
    # Adding a unique id for departments/municipal data
        #add_unique_id(dataFrame=newDataFrame3)
    
    # Replacing municipal code
        #replace_dane_code(newDataFrame3, 'municipal_code')
    
    # Removing name of deps maps data
        #newDataFrame4 = remove_columns(columnsToDelete=columnsToDeleteDeptCodes, dataFrame=dataFrame4)
    # Rename the deps maps data 
        #rename_columns(newColumnsName=newColumnsDeptCodes, dataFrame=newDataFrame4)
        #merged_df = pd.merge(newDataFrame3, newDataFrame4, left_on='department_code', right_on='id', how='left')
    
    export_csv_files(file1, newDataFrame1)
    #export_csv_files(file2, dataFrame2)
    #export_csv_files(file3, merged_df)
    
    cases_all = extract_column(newDataFrame1, 'cases_all')
    cases_lab = extract_column(newDataFrame1, 'cases_lab')
    
    dataFrameCasesAll = cases_all
    dataFrameCasesLab = cases_lab
      
    dictValue = calculateOperationsOnDataFrame(cases_all, 'cases_all')
    dictValue2 = calculateOperationsOnDataFrame(cases_lab, 'cases_lab')
    
    listDict = [dictValue, dictValue2, dataFrameCasesAll, dataFrameCasesLab]
    
    return listDict

def calculateOperationsOnDataFrame(dataFrame, columnName):
    dictionary = {}
    valueCalculated1 = calculateModa(dataFrame, columnName)
    valueCalculated2 = calculateMedia(dataFrame, columnName)
    valueCalculated3 = calculatemaximumValue(dataFrame, columnName)
    valueCalculated4 = calculateminimumValue(dataFrame, columnName)
    valueCalculated5 = calculateMediana(dataFrame, columnName)
    
    dictionary['moda'] = valueCalculated1
    dictionary['media'] = valueCalculated2
    dictionary['mediana'] = valueCalculated5
    dictionary['maximo'] = valueCalculated3
    dictionary['minimo'] = valueCalculated4
    return dictionary

def remove_columns(columnsToDelete, dataFrame):
    newDataFrame = dataFrame.drop(columns=columnsToDelete)
    return newDataFrame

def extract_column(dataFrame, columnName):
    filterColumn = dataFrame[columnName][dataFrame[columnName] != 0]
    return filterColumn.to_frame()

def rename_columns(newColumnsName, dataFrame):
    dataFrame.columns = newColumnsName
    
def add_unique_id(dataFrame):
    dataFrame.insert(0, 'id', range(1, 1 + len(dataFrame)))
    
def add(dataFrame):
    dataFrame.insert(0, 'id', range(1, 1 + len(dataFrame)))
    
def separate_dane_code(dataFrame, columnName):
    # Creating new row to store the municipal_code
    dataFrame['municipal_code'] = dataFrame[columnName].astype(str).str[-3:].astype(int)
    # Creating new row to store the department_code
    dataFrame['department_code'] = dataFrame[columnName].astype(str).str[:-3].astype(int)

def replace_dane_code(dataFrame, columnName):
    dataFrame.loc[:, 'municipal_code'] = dataFrame[columnName].astype(str).str[-3:].astype(int)

def export_csv_files(route, dataFrame):
    dataFrame.to_csv(route, index=False)
