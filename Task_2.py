import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer

data_vault = "Dataset/df_file.csv"
encoded_porter = "Dataset/Results/porter_output.csv"
encoded_snowball = "Dataset/Results/snowball_output.csv"

def data_extraction(source):
    return pd.read_csv(source)

def text_segmenter(text_block):
    return word_tokenize(text_block)

def encoder_porter(segments):
    stemmer = PorterStemmer()
    return [stemmer.stem(segment) for segment in segments]

def encoder_snowball(segments):
    stemmer = SnowballStemmer(language="english")
    return [stemmer.stem(segment) for segment in segments]

def data_manipulation(data_set):
    data_set["encoded_porter"] = data_set["Text"].apply(text_segmenter).apply(encoder_porter)
    data_set["encoded_snowball"] = data_set["Text"].apply(text_segmenter).apply(encoder_snowball)

    data_set["encoded_porter"].to_csv(encoded_porter, index=False)
    data_set["encoded_snowball"].to_csv(encoded_snowball, index=False)
    
    return data_set["encoded_porter"], data_set["encoded_snowball"]

data = data_extraction(data_vault)
porter_result, snowball_result = data_manipulation(data)

print("Encoding completed! Results saved as", encoded_porter, "and", encoded_snowball)
print("Porter encoded data:")
print(porter_result)
print("\nSnowball encoded data:")
print(snowball_result)
