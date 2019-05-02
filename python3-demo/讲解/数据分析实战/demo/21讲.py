#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/27 21:44 
# @Author : 韧桂 
# @Site :  
# @File : 21讲.py 
# @Software: PyCharm

# 数据说明：
# 1、文档共有4中类型：女性、体育、文学、校园
# 2、训练集放到train文件夹里，测试集放到test文件夹里。停用词放到stop文件夹里。
# 请使用朴素贝叶斯分类对训练集进行训练，并对测试集进行验证，并给出测试集的准确率。
import io

import jieba
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

LABEL_MAP = {'体育': 0, '女性': 1, '文学': 2, '校园': 3}
# 加载停用词
# with open('./text_classification/stop/stopword.txt', 'rb') as f:
#     STOP_WORDS = [line.strip() for line in f.readlines()]
STOP_WORDS = [line.strip().decode('utf-8') for line in io.open('./text_classification/stop/stopword.txt', 'rb').readlines()]



def load_data(base_path):
    """
    :param base_path: 基础路径
    :return: 分词列表，标签列表
    """
    documents = []
    labels = []

    for root, dirs, files in os.walk(base_path): # 循环所有文件并进行分词打标
        for file in files:
            label = root.split('\\')[-1] # 因为windows上路径符号自动转成\了，所以要转义下
            labels.append(label)
            filename = os.path.join(root, file)
            with open(filename, 'rb') as f: # 因为字符集问题因此直接用二进制方式读取
                content = f.read()
                word_list = list(jieba.cut(content))   #对文档进行分词
                words = [wl for wl in word_list]
                documents.append(' '.join(words))
    return documents, labels

def train_fun(td, train_labels, test_contents, testl):
    """
    构造模型并计算测试集准确率，字数限制变量名简写
    :param td: 训练集数据
    :param tl: 训练集标签
    :param testd: 测试集数据
    :param testl: 测试集标签
    :return: 测试集准确率
    """
    # 计算矩阵。
    #计算单词权重
    tt = TfidfVectorizer(stop_words=STOP_WORDS, max_df=0.5)
    #这里 max_df 参数用来描述单词在文档中的最高出现率。假设 max_df=0.5，代表一个单词在50% 的文档中都出现过了，那么它只携带了非常少的信息，因此就不作为分词统计。
    train_features = tt.fit_transform(td)   # fit_transform方法拟合，得到 TF-IDF 特征空间 features，你可以理解为选出来的分词就是特征。

    # 训练模型
    #生成朴素贝叶斯分类器
    clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)  #其中 alpha 为平滑参数。当 alpha=1 时，使用的是 Laplace 平滑。当 0<alpha<1 时,使用的是 Lidstone 平滑
    #将特征训练集的特征空间 train_features，以及训练集对应的分类 train_labels 传递给贝叶斯分类器 clf，它会自动生成一个符合特征空间和对应分类的分类器

    # 模型预测
    #使用生成的分类器做预测
    test_tf = TfidfVectorizer(stop_words=STOP_WORDS, max_df=0.5, vocabulary=tt.vocabulary_) #获取到测试集的特征矩阵。
    test_features = test_tf.fit_transform(test_contents)

    predicted_labels = clf.predict(test_features) #用训练好的分类器对新数据做预测。predict 函数做的工作就是求解所有后验概率并找出最大的那个

    # 获取结果
    #计算准确率
    x = metrics.accuracy_score(testl, predicted_labels)
    # x = metrics.accuracy_score(test_labels, predicted_labels)
    return x
    # print(metrics.accuracy_score(test_labels, predicted_labels))


# text_classification 与代码同目录下
train_documents, train_labels = load_data('./text_classification/train')
test_documents, test_labels = load_data('./text_classification/test')
x = train_fun(train_documents, train_labels, test_documents, test_labels)
print(x)



