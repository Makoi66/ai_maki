from google.generativeai.types import HarmCategory, HarmBlockThreshold


tele_token = '7032308631:AAHT2LCpKNJ4ckInsmHoFTOzULY5HB5FnzE'


models_tokens = {
    'gemini': 'AIzaSyCc_9tNmMDtL_4IDJ0H6hDWSJ7F4e26KLk',
}


models = [
    'models/gemini-2.0-flash',
    'models/gemini-2.0-pro-exp'
]

gemini_settings = {
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
}