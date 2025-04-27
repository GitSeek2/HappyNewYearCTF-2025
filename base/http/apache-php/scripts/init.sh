#!/bin/bash

rm -rf /init.sh

if [ -z "$GZCTF_FLAG" ]; then
    export GZCTF_FLAG="flag{seek_to_geek}"
fi

apachectl -D FOREGROUND