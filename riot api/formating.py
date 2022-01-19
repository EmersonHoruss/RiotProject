# This module is about format from json to excel converting
# all nested values in not neted values

from os import name
from typing import Dict, List
from myConsole import printProgressBar, report
import time

constanstKeys = {
    "info_participants": "participantId",
    "info_teams": "teamId",
    "none": "",
}


def castToString(item: str) -> str:
    return item if type(item) is str else str(item)
    pass


def listItemsToString(list: List) -> List:
    copiedList = list.copy()
    for index, item in enumerate(copiedList):
        copiedList[index] = castToString(item)
        pass
    return copiedList
    pass


def formatList(list: List) -> str:
    """"
    Goal: format a list. Each value is casted to str and separated by '\n' 
    Parameters: List with native values except for list or dict
    Return: str
    Exceptions: dosen't contain error manager
    """
    format = ""
    castedItemsListToString = listItemsToString(list)
    for index, item in enumerate(castedItemsListToString):
        strItem = castToString(item)
        format = format + strItem
        if index != len(list) - 1:
            format = format + "\n"

    return format
    pass


def isDict(item: any) -> bool:
    return True if isinstance(item, Dict) else False


def getKeyFormat(keyOut: str, keyIn: str, separator: str = "_") -> str:
    return keyOut + separator + keyIn
    pass


def addItemInDict(keyOut: str, valueOut: Dict, format: Dict):
    for keyIn, valueIn in valueOut.items():
        keyFormat = getKeyFormat(keyOut, keyIn)
        format[keyFormat] = valueIn
        pass
    pass


# item is key and value of a dict
def formatDictInDict(dict: Dict) -> Dict:
    """"
    Goal: format a dict in a dict in the way to make pair key value dict's child
    in a pair key dict's parent
    Parameters: dict
    Return: dict
    Exceptions: dosen't contain error manager
    """
    format = {}
    for key, value in dict.items():
        if isDict(value):
            addItemInDict(key, value, format)
        else:
            format[key] = value
        pass
    return format
    pass


def defineName(nameParameter: str = "none") -> str:
    for key, value in constanstKeys.items():
        if key == nameParameter:
            return value
        pass
    return nameParameter
    pass


def noneName(nameParameter: str = "") -> str:
    return nameParameter if nameParameter != "" else "none"


def mngName(nameParameter: str = "") -> str:
    nameSemiReady = noneName(nameParameter)
    nameReady = defineName(nameSemiReady)
    return nameReady


def getValueOfName(nameParameter: str, dict: Dict) -> str:
    for index, value in dict.items():
        if index == nameParameter:
            return castToString(value)
        pass
    return ""
    pass


def getRootKeyList(nameReady: str, valueOfName: str) -> str:
    nameConstructed = getKeyFormat(nameReady, valueOfName)
    return nameConstructed
    pass


# nameReady + _ + valueOfName
def formatDictInList(list: List, nameList: str = "") -> Dict:
    """"
    Goal: format dict in list. Each dict needs to have an attribute wich serve
    to construct name of each new pair key value. The name's attribute is
    in constantsKeys and its get it by a name wich is nameList.
    Parameters: list as List with just dicts into and nameList as str
    Return: Dict with pair values of the each dumped dict
    Exceptions: dosen't contain error manager
    """
    dict = {}
    # print(list, nameList)
    for index, item in enumerate(list):
        nameReady = mngName(nameList)
        valueOfName = getValueOfName(nameReady, item)
        # print(nameReady, type(nameReady), valueOfName, type(valueOfName))

        rootKey = getRootKeyList(nameReady, valueOfName)
        addItemInDict(rootKey, item, dict)
        # print(index, item, nameReady, valueOfName, rootKey)
        pass
    return dict
    pass


# validator
def validateForJustList(possibleJustList: any) -> bool:
    """"
    Goal: Validate a list just dosen't contain dict or list
    Parameters: any kind of data
    Return: bool
    Exceptions: dosen't contain error manager
    """
    if isinstance(possibleJustList, List):
        for item in possibleJustList:
            if isinstance(item, Dict) or isinstance(item, List):
                return False
        return True
    return False
    pass


def validateForDictInDict(possibleDictInDict: any) -> bool:
    """"
    Goal: Valida a dict containe at least other dict
    Parameters: any kind of data
    Return: bool
    Exceptions: dosen't contain error manager
    """
    if isinstance(possibleDictInDict, Dict):
        for index in possibleDictInDict:
            value = possibleDictInDict[index]
            if isinstance(value, Dict):
                return True
        pass

    return False
    pass


def validateForDictInList(possibleDictInList: any) -> bool:
    """"
    Goal: validate that a list just containe only lists or only dicts
    Parameters: any kind of data
    Return: bool
    Exceptions: dosen't contain error manager
    """
    if isinstance(possibleDictInList, List):
        for item in possibleDictInList:
            if not isinstance(item, Dict):
                return False
        pass
        return True
    return False
    pass


def lookerForJustList(possibleJustList: any) -> str:
    if isinstance(possibleJustList, Dict):
        for index in possibleJustList:
            value = possibleJustList[index]
            if isinstance(value, List):
                for item in value:
                    if isinstance(item, Dict) or isinstance(item, List):
                        return ""
                return index
    return ""

    pass


def lookerForDictInDict(possibleDictInDict: any) -> str:
    if isinstance(possibleDictInDict, Dict):
        for index in possibleDictInDict:
            value = possibleDictInDict[index]
            if isinstance(value, Dict):
                return index
        pass

    return ""
    pass


def lookerForDictInList(possibleDictInList: any) -> str:
    if isinstance(possibleDictInList, Dict):
        for index in possibleDictInList:
            value = possibleDictInList[index]
            if isinstance(value, List):
                for item in value:
                    if not isinstance(item, Dict):
                        return ""
                return index
    return ""
    pass


def goNext(possibleStop: any) -> bool:
    # print(lookForJustList(possibleStop), lookForDictInDict(possibleStop), lookForDictInList(possibleStop))
    return (
        bool(lookerForJustList(possibleStop))
        or bool(lookerForDictInDict(possibleStop))
        or bool(lookerForDictInList(possibleStop))
    )

    pass


def handleLookers(value: Dict) -> Dict:
    key = lookerForJustList(value)
    if key:
        value[key] = formatList(value[key])
        return value

    key = lookerForDictInDict(value)
    if key:
        return formatDictInDict(value)

    key = lookerForDictInList(value)
    if key:
        value[key] = formatDictInList(value[key], key)
        return value

    return {}
    pass


def formatOneItem(oneItem: Dict) -> Dict:
    fakeItem = {"fakeItemKey": oneItem}

    for key in fakeItem:
        value = fakeItem[key]
        go = goNext(value)
        while go:
            value = handleLookers(value)
            go = goNext(value)
        fakeItem = value
    return fakeItem


def mainFormating(data: List) -> List:
    formatedData = []
    total = len(data)
    prefix = "Formated items: "
    suffix = "Done"
    startProcess = time.time()
    printProgressBar(0, total, prefix, suffix)
    for index, item in enumerate(data):
        printProgressBar(index + 1, total, prefix, suffix)
        formatedData.append(formatOneItem(item))
    endProcess = time.time()
    spendTime = endProcess - startProcess
    report(
        spendTime,
        total,
        cantChar=30,
        msgTime="Spend time is: ",
        msgData="Total data processed: ",
    )
    return formatedData


# xd = time.gmtime()
# print(xd.tm_)
