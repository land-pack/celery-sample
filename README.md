#Celery Sample
Currently, I work with `celery`,but I have no deep understand it, so I have write this simple demo for beginer like me for now!

###How do we need to install?
-----------------------------

```
pip install -r requirements.txt

```

###How to run this demmo?
-------------------------
It's also very simple, just need to open three terminal for now.

terminal-A

```
redis-server
```

terminal-B

```
celery worker -A celery_http_client -l info -c 5
```
My system is kali linux, I run as `root` user, so the celery default are no like to run, you need to set a env variable, if you have the same situation like me just simple run `export C_FORCE_ROOT` command.

terminal-C

```
python celery_http_client.py
```
We tell the celery , we got some job and you need to help me ...

