from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Text
from flask_cors import CORS
from sqlalchemy import or_
import random
import json
import csv

# 需要修改对应地址
# rumorFile = r'D:\vue_node\COVID-19-Visualization\covid-vis\flask\DXYRumors.csv'
newsFile = r'D:\肺炎\DXY-COVID-19-Data\csv\DXYNews.csv'
rumorFile = r'D:\肺炎\DXY-COVID-19-Data\csv\DXYRumors.csv'



# 2.创建Flask 应用程序实例
# 需要传入__name__, 作用是为了确定资源所在路径
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:fengyunjia@127.0.0.1:3306/flask_sql_demo'  # mysql://username:password@hostname/database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/cov19'  # mysql://username:password@hostname/database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = 'root' # 加密混淆使用
CORS(app)


def read_rumor(rumorFile, title, body, summary, time):
    with open(rumorFile, 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        for row in reader:
            title.append(row[2])
            summary.append(row[3])
            body.append(row[5])
            time.append(row[8])
        title.pop(0)
        summary.pop(0)
        body.pop(0)
        time.pop(0)


def read_news(newsFile, title, source, summary,url, time):
    with open(newsFile,'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
    for row in reader:
        time.append(row[2])
        title.append(row[3])
        summary.append(row[4])
        source.append(row[5])
        url.append(row[6])
    title.pop(0)
    summary.pop(0)
    source.pop(0)
    time.pop(0)


class Rumors(db.Model):
    # 定义表名
    __tablename__ = 'rumors'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(Text)
    summary = db.Column(Text)
    body = db.Column(Text)
    time = db.Column(Text)

    def __repr__(self):
        return '<Rumors: %s %s %s %s>' % (self.title, self.summary, self.body, self.time)

    def to_json(self):
        json_data = {
          'id': self.id,
          'title': self.title,
          'summary': self.summary,
          'body': self.body,
          'time': self.time
        }
        return json.dumps(json_data, ensure_ascii=False)

class News(db.Model):

    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(Text)
    summary = db.Column(Text)
    source = db.Column(Text)
    time = db.Column(Text)
    url = db.Column(Text)

    def __repr__(self):
        return '<News: %s %s %s %s %s>' % (self.title, self.summary, self.source, self.time, self.url)

    def to_json(self):
        json_data = {
          'id': self.id,
          'title': self.title,
          'summary': self.summary,
          'source': self.source,
          'url': self.url,
          'time': self.time
        }
        return json.dumps(json_data, ensure_ascii=False)


@app.route('/rumors_search', methods=['GET', 'POST'])
def get_rumor():
    if request.method == 'POST':
      q = request.get_json()['title']
      # print(q)
      rumor = Rumors.query.filter(or_(Rumors.title.contains(q), Rumors.body.contains(q), Rumors.summary.contains(q))).limit(13)
      dict = []
      print(rumor.all())
      for i in rumor.all():
        dict.append(i.to_json())
      # print(json.dumps(dict))
    return json.dumps(dict)


@app.route('/rumors', methods=['GET'])
def show_rumor():
      random_list = []
      random_count = 0
      rows = db.session.query(Rumors).count()
      mark = True
      while mark:
        if random_count >= 10:
          break
        else:
          random_num = random.randint(0, rows-1)
          if random_num in random_list:
            continue
          else:
            random_list.append(random_num)
            random_count += 1
      dict = []
      for i in random_list:
        dict.append(Rumors.query.filter_by(id=i).first().to_json())
      # print(dict)
      return json.dumps(dict)



@app.route('/news_search',methods=['GET', 'POST'])
def get_news():
    if request.method == 'POST':
      q = request.get_json()['title']
      # print(q)
      dict = []
      news = News.query.filter(or_(News.title.contains(q), News.source.contains(q), News.summary.contains(q))).limit(10)
      print(news.all())
      for i in news.all():
        dict.append(i.to_json())
    return json.dumps(dict)

def sql_initialize():
    source = []
    time = []
    title = []
    summary = []
    url = []
    read_news(newsFile, title, source, summary, url, time)
    for i in range(len(title)):
        item = News(title=title[i], summary=summary[i], source=source[i], url=url[i], time=time[i])
        db.session.add(item)
    db.session.commit()
    body = []
    time = []
    title = []
    summary = []
    read_rumor(rumorFile, title, body, summary, time)
    for i in range(len(title)):
        item = Rumors(title=title[i], summary=summary[i], body=body[i], time=time[i])
        db.session.add(item)
    db.session.commit()


# 4.启动程序
if __name__ == '__main__':
    # 只在初始化数据库时运行下面代码：
    # db.drop_all()
    # 创建表
    # db.create_all()
    # sql_initialize()

    app.run(debug=True)
