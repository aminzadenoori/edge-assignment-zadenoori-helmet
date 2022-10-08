from datetime import datetime

import slack
from app.config.environment import ENVIRONMENT

CLIENT = slack.WebClient(token=ENVIRONMENT.SLACK_TOKEN)

def send_slack_message(path:str, error:str)->None:
    """_summary_

    Parameters
    ----------
    path : str
        _description_
    error : str
        _description_
    """
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    TEXT = f"Something went wrong with: {path}! Error: {error}"
    CLIENT.chat_postMessage(
        channel="C040WL00GLV", 
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "emoji": True,
                    "text": "Oooops...Something went wrong with the script!!!!"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*<{ENVIRONMENT.SLACK_ERROR_LINK}|{ENVIRONMENT.SLACK_ERROR_LINK_NAME}>*\n{TEXT}"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://cdn-icons-png.flaticon.com/512/682/682010.png",
                    "alt_text": "notifications warning icon"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://api.slack.com/img/blocks/bkb_template_images/notificationsWarningIcon.png",
                        "alt_text": "notifications warning icon"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Error occurs at: {now}*"
                    }
                ]
            }
        ]
    )