# import os
# import jieba
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
#
# # 1. 加载数据
# # 加载停用词表
# l_stopWords = set()
# with open('./text_classification/stop/stopword.txt', 'rb') as l_f:
#     for l_line in l_f:
#         l_stopWords.add(l_line.strip())
#
# l_labelMap = {'体育': 0, '女性': 1, '文学': 2, '校园': 3}
#
#
# # 加载训练数据和测试数据
# def LoadData(filepath):
#     l_documents = []
#     l_labels = []
#     for root, dirs, files in os.walk(filepath):
#         for l_file in files:
#             l_label = root.split('/')[-1]
#             l_filename = os.path.join(root, l_file)
#
#             with open(l_filename, 'r') as l_f:
#                 l_content = l_f.read()
#                 l_wordlist = list(jieba.cut(l_content))
#                 l_words = [item for item in l_wordlist if item not in l_stopWords]
#                 l_documents.append(' '.join(l_words))
#                 l_labels.append(l_labelMap[l_label])
#
#     return l_documents, l_labels
#
#
# l_trainDocuments, l_trainLabels = LoadData('./text_classification/train')
# l_testDocuments, l_testLabels = LoadData('./text_classification/test')
#
# # # 2. 计算权重矩阵
# l_tfidfVec = TfidfVectorizer(max_df=0.5)
# l_tfidfMatrix = l_tfidfVec.fit_transform(l_trainDocuments)
#
# # for item in l_tfidfVec.get_feature_names():
# # print item
# # print l_tfidfVec.get_feature_names()
# # print l_tfidfVec.vocabulary_
# print(l_tfidfMatrix.toarray().shape)
#
# # # 3. 朴素贝叶斯模型
# # ## 3.1 模型训练
# l_clf = MultinomialNB(alpha=0.001)
# l_clf.fit(l_tfidfMatrix, l_trainLabels)
#
# # ## 3.2 模型预测
# l_testTfidf = TfidfVectorizer(max_df=0.5, vocabulary=l_tfidfVec.vocabulary_)
# l_testFeature = l_testTfidf.fit_transform(l_testDocuments)
# l_hats = l_clf.predict(l_testFeature)
#
# # ## 3.3 模型评估
# from sklearn.metrics import accuracy_score
#
# print(accuracy_score(l_hats, l_testLabels))


# train_contents = []
# train_labels = []
# test_contents = []
# test_labels = []
# #  导入文件
# import os
# import io
#
# start = os.listdir(r'text_classification/train')
# for item in start:
#     test_path = 'text_classification/test/' + item + '/'
#     train_path = 'text_classification/train/' + item + '/'
#     for file in os.listdir(test_path):
#         with open(test_path + file, encoding="GBK") as f:
#             test_contents.append(f.readline())
#             # print(test_contents)
#             test_labels.append(item)
#     for file in os.listdir(train_path):
#         with open(train_path + file, encoding='gb18030', errors='ignore') as f:
#             train_contents.append(f.readline())
#             train_labels.append(item)
# print(len(train_contents), len(test_contents))
#
# # 导入stop word
# import jieba
# from sklearn import metrics
# from sklearn.naive_bayes import MultinomialNB
#
# stop_words = [line.strip() for line in io.open('text_classification/stop/stopword.txt').readlines()]
#
# # 分词方式使用jieba,计算单词的权重
# tf = TfidfVectorizer(tokenizer=jieba.cut, stop_words=stop_words, max_df=0.5)
# train_features = tf.fit_transform(train_contents)
# print(train_features.shape)
#
# # 模块4：生成朴素贝叶斯分类器
# # 多项式贝叶斯分类器
# clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)
#
# # 模块5：使用生成的分类器做预测
# test_tf = TfidfVectorizer(tokenizer=jieba.cut, stop_words=stop_words, max_df=0.5, vocabulary=tf.vocabulary_)
# test_features = test_tf.fit_transform(test_contents)
#
# print(test_features.shape)
# predicted_labels = clf.predict(test_features)
# print(metrics.accuracy_score(test_labels, predicted_labels))


