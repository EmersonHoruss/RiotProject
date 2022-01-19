import pandas as pd
import operator


diccionario_rename = {
    'info_gameId':'gameId','info_gameDuration':'gameDuration','info_gameMode':'gameMode',
                                      'info_gameType':'gameType','info_mapId':'mapId',
                                      'info_participants_participantId_1_summonerLevel': 'p1_summonerLevel',
                                      'info_participants_participantId_1_championId': 'p1_championId',
                                      'info_participants_participantId_1_championName': 'p1_championName',
                                      'info_participants_participantId_1_champExperience': 'p1_champExperience',
                                      'info_participants_participantId_1_champLevel': 'p1_champLevel',
                                      'info_participants_participantId_1_individualPosition': 'p1_individualPosition',
                                      'info_participants_participantId_1_kills': 'p1_kills',
                                      'info_participants_participantId_1_deaths': 'p1_deaths',
                                      'info_participants_participantId_1_assists': 'p1_assists',
                                      'info_participants_participantId_1_totalMinionsKilled': 'p1_totalMinionsKilled',
                                      'info_participants_participantId_1_firstBloodAssist': 'p1_firstBloodAssist',
                                      'info_participants_participantId_1_firstBloodKill': 'p1_firstBloodKill',
                                      'info_participants_participantId_1_firstTowerAssist': 'p1_firstTowerAssist',
                                      'info_participants_participantId_1_firstTowerKill': 'p1_firstTowerKill',
                                      'info_participants_participantId_1_doubleKills': 'p1_doubleKills',
                                      'info_participants_participantId_1_tripleKills': 'p1_tripleKills',
                                      'info_participants_participantId_1_quadraKills': 'p1_quadraKills',
                                      'info_participants_participantId_1_pentaKills': 'p1_pentaKills',
                                      'info_participants_participantId_1_largestKillingSpree': 'p1_largestKillingSpree',
                                      'info_participants_participantId_1_largestMultiKill': 'p1_largestMultiKill',
                                      'info_participants_participantId_1_baronKills': 'p1_baronKills',
                                      'info_participants_participantId_1_dragonKills': 'p1_dragonKills',
                                      'info_participants_participantId_1_objectivesStolen': 'p1_objectivesStolen',
                                      'info_participants_participantId_1_goldEarned': 'p1_goldEarned',
                                      'info_participants_participantId_1_goldSpent': 'p1_goldSpent',
                                      'info_participants_participantId_1_magicDamageDealt': 'p1_magicDamageDealt',
                                      'info_participants_participantId_1_magicDamageDealtToChampions': 'p1_magicDamageDealtToChampions',
                                      'info_participants_participantId_1_magicDamageTaken': 'p1_magicDamageTaken',
                                      'info_participants_participantId_1_physicalDamageDealt': 'p1_physicalDamageDealt',
                                      'info_participants_participantId_1_physicalDamageDealtToChampions': 'p1_physicalDamageDealtToChampions',
                                      'info_participants_participantId_1_physicalDamageTaken': 'p1_physicalDamageTaken',
                                      'info_participants_participantId_1_trueDamageDealt': 'p1_trueDamageDealt',
                                      'info_participants_participantId_1_totalDamageDealt': 'p1_totalDamageDealt',
                                      'info_participants_participantId_1_totalDamageDealtToChampions': 'p1_totalDamageDealtToChampions',
                                      'info_participants_participantId_1_totalDamageTaken': 'p1_totalDamageTaken',
                                      'info_participants_participantId_1_damageSelfMitigated': 'p1_damageSelfMitigated',
                                      'info_participants_participantId_1_totalDamageShieldedOnTeammates': 'p1_totalDamageShieldedOnTeammates',
                                      'info_participants_participantId_1_totalHeal': 'p1_totalHeal',
                                      'info_participants_participantId_1_totalHealsOnTeammates': 'p1_totalHealsOnTeammates',
                                      'info_participants_participantId_1_damageDealtToBuildings': 'p1_damageDealtToBuildings',
                                      'info_participants_participantId_1_damageDealtToObjectives': 'p1_damageDealtToObjectives',
                                      'info_participants_participantId_1_damageDealtToTurrets': 'p1_damageDealtToTurrets',
                                      'info_participants_participantId_1_nexusKills': 'p1_nexusKills',
                                      'info_participants_participantId_1_nexusLost': 'p1_nexusLost',
                                      'info_participants_participantId_1_turretKills': 'p1_turretKills',
                                      'info_participants_participantId_1_turretsLost': 'p1_turretsLost',
                                      'info_participants_participantId_1_inhibitorKills': 'p1_inhibitorKills',
                                      'info_participants_participantId_1_detectorWardsPlaced': 'p1_detectorWardsPlaced',
                                      'info_participants_participantId_1_wardsKilled': 'p1_wardsKilled',
                                      'info_participants_participantId_1_wardsPlaced': 'p1_wardsPlaced',
                                      'info_participants_participantId_1_gameEndedInEarlySurrender': 'p1_gameEndedInEarlySurrender',
                                      'info_participants_participantId_1_gameEndedInSurrender': 'p1_gameEndedInSurrender',
                                      'info_participants_participantId_1_teamEarlySurrendered': 'p1_teamEarlySurrendered',
                                      'info_participants_participantId_1_teamId': 'p1_teamId',
                                      'info_participants_participantId_1_totalTimeSpentDead': 'p1_totalTimeSpentDead',
                                      'info_participants_participantId_1_win': 'p1_win',
                                      'info_participants_participantId_2_summonerLevel': 'p2_summonerLevel',
                                      'info_participants_participantId_2_championId': 'p2_championId',
                                      'info_participants_participantId_2_championName': 'p2_championName',
                                      'info_participants_participantId_2_champExperience': 'p2_champExperience',
                                      'info_participants_participantId_2_champLevel': 'p2_champLevel',
                                      'info_participants_participantId_2_individualPosition': 'p2_individualPosition',
                                      'info_participants_participantId_2_kills': 'p2_kills',
                                      'info_participants_participantId_2_deaths': 'p2_deaths',
                                      'info_participants_participantId_2_assists': 'p2_assists',
                                      'info_participants_participantId_2_totalMinionsKilled': 'p2_totalMinionsKilled',
                                      'info_participants_participantId_2_firstBloodAssist': 'p2_firstBloodAssist',
                                      'info_participants_participantId_2_firstBloodKill': 'p2_firstBloodKill',
                                      'info_participants_participantId_2_firstTowerAssist': 'p2_firstTowerAssist',
                                      'info_participants_participantId_2_firstTowerKill': 'p2_firstTowerKill',
                                      'info_participants_participantId_2_doubleKills': 'p2_doubleKills',
                                      'info_participants_participantId_2_tripleKills': 'p2_tripleKills',
                                      'info_participants_participantId_2_quadraKills': 'p2_quadraKills',
                                      'info_participants_participantId_2_pentaKills': 'p2_pentaKills',
                                      'info_participants_participantId_2_largestKillingSpree': 'p2_largestKillingSpree',
                                      'info_participants_participantId_2_largestMultiKill': 'p2_largestMultiKill',
                                      'info_participants_participantId_2_baronKills': 'p2_baronKills',
                                      'info_participants_participantId_2_dragonKills': 'p2_dragonKills',
                                      'info_participants_participantId_2_objectivesStolen': 'p2_objectivesStolen',
                                      'info_participants_participantId_2_goldEarned': 'p2_goldEarned',
                                      'info_participants_participantId_2_goldSpent': 'p2_goldSpent',
                                      'info_participants_participantId_2_magicDamageDealt': 'p2_magicDamageDealt',
                                      'info_participants_participantId_2_magicDamageDealtToChampions': 'p2_magicDamageDealtToChampions',
                                      'info_participants_participantId_2_magicDamageTaken': 'p2_magicDamageTaken',
                                      'info_participants_participantId_2_physicalDamageDealt': 'p2_physicalDamageDealt',
                                      'info_participants_participantId_2_physicalDamageDealtToChampions': 'p2_physicalDamageDealtToChampions',
                                      'info_participants_participantId_2_physicalDamageTaken': 'p2_physicalDamageTaken',
                                      'info_participants_participantId_2_trueDamageDealt': 'p2_trueDamageDealt',
                                      'info_participants_participantId_2_totalDamageDealt': 'p2_totalDamageDealt',
                                      'info_participants_participantId_2_totalDamageDealtToChampions': 'p2_totalDamageDealtToChampions',
                                      'info_participants_participantId_2_totalDamageTaken': 'p2_totalDamageTaken',
                                      'info_participants_participantId_2_damageSelfMitigated': 'p2_damageSelfMitigated',
                                      'info_participants_participantId_2_totalDamageShieldedOnTeammates': 'p2_totalDamageShieldedOnTeammates',
                                      'info_participants_participantId_2_totalHeal': 'p2_totalHeal',
                                      'info_participants_participantId_2_totalHealsOnTeammates': 'p2_totalHealsOnTeammates',
                                      'info_participants_participantId_2_damageDealtToBuildings': 'p2_damageDealtToBuildings',
                                      'info_participants_participantId_2_damageDealtToObjectives': 'p2_damageDealtToObjectives',
                                      'info_participants_participantId_2_damageDealtToTurrets': 'p2_damageDealtToTurrets',
                                      'info_participants_participantId_2_nexusKills': 'p2_nexusKills',
                                      'info_participants_participantId_2_nexusLost': 'p2_nexusLost',
                                      'info_participants_participantId_2_turretKills': 'p2_turretKills',
                                      'info_participants_participantId_2_turretsLost': 'p2_turretsLost',
                                      'info_participants_participantId_2_inhibitorKills': 'p2_inhibitorKills',
                                      'info_participants_participantId_2_detectorWardsPlaced': 'p2_detectorWardsPlaced',
                                      'info_participants_participantId_2_wardsKilled': 'p2_wardsKilled',
                                      'info_participants_participantId_2_wardsPlaced': 'p2_wardsPlaced',
                                      'info_participants_participantId_2_gameEndedInEarlySurrender': 'p2_gameEndedInEarlySurrender',
                                      'info_participants_participantId_2_gameEndedInSurrender': 'p2_gameEndedInSurrender',
                                      'info_participants_participantId_2_teamEarlySurrendered': 'p2_teamEarlySurrendered',
                                      'info_participants_participantId_2_teamId': 'p2_teamId',
                                      'info_participants_participantId_2_totalTimeSpentDead': 'p2_totalTimeSpentDead',
                                      'info_participants_participantId_2_win': 'p2_win',
                                      'info_participants_participantId_3_summonerLevel': 'p3_summonerLevel',
                                      'info_participants_participantId_3_championId': 'p3_championId',
                                      'info_participants_participantId_3_championName': 'p3_championName',
                                      'info_participants_participantId_3_champExperience': 'p3_champExperience',
                                      'info_participants_participantId_3_champLevel': 'p3_champLevel',
                                      'info_participants_participantId_3_individualPosition': 'p3_individualPosition',
                                      'info_participants_participantId_3_kills': 'p3_kills',
                                      'info_participants_participantId_3_deaths': 'p3_deaths',
                                      'info_participants_participantId_3_assists': 'p3_assists',
                                      'info_participants_participantId_3_totalMinionsKilled': 'p3_totalMinionsKilled',
                                      'info_participants_participantId_3_firstBloodAssist': 'p3_firstBloodAssist',
                                      'info_participants_participantId_3_firstBloodKill': 'p3_firstBloodKill',
                                      'info_participants_participantId_3_firstTowerAssist': 'p3_firstTowerAssist',
                                      'info_participants_participantId_3_firstTowerKill': 'p3_firstTowerKill',
                                      'info_participants_participantId_3_doubleKills': 'p3_doubleKills',
                                      'info_participants_participantId_3_tripleKills': 'p3_tripleKills',
                                      'info_participants_participantId_3_quadraKills': 'p3_quadraKills',
                                      'info_participants_participantId_3_pentaKills': 'p3_pentaKills',
                                      'info_participants_participantId_3_largestKillingSpree': 'p3_largestKillingSpree',
                                      'info_participants_participantId_3_largestMultiKill': 'p3_largestMultiKill',
                                      'info_participants_participantId_3_baronKills': 'p3_baronKills',
                                      'info_participants_participantId_3_dragonKills': 'p3_dragonKills',
                                      'info_participants_participantId_3_objectivesStolen': 'p3_objectivesStolen',
                                      'info_participants_participantId_3_goldEarned': 'p3_goldEarned',
                                      'info_participants_participantId_3_goldSpent': 'p3_goldSpent',
                                      'info_participants_participantId_3_magicDamageDealt': 'p3_magicDamageDealt',
                                      'info_participants_participantId_3_magicDamageDealtToChampions': 'p3_magicDamageDealtToChampions',
                                      'info_participants_participantId_3_magicDamageTaken': 'p3_magicDamageTaken',
                                      'info_participants_participantId_3_physicalDamageDealt': 'p3_physicalDamageDealt',
                                      'info_participants_participantId_3_physicalDamageDealtToChampions': 'p3_physicalDamageDealtToChampions',
                                      'info_participants_participantId_3_physicalDamageTaken': 'p3_physicalDamageTaken',
                                      'info_participants_participantId_3_trueDamageDealt': 'p3_trueDamageDealt',
                                      'info_participants_participantId_3_totalDamageDealt': 'p3_totalDamageDealt',
                                      'info_participants_participantId_3_totalDamageDealtToChampions': 'p3_totalDamageDealtToChampions',
                                      'info_participants_participantId_3_totalDamageTaken': 'p3_totalDamageTaken',
                                      'info_participants_participantId_3_damageSelfMitigated': 'p3_damageSelfMitigated',
                                      'info_participants_participantId_3_totalDamageShieldedOnTeammates': 'p3_totalDamageShieldedOnTeammates',
                                      'info_participants_participantId_3_totalHeal': 'p3_totalHeal',
                                      'info_participants_participantId_3_totalHealsOnTeammates': 'p3_totalHealsOnTeammates',
                                      'info_participants_participantId_3_damageDealtToBuildings': 'p3_damageDealtToBuildings',
                                      'info_participants_participantId_3_damageDealtToObjectives': 'p3_damageDealtToObjectives',
                                      'info_participants_participantId_3_damageDealtToTurrets': 'p3_damageDealtToTurrets',
                                      'info_participants_participantId_3_nexusKills': 'p3_nexusKills',
                                      'info_participants_participantId_3_nexusLost': 'p3_nexusLost',
                                      'info_participants_participantId_3_turretKills': 'p3_turretKills',
                                      'info_participants_participantId_3_turretsLost': 'p3_turretsLost',
                                      'info_participants_participantId_3_inhibitorKills': 'p3_inhibitorKills',
                                      'info_participants_participantId_3_detectorWardsPlaced': 'p3_detectorWardsPlaced',
                                      'info_participants_participantId_3_wardsKilled': 'p3_wardsKilled',
                                      'info_participants_participantId_3_wardsPlaced': 'p3_wardsPlaced',
                                      'info_participants_participantId_3_gameEndedInEarlySurrender': 'p3_gameEndedInEarlySurrender',
                                      'info_participants_participantId_3_gameEndedInSurrender': 'p3_gameEndedInSurrender',
                                      'info_participants_participantId_3_teamEarlySurrendered': 'p3_teamEarlySurrendered',
                                      'info_participants_participantId_3_teamId': 'p3_teamId',
                                      'info_participants_participantId_3_totalTimeSpentDead': 'p3_totalTimeSpentDead',
                                      'info_participants_participantId_3_win': 'p3_win',
                                      'info_participants_participantId_4_summonerLevel': 'p4_summonerLevel',
                                      'info_participants_participantId_4_championId': 'p4_championId',
                                      'info_participants_participantId_4_championName': 'p4_championName',
                                      'info_participants_participantId_4_champExperience': 'p4_champExperience',
                                      'info_participants_participantId_4_champLevel': 'p4_champLevel',
                                      'info_participants_participantId_4_individualPosition': 'p4_individualPosition',
                                      'info_participants_participantId_4_kills': 'p4_kills',
                                      'info_participants_participantId_4_deaths': 'p4_deaths',
                                      'info_participants_participantId_4_assists': 'p4_assists',
                                      'info_participants_participantId_4_totalMinionsKilled': 'p4_totalMinionsKilled',
                                      'info_participants_participantId_4_firstBloodAssist': 'p4_firstBloodAssist',
                                      'info_participants_participantId_4_firstBloodKill': 'p4_firstBloodKill',
                                      'info_participants_participantId_4_firstTowerAssist': 'p4_firstTowerAssist',
                                      'info_participants_participantId_4_firstTowerKill': 'p4_firstTowerKill',
                                      'info_participants_participantId_4_doubleKills': 'p4_doubleKills',
                                      'info_participants_participantId_4_tripleKills': 'p4_tripleKills',
                                      'info_participants_participantId_4_quadraKills': 'p4_quadraKills',
                                      'info_participants_participantId_4_pentaKills': 'p4_pentaKills',
                                      'info_participants_participantId_4_largestKillingSpree': 'p4_largestKillingSpree',
                                      'info_participants_participantId_4_largestMultiKill': 'p4_largestMultiKill',
                                      'info_participants_participantId_4_baronKills': 'p4_baronKills',
                                      'info_participants_participantId_4_dragonKills': 'p4_dragonKills',
                                      'info_participants_participantId_4_objectivesStolen': 'p4_objectivesStolen',
                                      'info_participants_participantId_4_goldEarned': 'p4_goldEarned',
                                      'info_participants_participantId_4_goldSpent': 'p4_goldSpent',
                                      'info_participants_participantId_4_magicDamageDealt': 'p4_magicDamageDealt',
                                      'info_participants_participantId_4_magicDamageDealtToChampions': 'p4_magicDamageDealtToChampions',
                                      'info_participants_participantId_4_magicDamageTaken': 'p4_magicDamageTaken',
                                      'info_participants_participantId_4_physicalDamageDealt': 'p4_physicalDamageDealt',
                                      'info_participants_participantId_4_physicalDamageDealtToChampions': 'p4_physicalDamageDealtToChampions',
                                      'info_participants_participantId_4_physicalDamageTaken': 'p4_physicalDamageTaken',
                                      'info_participants_participantId_4_trueDamageDealt': 'p4_trueDamageDealt',
                                      'info_participants_participantId_4_totalDamageDealt': 'p4_totalDamageDealt',
                                      'info_participants_participantId_4_totalDamageDealtToChampions': 'p4_totalDamageDealtToChampions',
                                      'info_participants_participantId_4_totalDamageTaken': 'p4_totalDamageTaken',
                                      'info_participants_participantId_4_damageSelfMitigated': 'p4_damageSelfMitigated',
                                      'info_participants_participantId_4_totalDamageShieldedOnTeammates': 'p4_totalDamageShieldedOnTeammates',
                                      'info_participants_participantId_4_totalHeal': 'p4_totalHeal',
                                      'info_participants_participantId_4_totalHealsOnTeammates': 'p4_totalHealsOnTeammates',
                                      'info_participants_participantId_4_damageDealtToBuildings': 'p4_damageDealtToBuildings',
                                      'info_participants_participantId_4_damageDealtToObjectives': 'p4_damageDealtToObjectives',
                                      'info_participants_participantId_4_damageDealtToTurrets': 'p4_damageDealtToTurrets',
                                      'info_participants_participantId_4_nexusKills': 'p4_nexusKills',
                                      'info_participants_participantId_4_nexusLost': 'p4_nexusLost',
                                      'info_participants_participantId_4_turretKills': 'p4_turretKills',
                                      'info_participants_participantId_4_turretsLost': 'p4_turretsLost',
                                      'info_participants_participantId_4_inhibitorKills': 'p4_inhibitorKills',
                                      'info_participants_participantId_4_detectorWardsPlaced': 'p4_detectorWardsPlaced',
                                      'info_participants_participantId_4_wardsKilled': 'p4_wardsKilled',
                                      'info_participants_participantId_4_wardsPlaced': 'p4_wardsPlaced',
                                      'info_participants_participantId_4_gameEndedInEarlySurrender': 'p4_gameEndedInEarlySurrender',
                                      'info_participants_participantId_4_gameEndedInSurrender': 'p4_gameEndedInSurrender',
                                      'info_participants_participantId_4_teamEarlySurrendered': 'p4_teamEarlySurrendered',
                                      'info_participants_participantId_4_teamId': 'p4_teamId',
                                      'info_participants_participantId_4_totalTimeSpentDead': 'p4_totalTimeSpentDead',
                                      'info_participants_participantId_4_win': 'p4_win',
                                      'info_participants_participantId_5_summonerLevel': 'p5_summonerLevel',
                                      'info_participants_participantId_5_championId': 'p5_championId',
                                      'info_participants_participantId_5_championName': 'p5_championName',
                                      'info_participants_participantId_5_champExperience': 'p5_champExperience',
                                      'info_participants_participantId_5_champLevel': 'p5_champLevel',
                                      'info_participants_participantId_5_individualPosition': 'p5_individualPosition',
                                      'info_participants_participantId_5_kills': 'p5_kills',
                                      'info_participants_participantId_5_deaths': 'p5_deaths',
                                      'info_participants_participantId_5_assists': 'p5_assists',
                                      'info_participants_participantId_5_totalMinionsKilled': 'p5_totalMinionsKilled',
                                      'info_participants_participantId_5_firstBloodAssist': 'p5_firstBloodAssist',
                                      'info_participants_participantId_5_firstBloodKill': 'p5_firstBloodKill',
                                      'info_participants_participantId_5_firstTowerAssist': 'p5_firstTowerAssist',
                                      'info_participants_participantId_5_firstTowerKill': 'p5_firstTowerKill',
                                      'info_participants_participantId_5_doubleKills': 'p5_doubleKills',
                                      'info_participants_participantId_5_tripleKills': 'p5_tripleKills',
                                      'info_participants_participantId_5_quadraKills': 'p5_quadraKills',
                                      'info_participants_participantId_5_pentaKills': 'p5_pentaKills',
                                      'info_participants_participantId_5_largestKillingSpree': 'p5_largestKillingSpree',
                                      'info_participants_participantId_5_largestMultiKill': 'p5_largestMultiKill',
                                      'info_participants_participantId_5_baronKills': 'p5_baronKills',
                                      'info_participants_participantId_5_dragonKills': 'p5_dragonKills',
                                      'info_participants_participantId_5_objectivesStolen': 'p5_objectivesStolen',
                                      'info_participants_participantId_5_goldEarned': 'p5_goldEarned',
                                      'info_participants_participantId_5_goldSpent': 'p5_goldSpent',
                                      'info_participants_participantId_5_magicDamageDealt': 'p5_magicDamageDealt',
                                      'info_participants_participantId_5_magicDamageDealtToChampions': 'p5_magicDamageDealtToChampions',
                                      'info_participants_participantId_5_magicDamageTaken': 'p5_magicDamageTaken',
                                      'info_participants_participantId_5_physicalDamageDealt': 'p5_physicalDamageDealt',
                                      'info_participants_participantId_5_physicalDamageDealtToChampions': 'p5_physicalDamageDealtToChampions',
                                      'info_participants_participantId_5_physicalDamageTaken': 'p5_physicalDamageTaken',
                                      'info_participants_participantId_5_trueDamageDealt': 'p5_trueDamageDealt',
                                      'info_participants_participantId_5_totalDamageDealt': 'p5_totalDamageDealt',
                                      'info_participants_participantId_5_totalDamageDealtToChampions': 'p5_totalDamageDealtToChampions',
                                      'info_participants_participantId_5_totalDamageTaken': 'p5_totalDamageTaken',
                                      'info_participants_participantId_5_damageSelfMitigated': 'p5_damageSelfMitigated',
                                      'info_participants_participantId_5_totalDamageShieldedOnTeammates': 'p5_totalDamageShieldedOnTeammates',
                                      'info_participants_participantId_5_totalHeal': 'p5_totalHeal',
                                      'info_participants_participantId_5_totalHealsOnTeammates': 'p5_totalHealsOnTeammates',
                                      'info_participants_participantId_5_damageDealtToBuildings': 'p5_damageDealtToBuildings',
                                      'info_participants_participantId_5_damageDealtToObjectives': 'p5_damageDealtToObjectives',
                                      'info_participants_participantId_5_damageDealtToTurrets': 'p5_damageDealtToTurrets',
                                      'info_participants_participantId_5_nexusKills': 'p5_nexusKills',
                                      'info_participants_participantId_5_nexusLost': 'p5_nexusLost',
                                      'info_participants_participantId_5_turretKills': 'p5_turretKills',
                                      'info_participants_participantId_5_turretsLost': 'p5_turretsLost',
                                      'info_participants_participantId_5_inhibitorKills': 'p5_inhibitorKills',
                                      'info_participants_participantId_5_detectorWardsPlaced': 'p5_detectorWardsPlaced',
                                      'info_participants_participantId_5_wardsKilled': 'p5_wardsKilled',
                                      'info_participants_participantId_5_wardsPlaced': 'p5_wardsPlaced',
                                      'info_participants_participantId_5_gameEndedInEarlySurrender': 'p5_gameEndedInEarlySurrender',
                                      'info_participants_participantId_5_gameEndedInSurrender': 'p5_gameEndedInSurrender',
                                      'info_participants_participantId_5_teamEarlySurrendered': 'p5_teamEarlySurrendered',
                                      'info_participants_participantId_5_teamId': 'p5_teamId',
                                      'info_participants_participantId_5_totalTimeSpentDead': 'p5_totalTimeSpentDead',
                                      'info_participants_participantId_5_win': 'p5_win',
                                      'info_participants_participantId_6_summonerLevel': 'p6_summonerLevel',
                                      'info_participants_participantId_6_championId': 'p6_championId',
                                      'info_participants_participantId_6_championName': 'p6_championName',
                                      'info_participants_participantId_6_champExperience': 'p6_champExperience',
                                      'info_participants_participantId_6_champLevel': 'p6_champLevel',
                                      'info_participants_participantId_6_individualPosition': 'p6_individualPosition',
                                      'info_participants_participantId_6_kills': 'p6_kills',
                                      'info_participants_participantId_6_deaths': 'p6_deaths',
                                      'info_participants_participantId_6_assists': 'p6_assists',
                                      'info_participants_participantId_6_totalMinionsKilled': 'p6_totalMinionsKilled',
                                      'info_participants_participantId_6_firstBloodAssist': 'p6_firstBloodAssist',
                                      'info_participants_participantId_6_firstBloodKill': 'p6_firstBloodKill',
                                      'info_participants_participantId_6_firstTowerAssist': 'p6_firstTowerAssist',
                                      'info_participants_participantId_6_firstTowerKill': 'p6_firstTowerKill',
                                      'info_participants_participantId_6_doubleKills': 'p6_doubleKills',
                                      'info_participants_participantId_6_tripleKills': 'p6_tripleKills',
                                      'info_participants_participantId_6_quadraKills': 'p6_quadraKills',
                                      'info_participants_participantId_6_pentaKills': 'p6_pentaKills',
                                      'info_participants_participantId_6_largestKillingSpree': 'p6_largestKillingSpree',
                                      'info_participants_participantId_6_largestMultiKill': 'p6_largestMultiKill',
                                      'info_participants_participantId_6_baronKills': 'p6_baronKills',
                                      'info_participants_participantId_6_dragonKills': 'p6_dragonKills',
                                      'info_participants_participantId_6_objectivesStolen': 'p6_objectivesStolen',
                                      'info_participants_participantId_6_goldEarned': 'p6_goldEarned',
                                      'info_participants_participantId_6_goldSpent': 'p6_goldSpent',
                                      'info_participants_participantId_6_magicDamageDealt': 'p6_magicDamageDealt',
                                      'info_participants_participantId_6_magicDamageDealtToChampions': 'p6_magicDamageDealtToChampions',
                                      'info_participants_participantId_6_magicDamageTaken': 'p6_magicDamageTaken',
                                      'info_participants_participantId_6_physicalDamageDealt': 'p6_physicalDamageDealt',
                                      'info_participants_participantId_6_physicalDamageDealtToChampions': 'p6_physicalDamageDealtToChampions',
                                      'info_participants_participantId_6_physicalDamageTaken': 'p6_physicalDamageTaken',
                                      'info_participants_participantId_6_trueDamageDealt': 'p6_trueDamageDealt',
                                      'info_participants_participantId_6_totalDamageDealt': 'p6_totalDamageDealt',
                                      'info_participants_participantId_6_totalDamageDealtToChampions': 'p6_totalDamageDealtToChampions',
                                      'info_participants_participantId_6_totalDamageTaken': 'p6_totalDamageTaken',
                                      'info_participants_participantId_6_damageSelfMitigated': 'p6_damageSelfMitigated',
                                      'info_participants_participantId_6_totalDamageShieldedOnTeammates': 'p6_totalDamageShieldedOnTeammates',
                                      'info_participants_participantId_6_totalHeal': 'p6_totalHeal',
                                      'info_participants_participantId_6_totalHealsOnTeammates': 'p6_totalHealsOnTeammates',
                                      'info_participants_participantId_6_damageDealtToBuildings': 'p6_damageDealtToBuildings',
                                      'info_participants_participantId_6_damageDealtToObjectives': 'p6_damageDealtToObjectives',
                                      'info_participants_participantId_6_damageDealtToTurrets': 'p6_damageDealtToTurrets',
                                      'info_participants_participantId_6_nexusKills': 'p6_nexusKills',
                                      'info_participants_participantId_6_nexusLost': 'p6_nexusLost',
                                      'info_participants_participantId_6_turretKills': 'p6_turretKills',
                                      'info_participants_participantId_6_turretsLost': 'p6_turretsLost',
                                      'info_participants_participantId_6_inhibitorKills': 'p6_inhibitorKills',
                                      'info_participants_participantId_6_detectorWardsPlaced': 'p6_detectorWardsPlaced',
                                      'info_participants_participantId_6_wardsKilled': 'p6_wardsKilled',
                                      'info_participants_participantId_6_wardsPlaced': 'p6_wardsPlaced',
                                      'info_participants_participantId_6_gameEndedInEarlySurrender': 'p6_gameEndedInEarlySurrender',
                                      'info_participants_participantId_6_gameEndedInSurrender': 'p6_gameEndedInSurrender',
                                      'info_participants_participantId_6_teamEarlySurrendered': 'p6_teamEarlySurrendered',
                                      'info_participants_participantId_6_teamId': 'p6_teamId',
                                      'info_participants_participantId_6_totalTimeSpentDead': 'p6_totalTimeSpentDead',
                                      'info_participants_participantId_6_win': 'p6_win',
                                      'info_participants_participantId_7_summonerLevel': 'p7_summonerLevel',
                                      'info_participants_participantId_7_championId': 'p7_championId',
                                      'info_participants_participantId_7_championName': 'p7_championName',
                                      'info_participants_participantId_7_champExperience': 'p7_champExperience',
                                      'info_participants_participantId_7_champLevel': 'p7_champLevel',
                                      'info_participants_participantId_7_individualPosition': 'p7_individualPosition',
                                      'info_participants_participantId_7_kills': 'p7_kills',
                                      'info_participants_participantId_7_deaths': 'p7_deaths',
                                      'info_participants_participantId_7_assists': 'p7_assists',
                                      'info_participants_participantId_7_totalMinionsKilled': 'p7_totalMinionsKilled',
                                      'info_participants_participantId_7_firstBloodAssist': 'p7_firstBloodAssist',
                                      'info_participants_participantId_7_firstBloodKill': 'p7_firstBloodKill',
                                      'info_participants_participantId_7_firstTowerAssist': 'p7_firstTowerAssist',
                                      'info_participants_participantId_7_firstTowerKill': 'p7_firstTowerKill',
                                      'info_participants_participantId_7_doubleKills': 'p7_doubleKills',
                                      'info_participants_participantId_7_tripleKills': 'p7_tripleKills',
                                      'info_participants_participantId_7_quadraKills': 'p7_quadraKills',
                                      'info_participants_participantId_7_pentaKills': 'p7_pentaKills',
                                      'info_participants_participantId_7_largestKillingSpree': 'p7_largestKillingSpree',
                                      'info_participants_participantId_7_largestMultiKill': 'p7_largestMultiKill',
                                      'info_participants_participantId_7_baronKills': 'p7_baronKills',
                                      'info_participants_participantId_7_dragonKills': 'p7_dragonKills',
                                      'info_participants_participantId_7_objectivesStolen': 'p7_objectivesStolen',
                                      'info_participants_participantId_7_goldEarned': 'p7_goldEarned',
                                      'info_participants_participantId_7_goldSpent': 'p7_goldSpent',
                                      'info_participants_participantId_7_magicDamageDealt': 'p7_magicDamageDealt',
                                      'info_participants_participantId_7_magicDamageDealtToChampions': 'p7_magicDamageDealtToChampions',
                                      'info_participants_participantId_7_magicDamageTaken': 'p7_magicDamageTaken',
                                      'info_participants_participantId_7_physicalDamageDealt': 'p7_physicalDamageDealt',
                                      'info_participants_participantId_7_physicalDamageDealtToChampions': 'p7_physicalDamageDealtToChampions',
                                      'info_participants_participantId_7_physicalDamageTaken': 'p7_physicalDamageTaken',
                                      'info_participants_participantId_7_trueDamageDealt': 'p7_trueDamageDealt',
                                      'info_participants_participantId_7_totalDamageDealt': 'p7_totalDamageDealt',
                                      'info_participants_participantId_7_totalDamageDealtToChampions': 'p7_totalDamageDealtToChampions',
                                      'info_participants_participantId_7_totalDamageTaken': 'p7_totalDamageTaken',
                                      'info_participants_participantId_7_damageSelfMitigated': 'p7_damageSelfMitigated',
                                      'info_participants_participantId_7_totalDamageShieldedOnTeammates': 'p7_totalDamageShieldedOnTeammates',
                                      'info_participants_participantId_7_totalHeal': 'p7_totalHeal',
                                      'info_participants_participantId_7_totalHealsOnTeammates': 'p7_totalHealsOnTeammates',
                                      'info_participants_participantId_7_damageDealtToBuildings': 'p7_damageDealtToBuildings',
                                      'info_participants_participantId_7_damageDealtToObjectives': 'p7_damageDealtToObjectives',
                                      'info_participants_participantId_7_damageDealtToTurrets': 'p7_damageDealtToTurrets',
                                      'info_participants_participantId_7_nexusKills': 'p7_nexusKills',
                                      'info_participants_participantId_7_nexusLost': 'p7_nexusLost',
                                      'info_participants_participantId_7_turretKills': 'p7_turretKills',
                                      'info_participants_participantId_7_turretsLost': 'p7_turretsLost',
                                      'info_participants_participantId_7_inhibitorKills': 'p7_inhibitorKills',
                                      'info_participants_participantId_7_detectorWardsPlaced': 'p7_detectorWardsPlaced',
                                      'info_participants_participantId_7_wardsKilled': 'p7_wardsKilled',
                                      'info_participants_participantId_7_wardsPlaced': 'p7_wardsPlaced',
                                      'info_participants_participantId_7_gameEndedInEarlySurrender': 'p7_gameEndedInEarlySurrender',
                                      'info_participants_participantId_7_gameEndedInSurrender': 'p7_gameEndedInSurrender',
                                      'info_participants_participantId_7_teamEarlySurrendered': 'p7_teamEarlySurrendered',
                                      'info_participants_participantId_7_teamId': 'p7_teamId',
                                      'info_participants_participantId_7_totalTimeSpentDead': 'p7_totalTimeSpentDead',
                                      'info_participants_participantId_7_win': 'p7_win',
                                      'info_participants_participantId_8_summonerLevel': 'p8_summonerLevel',
                                      'info_participants_participantId_8_championId': 'p8_championId',
                                      'info_participants_participantId_8_championName': 'p8_championName',
                                      'info_participants_participantId_8_champExperience': 'p8_champExperience',
                                      'info_participants_participantId_8_champLevel': 'p8_champLevel',
                                      'info_participants_participantId_8_individualPosition': 'p8_individualPosition',
                                      'info_participants_participantId_8_kills': 'p8_kills',
                                      'info_participants_participantId_8_deaths': 'p8_deaths',
                                      'info_participants_participantId_8_assists': 'p8_assists',
                                      'info_participants_participantId_8_totalMinionsKilled': 'p8_totalMinionsKilled',
                                      'info_participants_participantId_8_firstBloodAssist': 'p8_firstBloodAssist',
                                      'info_participants_participantId_8_firstBloodKill': 'p8_firstBloodKill',
                                      'info_participants_participantId_8_firstTowerAssist': 'p8_firstTowerAssist',
                                      'info_participants_participantId_8_firstTowerKill': 'p8_firstTowerKill',
                                      'info_participants_participantId_8_doubleKills': 'p8_doubleKills',
                                      'info_participants_participantId_8_tripleKills': 'p8_tripleKills',
                                      'info_participants_participantId_8_quadraKills': 'p8_quadraKills',
                                      'info_participants_participantId_8_pentaKills': 'p8_pentaKills',
                                      'info_participants_participantId_8_largestKillingSpree': 'p8_largestKillingSpree',
                                      'info_participants_participantId_8_largestMultiKill': 'p8_largestMultiKill',
                                      'info_participants_participantId_8_baronKills': 'p8_baronKills',
                                      'info_participants_participantId_8_dragonKills': 'p8_dragonKills',
                                      'info_participants_participantId_8_objectivesStolen': 'p8_objectivesStolen',
                                      'info_participants_participantId_8_goldEarned': 'p8_goldEarned',
                                      'info_participants_participantId_8_goldSpent': 'p8_goldSpent',
                                      'info_participants_participantId_8_magicDamageDealt': 'p8_magicDamageDealt',
                                      'info_participants_participantId_8_magicDamageDealtToChampions': 'p8_magicDamageDealtToChampions',
                                      'info_participants_participantId_8_magicDamageTaken': 'p8_magicDamageTaken',
                                      'info_participants_participantId_8_physicalDamageDealt': 'p8_physicalDamageDealt',
                                      'info_participants_participantId_8_physicalDamageDealtToChampions': 'p8_physicalDamageDealtToChampions',
                                      'info_participants_participantId_8_physicalDamageTaken': 'p8_physicalDamageTaken',
                                      'info_participants_participantId_8_trueDamageDealt': 'p8_trueDamageDealt',
                                      'info_participants_participantId_8_totalDamageDealt': 'p8_totalDamageDealt',
                                      'info_participants_participantId_8_totalDamageDealtToChampions': 'p8_totalDamageDealtToChampions',
                                      'info_participants_participantId_8_totalDamageTaken': 'p8_totalDamageTaken',
                                      'info_participants_participantId_8_damageSelfMitigated': 'p8_damageSelfMitigated',
                                      'info_participants_participantId_8_totalDamageShieldedOnTeammates': 'p8_totalDamageShieldedOnTeammates',
                                      'info_participants_participantId_8_totalHeal': 'p8_totalHeal',
                                      'info_participants_participantId_8_totalHealsOnTeammates': 'p8_totalHealsOnTeammates',
                                      'info_participants_participantId_8_damageDealtToBuildings': 'p8_damageDealtToBuildings',
                                      'info_participants_participantId_8_damageDealtToObjectives': 'p8_damageDealtToObjectives',
                                      'info_participants_participantId_8_damageDealtToTurrets': 'p8_damageDealtToTurrets',
                                      'info_participants_participantId_8_nexusKills': 'p8_nexusKills',
                                      'info_participants_participantId_8_nexusLost': 'p8_nexusLost',
                                      'info_participants_participantId_8_turretKills': 'p8_turretKills',
                                      'info_participants_participantId_8_turretsLost': 'p8_turretsLost',
                                      'info_participants_participantId_8_inhibitorKills': 'p8_inhibitorKills',
                                      'info_participants_participantId_8_detectorWardsPlaced': 'p8_detectorWardsPlaced',
                                      'info_participants_participantId_8_wardsKilled': 'p8_wardsKilled',
                                      'info_participants_participantId_8_wardsPlaced': 'p8_wardsPlaced',
                                      'info_participants_participantId_8_gameEndedInEarlySurrender': 'p8_gameEndedInEarlySurrender',
                                      'info_participants_participantId_8_gameEndedInSurrender': 'p8_gameEndedInSurrender',
                                      'info_participants_participantId_8_teamEarlySurrendered': 'p8_teamEarlySurrendered',
                                      'info_participants_participantId_8_teamId': 'p8_teamId',
                                      'info_participants_participantId_8_totalTimeSpentDead': 'p8_totalTimeSpentDead',
                                      'info_participants_participantId_8_win': 'p8_win',
                                      'info_participants_participantId_9_summonerLevel': 'p9_summonerLevel',
                                      'info_participants_participantId_9_championId': 'p9_championId',
                                      'info_participants_participantId_9_championName': 'p9_championName',
                                      'info_participants_participantId_9_champExperience': 'p9_champExperience',
                                      'info_participants_participantId_9_champLevel': 'p9_champLevel',
                                      'info_participants_participantId_9_individualPosition': 'p9_individualPosition',
                                      'info_participants_participantId_9_kills': 'p9_kills',
                                      'info_participants_participantId_9_deaths': 'p9_deaths',
                                      'info_participants_participantId_9_assists': 'p9_assists',
                                      'info_participants_participantId_9_totalMinionsKilled': 'p9_totalMinionsKilled',
                                      'info_participants_participantId_9_firstBloodAssist': 'p9_firstBloodAssist',
                                      'info_participants_participantId_9_firstBloodKill': 'p9_firstBloodKill',
                                      'info_participants_participantId_9_firstTowerAssist': 'p9_firstTowerAssist',
                                      'info_participants_participantId_9_firstTowerKill': 'p9_firstTowerKill',
                                      'info_participants_participantId_9_doubleKills': 'p9_doubleKills',
                                      'info_participants_participantId_9_tripleKills': 'p9_tripleKills',
                                      'info_participants_participantId_9_quadraKills': 'p9_quadraKills',
                                      'info_participants_participantId_9_pentaKills': 'p9_pentaKills',
                                      'info_participants_participantId_9_largestKillingSpree': 'p9_largestKillingSpree',
                                      'info_participants_participantId_9_largestMultiKill': 'p9_largestMultiKill',
                                      'info_participants_participantId_9_baronKills': 'p9_baronKills',
                                      'info_participants_participantId_9_dragonKills': 'p9_dragonKills',
                                      'info_participants_participantId_9_objectivesStolen': 'p9_objectivesStolen',
                                      'info_participants_participantId_9_goldEarned': 'p9_goldEarned',
                                      'info_participants_participantId_9_goldSpent': 'p9_goldSpent',
                                      'info_participants_participantId_9_magicDamageDealt': 'p9_magicDamageDealt',
                                      'info_participants_participantId_9_magicDamageDealtToChampions': 'p9_magicDamageDealtToChampions',
                                      'info_participants_participantId_9_magicDamageTaken': 'p9_magicDamageTaken',
                                      'info_participants_participantId_9_physicalDamageDealt': 'p9_physicalDamageDealt',
                                      'info_participants_participantId_9_physicalDamageDealtToChampions': 'p9_physicalDamageDealtToChampions',
                                      'info_participants_participantId_9_physicalDamageTaken': 'p9_physicalDamageTaken',
                                      'info_participants_participantId_9_trueDamageDealt': 'p9_trueDamageDealt',
                                      'info_participants_participantId_9_totalDamageDealt': 'p9_totalDamageDealt',
                                      'info_participants_participantId_9_totalDamageDealtToChampions': 'p9_totalDamageDealtToChampions',
                                      'info_participants_participantId_9_totalDamageTaken': 'p9_totalDamageTaken',
                                      'info_participants_participantId_9_damageSelfMitigated': 'p9_damageSelfMitigated',
                                      'info_participants_participantId_9_totalDamageShieldedOnTeammates': 'p9_totalDamageShieldedOnTeammates',
                                      'info_participants_participantId_9_totalHeal': 'p9_totalHeal',
                                      'info_participants_participantId_9_totalHealsOnTeammates': 'p9_totalHealsOnTeammates',
                                      'info_participants_participantId_9_damageDealtToBuildings': 'p9_damageDealtToBuildings',
                                      'info_participants_participantId_9_damageDealtToObjectives': 'p9_damageDealtToObjectives',
                                      'info_participants_participantId_9_damageDealtToTurrets': 'p9_damageDealtToTurrets',
                                      'info_participants_participantId_9_nexusKills': 'p9_nexusKills',
                                      'info_participants_participantId_9_nexusLost': 'p9_nexusLost',
                                      'info_participants_participantId_9_turretKills': 'p9_turretKills',
                                      'info_participants_participantId_9_turretsLost': 'p9_turretsLost',
                                      'info_participants_participantId_9_inhibitorKills': 'p9_inhibitorKills',
                                      'info_participants_participantId_9_detectorWardsPlaced': 'p9_detectorWardsPlaced',
                                      'info_participants_participantId_9_wardsKilled': 'p9_wardsKilled',
                                      'info_participants_participantId_9_wardsPlaced': 'p9_wardsPlaced',
                                      'info_participants_participantId_9_gameEndedInEarlySurrender': 'p9_gameEndedInEarlySurrender',
                                      'info_participants_participantId_9_gameEndedInSurrender': 'p9_gameEndedInSurrender',
                                      'info_participants_participantId_9_teamEarlySurrendered': 'p9_teamEarlySurrendered',
                                      'info_participants_participantId_9_teamId': 'p9_teamId',
                                      'info_participants_participantId_9_totalTimeSpentDead': 'p9_totalTimeSpentDead',
                                      'info_participants_participantId_9_win': 'p9_win',
                                      'info_participants_participantId_10_summonerLevel': 'p10_summonerLevel',
                                      'info_participants_participantId_10_championId': 'p10_championId',
                                      'info_participants_participantId_10_championName': 'p10_championName',
                                      'info_participants_participantId_10_champExperience': 'p10_champExperience',
                                      'info_participants_participantId_10_champLevel': 'p10_champLevel',
                                      'info_participants_participantId_10_individualPosition': 'p10_individualPosition',
                                      'info_participants_participantId_10_kills': 'p10_kills',
                                      'info_participants_participantId_10_deaths': 'p10_deaths',
                                      'info_participants_participantId_10_assists': 'p10_assists',
                                      'info_participants_participantId_10_totalMinionsKilled': 'p10_totalMinionsKilled',
                                      'info_participants_participantId_10_firstBloodAssist': 'p10_firstBloodAssist',
                                      'info_participants_participantId_10_firstBloodKill': 'p10_firstBloodKill',
                                      'info_participants_participantId_10_firstTowerAssist': 'p10_firstTowerAssist',
                                      'info_participants_participantId_10_firstTowerKill': 'p10_firstTowerKill',
                                      'info_participants_participantId_10_doubleKills': 'p10_doubleKills',
                                      'info_participants_participantId_10_tripleKills': 'p10_tripleKills',
                                      'info_participants_participantId_10_quadraKills': 'p10_quadraKills',
                                      'info_participants_participantId_10_pentaKills': 'p10_pentaKills',
                                      'info_participants_participantId_10_largestKillingSpree': 'p10_largestKillingSpree',
                                      'info_participants_participantId_10_largestMultiKill': 'p10_largestMultiKill',
                                      'info_participants_participantId_10_baronKills': 'p10_baronKills',
                                      'info_participants_participantId_10_dragonKills': 'p10_dragonKills',
                                      'info_participants_participantId_10_objectivesStolen': 'p10_objectivesStolen',
                                      'info_participants_participantId_10_goldEarned': 'p10_goldEarned',
                                      'info_participants_participantId_10_goldSpent': 'p10_goldSpent',
                                      'info_participants_participantId_10_magicDamageDealt': 'p10_magicDamageDealt',
                                      'info_participants_participantId_10_magicDamageDealtToChampions': 'p10_magicDamageDealtToChampions',
                                      'info_participants_participantId_10_magicDamageTaken': 'p10_magicDamageTaken',
                                      'info_participants_participantId_10_physicalDamageDealt': 'p10_physicalDamageDealt',
                                      'info_participants_participantId_10_physicalDamageDealtToChampions': 'p10_physicalDamageDealtToChampions',
                                      'info_participants_participantId_10_physicalDamageTaken': 'p10_physicalDamageTaken',
                                      'info_participants_participantId_10_trueDamageDealt': 'p10_trueDamageDealt',
                                      'info_participants_participantId_10_totalDamageDealt': 'p10_totalDamageDealt',
                                      'info_participants_participantId_10_totalDamageDealtToChampions': 'p10_totalDamageDealtToChampions',
                                      'info_participants_participantId_10_totalDamageTaken': 'p10_totalDamageTaken',
                                      'info_participants_participantId_10_damageSelfMitigated': 'p10_damageSelfMitigated',
                                      'info_participants_participantId_10_totalDamageShieldedOnTeammates': 'p10_totalDamageShieldedOnTeammates',
                                      'info_participants_participantId_10_totalHeal': 'p10_totalHeal',
                                      'info_participants_participantId_10_totalHealsOnTeammates': 'p10_totalHealsOnTeammates',
                                      'info_participants_participantId_10_damageDealtToBuildings': 'p10_damageDealtToBuildings',
                                      'info_participants_participantId_10_damageDealtToObjectives': 'p10_damageDealtToObjectives',
                                      'info_participants_participantId_10_damageDealtToTurrets': 'p10_damageDealtToTurrets',
                                      'info_participants_participantId_10_nexusKills': 'p10_nexusKills',
                                      'info_participants_participantId_10_nexusLost': 'p10_nexusLost',
                                      'info_participants_participantId_10_turretKills': 'p10_turretKills',
                                      'info_participants_participantId_10_turretsLost': 'p10_turretsLost',
                                      'info_participants_participantId_10_inhibitorKills': 'p10_inhibitorKills',
                                      'info_participants_participantId_10_detectorWardsPlaced': 'p10_detectorWardsPlaced',
                                      'info_participants_participantId_10_wardsKilled': 'p10_wardsKilled',
                                      'info_participants_participantId_10_wardsPlaced': 'p10_wardsPlaced',
                                      'info_participants_participantId_10_gameEndedInEarlySurrender': 'p10_gameEndedInEarlySurrender',
                                      'info_participants_participantId_10_gameEndedInSurrender': 'p10_gameEndedInSurrender',
                                      'info_participants_participantId_10_teamEarlySurrendered': 'p10_teamEarlySurrendered',
                                      'info_participants_participantId_10_teamId': 'p10_teamId',
                                      'info_participants_participantId_10_totalTimeSpentDead': 'p10_totalTimeSpentDead',
                                      'info_participants_participantId_10_win': 'p10_win',
                                      'info_teams_teamId_100_objectives_baron_first': 'team_100_obj_baron_first',
                                      'info_teams_teamId_100_objectives_baron_kills': 'team_100_obj_baron_kills',
                                      'info_teams_teamId_100_objectives_champion_first': 'team_100_obj_champion_first',
                                      'info_teams_teamId_100_objectives_champion_kills': 'team_100_obj_champion_kills',
                                      'info_teams_teamId_100_objectives_dragon_first': 'team_100_obj_dragon_first',
                                      'info_teams_teamId_100_objectives_dragon_kills': 'team_100_obj_dragon_kills',
                                      'info_teams_teamId_100_objectives_inhibitor_first': 'team_100_obj_inhibitor_first',
                                      'info_teams_teamId_100_objectives_inhibitor_kills': 'team_100_obj_inhibitor_kills',
                                      'info_teams_teamId_100_objectives_riftHerald_first': 'team_100_obj_riftHerald_first',
                                      'info_teams_teamId_100_objectives_riftHerald_kills': 'team_100_obj_riftHerald_kills',
                                      'info_teams_teamId_100_objectives_tower_first': 'team_100_obj_tower_first',
                                      'info_teams_teamId_100_objectives_tower_kills': 'team_100_obj_tower_kills',
                                      'info_teams_teamId_100_win': 'team_100_win',
                                      'info_teams_teamId_200_objectives_baron_first': 'team_200_obj_baron_first',
                                      'info_teams_teamId_200_objectives_baron_kills': 'team_200_obj_baron_kills',
                                      'info_teams_teamId_200_objectives_champion_first': 'team_200_obj_champion_first',
                                      'info_teams_teamId_200_objectives_champion_kills': 'team_200_obj_champion_kills',
                                      'info_teams_teamId_200_objectives_dragon_first': 'team_200_obj_dragon_first',
                                      'info_teams_teamId_200_objectives_dragon_kills': 'team_200_obj_dragon_kills',
                                      'info_teams_teamId_200_objectives_inhibitor_first': 'team_200_obj_inhibitor_first',
                                      'info_teams_teamId_200_objectives_inhibitor_kills': 'team_200_obj_inhibitor_kills',
                                      'info_teams_teamId_200_objectives_riftHerald_first': 'team_200_obj_riftHerald_first',
                                      'info_teams_teamId_200_objectives_riftHerald_kills': 'team_200_obj_riftHerald_kills',
                                      'info_teams_teamId_200_objectives_tower_first': 'team_200_obj_tower_first',
                                      'info_teams_teamId_200_objectives_tower_kills': 'team_200_obj_tower_kills',
                                      'info_teams_teamId_200_win': 'team_200_win'
                                       }                                    

