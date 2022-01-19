import json
from os import write
from typing import Dict

import pandas as pd


def dumpsJson(data: any) -> str:
    return json.dumps(data)
    pass


def joinNameWithExtensionFile(nameFile: str, extensionFile: str):
    return nameFile + "." + extensionFile
    pass


def getData(fileName: str):
    with open(fileName) as file:
        return json.load(file)
    pass


def generateJsonFile(data: any, fileReady: str):
    dataStr = dumpsJson(data)
    with open(fileReady, "w") as file:
        file.write(dataStr)
    pass


def deleteJsonFile(nameFile: str):
    pass


# save data in json format
def saveDataJson(data: any, nameFile: str):
    fileReady = joinNameWithExtensionFile(nameFile, "json")
    dataStr = dumpsJson(data)
    with open(fileReady, "w") as file:
        file.write(dataStr)
    pass


# save data in json and xlsx format
def saveDataJsonXlsx(data: any, nameFile: str):
    fileReadyXlsx = joinNameWithExtensionFile(nameFile, "xlsx")
    fileReadyJson = joinNameWithExtensionFile(nameFile, "json")

    generateJsonFile(data, fileReadyJson)
    df_json = pd.read_json(fileReadyJson)
    df_json.to_excel(fileReadyXlsx)
    pass


# save data in xlsx format
def saveDataXlsx(nameFile: str):
    fileReadyXlsx = joinNameWithExtensionFile(nameFile, "xlsx")
    fileReadyJson = joinNameWithExtensionFile(nameFile, "json")
    df_json = pd.read_json(fileReadyJson)
    df_json.to_excel(fileReadyXlsx)
    pass


# df_json = pd.read_json('deleteme2.json')
# df_json.to_excel('deleteme6.xlsx')
