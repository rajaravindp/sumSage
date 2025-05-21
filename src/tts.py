import os
import boto3
from typing import IO

def tts(text, voice_id="Ivy", output_format="mp3", language_code="en-US") -> IO[bytes]:
    """
    Convert text to speech using Amazon Polly.
    """
    session = boto3.Session()
    polly_client = session.client(
        service_name='polly',
        verify=False)

    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat=output_format,
        VoiceId=voice_id,
        LanguageCode=language_code
    )

    return response['AudioStream']