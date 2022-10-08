import os
import pathlib
import time

import numpy as np
import tflite_runtime.interpreter as tflite
from PIL import Image

from . import detect
from app.utils.utils import convert_infr_time_to_fps


class Detector:
    """
    Detector class is a high level class for detecting object using Raspberry devices.
    When an instance of the Detector is created you can call inference method and feed your
    input image in order to get the detection results.
    """

    def __init__(self):
        self.fps = None
        self.inference_time = None
        self.name = 'ssd_mobilenet_v2_coco_quant_postprocess'
        current_dir = pathlib.Path(__file__).parent
        model_path = os.path.join(current_dir, 'yolov4-416-fp16.tflite')
        self.interpreter = tflite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()

    def __del__(self):
        del self.interpreter

    def inference(self, input_image: np.ndarray, score_th=0.5) -> int:
        """Run inference on an image and get Frames rate (fps)

        :param input_image: A numpy array with shape [height, width, channels]
        :param score_th: score threshold
        :return: List of objects, each obj is a dict with two keys "id" and "bbox" and "score"
            e.g. [{"id": 0, "bbox": [x1, y1, x2, y2], "score":s%}, {...}, {...}, ...]
        """
        image = Image.fromarray(np.uint8(input_image))

        # Start inference time
        t_begin = time.perf_counter()
        scale = detect.set_input(self.interpreter, image.size,
                                 lambda size: image.resize(size, Image.ANTIALIAS))
        self.interpreter.invoke()
        objs = detect.get_output(self.interpreter, score_threshold=score_th, image_scale=scale)

        self.inference_time = time.perf_counter() - t_begin  # Seconds

        self.fps = convert_infr_time_to_fps(self.inference_time)

        return sum(obj.id == 0 for obj in objs)
