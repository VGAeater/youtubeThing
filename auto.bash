#!/bin/bash


python3 main.py
python3 trans.py

IFS=',' read -ra ADDR <<< $(tail -n 1 sub.ass)
stopat=${ADDR[2]}

ffmpeg -i source.mp4 -t ${stopat}s -vf "fade=in:0:d=0.5, fade=out:1783.5:d=0.5, ass=sub.ass, crop=w=810:h=1440:x=875:y=0" -y next.mp4
ffmpeg -i next.mp4 -i audio.mp3 -map 0:v -map 1:a -c:v copy -c:a copy -y output.mp4

python3 upload.py