columnas_seleccionadas = ['info_gameId','info_gameDuration','info_gameMode','info_gameType',
                   'info_mapId','info_participants_participantId_1_summonerLevel','info_participants_participantId_1_championId',
                   'info_participants_participantId_1_championName','info_participants_participantId_1_champExperience',
                   'info_participants_participantId_1_champLevel','info_participants_participantId_1_individualPosition',
                   'info_participants_participantId_1_kills','info_participants_participantId_1_deaths',
                   'info_participants_participantId_1_assists','info_participants_participantId_1_totalMinionsKilled', 
                   'info_participants_participantId_1_firstBloodAssist','info_participants_participantId_1_firstBloodKill',
                   'info_participants_participantId_1_firstTowerAssist','info_participants_participantId_1_firstTowerKill',
                   'info_participants_participantId_1_doubleKills','info_participants_participantId_1_tripleKills',
                   'info_participants_participantId_1_doubleKills','info_participants_participantId_1_tripleKills',
                   'info_participants_participantId_1_quadraKills','info_participants_participantId_1_pentaKills',
                   'info_participants_participantId_1_largestKillingSpree','info_participants_participantId_1_largestMultiKill',
                   'info_participants_participantId_1_baronKills','info_participants_participantId_1_dragonKills',
                   'info_participants_participantId_1_objectivesStolen','info_participants_participantId_1_goldEarned',
                   'info_participants_participantId_1_goldSpent','info_participants_participantId_1_magicDamageDealt',
                   'info_participants_participantId_1_magicDamageDealtToChampions','info_participants_participantId_1_magicDamageTaken',
                   'info_participants_participantId_1_physicalDamageDealt','info_participants_participantId_1_physicalDamageDealtToChampions',
                   'info_participants_participantId_1_physicalDamageTaken','info_participants_participantId_1_trueDamageDealt',
                   'info_participants_participantId_1_totalDamageDealt','info_participants_participantId_1_totalDamageDealtToChampions',
                   'info_participants_participantId_1_totalDamageTaken','info_participants_participantId_1_damageSelfMitigated',
                   'info_participants_participantId_1_totalDamageShieldedOnTeammates','info_participants_participantId_1_totalHeal',
                   'info_participants_participantId_1_totalHealsOnTeammates','info_participants_participantId_1_damageDealtToBuildings',
                   'info_participants_participantId_1_damageDealtToObjectives','info_participants_participantId_1_damageDealtToTurrets',
                   'info_participants_participantId_1_nexusKills','info_participants_participantId_1_nexusLost',
                   'info_participants_participantId_1_turretKills','info_participants_participantId_1_turretsLost',
                   'info_participants_participantId_1_inhibitorKills','info_participants_participantId_1_detectorWardsPlaced',
                   'info_participants_participantId_1_wardsKilled','info_participants_participantId_1_wardsPlaced',
                   'info_participants_participantId_1_gameEndedInEarlySurrender','info_participants_participantId_1_gameEndedInSurrender',
                   'info_participants_participantId_1_teamEarlySurrendered','info_participants_participantId_1_teamId',
                   'info_participants_participantId_1_totalTimeSpentDead','info_participants_participantId_1_win',
                   'info_participants_participantId_2_summonerLevel','info_participants_participantId_2_championId',
                   'info_participants_participantId_2_championName','info_participants_participantId_2_champExperience',
                   'info_participants_participantId_2_champLevel','info_participants_participantId_2_individualPosition',
                   'info_participants_participantId_2_kills','info_participants_participantId_2_deaths',
                   'info_participants_participantId_2_assists','info_participants_participantId_2_totalMinionsKilled', 
                   'info_participants_participantId_2_firstBloodAssist','info_participants_participantId_2_firstBloodKill',
                   'info_participants_participantId_2_firstTowerAssist','info_participants_participantId_2_firstTowerKill',
                   'info_participants_participantId_2_doubleKills','info_participants_participantId_2_tripleKills',
                   'info_participants_participantId_2_doubleKills','info_participants_participantId_2_tripleKills',
                   'info_participants_participantId_2_quadraKills','info_participants_participantId_2_pentaKills',
                   'info_participants_participantId_2_largestKillingSpree','info_participants_participantId_2_largestMultiKill',
                   'info_participants_participantId_2_baronKills','info_participants_participantId_2_dragonKills',
                   'info_participants_participantId_2_objectivesStolen','info_participants_participantId_2_goldEarned',
                   'info_participants_participantId_2_goldSpent','info_participants_participantId_2_magicDamageDealt',
                   'info_participants_participantId_2_magicDamageDealtToChampions','info_participants_participantId_2_magicDamageTaken',
                   'info_participants_participantId_2_physicalDamageDealt','info_participants_participantId_2_physicalDamageDealtToChampions',
                   'info_participants_participantId_2_physicalDamageTaken','info_participants_participantId_2_trueDamageDealt',
                   'info_participants_participantId_2_totalDamageDealt','info_participants_participantId_2_totalDamageDealtToChampions',
                   'info_participants_participantId_2_totalDamageTaken','info_participants_participantId_2_damageSelfMitigated',
                   'info_participants_participantId_2_totalDamageShieldedOnTeammates','info_participants_participantId_2_totalHeal',
                   'info_participants_participantId_2_totalHealsOnTeammates','info_participants_participantId_2_damageDealtToBuildings',
                   'info_participants_participantId_2_damageDealtToObjectives','info_participants_participantId_2_damageDealtToTurrets',
                   'info_participants_participantId_2_nexusKills','info_participants_participantId_2_nexusLost',
                   'info_participants_participantId_2_turretKills','info_participants_participantId_2_turretsLost',
                   'info_participants_participantId_2_inhibitorKills','info_participants_participantId_2_detectorWardsPlaced',
                   'info_participants_participantId_2_wardsKilled','info_participants_participantId_2_wardsPlaced',
                   'info_participants_participantId_2_gameEndedInEarlySurrender','info_participants_participantId_2_gameEndedInSurrender',
                   'info_participants_participantId_2_teamEarlySurrendered','info_participants_participantId_2_teamId',
                   'info_participants_participantId_2_totalTimeSpentDead','info_participants_participantId_2_win',
                   'info_participants_participantId_3_summonerLevel','info_participants_participantId_3_championId',
                   'info_participants_participantId_3_championName','info_participants_participantId_3_champExperience',
                   'info_participants_participantId_3_champLevel','info_participants_participantId_3_individualPosition',
                   'info_participants_participantId_3_kills','info_participants_participantId_3_deaths',
                   'info_participants_participantId_3_assists','info_participants_participantId_3_totalMinionsKilled', 
                   'info_participants_participantId_3_firstBloodAssist','info_participants_participantId_3_firstBloodKill',
                   'info_participants_participantId_3_firstTowerAssist','info_participants_participantId_3_firstTowerKill',
                   'info_participants_participantId_3_doubleKills','info_participants_participantId_3_tripleKills',
                   'info_participants_participantId_3_doubleKills','info_participants_participantId_3_tripleKills',
                   'info_participants_participantId_3_quadraKills','info_participants_participantId_3_pentaKills',
                   'info_participants_participantId_3_largestKillingSpree','info_participants_participantId_3_largestMultiKill',
                   'info_participants_participantId_3_baronKills','info_participants_participantId_3_dragonKills',
                   'info_participants_participantId_3_objectivesStolen','info_participants_participantId_3_goldEarned',
                   'info_participants_participantId_3_goldSpent','info_participants_participantId_3_magicDamageDealt',
                   'info_participants_participantId_3_magicDamageDealtToChampions','info_participants_participantId_3_magicDamageTaken',
                   'info_participants_participantId_3_physicalDamageDealt','info_participants_participantId_3_physicalDamageDealtToChampions',
                   'info_participants_participantId_3_physicalDamageTaken','info_participants_participantId_3_trueDamageDealt',
                   'info_participants_participantId_3_totalDamageDealt','info_participants_participantId_3_totalDamageDealtToChampions',
                   'info_participants_participantId_3_totalDamageTaken','info_participants_participantId_3_damageSelfMitigated',
                   'info_participants_participantId_3_totalDamageShieldedOnTeammates','info_participants_participantId_3_totalHeal',
                   'info_participants_participantId_3_totalHealsOnTeammates','info_participants_participantId_3_damageDealtToBuildings',
                   'info_participants_participantId_3_damageDealtToObjectives','info_participants_participantId_3_damageDealtToTurrets',
                   'info_participants_participantId_3_nexusKills','info_participants_participantId_3_nexusLost',
                   'info_participants_participantId_3_turretKills','info_participants_participantId_3_turretsLost',
                   'info_participants_participantId_3_inhibitorKills','info_participants_participantId_3_detectorWardsPlaced',
                   'info_participants_participantId_3_wardsKilled','info_participants_participantId_3_wardsPlaced',
                   'info_participants_participantId_3_gameEndedInEarlySurrender','info_participants_participantId_3_gameEndedInSurrender',
                   'info_participants_participantId_3_teamEarlySurrendered','info_participants_participantId_3_teamId',
                   'info_participants_participantId_3_totalTimeSpentDead','info_participants_participantId_3_win',
                   'info_participants_participantId_4_summonerLevel','info_participants_participantId_4_championId',
                   'info_participants_participantId_4_championName','info_participants_participantId_4_champExperience',
                   'info_participants_participantId_4_champLevel','info_participants_participantId_4_individualPosition',
                   'info_participants_participantId_4_kills','info_participants_participantId_4_deaths',
                   'info_participants_participantId_4_assists','info_participants_participantId_4_totalMinionsKilled', 
                   'info_participants_participantId_4_firstBloodAssist','info_participants_participantId_4_firstBloodKill',
                   'info_participants_participantId_4_firstTowerAssist','info_participants_participantId_4_firstTowerKill',
                   'info_participants_participantId_4_doubleKills','info_participants_participantId_4_tripleKills',
                   'info_participants_participantId_4_doubleKills','info_participants_participantId_4_tripleKills',
                   'info_participants_participantId_4_quadraKills','info_participants_participantId_4_pentaKills',
                   'info_participants_participantId_4_largestKillingSpree','info_participants_participantId_4_largestMultiKill',
                   'info_participants_participantId_4_baronKills','info_participants_participantId_4_dragonKills',
                   'info_participants_participantId_4_objectivesStolen','info_participants_participantId_4_goldEarned',
                   'info_participants_participantId_4_goldSpent','info_participants_participantId_4_magicDamageDealt',
                   'info_participants_participantId_4_magicDamageDealtToChampions','info_participants_participantId_4_magicDamageTaken',
                   'info_participants_participantId_4_physicalDamageDealt','info_participants_participantId_4_physicalDamageDealtToChampions',
                   'info_participants_participantId_4_physicalDamageTaken','info_participants_participantId_4_trueDamageDealt',
                   'info_participants_participantId_4_totalDamageDealt','info_participants_participantId_4_totalDamageDealtToChampions',
                   'info_participants_participantId_4_totalDamageTaken','info_participants_participantId_4_damageSelfMitigated',
                   'info_participants_participantId_4_totalDamageShieldedOnTeammates','info_participants_participantId_4_totalHeal',
                   'info_participants_participantId_4_totalHealsOnTeammates','info_participants_participantId_4_damageDealtToBuildings',
                   'info_participants_participantId_4_damageDealtToObjectives','info_participants_participantId_4_damageDealtToTurrets',
                   'info_participants_participantId_4_nexusKills','info_participants_participantId_4_nexusLost',
                   'info_participants_participantId_4_turretKills','info_participants_participantId_4_turretsLost',
                   'info_participants_participantId_4_inhibitorKills','info_participants_participantId_4_detectorWardsPlaced',
                   'info_participants_participantId_4_wardsKilled','info_participants_participantId_4_wardsPlaced',
                   'info_participants_participantId_4_gameEndedInEarlySurrender','info_participants_participantId_4_gameEndedInSurrender',
                   'info_participants_participantId_4_teamEarlySurrendered','info_participants_participantId_4_teamId',
                   'info_participants_participantId_4_totalTimeSpentDead','info_participants_participantId_4_win',
                   'info_participants_participantId_5_summonerLevel','info_participants_participantId_5_championId',
                   'info_participants_participantId_5_championName','info_participants_participantId_5_champExperience',
                   'info_participants_participantId_5_champLevel','info_participants_participantId_5_individualPosition',
                   'info_participants_participantId_5_kills','info_participants_participantId_5_deaths',
                   'info_participants_participantId_5_assists','info_participants_participantId_5_totalMinionsKilled', 
                   'info_participants_participantId_5_firstBloodAssist','info_participants_participantId_5_firstBloodKill',
                   'info_participants_participantId_5_firstTowerAssist','info_participants_participantId_5_firstTowerKill',
                   'info_participants_participantId_5_doubleKills','info_participants_participantId_5_tripleKills',
                   'info_participants_participantId_5_doubleKills','info_participants_participantId_5_tripleKills',
                   'info_participants_participantId_5_quadraKills','info_participants_participantId_5_pentaKills',
                   'info_participants_participantId_5_largestKillingSpree','info_participants_participantId_5_largestMultiKill',
                   'info_participants_participantId_5_baronKills','info_participants_participantId_5_dragonKills',
                   'info_participants_participantId_5_objectivesStolen','info_participants_participantId_5_goldEarned',
                   'info_participants_participantId_5_goldSpent','info_participants_participantId_5_magicDamageDealt',
                   'info_participants_participantId_5_magicDamageDealtToChampions','info_participants_participantId_5_magicDamageTaken',
                   'info_participants_participantId_5_physicalDamageDealt','info_participants_participantId_5_physicalDamageDealtToChampions',
                   'info_participants_participantId_5_physicalDamageTaken','info_participants_participantId_5_trueDamageDealt',
                   'info_participants_participantId_5_totalDamageDealt','info_participants_participantId_5_totalDamageDealtToChampions',
                   'info_participants_participantId_5_totalDamageTaken','info_participants_participantId_5_damageSelfMitigated',
                   'info_participants_participantId_5_totalDamageShieldedOnTeammates','info_participants_participantId_5_totalHeal',
                   'info_participants_participantId_5_totalHealsOnTeammates','info_participants_participantId_5_damageDealtToBuildings',
                   'info_participants_participantId_5_damageDealtToObjectives','info_participants_participantId_5_damageDealtToTurrets',
                   'info_participants_participantId_5_nexusKills','info_participants_participantId_5_nexusLost',
                   'info_participants_participantId_5_turretKills','info_participants_participantId_5_turretsLost',
                   'info_participants_participantId_5_inhibitorKills','info_participants_participantId_5_detectorWardsPlaced',
                   'info_participants_participantId_5_wardsKilled','info_participants_participantId_5_wardsPlaced',
                   'info_participants_participantId_5_gameEndedInEarlySurrender','info_participants_participantId_5_gameEndedInSurrender',
                   'info_participants_participantId_5_teamEarlySurrendered','info_participants_participantId_5_teamId',
                   'info_participants_participantId_5_totalTimeSpentDead','info_participants_participantId_5_win',
                   'info_participants_participantId_6_summonerLevel','info_participants_participantId_6_championId',
                   'info_participants_participantId_6_championName','info_participants_participantId_6_champExperience',
                   'info_participants_participantId_6_champLevel','info_participants_participantId_6_individualPosition',
                   'info_participants_participantId_6_kills','info_participants_participantId_6_deaths',
                   'info_participants_participantId_6_assists','info_participants_participantId_6_totalMinionsKilled', 
                   'info_participants_participantId_6_firstBloodAssist','info_participants_participantId_6_firstBloodKill',
                   'info_participants_participantId_6_firstTowerAssist','info_participants_participantId_6_firstTowerKill',
                   'info_participants_participantId_6_doubleKills','info_participants_participantId_6_tripleKills',
                   'info_participants_participantId_6_doubleKills','info_participants_participantId_6_tripleKills',
                   'info_participants_participantId_6_quadraKills','info_participants_participantId_6_pentaKills',
                   'info_participants_participantId_6_largestKillingSpree','info_participants_participantId_6_largestMultiKill',
                   'info_participants_participantId_6_baronKills','info_participants_participantId_6_dragonKills',
                   'info_participants_participantId_6_objectivesStolen','info_participants_participantId_6_goldEarned',
                   'info_participants_participantId_6_goldSpent','info_participants_participantId_6_magicDamageDealt',
                   'info_participants_participantId_6_magicDamageDealtToChampions','info_participants_participantId_6_magicDamageTaken',
                   'info_participants_participantId_6_physicalDamageDealt','info_participants_participantId_6_physicalDamageDealtToChampions',
                   'info_participants_participantId_6_physicalDamageTaken','info_participants_participantId_6_trueDamageDealt',
                   'info_participants_participantId_6_totalDamageDealt','info_participants_participantId_6_totalDamageDealtToChampions',
                   'info_participants_participantId_6_totalDamageTaken','info_participants_participantId_6_damageSelfMitigated',
                   'info_participants_participantId_6_totalDamageShieldedOnTeammates','info_participants_participantId_6_totalHeal',
                   'info_participants_participantId_6_totalHealsOnTeammates','info_participants_participantId_6_damageDealtToBuildings',
                   'info_participants_participantId_6_damageDealtToObjectives','info_participants_participantId_6_damageDealtToTurrets',
                   'info_participants_participantId_6_nexusKills','info_participants_participantId_6_nexusLost',
                   'info_participants_participantId_6_turretKills','info_participants_participantId_6_turretsLost',
                   'info_participants_participantId_6_inhibitorKills','info_participants_participantId_6_detectorWardsPlaced',
                   'info_participants_participantId_6_wardsKilled','info_participants_participantId_6_wardsPlaced',
                   'info_participants_participantId_6_gameEndedInEarlySurrender','info_participants_participantId_6_gameEndedInSurrender',
                   'info_participants_participantId_6_teamEarlySurrendered','info_participants_participantId_6_teamId',
                   'info_participants_participantId_6_totalTimeSpentDead','info_participants_participantId_6_win',
                   'info_participants_participantId_7_summonerLevel','info_participants_participantId_7_championId',
                   'info_participants_participantId_7_championName','info_participants_participantId_7_champExperience',
                   'info_participants_participantId_7_champLevel','info_participants_participantId_7_individualPosition',
                   'info_participants_participantId_7_kills','info_participants_participantId_7_deaths',
                   'info_participants_participantId_7_assists','info_participants_participantId_7_totalMinionsKilled', 
                   'info_participants_participantId_7_firstBloodAssist','info_participants_participantId_7_firstBloodKill',
                   'info_participants_participantId_7_firstTowerAssist','info_participants_participantId_7_firstTowerKill',
                   'info_participants_participantId_7_doubleKills','info_participants_participantId_7_tripleKills',
                   'info_participants_participantId_7_doubleKills','info_participants_participantId_7_tripleKills',
                   'info_participants_participantId_7_quadraKills','info_participants_participantId_7_pentaKills',
                   'info_participants_participantId_7_largestKillingSpree','info_participants_participantId_7_largestMultiKill',
                   'info_participants_participantId_7_baronKills','info_participants_participantId_7_dragonKills',
                   'info_participants_participantId_7_objectivesStolen','info_participants_participantId_7_goldEarned',
                   'info_participants_participantId_7_goldSpent','info_participants_participantId_7_magicDamageDealt',
                   'info_participants_participantId_7_magicDamageDealtToChampions','info_participants_participantId_7_magicDamageTaken',
                   'info_participants_participantId_7_physicalDamageDealt','info_participants_participantId_7_physicalDamageDealtToChampions',
                   'info_participants_participantId_7_physicalDamageTaken','info_participants_participantId_7_trueDamageDealt',
                   'info_participants_participantId_7_totalDamageDealt','info_participants_participantId_7_totalDamageDealtToChampions',
                   'info_participants_participantId_7_totalDamageTaken','info_participants_participantId_7_damageSelfMitigated',
                   'info_participants_participantId_7_totalDamageShieldedOnTeammates','info_participants_participantId_7_totalHeal',
                   'info_participants_participantId_7_totalHealsOnTeammates','info_participants_participantId_7_damageDealtToBuildings',
                   'info_participants_participantId_7_damageDealtToObjectives','info_participants_participantId_7_damageDealtToTurrets',
                   'info_participants_participantId_7_nexusKills','info_participants_participantId_7_nexusLost',
                   'info_participants_participantId_7_turretKills','info_participants_participantId_7_turretsLost',
                   'info_participants_participantId_7_inhibitorKills','info_participants_participantId_7_detectorWardsPlaced',
                   'info_participants_participantId_7_wardsKilled','info_participants_participantId_7_wardsPlaced',
                   'info_participants_participantId_7_gameEndedInEarlySurrender','info_participants_participantId_7_gameEndedInSurrender',
                   'info_participants_participantId_7_teamEarlySurrendered','info_participants_participantId_7_teamId',
                   'info_participants_participantId_7_totalTimeSpentDead','info_participants_participantId_7_win',
                   'info_participants_participantId_8_summonerLevel','info_participants_participantId_8_championId',
                   'info_participants_participantId_8_championName','info_participants_participantId_8_champExperience',
                   'info_participants_participantId_8_champLevel','info_participants_participantId_8_individualPosition',
                   'info_participants_participantId_8_kills','info_participants_participantId_8_deaths',
                   'info_participants_participantId_8_assists','info_participants_participantId_8_totalMinionsKilled', 
                   'info_participants_participantId_8_firstBloodAssist','info_participants_participantId_8_firstBloodKill',
                   'info_participants_participantId_8_firstTowerAssist','info_participants_participantId_8_firstTowerKill',
                   'info_participants_participantId_8_doubleKills','info_participants_participantId_8_tripleKills',
                   'info_participants_participantId_8_doubleKills','info_participants_participantId_8_tripleKills',
                   'info_participants_participantId_8_quadraKills','info_participants_participantId_8_pentaKills',
                   'info_participants_participantId_8_largestKillingSpree','info_participants_participantId_8_largestMultiKill',
                   'info_participants_participantId_8_baronKills','info_participants_participantId_8_dragonKills',
                   'info_participants_participantId_8_objectivesStolen','info_participants_participantId_8_goldEarned',
                   'info_participants_participantId_8_goldSpent','info_participants_participantId_8_magicDamageDealt',
                   'info_participants_participantId_8_magicDamageDealtToChampions','info_participants_participantId_8_magicDamageTaken',
                   'info_participants_participantId_8_physicalDamageDealt','info_participants_participantId_8_physicalDamageDealtToChampions',
                   'info_participants_participantId_8_physicalDamageTaken','info_participants_participantId_8_trueDamageDealt',
                   'info_participants_participantId_8_totalDamageDealt','info_participants_participantId_8_totalDamageDealtToChampions',
                   'info_participants_participantId_8_totalDamageTaken','info_participants_participantId_8_damageSelfMitigated',
                   'info_participants_participantId_8_totalDamageShieldedOnTeammates','info_participants_participantId_8_totalHeal',
                   'info_participants_participantId_8_totalHealsOnTeammates','info_participants_participantId_8_damageDealtToBuildings',
                   'info_participants_participantId_8_damageDealtToObjectives','info_participants_participantId_8_damageDealtToTurrets',
                   'info_participants_participantId_8_nexusKills','info_participants_participantId_8_nexusLost',
                   'info_participants_participantId_8_turretKills','info_participants_participantId_8_turretsLost',
                   'info_participants_participantId_8_inhibitorKills','info_participants_participantId_8_detectorWardsPlaced',
                   'info_participants_participantId_8_wardsKilled','info_participants_participantId_8_wardsPlaced',
                   'info_participants_participantId_8_gameEndedInEarlySurrender','info_participants_participantId_8_gameEndedInSurrender',
                   'info_participants_participantId_8_teamEarlySurrendered','info_participants_participantId_8_teamId',
                   'info_participants_participantId_8_totalTimeSpentDead','info_participants_participantId_8_win',                   
                   'info_participants_participantId_9_summonerLevel','info_participants_participantId_9_championId',
                   'info_participants_participantId_9_championName','info_participants_participantId_9_champExperience',
                   'info_participants_participantId_9_champLevel','info_participants_participantId_9_individualPosition',
                   'info_participants_participantId_9_kills','info_participants_participantId_9_deaths',
                   'info_participants_participantId_9_assists','info_participants_participantId_9_totalMinionsKilled', 
                   'info_participants_participantId_9_firstBloodAssist','info_participants_participantId_9_firstBloodKill',
                   'info_participants_participantId_9_firstTowerAssist','info_participants_participantId_9_firstTowerKill',
                   'info_participants_participantId_9_doubleKills','info_participants_participantId_9_tripleKills',
                   'info_participants_participantId_9_doubleKills','info_participants_participantId_9_tripleKills',
                   'info_participants_participantId_9_quadraKills','info_participants_participantId_9_pentaKills',
                   'info_participants_participantId_9_largestKillingSpree','info_participants_participantId_9_largestMultiKill',
                   'info_participants_participantId_9_baronKills','info_participants_participantId_9_dragonKills',
                   'info_participants_participantId_9_objectivesStolen','info_participants_participantId_9_goldEarned',
                   'info_participants_participantId_9_goldSpent','info_participants_participantId_9_magicDamageDealt',
                   'info_participants_participantId_9_magicDamageDealtToChampions','info_participants_participantId_9_magicDamageTaken',
                   'info_participants_participantId_9_physicalDamageDealt','info_participants_participantId_9_physicalDamageDealtToChampions',
                   'info_participants_participantId_9_physicalDamageTaken','info_participants_participantId_9_trueDamageDealt',
                   'info_participants_participantId_9_totalDamageDealt','info_participants_participantId_9_totalDamageDealtToChampions',
                   'info_participants_participantId_9_totalDamageTaken','info_participants_participantId_9_damageSelfMitigated',
                   'info_participants_participantId_9_totalDamageShieldedOnTeammates','info_participants_participantId_9_totalHeal',
                   'info_participants_participantId_9_totalHealsOnTeammates','info_participants_participantId_9_damageDealtToBuildings',
                   'info_participants_participantId_9_damageDealtToObjectives','info_participants_participantId_9_damageDealtToTurrets',
                   'info_participants_participantId_9_nexusKills','info_participants_participantId_9_nexusLost',
                   'info_participants_participantId_9_turretKills','info_participants_participantId_9_turretsLost',
                   'info_participants_participantId_9_inhibitorKills','info_participants_participantId_9_detectorWardsPlaced',
                   'info_participants_participantId_9_wardsKilled','info_participants_participantId_9_wardsPlaced',
                   'info_participants_participantId_9_gameEndedInEarlySurrender','info_participants_participantId_9_gameEndedInSurrender',
                   'info_participants_participantId_9_teamEarlySurrendered','info_participants_participantId_9_teamId',
                   'info_participants_participantId_9_totalTimeSpentDead','info_participants_participantId_9_win',
                   'info_participants_participantId_10_summonerLevel','info_participants_participantId_10_championId',
                   'info_participants_participantId_10_championName','info_participants_participantId_10_champExperience',
                   'info_participants_participantId_10_champLevel','info_participants_participantId_10_individualPosition',
                   'info_participants_participantId_10_kills','info_participants_participantId_10_deaths',
                   'info_participants_participantId_10_assists','info_participants_participantId_10_totalMinionsKilled', 
                   'info_participants_participantId_10_firstBloodAssist','info_participants_participantId_10_firstBloodKill',
                   'info_participants_participantId_10_firstTowerAssist','info_participants_participantId_10_firstTowerKill',
                   'info_participants_participantId_10_doubleKills','info_participants_participantId_10_tripleKills',
                   'info_participants_participantId_10_doubleKills','info_participants_participantId_10_tripleKills',
                   'info_participants_participantId_10_quadraKills','info_participants_participantId_10_pentaKills',
                   'info_participants_participantId_10_largestKillingSpree','info_participants_participantId_10_largestMultiKill',
                   'info_participants_participantId_10_baronKills','info_participants_participantId_10_dragonKills',
                   'info_participants_participantId_10_objectivesStolen','info_participants_participantId_10_goldEarned',
                   'info_participants_participantId_10_goldSpent','info_participants_participantId_10_magicDamageDealt',
                   'info_participants_participantId_10_magicDamageDealtToChampions','info_participants_participantId_10_magicDamageTaken',
                   'info_participants_participantId_10_physicalDamageDealt','info_participants_participantId_10_physicalDamageDealtToChampions',
                   'info_participants_participantId_10_physicalDamageTaken','info_participants_participantId_10_trueDamageDealt',
                   'info_participants_participantId_10_totalDamageDealt','info_participants_participantId_10_totalDamageDealtToChampions',
                   'info_participants_participantId_10_totalDamageTaken','info_participants_participantId_10_damageSelfMitigated',
                   'info_participants_participantId_10_totalDamageShieldedOnTeammates','info_participants_participantId_10_totalHeal',
                   'info_participants_participantId_10_totalHealsOnTeammates','info_participants_participantId_10_damageDealtToBuildings',
                   'info_participants_participantId_10_damageDealtToObjectives','info_participants_participantId_10_damageDealtToTurrets',
                   'info_participants_participantId_10_nexusKills','info_participants_participantId_10_nexusLost',
                   'info_participants_participantId_10_turretKills','info_participants_participantId_10_turretsLost',
                   'info_participants_participantId_10_inhibitorKills','info_participants_participantId_10_detectorWardsPlaced',
                   'info_participants_participantId_10_wardsKilled','info_participants_participantId_10_wardsPlaced',
                   'info_participants_participantId_10_gameEndedInEarlySurrender','info_participants_participantId_10_gameEndedInSurrender',
                   'info_participants_participantId_10_teamEarlySurrendered','info_participants_participantId_10_teamId',
                   'info_participants_participantId_10_totalTimeSpentDead','info_participants_participantId_10_win',
                   'info_teams_teamId_100_objectives_baron_first','info_teams_teamId_100_objectives_baron_kills',
                   'info_teams_teamId_100_objectives_champion_first','info_teams_teamId_100_objectives_champion_kills',
                   'info_teams_teamId_100_objectives_dragon_first','info_teams_teamId_100_objectives_dragon_kills',
                   'info_teams_teamId_100_objectives_inhibitor_first','info_teams_teamId_100_objectives_inhibitor_kills',
                   'info_teams_teamId_100_objectives_riftHerald_first','info_teams_teamId_100_objectives_riftHerald_kills',
                   'info_teams_teamId_100_objectives_tower_first','info_teams_teamId_100_objectives_tower_kills',
                   'info_teams_teamId_100_win','info_teams_teamId_200_objectives_baron_first','info_teams_teamId_200_objectives_baron_kills',
                   'info_teams_teamId_200_objectives_champion_first','info_teams_teamId_200_objectives_champion_kills',
                   'info_teams_teamId_200_objectives_dragon_first','info_teams_teamId_200_objectives_dragon_kills',
                   'info_teams_teamId_200_objectives_inhibitor_first','info_teams_teamId_200_objectives_inhibitor_kills',
                   'info_teams_teamId_200_objectives_riftHerald_first','info_teams_teamId_200_objectives_riftHerald_kills',
                   'info_teams_teamId_200_objectives_tower_first','info_teams_teamId_200_objectives_tower_kills',
                   'info_teams_teamId_200_win'
                 ]

