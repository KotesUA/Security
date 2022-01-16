Tried dictionary on md5:
```commandline
hashcat -m 0 -a 0 -d 1 md5.csv top_100k.txt
```
Result:
```commandline
Time.Started.....: Sun Jan 16 23:15:04 2022 (1 min, 44 secs)
Recovered........: 47905/72400 (66.17%) Digests
Remaining........: 24495 (33.83%) Digests
```
_

With mask ?1?2?2?2?2?2?2:
```commandline
hashcat -m 0 -a 3 -d 1 md5.csv
```
Result:
```commandline
Speed.#1.........:   221.9 MH/s (13.12ms) @ Accel:16 Loops:32 Thr:256 Vec:1
Recovered........: 47905/72400 (66.17%) Digests
```
_

Also tried with sha1-salt and argon2i from different classmates, but kept recieving this error:
```commandline
Hashfile 'sha1_salt.csv' on line 54323 (9073a6...4d90197386c521e,09c2810034142e6d): Separator unmatched
```
hashcat -m 110 -a 0 -d 1 strongHashes.csv top_100k.txt