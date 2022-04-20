# COCOAPI-state说明

cocoapi-state是根据cocoapi修改得到，适用于以coco形式标注的目标检测数据集，但是相比原本的cocoapi拥有更多的功能。
其中包括：

1. 支持目标矩形边框的可视化；
2. 支持目标状态属性的标注；
3. 支持目标每个类别属性的bbox IoU metrics输出；
4. 支持目标每个状态属性的bbox IoU metrics输出。

目前cocoapi-state可用于intruscapes数据集的行人入侵检测任务评估。

intruscapes数据集是一个针对行人入侵检测任务的数据集，其图像数据和行人bbox标注数据来自于citypersons，其行人入侵状态
标签来自额外的人工标注。对于行人目标的入侵状态包含三种属性：

1. "None": 没有入侵状态标签；
2. "Non Intrusion": 处于无入侵状态；
3. "Intrusion": 处于入侵状态。

### 安装方法
目前只支持python安装
1. 第一步，下载库到本地，可采用git clone，也可采用下载压缩包后解压
```
git clone https://github.com/szy4017/cocoapi-state.git
```

2. 第二步，安装依赖库`cython`
```
pip install cython
```

3. 第三步，运行安装脚本`setup.py`
```
python setup.py install
```
