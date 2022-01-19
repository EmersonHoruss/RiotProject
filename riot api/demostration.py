# This modules is about demostrate how works all joined
# step 1: import all modules, specified the main functions, constants and for helperIO just the saveData files
# such us saveDataJsonXlsx or saveDataJson or saveDataXlsx
from extracting import NUM_SUMMONERS, QUERY_PARAMS_MATCH, mainExtracting, SET_CONSTANTS
from formating import mainFormating
from helpersIO import saveDataJson, saveDataJsonXlsx

# step 2: extract data 
extractedData = mainExtracting(
    token=SET_CONSTANTS["TOKEN"],
    paramsEntries=SET_CONSTANTS["PARAMS_ENTRIES"],
    queryParamsMatch=SET_CONSTANTS["QUERY_PARAMS_MATCH"],
    numSummoners=5
)

# step 3: format data if you want to cast json to xlsx file
formatedData = mainFormating(extractedData)

# step 4: save data, in this case we use saveDataJsonXlsx because we want to generate both files, if you
# want use other, remember, just use the casting if you want to save data as xlsx file format, otherwise
# it's unnecesarily
saveDataJsonXlsx(formatedData, "2sums_1match")
# saveDataJson(extractedData, "holaJson")

# so... just try it! and enjoy, go culebrita xd!!!!