# import os
# import pandas as pd
# import jieba
# from sklearn import metrics
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.feature_extraction.text import TfidfVectorizer
#
# def load_data(path):
#     l_labels = []
#     l_documents = []
#     #os.walk返回三元组(root, dirs, files)
#     #root指的是当前正在遍历的这个文件夹本身的地址
#     #dirs是一个list，内容是该文件夹中所有的目录的名字
#     #files是一个list，内容是该文件夹中所有的文件，不包含子目录
#     for root, dirs, files in os.walk(path):
#         print (root, dirs, files)
#         for l_file in files:
#             l_label = root.split('/')[-1]
#             l_filepath = os.path.join(root, l_file)
#             with open(l_filepath, 'r') as l_f:
#                 l_content = l_f.read()
#                 l_words = ' '.join(list(jieba.cut(l_content)) )
#                 l_labels.append(l_label)
#                 l_documents.append(l_words)
#     return l_documents, l_labels
#
# #第一步：对文档进行分词
# train_documents, train_labels = load_data('./text_classification/train/')
# test_documents, test_labels = load_data('./text_classification/test/')
#
# #第二步：加载停用词
# STOP_WORDS = [line.strip() for line in open('./text_classification/stop/stopword.txt' ,'r').readlines()]
#
# #第三步：计算单词的权重
# tf = TfidfVectorizer(stop_words=STOP_WORDS, max_df=0.5)
# train_features = tf.fit_transform(train_documents)
#
# #第四步：生成朴素贝叶斯分类器
# clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)
#
# #第五步：使用生成的分类器做预测
# test_tf = TfidfVectorizer(stop_words=STOP_WORDS, max_df=0.5, vocabulary=tf.vocabulary_)
# test_features = test_tf.fit_transform(test_documents)
#
# predict_labels = clf.predict(test_features)
#
# #第六步：计算准确率
# print (metrics.accuracy_score(test_labels, predict_labels))


# import os
# import jieba
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn import metrics
#
#
# def load_data(base_path):
#     documents = []
#     labels = []
#     for root, dirs, files in os.walk(base_path):  # 循环所有文件并进行分词打标
#         for file in files:
#             label = root.split('\\')[-1]  # 因为windows上路径符号自动转成\了，所以要转义下
#             labels.append(label)
#             filename = os.path.join(root, file)
#             with open(filename, 'rb') as f:  # 因为字符集问题因此直接用二进制方式读取
#                 content = f.read()
#                 word_list = list(jieba.cut(content))
#                 words = [wl for wl in word_list]
#                 documents.append(' '.join(words))
#     return documents, labels
#
#
# train_contents, train_labels = load_data('./text_classification/train')
# test_contents, test_labels = load_data('./text_classification/test')
# stop_words = []
#
# import io
#
# stop_words = [line.strip().encode('utf-8') for line in io.open('./text_classification/stop/stopword.txt').readlines()]
#
# tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5)
# train_features = tf.fit_transform(train_contents)
# # 多项式贝叶斯分类器
#
# clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)
#
# test_tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5, vocabulary=tf.vocabulary_)
# test_features = test_tf.fit_transform(test_contents)
# predicted_labels = clf.predict(test_features)
# print(metrics.accuracy_score(test_labels, predicted_labels))

