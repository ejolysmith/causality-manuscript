from typing import List

import delta
import os
import numpy as np
import glob
from delta.utilities import find_contours, CroppingBox
import delta.utilities as utils

class Experiment:

    def __init__(self,
                 path,
                 segmentation_channel = 0,
                 delta_config_file = None,
                 file_counter_init = 0):

        self.segmentation_channel = segmentation_channel
        self.path = path

        if delta_config_file is None:
            delta_config_file = "/home/laurent/.delta/config_mothermachine_gen_train.json"

        delta.config.load_config(delta_config_file)

        if os.path.isdir(path):
            self.type = 'folder'
            self.files = sorted(glob.glob(path + '*.tif*') + glob.glob(path + '*.czi'))
            self.number_files = len(self.files)
            self.reader = [delta.utilities.xpreader(f, use_bioformats=True, segmentation_channel=self.segmentation_channel) for f in self.files]
        else:
            self.type = 'file'
            self.files = path
            self.path = "/".join(self.path.split('/')[0:-1]) + "/"
            self.number_files = 1
            self.reader = delta.utilities.xpreader(self.files, use_bioformats=True, segmentation_channel=self.segmentation_channel)

        self.proc = []
        self.file_counter = file_counter_init

    def generate_training_data(self,
                               output_path = None,
                               ):
        if output_path is None:
            output_path = os.path.join(self.path,"out/")

        if os.path.exists(output_path) is False:
            os.mkdir(output_path)

        if os.path.exists(os.path.join(output_path, "img/")) is False:
            os.mkdir(os.path.join(output_path, "img/"))

        if os.path.exists(os.path.join(output_path, "seg/")) is False:
            os.mkdir(os.path.join(output_path, "seg/"))

        for r in [self.reader]:
            #with delta.pipeline.Pipeline(r,  resfolder=output_path) as processor:
            processor = delta.pipeline.Pipeline(r,  resfolder=output_path)
            processor.preprocess()
            #self.proc.append(processor)

            # Output images and masks from segmented data

            for pos in processor.positions[0:30]:
                # TODO: argument for specifying both brightfield and fluo
                pos.reader.segmentation_channel = (pos.reader.segmentation_channel + 1) % 2  # 1->0, 0->1
                pos.segment(list(range(processor.reader.timepoints)))

                # Now need to get Bf images
                pos.reader.segmentation_channel = (pos.reader.segmentation_channel + 1) % 2  # 1->0, 0->1
                # Load trans frames:
                trans_frames = pos.reader.getframes(
                    positions=pos.position_nb,
                    channels=pos.reader.segmentation_channel,
                    frames=list(range(processor.reader.timepoints)),
                    rescale=(0, 1),
                    rotate=pos.rotate,
                )

                # If trans_frames is 2 dimensions, an extra dimension is added at axis=0 for time
                # (1 timepoint may cause this issue)
                if trans_frames.ndim == 2:
                    trans_frames = trans_frames[np.newaxis, :, :]

                # Correct drift:
                if pos.drift_correction:
                    trans_frames, pos.drift_values = utils.driftcorr(
                        trans_frames, template=pos.drifttemplate, box=pos.driftcorbox
                    )

                # Run through frames and ROIs and compile segmentation inputs:
                for roi in pos.rois:
                    roi.img_stack = []
                    for img in trans_frames:
                        roi.get_segmentation_inputs(img)
                        #inputs,windows = roi.get_segmentation_inputs(img)
                        #roi.img_stack.append(np.squeeze(inputs))

                for rois in pos.rois:
                    filelist = []

                    for i in range(len(rois.img_stack)):
                        #filelist.append( 'Pos01_Chamber' + str(rois.roi_nb) + 'Frame' + str(i) + '.png')
                        filelist.append( 'Sample{:08d}.png'.format(self.file_counter))
                        self.file_counter += 1

                    if np.sum(np.array(rois.seg_stack)[:]) > 50:
                        delta.data.saveResult_seg(os.path.join(output_path, 'img/'), np.array(rois.img_stack), filelist)
                        delta.data.saveResult_seg(os.path.join(output_path, 'seg/'), np.array(rois.seg_stack), filelist)
                    else:
                        # 5% chance keeping empty trenches
                        if np.random.rand() < 0.05:
                            delta.data.saveResult_seg(os.path.join(output_path, 'img/'), np.array(rois.img_stack), filelist)
                            delta.data.saveResult_seg(os.path.join(output_path, 'seg/'), np.array(rois.seg_stack), filelist)

            del processor




