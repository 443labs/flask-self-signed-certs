# Flask App Demo

The purpose of this python project is to expose a small flask app using self-signed certificates.

## Setup

```shell
# create a virtual environment
python3 -m venv venv

# activate the virtual environment
. venv/bin/activate

# upgrade pip
pip install --upgrade pip

# install requirements
pip install -r requirements.txt

# launch locally
python3 app.py
```

## Freezing Requirements

Please run the following command to freeze requirements in a consistent manner, when adding new modules to the project.

```shell
pip freeze | LC_COLLATE=C sort > requirements.txt
```

## Routes

The following routes are supported:
* `GET /` => Returns a sample JSON payload.
* `POST /` => Echos any JSON payload, or returns the sample JSON.

## Testing

* Browser: You may visit https://127.0.0.1:5000/ in a browser. Be aware that you will be warned about the self-signed cert.
* Curl: `curl -k -X POST -H 'Content-Type: application/json' https://127.0.0.1:5000/ -d '{"name":"mark"}'`

## Viewing the SSL Certificate (openssl)

You may use a variety of tools to inspect the certificate, including a browser, openssl, or curl.

Here are a few examples.

```shell
# openssl
openssl s_client -connect 127.0.0.1:5000

# output
CONNECTED(00000003)
depth=0 O = Dummy Certificate, CN = *
verify error:num=18:self signed certificate
verify return:1
depth=0 O = Dummy Certificate, CN = *
verify return:1
---
Certificate chain
 0 s:/O=Dummy Certificate/CN=*
   i:/O=Dummy Certificate/CN=*
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDAzCCAeugAwIBAgIUE+BlM8wrL4IWtTV98FcDmKBZ2cIwDQYJKoZIhvcNAQEL
BQAwKDEaMBgGA1UECgwRRHVtbXkgQ2VydGlmaWNhdGUxCjAIBgNVBAMMASowHhcN
MjIwNzAxMTY0ODUxWhcNMjMwNzAxMTY0ODUxWjAoMRowGAYDVQQKDBFEdW1teSBD
ZXJ0aWZpY2F0ZTEKMAgGA1UEAwwBKjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCC
AQoCggEBAI3YPlC9ZmrotBmaVb57JldjWmxFy5Uxcv5Xl2EnzksOZly2odbw39RZ
GpFKXTULJbawlPrHvgiofxD+lJwNzjfG4q7b2aKui9u9qjY+6eLiI7xwz7Ggpqos
lwK9rElOJssg1AtFjNXn9BM4atkxSejKuWMiIYcITRxBDP93wfbsYerZNzFjFwt0
cqlxIq31j/+esyVGaJ09T9LjGfk5lpGY32ZZs7uWg9dBwtwR9LoZzMNOhe9Whqlj
GE4oHV1pTu/W9ZMvZ4CQX+odSTfKtmR28tHrrdGufvemQl8O/I+e6Sv4pWRluosP
U2I8o+YkkvwAO6Y3oe0F1NPM3F4xqekCAwEAAaMlMCMwEwYDVR0lBAwwCgYIKwYB
BQUHAwEwDAYDVR0RBAUwA4IBKjANBgkqhkiG9w0BAQsFAAOCAQEABAn8YIH0byiM
irIH4+V09AxNrhCF+j5rHDPoXb89SNBxPVlVDdI4N4foPU31jDnPhtRRUJMCvBaq
8AYb2c6q9bIaXLo7ZoZx5iGO+oFqP+TrP/5LNnZQZEmI+kLZjL0s5adSvTxEMhJB
vqt0CgXPGJZT3loQHDCoC3dSB8LS2yGrBpA8Bxj4vvg6Mxm6G+EOKTpMVaIyq//j
1gAY53VkQAx3xcRcibipVcuIlGTf/aeKI+1qe18TdR1GRhwVIwTC/US0uJY+cr5A
WGnvLDcdT+fLKlQy82S4HQjFqYVvEXeOX7Ol57ygYEtn2nLqR0psqIlCOWLERDkO
7TjplQGtEQ==
-----END CERTIFICATE-----
subject=/O=Dummy Certificate/CN=*
issuer=/O=Dummy Certificate/CN=*
---
No client certificate CA names sent
Server Temp Key: ECDH, X25519, 253 bits
---
SSL handshake has read 1396 bytes and written 289 bytes
---
New, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 2BFFD22F80C22073A647EEE3526F00D38F0FD8A6081B54B86C4A66735444EB82
    Session-ID-ctx:
    Master-Key: 33D609BCC2498C06EAA774F44F22F5CCC66FE96C9E440C8D885ABAB7EC166E6DDFAACCE15618F48CEDBBBF9778C07B10
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 70 da 86 28 17 44 34 7c-51 f3 4c c3 df af 4d 4a   p..(.D4|Q.L...MJ
    0010 - 13 ab 82 20 57 33 28 a1-67 ec 11 06 9e c1 b8 e6   ... W3(.g.......
    0020 - c2 e6 52 10 24 f8 25 62-db 02 69 e8 32 66 a8 e8   ..R.$.%b..i.2f..
    0030 - 0d b6 38 cb df eb 66 74-98 7d 75 33 c8 f7 39 b9   ..8...ft.}u3..9.
    0040 - 8a 64 f9 8c 08 6a a4 68-96 11 5c 38 96 59 89 07   .d...j.h..\8.Y..
    0050 - e0 68 07 bd 9f 6b b1 2a-ae 88 6c 29 7f 8f c8 dc   .h...k.*..l)....
    0060 - f2 ae 5f 36 4e a0 cf 0e-07 43 62 2c 83 2c 2d 10   .._6N....Cb,.,-.
    0070 - bc a8 a2 05 a7 73 ca c3-ba f0 78 1b c1 77 16 34   .....s....x..w.4
    0080 - 20 22 7f 5c 35 a6 5e c4-5d 19 c5 a9 2a 66 52 a8    ".\5.^.]...*fR.
    0090 - db c0 c8 98 01 43 ec 54-6e 8a 38 88 d1 d5 25 33   .....C.Tn.8...%3

    Start Time: 1656694842
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
```

Or, you may prefer to view the SSL handshake using curl:

```shell
# curl
curl -kvv https://127.0.0.1:5000/

# output
*   Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*  CAfile: /etc/ssl/cert.pem
*  CApath: none
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384
* ALPN, server did not agree to a protocol
* Server certificate:
*  subject: O=Dummy Certificate; CN=*
*  start date: Jul  1 16:48:51 2022 GMT
*  expire date: Jul  1 16:48:51 2023 GMT
*  issuer: O=Dummy Certificate; CN=*
*  SSL certificate verify result: self signed certificate (18), continuing anyway.
> GET / HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/7.77.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Server: Werkzeug/2.1.2 Python/3.9.4
< Date: Fri, 01 Jul 2022 17:01:30 GMT
< Content-Type: application/json
< Content-Length: 117
< Connection: close
<
{
  "hostname": "Marks-MacBook-Pro.local",
  "local-time": "2022-07-01T12:01:21.854127-05:00",
  "method": "GET"
}
* Closing connection 0
* TLSv1.2 (OUT), TLS alert, close notify (256):
```