from flask import Flask, render_template,request,jsonify
from flask_cors import cross_origin
from Model import get_model, recommend
from utils import LogTime
import pandas as pd

global model1
global model2
global model3
global model4
global model5
global MovieIDList
global MovieTitleList
global MovieGenreList

app = Flask(__name__)


@app.route('/submit',methods=["POST"])
@cross_origin()
def result():
    # msg = "my name is caojianhua, China up!"
    # return render_template("MainPage.html", data1=msg)
    Content=[request.form.get("Content")]
    LeftOption=request.form.get("LeftOption")
    RightOption = int(request.form.get("RightOption"))
    if LeftOption=="UserCF":
        model=model1
    elif LeftOption=="ItemCF":
        model=model2
    elif LeftOption=="Random":
        model=model3
    elif LeftOption=="MostPopular":
        model=model4
    elif LeftOption=="LFM":
        model=model5
    # print(Content)
    # print(LeftOption)
    # print(RightOption)
    # return jsonify({"res":Content})  # response to your request.
    result = recommend(model,Content, RightOption)
    result=result[0]
    html=""
    for index in result:
        for i in range(len(MovieIDList)):
            if MovieIDList[i]==int(index):
                break
        # print(index)
        title=MovieTitleList[i]
        # print(title)
        genre=MovieGenreList[i]
        # print(genre)
        html=html+'<div class="MovieContainer"><div class="Movie"><div class="MovieCoverContainer" ><img class="MovieCover" src="/pic/'+index+'.jpg"></div><div class="MovieTitle">'+title+'</div><div class="MovieGenre">'+genre+'</div></div></div>'
    return html

# @app.route('/', methods=['POST'])



if __name__ == "__main__":
    main_time = LogTime(words="Main Function")
    # 选择推荐系统采用的数据集
    # dataset_name = 'ml-100k'
    dataset_name = 'ml-1m'
    # 选择采用不同算法的推荐系统
    model_type1 = 'UserCF'
    # model_type = 'UserCF-IIF'
    model_type2 = 'ItemCF'
    model_type3 = 'Random'
    model_type4 = 'MostPopular'
    # model_type = 'ItemCF-IUF'
    model_type5 = 'LFM'
    # 设置测试集比例
    test_size = 0.1
    # 获取训练后的模型
    model1=get_model(model_type1,20, dataset_name, test_size, False)
    model2=get_model(model_type2,20, dataset_name, test_size, False)
    model3=get_model(model_type3,20, dataset_name, test_size, False)
    model4=get_model(model_type4,20, dataset_name, test_size, False)
    model5=get_model(model_type5,20, dataset_name, test_size, False)
    print("---------------------------------------模型创建完毕-----------------------------------------")
    # # 设置想要获得推荐电影的用户编号
    # user_list=[1,2,3,4,5,6,7]
    # # 获取推荐结果
    # result=recommend(model,user_list,10)
    # print(result)
    # 获取所有电影信息
    movies = pd.read_table("data/ml-1m/movies.dat", sep="::", encoding='ISO-8859-1',engine='python', header=None,names=['MovieID', 'Title', 'Genres'])
    MovieIDList=movies["MovieID"].tolist()
    MovieTitleList=movies["Title"].tolist()
    MovieGenreList=movies["Genres"].tolist()
    main_time.finish()
    # 启动服务器
    app.run(port=2020, host="127.0.0.1", debug=True)