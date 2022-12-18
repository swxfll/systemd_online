```shell
python manage.py makemigrations # 创建数据配置文件，显示并记录所有数据的改动
python manage.py migrate  #创建表结构，将改动更新到数据库
python manage.py createsuperuser  # 创建超级管理员
python manage.py --help
```

# 部署
## Ide
```shell
pip3 freeze > requirements.txt
```

## Ubuntu
```shell
# 1.上传源码
# 2.创建虚拟环境
sudo apt install virtualenv
sudo virtualenv venv
source venv/bin/activate
sudo pip3 config set global.index-url https://pypi.douban.com/simple/
pip3 install -r requirements.txt
python manage.py runserver 0.0.0.0:8000  # 启动服务器，默认是127.0.0.1:8000
```