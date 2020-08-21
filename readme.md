# Syncopy RestAPI

This API will enable you to sync clipboard content among multiple devices.

## Heroku URL

[heroku-syncopy](https://syncopy-api.herokuapp.com)


## End Points

 [POST] **/auth** : To login the User 
 
 [POST] **/refresh** : To refresh JWT token
	
 [POST] **/logout** : To logout the User
	
 [POST] **/register**  : To register a new User
 
 [POST] **/clip** : To send clipboard data to the API
		
 [GET] **/sent/{user_id}/** : To get all the clip data from **{user_id}** (Sender Side)

 [DEL] **/sent/{user_id}/** : To delete all the clip data from **{user_id}** (Sender Side)

 [GET] **/recieved/{user_id}/** : To get all the clip data from **{user_id}** (Reciever Side)

 [GET] **/sent/{user_id}/{n}** : To get **{n}** clip data from **{user_id}** (Sender Side)
 
 [GET] **/recieved/{user_id}/{n}** : To get **{n}** clip data from **{user_id}** (Reciever Side) 

 [GET] **/sent/{user_id}/1** : To get the latest clip data from **{user_id}** (Sorted by [time])

 [PUT] **/sent/{user_id}/1** : To update {checked = True} int the latest clip data from **{user_id}** (Sorted by [time])
 
 [POST] **/generate_key** : To generate UUID for a user 
 #### payload:
 
 {
    "unique_str": "12312312321312312",
    "username": "pranav",
    "isPc": true
 } 
 
 [POST] **/add_connections** : Adds user data in connections table to establish a two way connection
 #### payload:
  {
    "uuid_sender": "11v2rr",
    "uuid_reciever": "33a3rr"
  }
  
 [GET] **/connections/{UUID}/** : To get all the available connections for given UUID
 
 [GET] **/key/{username}/** : To get UUID for given username

 
 
## Database Structure
	User Table and Clipboard Table have a One-To-Many Relationship

### Clipboard Table (clipboard)

|id|sender|sender_id|reciever|reciever_id|checked|time|content|user_id|
|----------------|-------------|--------|----|-----|-----|-------|------|------|
|1|user1|1|user2|2|0|878372873|"Copied Text"|1|
|2|user2|2|user1|1|1|989127937|"Copied Text"|2|

### User Table (userdata)
| id               |username                       |uuid                        | isPc
|----------------|-------------------------------|-----------------------------|--------------------|
|1|user1|usu231|0|
|2|user2|j233bq|1|

### Connection Table (connections)
| id               |id_sender                       |id_reciever    
|----------------|-------------------------------|-----------------------------
|1|2|3
|2|3|2

> connections table with create a two way data for every connection

> checked is a boolen ; 0 ->> True & 1->> False
