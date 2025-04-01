# 学习笔记

### 创建 Python 虚拟环境

#首先创建 Python 工程目录

mkdir my_project_name

#进入工程目录

cd my_project_name

#创建虚拟环境

python3 -m venv .venv

#激活虚拟环境

source .venv/bin/activate

#更新 pip

pip install --upgrade pip

#更新到 3.13.2 以后，需要使用一下命令更新 pip
python3 -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org --upgrade pip

#更新 ssl 证书
python3 -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org --upgrade certifi

#查看证书路径
python3 -m certifi

#设置环境变量，永久生效
echo 'export SSL_CERT_FILE=$(python3 -m certifi)' >> ~/.zprofile
source ~/.zprofile

