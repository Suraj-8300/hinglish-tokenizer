from transformers import AutoTokenizer

def get_tokens(text, model_name="bert-base-multilingual-cased"):
    """
    Tokenizes input text using a multilingual transformer tokenizer.
    Suitable for Hinglish, Hindi, English, etc.

    Args:
        text (str): Input sentence or paragraph
        model_name (str): HF model name with tokenizer support

    Returns:
        List[str]: List of tokens
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return tokenizer.tokenize(text)
