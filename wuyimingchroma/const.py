#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:11:24 2017

@author: wuyiming
"""

import pathlib, os
thispath = pathlib.Path(__file__).parent.resolve()

DEFAULT_CONVNETFILE = os.path.join(thispath, "fullcnn_crossentropy_6000.model")
DEFAULT_CONVNETFILE_DEEPCHROMA = os.path.join(thispath, "convnet_deepchroma.model")
DEFAULT_DNNFILE = os.path.join(thispath, "DRN_crossentropy_2000.model")

#PATH_MIDICQT = "/home/wuyiming/Projects/TranscriptionChordRecognition/Datas/midicqt/"
PATH_MIDI = os.path.join(thispath, "/home/wuyiming/Projects/TranscriptionChordRecognition/Datas/midi")
#PATH_CQT = "/home/wuyiming/Projects/ChordData/CQT/"
PATH_HCQT = os.path.join(thispath, "Datas/specs_train")
#PATH_HCQT = "../CQT_H_12/"
PATH_AUDIO = os.path.join(thispath, "/home/wuyiming/Projects/ChordData/Audio")
PATH_CHORDLAB = os.path.join(thispath, "Datas/labels_train")
#PATH_CHORDLAB = "MIREXresults/Truth"
#PATH_CHORDLAB = "../chordlab"
PATH_ESTIMATE = os.path.join(thispath, "Datas/labs_estimated/")
PATH_ESTIMATE_CROSS = os.path.join(thispath, "Datas/estimated_cross/")
#PATH_ESTIMATE_CROSS = "MIREXresults/KBK1"
PATH_SONIFYTEST = os.path.join(thispath, "Datas/sonify/")
PATH_MIDIHCQT = os.path.join(thispath, "/media/wuyiming/TOSHIBA EXT/midihcqt_24/")
#PATH_MIDIHCQT = "../midihcqt_12/"

SR = 44100
H = 4096

OCT_BIN = 12
OCTAVE = 7
CQT_H = 5
BIN_CNT = OCT_BIN*OCTAVE

N_CHORDS = 12*2+1


CONV_TRAIN_SEQLEN = 128
CONV_TRAIN_BATCH = 64

DECODER_TRAIN_SEQLEN = 128
DECODER_TRAIN_BATCH = 64

DNN_TRAIN_BATCH = 64

HIDDEN_UNITS = [512,512,512,512,512]
