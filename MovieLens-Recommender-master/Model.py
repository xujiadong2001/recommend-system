# -*- coding = utf-8 -*-
"""
Main function to build recommendation systems.

Created on 2018-04-16

@author: fuxuemingzhu
"""
import utils
from ItemCF import ItemBasedCF
from LFM import LFM
from UserCF import UserBasedCF
from dataset import DataSet
from most_popular import MostPopular
from random_pred import RandomPredict
from utils import LogTime
import pandas as pd

# def run_model(model_name, dataset_name, test_size=0.3, clean=False):
#     print('*' * 70)
#     print('\tThis is %s model trained on %s with test_size = %.2f' % (model_name, dataset_name, test_size))
#     print('*' * 70 + '\n')
#     model_manager = utils.ModelManager(dataset_name, test_size)
#     try:
#         trainset = model_manager.load_model('trainset')
#         testset = model_manager.load_model('testset')
#     except OSError:
#         ratings = DataSet.load_dataset(name=dataset_name)
#         trainset, testset = DataSet.train_test_split(ratings, test_size=test_size)
#         model_manager.save_model(trainset, 'trainset')
#         model_manager.save_model(testset, 'testset')
#     '''Do you want to clean workspace and retrain model again?'''
#     '''if you want to change test_size or retrain model, please set clean_workspace True'''
#     model_manager.clean_workspace(clean)
#     if model_name == 'UserCF':
#         model = UserBasedCF()
#     elif model_name == 'ItemCF':
#         model = ItemBasedCF()
#     elif model_name == 'Random':
#         model = RandomPredict()
#     elif model_name == 'MostPopular':
#         model = MostPopular()
#     elif model_name == 'UserCF-IIF':
#         model = UserBasedCF(use_iif_similarity=True)
#     elif model_name == 'ItemCF-IUF':
#         model = ItemBasedCF(use_iuf_similarity=True)
#     elif model_name == 'LFM':
#         # K, epochs, alpha, lamb, n_rec_movie
#         model = LFM(10, 20, 0.1, 0.01, 10)
#     else:
#         raise ValueError('No model named ' + model_name)
#     model.fit(trainset)
#     recommend_test(model, [1, 100, 233, 666, 888])
#     model.test(testset)
#
#
# def recommend_test(model, user_list):
#     for user in user_list:
#         recommend = model.recommend(str(user))
#         print("recommend for userid = %s:" % user)
#         print(recommend)
#         print()
#

def get_model(model_name,n_rec_movie, dataset_name, test_size=0.3, clean=False):    # 用指定的数据集根据特定的算法训练模型并输出模型在测试集上的性能
    print('*' * 70)
    print('\tThis is %s model trained on %s with test_size = %.2f' % (model_name, dataset_name, test_size))
    print('*' * 70 + '\n')
    model_manager = utils.ModelManager(dataset_name, test_size)
    try:
        trainset = model_manager.load_model('trainset')
        testset = model_manager.load_model('testset')
    except OSError:
        ratings = DataSet.load_dataset(name=dataset_name)
        trainset, testset = DataSet.train_test_split(ratings, test_size=test_size)
        model_manager.save_model(trainset, 'trainset')
        model_manager.save_model(testset, 'testset')
    '''Do you want to clean workspace and retrain model again?'''
    '''if you want to change test_size or retrain model, please set clean_workspace True'''
    model_manager.clean_workspace(clean)
    if model_name == 'UserCF':
        model = UserBasedCF(n_rec_movie=n_rec_movie)
    elif model_name == 'ItemCF':
        model = ItemBasedCF(n_rec_movie=n_rec_movie)
    elif model_name == 'Random':
        model = RandomPredict(n_rec_movie=n_rec_movie)
    elif model_name == 'MostPopular':
        model = MostPopular(n_rec_movie=n_rec_movie)
    elif model_name == 'UserCF-IIF':
        model = UserBasedCF(use_iif_similarity=True,n_rec_movie=n_rec_movie)
    elif model_name == 'ItemCF-IUF':
        model = ItemBasedCF(use_iuf_similarity=True,n_rec_movie=n_rec_movie)
    elif model_name == 'LFM':
        # K, epochs, alpha, lamb, n_rec_movie
        model = LFM(10, 5, 0.1, 0.01, n_rec_movie)
    else:
        raise ValueError('No model named ' + model_name)
    model.fit(trainset)
    # recommend_test(model, [1, 100, 233, 666, 888])
    # model.test(testset)
    return model

def recommend(model, user_list,n_rec_movie):     # 用训练后的模型为部分用户推荐指定数目的电影并保存在列表
    model.n_rec_movie = n_rec_movie
    result=[]
    for user in user_list:
        recommend = model.recommend(str(user))
        result.append(recommend)
        print("recommend for userid = %s:" % user)
        print(recommend)
        print()
    return result




if __name__ == '__main__':
    # main_time = LogTime(words="Main Function")
    # dataset_name = 'ml-100k'
    # # dataset_name = 'ml-1m'
    # model_type = 'UserCF'
    # # model_type = 'UserCF-IIF'
    # # model_type = 'ItemCF'
    # # model_type = 'Random'
    # # model_type = 'MostPopular'
    # # model_type = 'ItemCF-IUF'
    # # model_type = 'LFM'
    # test_size = 0.1
    # run_model(model_type, dataset_name, test_size, False)
    # main_time.finish()
    # -------------------------------------------------------------------------------------------------
    # main_time = LogTime(words="Main Function")
    # # 选择推荐系统采用的数据集
    # # dataset_name = 'ml-100k'
    # dataset_name = 'ml-1m'
    # # 选择采用不同算法的推荐系统
    # model_type = 'UserCF'
    # # model_type = 'UserCF-IIF'
    # # model_type = 'ItemCF'
    # # model_type = 'Random'
    # # model_type = 'MostPopular'
    # # model_type = 'ItemCF-IUF'
    # # model_type = 'LFM'
    # # 设置测试集比例
    # test_size = 0.1
    # # 获取训练后的模型
    # model=get_model(model_type,20, dataset_name, test_size, False)
    # # 设置想要获得推荐电影的用户编号
    # user_list=[1,2,3,4,5,6,7]
    # # 获取推荐结果
    # result=recommend(model,user_list)
    # print(result)
    # main_time.finish()

    movies = pd.read_table("data/ml-1m/movies.dat", sep="::", encoding='ISO-8859-1',engine='python', header=None,names=['MovieID', 'Title', 'Genres'])
    MovieIDList=movies["MovieID"].tolist()
    MovieTitleList=movies["Title"].tolist()
    MovieGenreList=movies["Genres"].tolist()
    print(MovieIDList)
    print(MovieTitleList)
    print(MovieGenreList)
    movies.head()
