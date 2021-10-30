# HTTPOXY
## Injection of environment variable via "Proxy:" HTTP Header
### Can lead to SSRF

### Run in docker:
```
cd 1-httpoxy
```

### Explanation
HTTP Server will interpret Proxy: header value and try to connect to it. This can lead to SSRF.

### References and recommended reading
https://httpoxy.org/

### Credits:
https://github.com/vulhub/vulhub/tree/4d17ab2d4df39eefad5c498c5aa60b036a05494d/cgi/httpoxy