def renameDf(a,b):
    dic = {}
    for (i,x) in enumerate(a):
        dic[x] = b[i]
    return dic

lol_v3_df = pd.read_excel('data_lol_v3.xlsx')

#Consulta 1 : Media de los niveles de jugadores, el nivel más alto y el mínimo.
means  = []
maxs = []
mins = []
sum_lvl_mean = 0
sum_lvl_max   = 0
sum_lvl_min   = 0

for x in range(1,11):
    columna = 'p' + str(x) + '_summonerLevel'    
    means.append(lol_v3_df[columna].mean())
    maxs.append(lol_v3_df[columna].max())
    mins.append(lol_v3_df[columna].min())
    if x != 10:
        sum_lvl_mean += means[x-1]
    else:
        sum_lvl_mean += means[x-1]
        sum_lvl_mean = sum_lvl_mean/len(means)
        maxs.sort()
        sum_lvl_max = maxs[-1]
        mins.sort()      
        sum_lvl_min = mins[-1]                          

#Consulta 2: Promedio de duración de las partidas en min 

game_duration_mean_min = 0

duracion_num = round(lol_v3_df['gameDuration'].mean())

game_duration_mean_min = duracion_num // 60

#Consulta 3: La partida más larga en min y la más corta en seg

long_game_duration_min  = lol_v3_df['gameDuration'].max() // 60
short_game_duration_min = lol_v3_df['gameDuration'].min() // 60

