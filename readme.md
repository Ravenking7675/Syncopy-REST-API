# Syncopy RestAPI

This API will enable you to sync clipboard content among multiple devices.

## End Points

 [POST] **/auth** : To login the User 
	
 [POST] **/logout** : To logout the User
	
 [POST] **/register**  : To register a new User
 
 [POST] **/clip** : To send clipboard data to the API
		
 [GET] **/sent/{user_id}/** : To get all the clip data from **{user_id}** (Sender Side)

 [GET] **/recieved/{user_id}/** : To get all the clip data from **{user_id}** (Reciever Side)

 [GET] **/sent/{user_id}/{n}** : To get **{n}** clip data from **{user_id}** 

 [GET] **/sent/{user_id}/1** : To get the latest clip data from **{user_id}** (Sorted by [time])

 [PUT] **/sent/{user_id}/1** : To update {checked = True} int the latest clip data from **{user_id}** (Sorted by [time])
 
 
## Database Structure
	User Table and Clipboard Table have a One-To-Many Relationship

### User Table
| id               |username                       |password                        |
|----------------|-------------------------------|-----------------------------|
|1|user1|pass1|
|2|user2|pass2|

### Clipboard Table

|id|sender|sender_id|reciever|reciever_id|checked|time|content|user_id|
|----------------|-------------|--------|----|-----|-----|-------|------|------|
|1|user1|1|user2|2|0|878372873|"Copied Text"|1|
|2|user2|2|user1|1|1|989127937|"Copied Text"|2|


> checked is a boolen ; 0 ->> True & 1->> False
