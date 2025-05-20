from google.generativeai.types import HarmCategory, HarmBlockThreshold


tele_token = ''


models_tokens = {
    'gemini': '',
}


models = [
    'models/gemini-2.5-flash-preview-05-20',
    'jopa/ne_najimai'
]

gemini_settings = {
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
}