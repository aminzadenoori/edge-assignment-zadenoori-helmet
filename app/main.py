import time

from app.client import Client
from app.cv_camera import CVCamera
#from app.ssd.detector import Detector
from app.utils.logger import logger
from app.config.environment import ENVIRONMENT
from app.Helmet_detection_YOLOV3 import helmetcounter


def run():
    #detector = Detector()
    client = Client()
    with CVCamera(resolution=(1920, 1080), framerate=30) as camera:
        logger.info('Init completed')
        while True:
            frame = camera.capture()
            count,infrence_time =helmetcounter(
                input_image=frame
            )
            logger.info('People: %d Inference time: %.2fs' % (count, infrence_time))
            client.send_people_count(count)
            time.sleep(ENVIRONMENT.SHOT_DELAY)


if __name__ == '__main__':
    run()
