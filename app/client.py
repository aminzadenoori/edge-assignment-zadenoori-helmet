from typing import Tuple
from app.utils.logger import logger
from app.config.environment import ENVIRONMENT

import requests


def init_os_variables() -> Tuple[int, str]:
    auth_key = ENVIRONMENT.AUTH_KEY
    if auth_key is None:
        raise Exception('Missing env variables.')
    try:
        device_id = ENVIRONMENT.DEVICE_ID
    except TypeError:
        raise Exception('Missing env variables.')

    return device_id, auth_key


class Client:
    def __init__(self, ip: str = 'api.koone.io', port: int = 443):
        self.ip = ip
        self.port = port
        self.device_id, self.auth_key = init_os_variables()
        self.api_count = self.make_url(api='/v1/edge/%d' % self.device_id)
        self.payload = {'auth_key': self.auth_key, 'count': 0}

    def send_people_count(self, count: int):
        if not isinstance(count, int):
            raise TypeError('Count should be a positive integer.')
        if count < 0:
            raise ValueError('Count cannot be negative.')
        self.payload['count'] = count
        try:
            req = requests.post(self.api_count, params=self.payload)
        except Exception as e:
            print(e)
        else:
            log_info(req)

    def make_url(self, protocol: str = 'https', api: str = '/') -> str:
        return '{}://{}:{}{}'.format(protocol, self.ip, self.port, api)


def log_info(resp: requests.Response):
    logger.info(resp.url)
    print('--------------------------------------')
    logger.info(resp.status_code)
    print('--------------------------------------')
    logger.info(resp.text)
    print('--------------------------------------')
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
