#! /usr/bin/python3
#

class GensimSummarizer(Summarizer):
    """A gensim Summarizer for text

    Attributes:
    """
    def __init__(self):
        pass

    def summarize(self, text):
        text = text.split('.')
        text = '\n'.join(text)
        try:
           summary = gensim.summarization.summarize(text)
        except Exception as e:
           summary = str(e)
           if type(e).__name__ == "TypeError":
              summary = ''.join(text.splitlines()[0:1])
        logger.info('summary='+repr(summary))
        print(summary)
