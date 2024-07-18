from environs import Env
from google.cloud import api_keys_v2, dialogflow
from google.cloud.api_keys_v2 import Key


def create_api_key(project_id: str) -> Key:
    client = api_keys_v2.ApiKeysClient()

    key = api_keys_v2.Key()
    key.display_name = 'API key'

    request = api_keys_v2.CreateKeyRequest()
    request.parent = f'projects/{project_id}/locations/global'
    request.key = key

    response = client.create_key(request=request).result()

    print(f'Successfully created an API key: {response.name}')
    return response


def detect_intent_text(project_id: str,
                       session_id: str,
                       text: str,
                       language_code: str = 'ru'):
    '''Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation.'''
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={'session': session, 'query_input': query_input}
    )

    return response.query_result.fulfillment_text, \
        response.query_result.intent.is_fallback


def main():
    env = Env()
    env.read_env()
    project_id = env.str('GOOGLE_CLOUD_PROJECT_ID')

    with open('project_api_key.txt', 'a', encoding='utf-8') as stream:
        stream.write(str(create_api_key(project_id)))


if __name__ == '__main__':
    main()
