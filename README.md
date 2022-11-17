# Brincando_com_Sockets

## Como rodar o servidor httpd Docker:

```console
foo@bar:~$ docker build -t <myname>/httpd .
foo@bar:~$ docker run -p 8888:80 -d <myname>/httpd
```