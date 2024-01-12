Prompt: maximum 9 words
```
Make image example for the meaning of words: "". With single words single example image. fit the frame picture.
```
```
Make an image to illustrate this text: "".
```
```
Make an example sentence of ... in english and illustrate its example by image.
```
# Anki
- **FRONT**
  - ``Vocab``
- **BACK**
  - chatGPT 
    - ``IPA``
  - gTTS
    - ``MP3``
  - Cambridge dictionary
    - ``Type``
    - ``Level``
    - ``meaning``
  - chatGPT
    - ``image``
    - ``example``
   
```
from gtts import gTTS
x = gTTS('ACB', lang='en')
x.save('x.mp3')
```
## Macro for making numbered lists in vim
```
1. Type ``1``
1. On line 1 press ``qw`` to start recording
1. Execute ``yyp^Ctrl-Aj``
1. Press ``q`` to stop recording.
1. Press ``8@a`` to add items 3 to 10.
```