#Consulta 4: #Los 5 campeones más populares teniendo en cuenta los 5 roles de juego.

Tops = []
Jgs  = []
Mids = []
Adcs = []
Sups = []

for index, row in lol_v3_df.iterrows():
    for x in range(1,11):
        col_line  = 'p' + str(x) + '_individualPosition'   
        col_champ = 'p' + str(x) + '_championName'     
        if row[col_line] == 'TOP':
            Tops.append(row[col_champ])
        elif row[col_line] == 'JUNGLE':
            Jgs.append(row[col_champ])
        elif row[col_line] == 'MIDDLE':
            Mids.append(row[col_champ])
        elif row[col_line] == 'BOTTOM':
            Adcs.append(row[col_champ])
        elif row[col_line] == 'UTILITY':
            Sups.append(row[col_champ])

popular_champs_top = {}
popular_champs_jg = {}
popular_champs_mid = {}
popular_champs_adc = {}
popular_champs_sup = {}


for x in range(0,5):
    if x == 0:
        idx = pd.Index(Tops)
        valores = idx.value_counts()
        for y in range(0,5):
            name   = 'top' + str(y+1) + '_name'
            amount = 'top' + str(y+1) + '_amount'
            popular_champs_top[name]   = valores.index[y]
            popular_champs_top[amount] = valores[y]
    if x == 1:
        idx = pd.Index(Jgs)
        valores = idx.value_counts()
        for y in range(0,5):
            name   = 'jg' + str(y+1) + '_name'
            amount = 'jg' + str(y+1) + '_amount'
            popular_champs_jg[name]   = valores.index[y]
            popular_champs_jg[amount] = valores[y]
    
    if x == 2:
        idx = pd.Index(Mids)
        valores = idx.value_counts()
        for y in range(0,5):
            name   = 'mid' + str(y+1) + '_name'
            amount = 'mid' + str(y+1) + '_amount'
            popular_champs_mid[name]   = valores.index[y]
            popular_champs_mid[amount] = valores[y]
    
    if x == 3:
        idx = pd.Index(Adcs)
        valores = idx.value_counts()
        for y in range(0,5):
            name   = 'adc' + str(y+1) + '_name'
            amount = 'adc' + str(y+1) + '_amount'
            popular_champs_adc[name]   = valores.index[y]
            popular_champs_adc[amount] = valores[y]
    
    if x == 4:
        idx = pd.Index(Sups)
        valores = idx.value_counts()
        for y in range(0,5):
            name   = 'sup' + str(y+1) + '_name'
            amount = 'sup' + str(y+1) + '_amount'
            popular_champs_sup[name]   = valores.index[y]
            popular_champs_sup[amount] = valores[y]


