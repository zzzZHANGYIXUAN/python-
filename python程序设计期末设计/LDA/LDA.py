# -*- coding:utf8 -*-
import os
import pandas as pd
import re
import jieba
import jieba.posseg as psg
import pyLDAvis
#所需可视化模块
import pyLDAvis.sklearn

#stress data
output_path = 'E:/python -project/the  python of study/LDA/result'
file_path = 'E:/python -project/the  python of study/LDA/data'
os.chdir(file_path)
data = pd.read_csv('all.csv',encoding='gb18030')  # utf-8
os.chdir(output_path)
dic_file = "E:/python -project/the  python of study/LDA/stop_dic/dict.txt"
stop_file = "E:/python -project/the  python of study/LDA/stop_dic/stopwords.txt"

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
def chinese_word_cut(mytext):
    jieba.load_userdict(dic_file)
    jieba.initialize()
    try:
        stopword_list = open(stop_file, encoding='utf-8')
    except:
        stopword_list = []
        print("error in stop_file")
    stop_list = []
    flag_list = ['n', 'nz', 'vn']
    for line in stopword_list:
        line = re.sub(u'\n|\\r', '', line)
        stop_list.append(line)

    word_list = []
    # jieba分词
    seg_list = psg.lcut(str(mytext))
    for seg_word in seg_list:
        word = re.sub(u'[^\u4e00-\u9fa5]', '', seg_word.word)
        find = 0
        for stop_word in stop_list:
            if stop_word == word or len(word) < 2:  # this word is stopword
                find = 1
                break
        if find == 0 and seg_word.flag in flag_list:
            word_list.append(word)
    return (" ").join(word_list)

data["content"] = data.弹幕
data["content_cutted"] = data.content.apply(chinese_word_cut)
#print the words of topic
def print_top_words(model, feature_names, n_top_words):
    tword = []
    #列表
    for topic_idx, topic in enumerate(model.components_):
        #41行代码中有model.components_的参数
        # for i, element in enumerate(seq):
        # print i, element
        # 0 one
        # 1 two
        # 2 three
        print("Topic #%d:" % topic_idx)
        topic_w = " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
        #""表示是用""中的空格把元素隔开
        tword.append(topic_w)
        #tword中添加topic_w
        print(topic_w)

    return tword
# CountVectorizer是属于常见的特征数值计算类，是一个文本特征提取方法。
# 对于每一个训练文本，它只考虑每种词汇在该训练文本中出现的频率。
# CountVectorizer会将文本中的词语转换为词频矩阵，
# 它通过fit_transform函数计算各个词语出现的次数
n_features = 1000
tf_vectorizer = CountVectorizer(strip_accents='unicode',
                                max_features=n_features,
                                stop_words='english',
                                max_df=0.1,
                                min_df=10)
# max_df
# 这个参数的作用是作为一个阈值，当构造语料库的关键词集的时候
# 如果某个词的document frequence大于max_df，这个词不会被当作关键词。
# min_df
# 如果某个词的document frequence小于min_df，则这个词不会被当作关键词，
# n_features
# 默认为None，可设为int，
# 对所有关键词的term frequency进行降序排序，只取前max_features个作为关键词集
tf = tf_vectorizer.fit_transform(data.content_cutted)
# CountVectorizer会将文本中的词语转换为词频矩阵，
# 它通过fit_transform函数计算各个词语出现的次数
# tf就是输入data。content输出的词频矩阵
#set up topics are 8
n_topics = 5
lda = LatentDirichletAllocation(n_components=n_topics, max_iter=50,
                                 learning_method='batch',
                                 learning_offset=5,
                                 random_state=0)
#n_components
#主题个数
#max_iter=50
#最大迭代次数
#learning_offset
# 仅仅在算法使用online时有意义，取值要大于1。用来减小前面训练样本批次对最终模型的影响
#doc_topic_prior=0.1,
#topic_word_prior=0.01,
lda.fit(tf)

tf_feature_names = tf_vectorizer.get_feature_names()
#every topic has 10 features words
n_top_words = 10
topic_word = print_top_words(lda, tf_feature_names, n_top_words)


data = pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)
pyLDAvis.display(data)
pyLDAvis.save_html(data,"lda.html")






# import matplotlib.pyplot as plt
# # ###########困惑度
# plexs = []
# n_max_topics = 40
# for i in range(1,n_max_topics):
#     print(i)
#     lda = LatentDirichletAllocation(n_components=i, max_iter=50,
#                                     learning_method='batch',
#                                     learning_offset=50,random_state=0)
#     lda.fit(tf)
#     #采用lda模型，每次的主题数目是不同的。主题数目是从1到n_max_topics
#     plexs.append(lda.perplexity(tf))
#     #把不同主题数目的lda的困惑度添加到plexs中
# n_t=39
# #区间最右侧的值。注意：不能大于n_max_topics
# x=list(range(1,n_t))
# plt.plot(x,plexs[1:n_t])
# plt.xlabel("number of topics")
# plt.ylabel("perplexity")
# plt.show()














