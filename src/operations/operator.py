def calculatemaximumValue(dataFrame, column):
    return dataFrame[column].max()

def calculateminimumValue(dataFrame, column):
    return dataFrame[column].min()

def calculateMedia(dataFrame, column):
    return roundNumbers(dataFrame[column].mean(), 2)

def calculateMediana(dataFrame, column):
    return dataFrame[column].median()

def calculateModa(dataFrame, column):
    return dataFrame[column].mode().iloc[0]

def roundNumbers(numberToRound, decimalsValue):
    return round(numberToRound, decimalsValue)