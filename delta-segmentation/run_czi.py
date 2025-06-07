#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import delta
import tensorflow as tf

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
  tf.config.experimental.set_memory_growth(gpu, True)

delta.config.load_config('models/config_mothermachine-1.json')

file_path = delta.config.eval_movie

# Init xpreader:
reader = delta.utilities.xpreader(
    '/media/euan/SP PHD U3/Data/EJ_MM6/EJ_MM6-01.czi',
    use_bioformats=True,
    segmentation_channel = 0,
    roi_channel = 0
)


print("""Initialized experiment reader:
    - %d positions
    - %d imaging channels
    - %d timepoints"""%(reader.positions, reader.channels, reader.timepoints)
)

# Init pipeline:
xp = delta.pipeline.Pipeline(reader)

xp.process()
