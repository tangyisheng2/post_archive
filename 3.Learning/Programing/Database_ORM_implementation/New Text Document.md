# 数据库ORM实现

## 前言

做小项目时候发现的新轮子

先扔代码，笔记等想起来在写

## 代码

```python
__author__ = "Eason Tang"

# Ref: https://zhuanlan.zhihu.com/p/27400862

# 导入:
# 不同类型均需import
from sqlalchemy import Column, Integer, TIMESTAMP, FLOAT
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'testaccount'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    time = Column(TIMESTAMP)
    longitude = Column(FLOAT)
    latitude = Column(FLOAT)

    # def __init__(self):
    #     # 确定表名
    #     # self.__tablename__ = table_name
    #     pass

def main():
    instance = User()
    # 初始化数据库连接:
    engine = create_engine('mysql+pymysql://stick_dev:G6ccPzIuyP6WRnoz@mqtt.tangyisheng2.com:3306/stick')
    # 创建DBSession类型:
    # self.DBSession = sessionmaker(bind=self.engine)
    session = sessionmaker(bind=engine)
    session = session()

    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    payload = {
        "id": 1
    }

    try:
        # 下面的注释是代表filter
        # user = session.query(Status) \
        #     .filter(Status.id == 1) \
        #     .all()
        for retval in session.query(User):
            print(vars(retval))
    except NoResultFound:
        print("No row was found for one()")

    # 增
    new_item = User(longitude=1, latitude=2)
    session.add(new_item)
    session.commit()

    # 改
    # 先查询项目
    try:
        # 下面的注释是代表filter
        # user = session.query(Status) \
        #     .filter(Status.id == 1) \
        #     .all()
        to_mod = session.query(User) \
            .filter(User.id == 1) \
            .first()
    except NoResultFound:
        print("No row was found for one()")

    to_mod.longitude = 100
    session.commit()

    # 删
    # 先查询项目
    try:
        # 下面的注释是代表filter
        # user = session.query(Status) \
        #     .filter(Status.id == 1) \
        #     .all()
        to_delete = session.query(User) \
            .filter(User.id == 1) \
            .first()
    except NoResultFound:
        print("No row was found for one()")

    session.delete(to_delete)
    session.commit()


if __name__ == "__main__":
    main()

```

