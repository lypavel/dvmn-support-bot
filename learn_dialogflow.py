import json

from environs import Env
from google.cloud import dialogflow


def create_intent(project_id,
                  display_name,
                  training_phrases_parts,
                  message_text):
    """Create an intent of the given intent type."""

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(
            text=training_phrases_part
        )

        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=[message_text])
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))


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
