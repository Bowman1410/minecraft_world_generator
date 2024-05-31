from nlp.model import NLPModel
from nlp.preprocess import preprocess_prompt
from world_generation.generator import WorldGenerator

def main():
    prompt = input("Enter a prompt for the Minecraft world: ")
    preprocessed_prompt = preprocess_prompt(prompt)

    nlp_model = NLPModel()
    response = nlp_model.generate_response(preprocessed_prompt)
    details = nlp_model.extract_details(response)

    world_generator = WorldGenerator()
    world = world_generator.generate_world(details)
    print(f"Generated world: {world}")

if __name__ == "__main__":
    main()