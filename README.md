# pythonbasics

 Python is a case sensitive programming language


<VirtualHost *:80>
    ServerName 172.16.9.137  
    ProxyPreserveHost On
    ProxyPass /
http://localhost:8080/
    ProxyPassReverse /
http://localhost:8080/
</VirtualHost>


kkkkkkkkkkkkkkkkkkk
