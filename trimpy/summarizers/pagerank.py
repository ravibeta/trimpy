#! /usr/bin/python3
#

class PageRankSummarizer(Summarizer):
    """A PageRank Summarizer for text
    Attributes:
    """
    def __init__(self):
        pass

    def word_similarity_graph(self, words):
            import networkx as nx
            G = nx.Graph() #undirected
            G.add_nodes_from(words)
            for i in range(len(words)):
                for j in range(len(words)):
                    if i == j:
                        continue
                    word_1 = words[i]
                    word_2 = words[j]
                    weight_i_j = word2vec.similarity(word_1, word_2)
                    if weight_i_j < WEIGHT_THRESHOLD:
                       continue
                    G.add_edge(word_1, word_2, weight_i_j)
            return G

    def summarize(self, text):
        from gensim.models import word2vec
        #import logging
        #logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        # load up trainer corpus from http://mattmahoney.net/dc/text8.zip
        """
        sentences = word2vec.Text8Corpus('/tmp/text8')
        model = word2vec.Word2Vec(sentences, size=200)
        model.save('/tmp/text8.model')
        model.save_word2vec_format('/tmp/text8.model.bin', binary=True)
        """
        # load the test sample
        sentences = text.split('\n')
        model = word2vec.Word2Vec(sentences, size=200)
        model.save_word2vec_format('/tmp/vectors.bin', binary=True)
        model = word2vec.Word2Vec.load_word2vec_format('/tmp/vectors.bin', binary=True)
        G = self.word_similarity_graph(model)
        pr = nx.pagerank(G,tol=1e-10)
        #get selection from text based on pagerank of words
        import operator
        sorted_pr = sorted(pr.items(), key=operator.itemgetter(1), reverse=True)
        important = [int(i[0]) for i in sorted_x][:10]
        scored_sentences = {}
        for sentence in sentences:
              matches = set(sentence.split()).intersection(important)
              score = 0
              for match in matches:
                  score+= pr[match]
              scored_sentences[sentence]=score
        reordered_sentences = [ i[0] for i in sorted(scored_sentences.items(), key=operator.itemgetter(1), reverse=True)[:10] ]
        ordered_sentences = [ x for x in sentences if x in reordered_sentences ]
        summary = '\n'.join(ordered_sentences)
        print(summary)
        return ordered_sentences
