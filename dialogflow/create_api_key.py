from environs import Env

from dialogflow_utils import create_api_key


def main():
    env = Env()
    env.read_env()
    project_id = env.str('GOOGLE_CLOUD_PROJECT_ID')

    with open('project_api_key.txt', 'a', encoding='utf-8') as stream:
        stream.write(str(create_api_key(project_id)))


if __name__ == '__main__':
    main()