def getROIBoxes_target_size(chambersmask: np.ndarray, target_size) -> List[CroppingBox]:
    """
    Extract the bounding boxes of the chambers in the binary mask
    produced by the chambers identification unet

    Parameters
    ----------
    chambersmask : 2D array of uint8/uint16/floats
        The mask of the chambers as returned by the chambers id unet.

    Returns
    -------
    chamberboxes : list of dictionaries
        List of cropping box dictionaries (see cropbox()).

    """

    import cv2
    import numpy as np

    tar_height = target_size[0]
    tar_width = target_size[1]

    chamberboxes = []
    if chambersmask.dtype == bool:
        chambersmask = chambersmask.astype(np.uint8)
    else:
        chambersmask = cv2.threshold(chambersmask, 0.5, 1, cv2.THRESH_BINARY)[1].astype(
            np.uint8
        )
    contours = find_contours(chambersmask)
    for chamber in contours:
        xtl, ytl, boxwidth, boxheight = cv2.boundingRect(chamber)

        extra_width = tar_width - boxwidth
        extra_height = tar_height - boxheight
        xtl_temp=int(xtl-np.ceil(extra_width/2))
        ytl_temp=int(ytl-np.ceil(extra_height/2))
        xbr_temp=int(xtl+np.floor(extra_width/2)+boxwidth)
        ybr_temp=int(ytl+np.floor(extra_height/2)+boxheight)
        x_size = np.shape(chambersmask)[1]
        y_size = np.shape(chambersmask)[0]

        if boxheight < tar_height and boxwidth < tar_width and xtl_temp >=0 and ytl_temp >=0 and xbr_temp <= x_size \
                and ybr_temp <= y_size:
            # Do not resize if box is smaller than target

            chamberboxes.append(
                CroppingBox(
                    xtl=int(xtl-np.ceil(extra_width/2)),
                    ytl=int(ytl-np.ceil(extra_height/2)),
                    xbr=int(xtl+np.floor(extra_width/2)+boxwidth),
                    ybr=int(ytl+np.floor(extra_height/2)+boxheight),
                )
            )  # tl = top left, br = bottom right.

        else: # don't add it
           """ chamberboxes.append(
                CroppingBox(
                    xtl=xtl,
                    ytl=int(
                        ytl - (boxheight * 0.1)
                    ),  # -10% of height to make sure the top isn't cropped
                    xbr=xtl + boxwidth,
                    ybr=ytl + boxheight,
                )
            )  # tl = top left, br = bottom right."""
    chamberboxes.sort(
        key=lambda elem: elem["xtl"]
    )  # Sorting by top-left X (normally sorted by Y top left)
    return chamberboxes


def make_weights(base_directory):
    import tqdm
    import skimage.io as io
    import tifffile
    import os


    wc = {
        0: 1, # background
        1: 5,  # objects
        255: 1 # objects in 8bits
    }
    masks_dir = base_directory + "seg/"
    masks_files = os.listdir(masks_dir)

    for x in range(len(masks_files)):
        fext = os.path.splitext(masks_files[x])[1].lower()
        if fext in (".png", ".jpg", ".jpeg"):
            image = io.imread(base_directory + "seg/" + masks_files[x], as_gray=True)
        elif fext in (".tif", ".tiff"):
            image = tifffile.imread(base_directory + "seg/" + masks_files[x])
        else:
            raise ValueError("Only PNG, JPG or single-page TIF files accepted")

        w = unet_weight_map(image, wc)
        image = w.astype(np.uint8)

        if fext in (".png", ".jpg", ".jpeg"):
            image = io.imsave(base_directory + "wei/" + masks_files[x], image, check_contrast=False)
        elif fext in (".tif", ".tiff"):
            image = tifffile.imsave(base_directory + "wei/" + masks_files[x], image)
        else:
            raise ValueError("Only PNG, JPG or single-page TIF files accepted")


def unet_weight_map(y, wc=None, w0 = 10, sigma = 5):

    """
    Generate weight maps as specified in the U-Net paper
    for boolean mask.

    "U-Net: Convolutional Networks for Biomedical Image Segmentation"
    https://arxiv.org/pdf/1505.04597.pdf

    Parameters
    ----------
    mask: Numpy array
        2D array of shape (image_height, image_width) representing binary mask
        of objects.
    wc: dict
        Dictionary of weight classes.
    w0: int
        Border weight parameter.
    sigma: int
        Border width parameter.

    Returns
    -------
    Numpy array
        Training weights. A 2D array of shape (image_height, image_width).
    """
    from scipy.ndimage.morphology import distance_transform_edt
    from skimage.measure import label

    labels = label(y)
    no_labels = labels == 0
    label_ids = sorted(np.unique(labels))[1:]

    if len(label_ids) > 1:
        distances = np.zeros((y.shape[0], y.shape[1], len(label_ids)))

        for i, label_id in enumerate(label_ids):
            distances[:,:,i] = distance_transform_edt(labels != label_id)

        distances = np.sort(distances, axis=2)
        d1 = distances[:,:,0]
        d2 = distances[:,:,1]
        w = w0 * np.exp(-1/2*((d1 + d2) / sigma)**2) * no_labels
    else:
        w = np.zeros_like(y)
    if wc:
        class_weights = np.zeros_like(y)
        for k, v in wc.items():
            class_weights[y == k] = v
        w = w + class_weights
    return w
