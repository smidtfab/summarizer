INSTALL_MSG = """
Bart will be released through pip in v 3.0.0, until then use it by installing from source:
git clone git@github.com:huggingface/transformers.git
git checkout d6de6423
cd transformers
pip install -e ".[dev]"
"""

import torch
try:
    import transformers
    from transformers import BartTokenizer, BartForConditionalGeneration
except ImportError:
    raise ImportError(INSTALL_MSG)
from IPython.display import display, Markdown


class Summarizer():
    def __init__(self):
        self.torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.tokenizer = BartTokenizer.from_pretrained('bart-large-cnn')
        self.model = BartForConditionalGeneration.from_pretrained('bart-large-cnn')
    
    def summarize(self, text):
        #LONG_BORING_TENNIS_ARTICLE = "Andy Murray came close to giving himself some extra preparation time for his wedding next week before ensuring that he still has unfinished tennis business to attend to. The world No 4 is into the semi-finals of the Miami Open, but not be .... <more text here>".replace('\n','')
        article_input_ids = self.tokenizer.batch_encode_plus([text], return_tensors='pt', max_length=1024)['input_ids'].to(self.torch_device)
        summary_ids = self.model.generate(article_input_ids,
                                            num_beams=4,
                                            length_penalty=2.0,
                                            max_length=142,
                                            #min_len=56,
                                            no_repeat_ngram_size=3)

        summary_txt = self.tokenizer.decode(summary_ids.squeeze(), skip_special_tokens=True)
        print('> **Summary: **'+summary_txt)
        return summary_txt

if __name__ == "__main__":
    s = Summarizer()
    s.summarize(text = "")