#Consulta 5.-#Promedio de nivel de campeón al final de las partidas

champLevelMean = 0

for x in range(0,10):
    variable = 'p' + str(x+1) + '_champLevel'
    if x != 9:
        champLevelMean += lol_v3_df[variable].mean()        
    else:
        champLevelMean += lol_v3_df[variable].mean()        
        champLevelMean = round(champLevelMean/10)

#Consulta 6 #Línea que realiza la mayor cantidad de kills

linesKills = {'topKills':0 , 'topRepeat':0,'topKillsMean':0,
              'jgKills':0 ,  'jgRepeat':0, 'jgKillsMean':0,
              'midKills':0 , 'midRepeat':0,'midKillsMean':0,
              'adcKills':0 , 'adcRepeat':0,'adcKillsMean':0,
              'supKills':0 , 'supRepeat':0,'supKillsMean':0,}

for index, row in lol_v3_df.iterrows():
    for x in range(1,11):
        col_line  = 'p' + str(x) + '_individualPosition'   
        col_kills = 'p' + str(x) + '_kills'     
        if row[col_line] == 'TOP':
            linesKills['topKills'] += row[col_kills]
            linesKills['topRepeat'] += 1
        elif row[col_line] == 'JUNGLE':
            linesKills['jgKills'] += row[col_kills]
            linesKills['jgRepeat'] += 1
        elif row[col_line] == 'MIDDLE':
            linesKills['midKills'] += row[col_kills]
            linesKills['midRepeat'] += 1
        elif row[col_line] == 'BOTTOM':
            linesKills['adcKills'] += row[col_kills]
            linesKills['adcRepeat'] += 1
        elif row[col_line] == 'UTILITY':
            linesKills['supKills'] += row[col_kills]
            linesKills['supRepeat'] += 1

