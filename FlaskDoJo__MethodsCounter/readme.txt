Simple application to practice basic of Flask
In order to sent any other methods then GET and POST please use curl or simmilar app.
Curl is installed as default on Macs so I use Curl here.
For Curl please write in terminal:
curl -X PUT  http://127.0.0.1:8000/request-counter
or
curl -X DELETE  http://127.0.0.1:8000/request-counter

explanation:
curl -X <method>                specify the method will be sent (may me any of methods)
http://127.0.0.1:8000           address to local host with port 8000
/request-counter                route used in the server in this __init__.py 


