from argparse import ArgumentParser, Namespace
import json
from pathlib import Path

from environs import Env

from dialogflow_utils import create_intent


def parse_arguments() -> Namespace:
    parser = ArgumentParser(
        description='Script for creating intents in Dialogflow agent.'
    )

    parser.add_argument(
        '--file_path',
        type=str,
        help='Path to JSON file with intents information.',
        required=False,
        default='questions.json'
    )

    return parser.parse_args()


def main() -> None:
    env = Env()
    env.read_env()
    project_id = env.str('GOOGLE_CLOUD_PROJECT_ID')

    args = parse_arguments()

    file_path = Path(args.file_path)

    with open(file_path, 'r', encoding='utf-8') as stream:
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
