import asyncio
from dotenv import load_dotenv

load_dotenv()

async def main():
    from src import dp
    from loader import bot

    await dp.start_polling(bot)

if __name__ == "__main__":
    from nltk.tokenize import RegexpTokenizer
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer

    tokenizer = RegexpTokenizer(r'\w+')
    sw = set(stopwords.words('russian'))
    ps = PorterStemmer()


    def get_useful_words(text):
        text = text.lower()
        # tokenization
        word_list = tokenizer.tokenize(text)

        # stop word removal
        useful_words = [w for w in word_list if w not in sw]

        # stemming
        stemmed_words = [ps.stem(w) for w in useful_words]

        return stemmed_words
    asyncio.run(main())
