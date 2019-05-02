


安装 pyenv：
curl https://pyenv.run | bash

把下边代码复制到 ~/.bash_profile
export PATH="/home/linjing/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

生成环境变量
source ~/.bash_profile

查看可下载版本
pyenv install -l

下载安装 python：
pyenv install 3.7.3

检查已安装版本
pyenv versions

用 pyenv 来安装虚拟版本
pyenv virtualenv 3.7.3 spider

切换虚拟版本
切换为spider
pyenv local spider

当前会话窗口python版本为spider的解释器
pyenv shell spider

### 二、jupyter





'https://github.com/MiracleYoung/You-are-Pythonista/blob/master/LearnFromZero/0.EnvPrepare/01.LearnPyenv.md'
