# mafia-webapp
Simple Django Application for mafia game

URL: https://mafias.herokuapp.com

Moderator APIs

Create Game
API:  /api/createNewGame/?gameName=test&playerCount=11
PARAM : gameName,playerCount
Response:  {"status": "success", "message": "Game updated successfully"}, 

Create Roles
API :  /api/addRoles/?gameName=test&roles={"mafia":3,"angel":1,"civilian":4,"joker":1,"detective":1}
PARAM : gameName,roles(jsonFormat)
RESPONSE: {"status": "success", "message": "roles updated successfully"}, {"status": "error", "message": "Game not found"}, {"status": "error", "message": "Count does not match player count"}

Assign Roles
API : /api/assignRoles/?gameName=test
PARAM: gameName
RESPONSE: {"status": "success", "message": "Roles assigned"}


Player APIs

Join Game
API:  /api/addPlayer/?gameName=test&playerName=kmk11
PARAM : gameName,playerName
Response:  {"status": "id", "message": "kmk6"} (kmk6 will be the player ID), {"status": "error", "message": "Game is full"},{"status": "error", "message": "Player already available"}

Get role
API: /api/getRole/?gameName=test&playerId=kmk3
PARAM : gameName,playerId
Response:  {"status": "success", "message": "civilian"} , {"status": "error", "message": "Player not found"}, {"status": "error", "message": "Roles not assigned"}

 Leave game
API: /api/leaveGame/?gameName=test&playerId=kmk61
PARAM : gameName,playerId
Response:  {"status": "success", "message": "player deleted"},{"status": "error", "message": "Player not available"}
