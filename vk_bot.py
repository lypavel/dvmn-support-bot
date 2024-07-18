import logging
from random import randint

from environs import Env

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType

from dialogflow import detect_intent_text

logger = logging.getLogger(__name__)


def reply_to_user(event, vk_api, project_id):
    reply_text = detect_intent_text(
        project_id,
        event.user_id,
        event.text
    )

    vk_api.messages.send(
        user_id=event.user_id,
        message=reply_text,
        random_id=randint(1, 1000)
    )


def main() -> None:
    env = Env()
    env.read_env()

    project_id = env.str('GOOGLE_CLOUD_PROJECT_ID')
    vk_api_token = env.str('VK_API_KEY')

    vk_session = vk.VkApi(token=vk_api_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            reply_to_user(event, vk_api, project_id)


if __name__ == '__main__':
    main()
