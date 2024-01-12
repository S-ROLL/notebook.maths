# Prompt
```
Make an example sentence of ... in english and illustrate its example by image.
```
```
Make an English vocabulary list 10 words for the topic about ... and put the IPA, part of speech, CEFR level and meaning after every single word.
```
```
Give me 50 English words for the topic about ...
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
# gTTS
```python
from gtts import gTTS
x = gTTS('ACB', lang='en')
x.save('x.mp3')
```
> ``x`` is a numbered lists. <br/>
> ``ACB`` is vocab.
# Macro for making numbered lists in vim
1. Type ``1``
1. On line 1 press ``qw`` to start recording
1. Execute ``yyp^Ctrl-Aj``
1. Press ``q`` to stop recording.
1. Press ``8@a`` to add items 3 to 10.

