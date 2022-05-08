#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:08:30 2018

@author: wuyiming & TW
"""

import numpy as np
from . import networks as N
from librosa.util import find_files
from librosa.core import cqt,load,note_to_hz
import os
from . import const as C
from . import utils as U

def estimate_chords(audiofile):
    fname = audiofile.split("/")[-1]
    print("Processing: %s" % fname)
    #load audio
    y,sr = load(audiofile,sr=C.SR)

    #extract Harmonic-CQT from audio
    fmin = note_to_hz("C1")
    hcqt = np.stack([np.abs(cqt(y,sr=C.SR,hop_length=C.H,n_bins=C.BIN_CNT,bins_per_octave=C.OCT_BIN,fmin=fmin*(h+1),filter_scale=2,tuning=None)).T.astype(np.float32) for h in range(C.CQT_H)])

    #extract feature using trained CNN extractor
    cnn_feat_extractor = N.FullCNNFeatExtractor()
    cnn_feat_extractor.load('fullcnn_crossentropy_6000.model')

    feat = cnn_feat_extractor.GetFeature(U.PreprocessSpec(hcqt)).data

    #decode label sequence
    decoder = N.NBLSTMCRF()
    decoder.load("nblstm_crf.model")

    labels = decoder.argmax(feat)

    #convert into .lab file
    labfile = os.path.join("Datas/labs_estimated",fname+".lab")
    U.SaveEstimatedLabelsFramewise(labels,labfile,feat)
    return labfile
