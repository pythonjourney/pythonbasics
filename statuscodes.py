201 - Resource has been created ( resource id returned )


200 - Resource has been created ( Details of rsource has been returned )


204 - Resource processed successfully with no content returned 

400 Bad Request - when you send something wrong in the request data


4XX - Fault with client (Its beowser or Request )


409 - ( Conflict Response ) - Entity you are creating already existing in the system

404 - Resource not found


GET Request is Idempotent - its gives some response when you do multiple get 

Do not send any request body in the get request

get rewuest will give same results if you send it multipe times

POST URI'S can have Path Parameter

Should never have a query parameter

Preferably should have a Request Payload



