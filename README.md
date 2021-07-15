# Automatic Audio Chord Recognition with MIDI-Traind Deep Feature and BLSTM-CRF Sequence Decoding Model

My version of the original work so it can be used as a package

```python
from wuyimingchroma import get_chroma
import librosa

y, sr = librosa.load(librosa.example('brahms'), sr=44100)

chroma = get_chroma(y=y)
print(chroma.shape)
```

