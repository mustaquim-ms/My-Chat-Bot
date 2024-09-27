import openai
import logging

class Chatbot:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        logging.basicConfig(level=logging.INFO)

    def respond(self, message):
        try:
            if not self.openai_api_key:
                raise ValueError("OpenAI API key is required.")

            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=message,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            logging.info("OpenAI API call successful.")
            return response.choices[0].text
        except openai.error.APIError as e:
            logging.error("OpenAI API error:", e)
            return f"An error occurred: {e}"
        except Exception as e:
            logging.error("Unexpected error:", e)
            return "Something went wrong."
