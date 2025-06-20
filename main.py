from tokenizer.tokenize import get_tokens

if __name__ == "__main__":
    text = "kal night ko tu aya hi nahi bro! kya scene tha?"
    tokens = get_tokens(text)

    print("Original Text:\n", text)
    print("\nTokenized Output:\n", tokens)
