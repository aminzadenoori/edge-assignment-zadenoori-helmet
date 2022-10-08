import os
import shutil
from datetime import datetime
from typing import Tuple, Optional
from app.config.environment import ENVIRONMENT

import cv2 as cv
import numpy as np

DATA_DIR = '/usr/src/app/data'
FILENAME = os.path.join(DATA_DIR, '%s.png')
MAX_PHOTOS = 30


def to_rgb(bgr_image: np.ndarray) -> np.ndarray:
    return cv.cvtColor(bgr_image, cv.COLOR_BGR2RGB)


def clean_data():
    shutil.rmtree(DATA_DIR)
    os.makedirs(DATA_DIR)


def save_frame(frame: np.ndarray):
    """Save OpenCV frame to file

    :param frame: a bgr frame
    """
    now = datetime.now()
    cv.imwrite(FILENAME % now.strftime('%Y-%m-%d_%H-%M-%S'), frame)


class CVCamera:
    def __init__(self, resolution: Optional[Tuple[int, int]] = None, framerate: Optional[int] = None):
        """Initialize the CVCamera object

        NOTE: The parameters are unused right now, they are there only for
        Compatibility with PiCamera

        :param resolution:
        :param framerate:
        """
        self.device = cv.VideoCapture('/dev/video0', cv.CAP_V4L)
        self.device.set(cv.CAP_PROP_FRAME_WIDTH, 2592)
        self.device.set(cv.CAP_PROP_FRAME_HEIGHT, 1944)
        self.count = 0
        clean_data()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.device.release()

    def capture(self) -> Optional[np.ndarray]:
        _, frame = self.device.read()
        if frame is None:
            raise Exception('Error: cannot grab a photo from the camera')
        if self.count < MAX_PHOTOS:
            self.count += 1
            save_frame(frame)
        return to_rgb(frame)


if __name__ == '__main__':
    import time

    with CVCamera() as camera:
        while camera.count < 50:
            camera.capture()
            time.sleep(2)
