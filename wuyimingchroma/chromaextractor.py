#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:08:30 2018

@author: wuyiming
"""

import numpy as np
from . import networks as N
from librosa.util import find_files
from librosa.core import cqt,load,note_to_hz
import os
from . import const as C
from . import utils as U


def get_chroma(audiofile=None, y=None, modeldir=C.DEFAULT_CONVNETFILE):
    #load audio
    if y is None and audiofile is None:
        raise ValueError("Either audiofile or y variables must be passed to get_chroma function")
    elif y is None:
        y,sr = load(audiofile,sr=C.SR)
    
    #extract Harmonic-CQT from audio
    fmin = note_to_hz("C1")
    hcqt = np.stack([np.abs(cqt(y,sr=C.SR,hop_length=C.H,n_bins=C.BIN_CNT,bins_per_octave=C.OCT_BIN,fmin=fmin*(h+1),filter_scale=2,tuning=None)).T.astype(np.float32) for h in range(C.CQT_H)])
    
    #extract feature using trained CNN extractor
    cnn_feat_extractor = N.FullCNNFeatExtractor()
    cnn_feat_extractor.load(modeldir)
    
    feat = cnn_feat_extractor.GetFeature(U.PreprocessSpec(hcqt)).data
    return feat
