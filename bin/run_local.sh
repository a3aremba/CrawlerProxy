#!/bin/sh
folder_prefix=$(git rev-parse --show-toplevel);
ps ax | grep $folder_prefix/virtenv/bin/mitmdump | awk '{print $1}' | xargs kill -9;
nohup $folder_prefix/virtenv/bin/mitmdump -p 9999 -s $folder_prefix/proxyScript.py &