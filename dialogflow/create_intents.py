import json

from environs import Env

from dialogflow_utils import create_intent


def main() -> None:
    env = Env()
    env.read_env()
    project_id = env.str('GOOGLE_CLOUD_PROJECT_ID')

    with open('questions.json', 'r', encoding='utf-8') as stream:
        intents_json = stream.read()
    intents = json.loads(intents_json)

    for intent, messages in intents.items():
        create_intent(
            project_id,
            intent,
            messages['questions'],
            messages['answer']
        )


if __name__ == '__main__':
    main()
