#!/bin/sh

rm -rf /init.sh

if [ -z "$GZCTF_FLAG" ]; then
    GZCTF_FLAG="flag{seek_to_geek}"
fi

echo -n $GZCTF_FLAG > /home/ctf/flag
unset GZCTF_FLAG

socat TCP-LISTEN:70,reuseaddr,fork EXEC:/run.sh,stderr