linesKills['topKillsMean'] = round(linesKills['topKills']/linesKills['topRepeat'],3)
linesKills['jgKillsMean']  = round(linesKills['jgKills']/linesKills['jgRepeat'],3)
linesKills['midKillsMean'] = round(linesKills['midKills']/linesKills['midRepeat'],3)
linesKills['adcKillsMean'] = round(linesKills['adcKills']/linesKills['adcRepeat'],3)
linesKills['supKillsMean'] = round(linesKills['supKills']/linesKills['supRepeat'],3)

#Consulta 7 Línea que realiza la mayor cantidad de muertes

linesDeaths = {'topDeaths':0 , 'topRepeat':0,'topDeathsMean':0,
              'jgDeaths':0 ,  'jgRepeat':0, 'jgDeathsMean':0,
              'midDeaths':0 , 'midRepeat':0,'midDeathsMean':0,
              'adcDeaths':0 , 'adcRepeat':0,'adcDeathsMean':0,
              'supDeaths':0 , 'supRepeat':0,'supDeathsMean':0,}

for index, row in lol_v3_df.iterrows():
    for x in range(1,11):
        col_line  = 'p' + str(x) + '_individualPosition'   
        col_deaths = 'p' + str(x) + '_deaths'     
        if row[col_line] == 'TOP':
            linesDeaths['topDeaths'] += row[col_deaths]
            linesDeaths['topRepeat'] += 1
        elif row[col_line] == 'JUNGLE':
            linesDeaths['jgDeaths'] += row[col_deaths]
            linesDeaths['jgRepeat'] += 1
        elif row[col_line] == 'MIDDLE':
            linesDeaths['midDeaths'] += row[col_deaths]
            linesDeaths['midRepeat'] += 1
        elif row[col_line] == 'BOTTOM':
            linesDeaths['adcDeaths'] += row[col_deaths]
            linesDeaths['adcRepeat'] += 1
        elif row[col_line] == 'UTILITY':
            linesDeaths['supDeaths'] += row[col_deaths]
            linesDeaths['supRepeat'] += 1