# import jieba
# import glob
# import io
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn import metrics
#
# classification = ["campus", "female", "sports", "literature"]
# train_files_list = []
# test_files_list = []
# trainpathprefix = "./text_classification/train/"
# testpathprefix = "./text_classification/test/"
# pathsuffix = "/*.txt"
# train_label = []
# test_label = []
# train_docments = []
# test_docments = []
# stopword_path = './text_classification/stop/stopword.txt'
#
# for i in classification:
#     trainpathstr = trainpathprefix + i + pathsuffix
#     testpathstr = testpathprefix + i + pathsuffix
#     trainpathlist = glob.glob(trainpathstr)
#     lentrainlist = len(trainpathlist)
#     train_label += [i for j in range(lentrainlist)]
#     testpathlist = glob.glob(testpathstr)
#     lentestlist = len(testpathlist)
#     test_label += [i for j in range(lentestlist)]
#     train_files_list += trainpathlist
#     test_files_list += testpathlist
#
# for i in train_files_list:
#     f = open(i, 'r')
#     content = f.readlines()[0]
#     contentlist = list(jieba.cut(content))
#     contentwithspace = " ".join(contentlist)
#     train_docments.append(contentwithspace)
#
# for i in test_files_list:
#     f = open(i, 'r')
#     content = f.readlines()[0]
#     contentlist = list(jieba.cut(content))
#     contentwithspace = ' '.join(contentlist)
#     test_docments.append(contentwithspace)
#
# stopwords = [l.strip('\n') for l in io.open(stopword_path, encoding='utf-8').readlines()]
# train_tf = TfidfVectorizer(stop_words=stopwords, max_df=0.5)
# train_features = train_tf.fit_transform(train_docments)
# clf = MultinomialNB(alpha=0.001).fit(train_features, train_label)
# test_tf = TfidfVectorizer(stop_words=stopwords, max_df=0.5, vocabulary=train_tf.vocabulary_)
# test_features = test_tf.fit_transform(test_docments)
# predicted_labels = clf.predict(test_features)
# print(metrics.accuracy_score(test_label, predicted_labels))



# import pandas as pd
# import numpy as np
# import io
# import os
# import jieba
# from sklearn import metrics
# from sklearn.naive_bayes import MultinomialNB
#
# def preprocess(path_name):
#     text_with_spaces=""
#     textfile=open(path_name,"r").read()
#     textcut=jieba.cut(textfile)
#     for word in textcut:
#         text_with_spaces+=word+" "
#     return text_with_spaces
#
# def loadtrainset(path,classtag):
#     allfiles=os.listdir(path)
#     processed_textset=[]
#     allclasstags=[]
#     for thisfile in allfiles:
#         path_name=path+"/"+thisfile
#         processed_textset.append(preprocess(path_name))
#         allclasstags.append(classtag)
#     return processed_textset,allclasstags
#
# stop_words = open('../stop/stopword.txt', 'r', encoding='utf-8').read()
# stop_words = stop_words.encode('utf-8').decode('utf-8-sig')
# stop_words = stop_words.split('\n')
#
# processed_textdata1,class1=loadtrainset("../train/女性", "女性")
# processed_textdata2,class2=loadtrainset("../train/体育", "体育")
# processed_textdata3,class3=loadtrainset("../train/文学", "文学")
# processed_textdata4,class4=loadtrainset("../train/校园", "校园")
# integrated_train_data=processed_textdata1+processed_textdata2+processed_textdata3+processed_textdata4
# classtags_list=class1+class2+class3+class4
# print(integrated_train_data[0])
# tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5)
# train_features = tf.fit_transform(integrated_train_data)
#
# train_labels=[0]
#
# clf = MultinomialNB(alpha=0.01).fit(train_features, classtags_list)
# # 多项式贝叶斯分类器
#
#
#
# test_textdata1,testClass1=loadtrainset("../test/女性", "女性")
# test_textdata2,testClass2=loadtrainset("../test/体育", "体育")
# test_textdata3,testClass3=loadtrainset("../test/文学", "文学")
# test_textdata4,testClass4=loadtrainset("../test/校园", "校园")
# integrated_test_data=test_textdata1+test_textdata2+test_textdata3+test_textdata4
# classtags_list=testClass1+testClass2+testClass3+testClass4
#
# test_tf = TfidfVectorizer( max_df=0.5)
# test_features=tf.transform(integrated_test_data)
# predicted_labels=clf.predict(test_features)
#
# print(metrics.accuracy_score(classtags_list, predicted_labels))



