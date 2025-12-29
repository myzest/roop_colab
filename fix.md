> 在托尼大大来之前，我们可以采取以下临时的解决方案：
> 
> # Colab 降级到3.10
> ```
> # Example: install Python 3.10
> !sudo apt-get update -y
> !sudo apt-get install python3.10 python3.10-distutils -y
> !sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
> !sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 2
> !sudo update-alternatives --config python3
> 
> # Make pip work with the new Python
> !curl -sS https://bootstrap.pypa.io/get-pip.py | python3
> ```
> 
> # 安装依赖那里改成如下：
> ```
> 
> #@title 3.安装依赖
> #有红色警告不用担心！
> %cd /content/roop_colab/roop/
> 
> !pip install -r requirements.txt
> !pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 --index-url https://download.pytorch.org/whl/cu118
> !pip install onnxruntime-gpu==1.22.0
> # install system packages
> !sudo apt-get update -y
> !sudo apt-get install -y python3-tk tk
> 
> # install Python packages
> !pip install customtkinter==5.2.0 tkinterdnd2==0.3.0
> ```
> 
> # run.py 文件开头添加
> ```
> import os
> os.environ.pop("MPLBACKEND", None)
> os.environ["MPLBACKEND"] = "Agg"
> ```

