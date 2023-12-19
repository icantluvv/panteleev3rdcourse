from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "sberbank-ai/rugpt3large_based_on_gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

def get_response(user_input, max_length=50):
 
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return response

if __name__ == "__main__":
    print("ChatBot: Привет!")
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ['exit', 'bye', 'quit']:
            print("ChatBot: До свидания!")
            break
        response = get_response(user_input)
        print("ChatBot:", response)


### Бот на трансформере