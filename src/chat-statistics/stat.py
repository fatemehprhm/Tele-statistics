import json
from pathlib import Path
from typing import Union

import arabic_reshaper
from bidi.algorithm import get_display
from hazm import Normalizer, word_tokenize
from loguru import logger
from src.Data import DATA_DIR
from wordcloud import WordCloud


class chatstatistics:
    def __init__(self, chat_json: Union[str, Path]):
        """
        Generate chat statistics from a telegra, chat json file

        """
        # load chat data
        logger.info("loading chat data from {chat_json}")

        with open(chat_json) as f:
            self.chat_data = json.load(f)

        # load stopwords
        logger.info("loading stopwords from {DATA_DIR / 'stop_words.txt'}")

        self.normalizer = Normalizer()
        stopwords = open(DATA_DIR / 'stop_words.txt').readlines()
        stopwords = list(map(str.strip, stopwords))
        self.stopwords = list(map(self.normalizer.normalize, stopwords))

    # generate word cloud
    def generate_word_cloud(self, output_dir: Union[str, Path]):

        text_content = ''
        for msg in self.chat_data['messages']:
            if type(msg['text']) is str:
                tokens = word_tokenize(msg['text'])
                tokens = list(filter(lambda item: item not in self.stopwords, 
                tokens))
                text_content += f" {' '.join(tokens)}"
        # Normalize and  reshape
        text_content = self.normalizer.normalize(text_content)
        text_content = arabic_reshaper.reshape(text_content)
        text_content = get_display(text_content)

        logger.info("generating word cloud ...")
        wordcloud = WordCloud(
            font_path=str(DATA_DIR / 'BNaznnBd.ttf'),
            background_color='white'
            ).generate(text_content)
        logger.info("Saving word cloud to {output_dir}")
        wordcloud.to_file(str(Path(output_dir) / 'worldcloud.png'))

if __name__ == "__main__":
    chat_stats = chatstatistics(chat_json=DATA_DIR/'recycle.json')
    chat_stats.generate_word_cloud(output_dir=DATA_DIR)