linesDeaths['topDeathsMean'] = round(linesDeaths['topDeaths']/linesDeaths['topRepeat'],3)
linesDeaths['jgDeathsMean']  = round(linesDeaths['jgDeaths']/linesDeaths['jgRepeat'],3)
linesDeaths['midDeathsMean'] = round(linesDeaths['midDeaths']/linesDeaths['midRepeat'],3)
linesDeaths['adcDeathsMean'] = round(linesDeaths['adcDeaths']/linesDeaths['adcRepeat'],3)
linesDeaths['supDeathsMean'] = round(linesDeaths['supDeaths']/linesDeaths['supRepeat'],3)


#Consulta 8 Línea que realiza la mayor cantidad de Asistencias

linesAssists = {'topAssists':0 , 'topRepeat':0,'topAssistsMean':0,
              'jgAssists':0 ,  'jgRepeat':0, 'jgAssistsMean':0,
              'midAssists':0 , 'midRepeat':0,'midAssistsMean':0,
              'adcAssists':0 , 'adcRepeat':0,'adcAssistsMean':0,
              'supAssists':0 , 'supRepeat':0,'supAssistsMean':0,}

for index, row in lol_v3_df.iterrows():
    for x in range(1,11):
        col_line  = 'p' + str(x) + '_individualPosition'   
        col_assists = 'p' + str(x) + '_assists'     
        if row[col_line] == 'TOP':
            linesAssists['topAssists'] += row[col_assists]
            linesAssists['topRepeat'] += 1
        elif row[col_line] == 'JUNGLE':
            linesAssists['jgAssists'] += row[col_assists]
            linesAssists['jgRepeat'] += 1
        elif row[col_line] == 'MIDDLE':
            linesAssists['midAssists'] += row[col_assists]
            linesAssists['midRepeat'] += 1
        elif row[col_line] == 'BOTTOM':
            linesAssists['adcAssists'] += row[col_assists]
            linesAssists['adcRepeat'] += 1
        elif row[col_line] == 'UTILITY':
            linesAssists['supAssists'] += row[col_assists]
            linesAssists['supRepeat'] += 1

