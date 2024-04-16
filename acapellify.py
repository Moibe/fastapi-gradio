from gradio_client import Client

def acapellify(audio_path):
    client = Client("Moibe/basico")
    result = client.predict(audio_path, api_name="/predict")
    return result