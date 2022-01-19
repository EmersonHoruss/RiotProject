# This module is about getting raw data of summoners' matches in json format

from typing import Any, Dict, List
import requests


# CONSTANTS
TOKEN: Dict = {"X-Riot-Token": ""}
PARAMS_ENTRIES: Dict = {"queue": "RANKED_SOLO_5x5", "tier": "DIAMOND", "division": "I"}
QUERY_PARAMS_MATCH: Dict = {"start": 0, "count": 1, "queue": 420, "type": "ranked"}
NUM_SUMMONERS: int or None = 2

SET_CONSTANTS: Dict = {
    "TOKEN": TOKEN,
    "PARAMS_ENTRIES": PARAMS_ENTRIES,
    "QUERY_PARAMS_MATCH": QUERY_PARAMS_MATCH,
    "NUM_SUMMONERS": NUM_SUMMONERS,
}

# FUNCTIONS
def getLeagueEntries(token: Dict, params: Dict or None = None,) -> Any:
    url = f'https://la2.api.riotgames.com/lol/league/v4/entries/{params["queue"]}/{params["tier"]}/{params["division"]}'
    res = requests.get(url, headers=token)
    return res.json()


def getSummonerByName(token: Dict, summonerName: str) -> Any:
    url = (
        "https://LA2.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
        + summonerName
    )
    res = requests.get(url, headers=token)
    return res.json()


def getSummonerById(token: Dict, summonerId: str) -> Any:
    url = "https://LA2.api.riotgames.com/lol/summoner/v4/summoners/" + summonerId
    res = requests.get(url, headers=token)
    return res.json()


def getListIdsMatchesByPuuid(
    token: Dict, puuidSummoner: str, queryParams: Dict or None = None
) -> Any:
    url = (
        "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"
        + puuidSummoner
        + "/ids"
    )
    res = requests.get(url, headers=token, params=queryParams)
    return res.json()


def getMatchByIdMatch(token: Dict, matchId: str) -> Any:
    url = "https://americas.api.riotgames.com/lol/match/v5/matches/" + matchId
    res = requests.get(url, headers=token)
    return res.json()


# HELPERS OF HELPERS FUNCTIONS
def validateSizeListPuuids(entries: List, size: int or None) -> int:
    return entries if not isinstance(size, int) else entries[:size]


# HELPERS FUNCTIONS TO MAIN FUNCTION
def getListPuuids(
    token: Dict, paramsEntries: Dict or None = None, size: int or None = None
) -> List:
    try:
        entries = validateSizeListPuuids(getLeagueEntries(token, paramsEntries), size)
        listPuuids = []
        i = 1
        for entry in entries:
            entryDetails = getSummonerById(token, entry["summonerId"])
            puuidEntry = entryDetails["puuid"]
            listPuuids.append(puuidEntry)
            print("Listas Puuids obtenidos: ", i)
            i += 1

        return listPuuids
    except ValueError:
        return [ValueError]


def getListIdsMatches(token: str, queryParamsMatches: Dict, listPuuids: List) -> List:
    try:
        listIdsMatches = []
        i= 1
        for puuid in listPuuids:
            idsMatches = getListIdsMatchesByPuuid(token, puuid, queryParamsMatches)
            for idMatch in idsMatches:
                listIdsMatches.append(idMatch)
            print("Listas de Ids Matches obtenidos: ", i)
            i+=1
        return listIdsMatches
    except ValueError:
        return [ValueError]


def getListMatches(token: Dict, listIdsMatches: List) -> List:
    try:
        listMatches = []
        i = 1
        for idMatch in listIdsMatches:
            match = getMatchByIdMatch(token, idMatch)
            listMatches.append(match)
            print("Registros obtenidos: ", i)
            i+=1
        return listMatches
    except ValueError:
        return [ValueError]


# MAIN FUNCTION
def mainExtracting(
    token: Dict, paramsEntries: Dict, queryParamsMatch: Dict, numSummoners: int or None
) -> List:
    listPuuids = getListPuuids(token, paramsEntries, numSummoners)
    listIdsMatches = getListIdsMatches(token, queryParamsMatch, listPuuids)
    listMatches = getListMatches(token, listIdsMatches)
    return listMatches


# print(main(TOKEN, PARAMS_ENTRIES, QUERY_PARAMS_MATCH, NUM_SUMMONERS))

