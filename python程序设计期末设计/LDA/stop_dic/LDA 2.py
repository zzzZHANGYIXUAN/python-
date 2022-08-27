import pandas as pd

df = pd.read_csv("C:\\Users\\Desktop\\neg.csv", errors='ignore')
print(df.head())
print(df.shape)
import jieba

jieba.load_userdict("C:\\Users\\Desktop\\中文分词词库整理\\中文分词词库整理\\百度分词词库.txt")  # 自定义分词词典


def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))  # 分词


df["content_cutted"] = df.content.apply(chinese_word_cut)

print(df.content_cutted.head())

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

n_features = 1000

tf_vectorizer = CountVectorizer(strip_accents='unicode',
                                max_features=n_features,
                                stop_words='english',
                                max_df=1.0,
                                min_df=0.1)  # 训练词矩阵
tf = tf_vectorizer.fit_transform(df.content_cutted)

from sklearn.decomposition import LatentDirichletAllocation

n_topics = 8
lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=50,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)  # LDA模型训练
lda.fit(tf)


def print_top_words(model, feature_names, n_top_words):  # 主题相关的top词计算
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


n_top_words = 10
tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words)

import pyLDAvis  # 所需可视化模块
import pyLDAvis.sklearn

data = pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)
pyLDAvis.show(data)  # 可视化主题模型