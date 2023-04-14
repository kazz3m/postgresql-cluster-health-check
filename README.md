# postgresql-cluster-health-check
PostgreSQL simple HTTP service with MASTER/REPLICA check for load balancers

What you need?
1. Credentials in .pgpass file
2. Python3 with psycopg2


# Master / Replica response

```
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.6.8
Date: Fri, 14 Apr 2023 23:34:40 GMT
Content-Type: text/html

MASTER%
```

```
HTTP/1.0 203 Non-Authoritative Information
Server: BaseHTTP/0.6 Python/3.6.8
Date: Fri, 14 Apr 2023 23:31:05 GMT
Content-Type: text/html

REPLICA%
```
