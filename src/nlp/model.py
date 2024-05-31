from transformers import OpenAIGPTTokenizer, OpenAIGPTLMHeadModel

class NLPModel:
    def __init__(self):
        self.tokenizer = OpenAIGPTTokenizer.from_pretrained('openai-gpt')
        self.model = OpenAIGPTLMHeadModel.from_pretrained('openai-gpt')

    def generate_response(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    def extract_details(self, response):
        # Implement logic to extract world generation details from the model's response
        details = {}
        if "castle" in response:
            details['castle'] = True
        if "forest" in response:
            details['forest'] = True
        if "river" in response:
            details['river'] = True
        return details
