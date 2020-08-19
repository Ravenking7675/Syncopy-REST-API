# Syncopy RestAPI

This API will enable you to sync clipboard content among multiple devices.

## End Points

**/login**  [POST] : To login the User 
	
**/logout**  [POST] : To logout the User
	
**/register**  [POST] : To register a new User
 
**/clip**  [POST] : To send clipboard data to the API
		
**/sent/{user_id}/**  [GET] : To get all the clip data from **{user_id}** (Sender Side)

**/recieved/{user_id}/**  [GET] : To get all the clip data from **{user_id}** (Reciever Side)

**/sent/{user_id}/{n}**  [GET] : To get **{n}** clip data from **{user_id}** 

**/sent/{user_id}/1**  [GET] : To get the latest clip data from **{user_id}** (Sorted by [time])

**/sent/{user_id}/1**  [PUT] : To update {checked = True} int the latest clip data from **{user_id}** (Sorted by [time])
 
 
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
|1|user1|1|user2|2|0|878372873|"Copied Text 1"|1|
|2|user2|2|user1|1|1|989127937|"Copied Text 2"|2|


> checked is a boolen ; 0 ->> True & 1->> False
> user_id is a sudo column for One-To-Many Relationship
> "master" ->> is a relational variable in User Table 
