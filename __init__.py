import requests

class PromptOptimizer:
    def __init__(self):
        self.system_prompt = """
        Instruction Set for Image Prompt Diversification:

        - If the prompt is in a language other than English, translate it to English first.
        - Imagine details such as setting, colors, lighting, and overall mood.
        - Determine if any specific languages or cultures are particularly relevant to the subject matter of the image prompt. Consider the popularity of languages online, prioritizing more widely used words.
        - Generate one distinctive new prompt that describes the same image from different perspectives while describing the same actual image. 
        - Ensure that the prompts are diverse and avoid overfitting by following these guidelines:
        - maintain a clear and vivid description of the image, including details about the main subject, setting, colours, lighting, and overall mood. 
        - express these elements using varied vocabulary and sentence structure. Don't reuse adjectives, nouns, verbs, or even phrases.
        - if a visual style or artist reference is present in the prompt, expand the prompt to contain many more details about the style or artists.
        - If no visual style is given, decide on a typical style that would be used in that type of image. Be detailed and specific.
        - The image generator is not very good at text and screenshots. Try and rewrite those into more conceptual prompts.
        - When asked for a random prompt, generate an evocative and surprising one that fits user constraints, and provide any unspecified details.
        - Dont omit any details from the original prompt.

        Respond only with the new prompt. Nothing Else.
        """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "A beautiful sunset over the mountains"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 9999999999}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("optimized_prompt",)
    FUNCTION = "optimize_prompt"

    CATEGORY = "utils"

    def optimize_prompt(self, prompt, seed):
        url = "https://text.pollinations.ai/"
        payload = {
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": "Prompt: " + prompt}
            ],
            "seed": seed,
            "model": "openai",
        }  
        headers = {
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            optimized_prompt = response.text
        else:
            optimzed_prompt = prompt

        return (optimized_prompt,)

NODE_CLASS_MAPPINGS = {
    "PromptOptimizer": PromptOptimizer
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptOptimizer": "Free Prompt Optimizer"
}