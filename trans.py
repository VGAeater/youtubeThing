#!/usr/bin/env python3

import wave
import sys
import json

from vosk import Model, KaldiRecognizer, SetLogLevel

SetLogLevel(0)

wf = wave.open("audio.wav", "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Audio file must be WAV format mono PCM.")
    sys.exit(1)

model = Model(lang="en-us")

rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)
rec.SetPartialWords(True)

while True:
    data = wf.readframes(wf.getnframes())
    if len(data) == 0:
        break
    rec.AcceptWaveform(data)

with open("sub.ass", "w") as file:
    file.write(
"""[Script Info]
PlayResY: 600
WrapStyle: 1

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,Strikeout,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Info, Futura, 40, &H00FFFFFF, &H000000FF, &H00000000, &H00000000, 1, 0, 0, 0, 100, 100, 0, 0, 5, 5, 10, 5, 0010, 0010, 0000, 0

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""")

    for blah in json.loads(rec.FinalResult())["result"]:
        start = float(blah["start"])
        end = float(blah["end"])
        file.write("Dialogue: 0, "+str(format(start/3600, "0.0f"))+":"+str(format(start/60%60, "02.0f"))+":"+str(format(start%60, "05.2f"))+", "+str(format(end/3600, "0.0f"))+":"+str(format(end/60%60, "02.0f"))+":"+str(format(end%60, "05.2f"))+", Info, , 0, 0, 0, , "+blah["word"]+"\n")