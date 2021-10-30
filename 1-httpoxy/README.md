# HTTPOXY
## Injection of environment variable via "Proxy:" HTTP Header
### Can lead to SSRF

### Run in docker:
```
docker run
```

### Explanation
HTTP Server will interpret Proxy: header value and try to connect to it. This can lead to SSRF.

### References and recommended reading
https://httpoxy.org/

### Credits:
https://github.com/vulhub/vulhub/tree/4d17ab2d4df39eefad5c498c5aa60b036a05494d/cgi/httpoxy
![image](https://user-images.githubusercontent.com/31791455/139532989-b9cbaa6e-6ab9-4b64-86ba-23f1153b2bc6.png)