linesAssists['topAssistsMean'] = round(linesAssists['topAssists']/linesAssists['topRepeat'],3)
linesAssists['jgAssistsMean']  = round(linesAssists['jgAssists']/linesAssists['jgRepeat'],3)
linesAssists['midAssistsMean'] = round(linesAssists['midAssists']/linesAssists['midRepeat'],3)
linesAssists['adcAssistsMean'] = round(linesAssists['adcAssists']/linesAssists['adcRepeat'],3)
linesAssists['supAssistsMean'] = round(linesAssists['supAssists']/linesAssists['supRepeat'],3)

#Consulta 9: Línea que realiza el mayor KDA

KDAlines = {'topKDA':0,'jgKDA':0,'midKDA':0,'adcKDA':0,'supKDA':0}

KDAlines['topKDA'] = round((linesKills['topKills'] + linesAssists['topAssists'])/linesDeaths['topDeaths'],3)
KDAlines['jgKDA'] = round((linesKills['jgKills'] + linesAssists['jgAssists'])/linesDeaths['jgDeaths'],3)
KDAlines['midKDA'] = round((linesKills['midKills'] + linesAssists['midAssists'])/linesDeaths['midDeaths'],3)
KDAlines['adcKDA'] = round((linesKills['adcKills'] + linesAssists['adcAssists'])/linesDeaths['adcDeaths'],3)
KDAlines['supKDA'] = round((linesKills['supKills'] + linesAssists['supAssists'])/linesDeaths['supDeaths'],3)


#Consulta 10 11 12 13: Campeón que realiza la mayor cantidad de kills

#Obtención de un array con todos los campeones:

p1_champs = list(lol_v3_df['p1_championName'].unique())
p2_champs = list(lol_v3_df['p2_championName'].unique())
p3_champs = list(lol_v3_df['p3_championName'].unique())
p4_champs = list(lol_v3_df['p4_championName'].unique())
p5_champs = list(lol_v3_df['p5_championName'].unique())
p6_champs = list(lol_v3_df['p6_championName'].unique())
p7_champs = list(lol_v3_df['p7_championName'].unique())
p8_champs = list(lol_v3_df['p8_championName'].unique())
p9_champs = list(lol_v3_df['p9_championName'].unique())
p10_champs = list(lol_v3_df['p10_championName'].unique())

champions_set = [p1_champs,p2_champs,p3_champs,p4_champs,p5_champs,p6_champs,p7_champs,p8_champs,p9_champs,p10_champs]

champs = list({ champ  for champions in champions_set for champ in champions })

champsKillsMean   = {}
champsAssistsMean = {}
champsDeathsMean  = {}
champsKillsAmount   = {}
champsAssistsAmount = {}
champsDeathsAmount = {}
champsKDA     = {}
#Agregamos el número de kills por cada campeón

for champ in champs:
    champsKillsMean[champ]   = 0
    champsAssistsMean[champ] = 0
    champsDeathsMean[champ]  = 0
    champsKillsAmount[champ]   = 0
    champsAssistsAmount[champ] = 0
    champsDeathsAmount[champ]  = 0
for index, row in lol_v3_df.iterrows():
    for x in range(1,11):
        col_champ  = 'p' + str(x) + '_championName'   
        col_kills  = 'p' + str(x) + '_kills'
        col_deaths  = 'p' + str(x) + '_deaths'
        col_assists  = 'p' + str(x) + '_assists'    
        champsKillsMean[row[col_champ]]   += row[col_kills]
        champsDeathsMean[row[col_champ]]  += row[col_deaths]
        champsAssistsMean[row[col_champ]] += row[col_assists]
        champsKillsAmount[row[col_champ]]   += 1        
        champsDeathsAmount[row[col_champ]]  += 1
        champsAssistsAmount[row[col_champ]] += 1
     
for champ in champs:
    champsKillsMean[champ]   = champsKillsMean[champ]/champsKillsAmount[champ] 
    champsDeathsMean[champ]  = champsDeathsMean[champ]/champsDeathsAmount[champ]        
    champsAssistsMean[champ] = champsAssistsMean[champ]/champsAssistsAmount[champ]
    champsKDA[champ] = round((champsKillsMean[champ] + champsAssistsMean[champ])/champsDeathsMean[champ],3)

champsKillsOrder = sorted(champsKillsMean.items(),key=operator.itemgetter(1),reverse=True)
champsDeathsOrder  = sorted(champsDeathsMean.items(),key=operator.itemgetter(1),reverse=True)
champsAssistsOrder = sorted(champsAssistsMean.items(),key=operator.itemgetter(1),reverse=True)
champsKDAOrder = sorted(champsKDA.items(),key=operator.itemgetter(1),reverse=True)

print(champsKillsOrder)
#Consulta 14: Promedio de Barons Nashor por equipo

teamBlueNashors = round(lol_v3_df['team_100_obj_baron_kills'].mean(),5)

teamRedNashors = round(lol_v3_df['team_200_obj_baron_kills'].mean(),5)

#Consulta 15: Promedio de Dragones por equipo

teamBlueDragons = round(lol_v3_df['team_100_obj_dragon_kills'].mean(),5)

teamRedDragons = round(lol_v3_df['team_200_obj_dragon_kills'].mean(),5)

#Consulta 16: Campeones con mayor cantidad de pentakills

champsPentakills = {}

for champ in champs:
    champsPentakills[champ] = 0

for index, row in lol_v3_df.iterrows():
    for x in range(1,11):
        col_champ  = 'p' + str(x) + '_championName'   
        col_pentakills  = 'p' + str(x) + '_pentaKills'   
        champsPentakills[row[col_champ]]   += row[col_pentakills]

champsPentaKillsOrder = sorted(champsPentakills.items(),key=operator.itemgetter(1),reverse=True)

#Consulta 17: Proporción del dinero ganado y gastado

propGoldEarnedSpent = 0
goldCount = 0
for index, row in lol_v3_df.iterrows():
    
    for x in range(1,11):
        goldCount += 1
        col_goldEarned  = 'p' + str(x) + '_goldEarned'   
        col_goldSpent   = 'p' + str(x) + '_goldSpent'  
        propGoldEarnedSpent += row[col_goldSpent]/row[col_goldEarned]

    if index == list(lol_v3_df.index)[-1]:
        propGoldEarnedSpent = propGoldEarnedSpent/goldCount




#Consulta 18: Campeones que realizan mayor daño mágico a campeones

champsMagicDamage = {}
champsMagicDamageMean = {}
champsCount = 0
for champ in champs:
    champ_repeat = champ + '_repeat'
    champsMagicDamage[champ] = 0
    champsMagicDamage[champ_repeat] = 0

for index, row in lol_v3_df.iterrows():
    for x in range(1,11):        
        col_champ  = 'p' + str(x) + '_championName'   
        col_magicDamage   = 'p' + str(x) + '_magicDamageDealtToChampions'  
        magicDamage = row[col_magicDamage]
        champ_repeat = row[col_champ] + '_repeat'
        champsMagicDamage[row[col_champ]] += magicDamage
        champsMagicDamage[champ_repeat] += 1
    
for champ in champs:
    champ_repeat = champ + '_repeat'
    champsMagicDamageMean[champ] = round(champsMagicDamage[champ]/champsMagicDamage[champ_repeat],3)

champsMagicDamageMeanOrder = sorted(champsMagicDamageMean.items(),key=operator.itemgetter(1),reverse=True)

#Consulta 19: Campeones que realizan mayor daño físico a campeones

champsPhysicalDamage = {}
champsPhysicalDamageMean = {}
champsCount = 0
for champ in champs:
    champ_repeat = champ + '_repeat'
    champsPhysicalDamage[champ] = 0
    champsPhysicalDamage[champ_repeat] = 0

for index, row in lol_v3_df.iterrows():
    for x in range(1,11):        
        col_champ  = 'p' + str(x) + '_championName'   
        col_physicalDamage   = 'p' + str(x) + '_physicalDamageDealtToChampions'  
        physicalDamage = row[col_physicalDamage]
        champ_repeat = row[col_champ] + '_repeat'
        champsPhysicalDamage[row[col_champ]] += physicalDamage
        champsPhysicalDamage[champ_repeat] += 1
    
for champ in champs:
    champ_repeat = champ + '_repeat'
    champsPhysicalDamageMean[champ] = round(champsPhysicalDamage[champ]/champsPhysicalDamage[champ_repeat],3)

champsPhysicalDamageMeanOrder = sorted(champsPhysicalDamageMean.items(),key=operator.itemgetter(1),reverse=True)

#Consulta 20: Campeones que realizan mayor daño total a campeones

champsTotalDamage = {}
champsTotalDamageMean = {}
champsCount = 0
for champ in champs:
    champ_repeat = champ + '_repeat'
    champsTotalDamage[champ] = 0
    champsTotalDamage[champ_repeat] = 0

for index, row in lol_v3_df.iterrows():
    for x in range(1,11):        
        col_champ  = 'p' + str(x) + '_championName'   
        col_totalDamage   = 'p' + str(x) + '_totalDamageDealtToChampions'  
        totalDamage = row[col_totalDamage]
        champ_repeat = row[col_champ] + '_repeat'
        champsTotalDamage[row[col_champ]] += totalDamage
        champsTotalDamage[champ_repeat] += 1
    
for champ in champs:
    champ_repeat = champ + '_repeat'
    champsTotalDamageMean[champ] = round(champsTotalDamage[champ]/champsTotalDamage[champ_repeat],3)

champsTotalDamageMeanOrder = sorted(champsTotalDamageMean.items(),key=operator.itemgetter(1),reverse=True)

#Consulta 21: Lineas ordendas segun su win rate

linesWinRate = {'topWins':0 , 'topLosses':0,'topWinRate':0,
                'jgWins':0 ,  'jgLosses':0, 'jgWinRate':0,
                'midWins':0 , 'midLosses':0,'midWinRate':0,
                'adcWins':0 , 'adcLosses':0,'adcWinRate':0,
                'supWins':0 , 'supLosses':0,'supWinRate':0,}

for index, row in lol_v3_df.iterrows():
    for x in range(1,11):
        col_line  = 'p' + str(x) + '_individualPosition'   
        col_win = 'p' + str(x) + '_win'     
        if row[col_line] == 'TOP':
            if row[col_win]:
                linesWinRate['topWins'] += 1
            else:
                linesWinRate['topLosses'] += 1
        elif row[col_line] == 'JUNGLE':
            if row[col_win]:
                linesWinRate['jgWins'] += 1
            else:
                linesWinRate['jgLosses'] += 1
        elif row[col_line] == 'MIDDLE':
            if row[col_win]:
                linesWinRate['midWins'] += 1
            else:
                linesWinRate['midLosses'] += 1
        elif row[col_line] == 'BOTTOM':
            if row[col_win]:
                linesWinRate['adcWins'] += 1
            else:
                linesWinRate['adcLosses'] += 1
        elif row[col_line] == 'UTILITY':
            if row[col_win]:
                linesWinRate['supWins'] += 1
            else:
                linesWinRate['supLosses'] += 1

linesWinRate['topWinRate'] = round(linesWinRate['topWins']/(linesWinRate['topWins'] + linesWinRate['topLosses']),4)
linesWinRate['jgWinRate']  = round(linesWinRate['jgWins']/(linesWinRate['jgWins'] + linesWinRate['jgLosses']),4)
linesWinRate['midWinRate'] = round(linesWinRate['midWins']/(linesWinRate['midWins'] + linesWinRate['midLosses']),4)
linesWinRate['adcWinRate'] = round(linesWinRate['adcWins']/(linesWinRate['adcWins'] + linesWinRate['adcLosses']),4)
linesWinRate['supWinRate'] = round(linesWinRate['supWins']/(linesWinRate['supWins'] + linesWinRate['supLosses']),4)



#Consulta 22: 5 Campeones con más win rate

champsWinsLosses = {}
champsWinRate = {}

for champ in champs:
    champ_win    = champ + '_win'
    champ_losses = champ + '_losses'
    champsWinsLosses[champ_win] = 0
    champsWinsLosses[champ_losses] = 0

for index, row in lol_v3_df.iterrows():
    for x in range(1,11):        
        col_champ  = 'p' + str(x) + '_championName'   
        col_win   = 'p' + str(x) + '_win'          
        champ_win = row[col_champ] + '_win'
        champ_losses = row[col_champ] + '_losses'
        if row[col_win]:
            champsWinsLosses[champ_win] += 1
        else:
            champsWinsLosses[champ_losses] += 1
    
for champ in champs:
    champ_win    = champ + '_win'
    champ_losses = champ + '_losses'
    champsWinRate[champ] = round(champsWinsLosses[champ_win]/(champsWinsLosses[champ_win]+champsWinsLosses[champ_losses]),4)

champsWinRateOrder = sorted(champsWinRate.items(),key=operator.itemgetter(1),reverse=True)
