# Steam Community Proxy in China #

For some unknown reason , Steam Community was blocked in Mainland of China. Steam Client use HTTP to get data from steam server. However, GFW would send a TCP RST package when connection to steam community was found, which would make steam got error `-101` or error `-118` in community pages.

This script would respond HTTP 301 to forward HTTP to HTTPS and forward all HTTPS data.

## usage ##

* install python (i only tested on python 3)
* clone or download this repo
* run steamproxy.py or ``import steamproxy`` and write your own main entry
* edit your host file.(you can append these lines if you run on localhost )

```
# Steam Community in China

127.0.0.1 steamcommunity.com
```

## License ##

WTFPL

## TODO ##

wait valve update `/public/url_list.txt`. all `%community%` should replaced by `%communityhttps%`.

I can't edit this file directly for steam would detect hash change and repair this file by it self.
