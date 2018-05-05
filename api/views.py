import random

from django.http import HttpResponse

import json

from api.models import Game


def index(request):
    return HttpResponse("<h1>Hello, world. you're visiting one of the world's best game \"MAFIA\".</H1>")

def createNewGame(request):
    response={}
    reqMethod = getPostOrGetRequest(request)
    print request.GET
    gameName = reqMethod.get("gameName")
    player = reqMethod.get("playerCount")
    try:
        gameObj = Game.objects.filter(name=gameName)[0]
        if gameObj:
            gameObj.player = player
            gameObj.save()
            response = generateStatusJson('success', 'Game updated successfully')

        else:
            gameObj = Game(name=gameName, player=player)
            gameObj.save()
            response = generateStatusJson('success', 'Game created successfully')

    except  Exception as e:
        response = generateStatusJson('error', e.message.encode('ascii', 'ignore').strip())

    return HttpResponse(response,content_type='application/json')


def addRoles(request):
    response={}
    reqMethod = getPostOrGetRequest(request)
    gameName = reqMethod.get("gameName")
    roles = reqMethod.get("roles")
    try:
        gameObj = Game.objects.filter(name=gameName)[0]
        print roles
        if gameObj:
            data = json.loads(roles)
            total = 0
            for item in data:
                val = data[item]
                total = total + int(val)

            if(total== gameObj.player):
                gameObj.roles = roles
                gameObj.save()
                response = generateStatusJson('success', 'roles updated successfully')
            else:
                response = generateStatusJson('error', 'Count does not match player count')
        else:
            response = generateStatusJson('error', 'Game not found')

    except  Exception as e:
        response = generateStatusJson('error', e.message.encode('ascii', 'ignore').strip())

    return HttpResponse(response, content_type='application/json')


def addPlayer(request):
    response={}
    reqMethod = getPostOrGetRequest(request)
    gameName = reqMethod.get("gameName")
    playerName = reqMethod.get("playerName")
    try:
        gameObj = Game.objects.filter(name=gameName)[0]
        if gameObj:
            playerDetails = gameObj.playerDetails
            data = json.loads(playerDetails)
            if(gameObj.player > len(data)):
                if(not playerDetails.__contains__(str(playerName))):
                    data[playerName] = ""
                    print data
                    gameObj.playerDetails = json.dumps(data)
                    gameObj.save()
                    response = generateStatusJson('id', playerName)
                else:
                    response = generateStatusJson('error', 'Player already available')
            else:
                response = generateStatusJson('error', 'Game is full')
        else:
            response = generateStatusJson('error', 'Game not found')

    except  Exception as e:
        response = generateStatusJson('error', e.message.encode('ascii', 'ignore').strip())

    return HttpResponse(response, content_type='application/json')


def assignRoles(request):
    response = {}
    reqMethod = getPostOrGetRequest(request)
    gameName = reqMethod.get("gameName")
    try:
        gameObj = Game.objects.filter(name=gameName)[0]
        if gameObj:
            playerDetails = gameObj.playerDetails
            playerdata = json.loads(playerDetails)
            if len(playerdata) == gameObj.player:
                roles = gameObj.roles
                data = json.loads(roles)
                randomList = []
                for item in data:
                    val = data[item]
                    for i in range(0,int(val)):
                        randomList.append(item)
                random.shuffle(randomList)

                i=0
                for item in playerdata:
                    playerdata[item] = randomList.__getitem__(i)
                    i=i+1
                gameObj.playerDetails = json.dumps(playerdata)
                gameObj.save()
                response = generateStatusJson('success', 'Roles assigned')
            else:
                response = generateStatusJson('error', 'Players not enough')
        else:
            response = generateStatusJson('error', 'Game not found')

    except Exception as e:
        response = generateStatusJson('error', e.message.encode('ascii', 'ignore').strip())

    return HttpResponse(response, content_type='application/json')


def getRole(request):
    response = {}
    reqMethod = getPostOrGetRequest(request)
    gameName = reqMethod.get("gameName")
    playerId = reqMethod.get("playerId")
    try:
        gameObj = Game.objects.filter(name=gameName)[0]
        if gameObj:
            playerDetails = gameObj.playerDetails
            playerdata = json.loads(playerDetails)
            if(playerDetails.__contains__(playerId)):
                if(playerdata[playerId]==""):
                    response = generateStatusJson('error', 'Roles not assigned')
                else:
                    response = generateStatusJson('success', playerdata[playerId])
            else:
                response = generateStatusJson('error', 'Player not found')
        else:
            response = generateStatusJson('error', 'Game not found')

    except Exception as e:
        response = generateStatusJson('error', e.message.encode('ascii', 'ignore').strip())

    return HttpResponse(response, content_type='application/json')


def resetGame(request):
    response = {}
    reqMethod = getPostOrGetRequest(request)
    print request.GET
    gameName = reqMethod.get("gameName")
    player = reqMethod.get("playerCount")
    try:
        gameObj = Game.objects.filter(name=gameName)[0]
        if gameObj:
            playerDetails = gameObj.playerDetails
            playerdata = json.loads(playerDetails)
            for item in playerdata:
                playerdata[item] = ""
            gameObj.playerDetails = json.dumps(playerdata)
            gameObj.save()
            response = generateStatusJson('success', 'Game reseted successfully')

        else:
            response = generateStatusJson('error', 'Game not found')

    except  Exception as e:
        response = generateStatusJson('error', e.message.encode('ascii', 'ignore').strip())

    return HttpResponse(response, content_type='application/json')


# to be moved to framework
def getPostOrGetRequest(request):
    if (request.method == 'GET'):
        reqMethod = request.GET
    elif (request.method == 'POST'):
        reqMethod = request.POST
    return reqMethod

def generateStatusJson(status,message):

    responseDict = {}
    responseDict = generateStatusDict(status,message)
    return str(json.dumps(responseDict))

def generateStatusDict(status,message):

    responseDict = {}
    responseDict["status"] = status
    responseDict["message"] = message
    return responseDict