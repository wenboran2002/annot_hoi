### 3D HOI Blender Annotation Tool
**简介**
基于blender的3d hoi标注工具，从包含human mesh的文件夹读入mesh,同时会自动读入物体的点云以及参考图片，标注者根据参考图片<font color=red>放缩、移动、旋转</font>物体使3d布局符合图片布局。
使用视频：[bilibili](https://www.bilibili.com/video/BV1SE421T7cb/)
或者从[交大云盘](https://jbox.sjtu.edu.cn/l/61ZUCj)下载



**下载** 
project:
如果电脑有gti可以使用
`git clone https://github.com/wenboran2002/annot_hoi.git`下载
如果没有可以点击Code->DownloadZIP下载并解压

blender:
（如果电脑已安装blender版本>2.83，需要重新安装一个2.83版本）
* 官网下载：[https://download.blender.org/release/Blender2.83/]
* 安装包：blender-2.83 数据在[交大云盘](https://jbox.sjtu.edu.cn/l/61ZUCj)
  ![install](https://github.com/wenboran2002/annot_hoi/blob/main/imgs/install.png))
  
**数据准备**
从[交大云盘](https://jbox.sjtu.edu.cn/l/61ZUCj)下载所需要的数据，如图：
解压在/src
目录结构如下：
```
- annot_hoi
  - src
      - annotation
      - templates
      - obj
      - human
      - show_boxes
      - blender-2.83.0-windows64
  -scripts
  - ...
```

**安装插件**
1. 先按a再按Del清除现有物体
2. 在上边栏选择Edit->Preference->Add-ons,点击install
    ![step1](https://github.com/wenboran2002/annot_hoi/blob/main/imgs/9.png)
    ![step1](https://github.com/wenboran2002/annot_hoi/blob/main/imgs/1.png)
3. 找到scripts/annot.py和scripts/space_view3d_point_cloud_visualizer.py并安装，同时在搜索栏搜索annot和point cloud,找到后在左边方框打√

![step1](https://github.com/wenboran2002/annot_hoi/blob/main/imgs/2.png)
![step1](https://github.com/wenboran2002/annot_hoi/blob/main/imgs/3.png)
4. 安装完成后右上角会出现三个按钮Load Wbr , Export Obj Pose and Location, Delete_this_object
   
**标注**
***需要达到效果：移动物体使人和物体的相对关系与图片中的符合，不一定完全一致，至少要求相对大小、位置以及大致的pose一致***
1. 点击右上角Load Wbr,在\src\human中选择对应的object文件夹![step1](https://github.com/wenboran2002/annot_hoi/blob/main/imgs/4.png)
2. 依序load文件，同时会load进物体以及参考图片
3. 用鼠标拖动右上角的z轴朝下，使视角正过来![step1](https://github.com/wenboran2002/annot_hoi/blob/main/imgs/step7.png)
4. 选中物体，开始标注：
   按<font color=red>s</font>同时移动鼠标为放缩
   按<font color=red>r</font>同时移动鼠标为左右旋转
   ![step1](https://github.com/wenboran2002/annot_hoi/blob/main/imgs/rotate.gif)
   按<font color=red>两次r</font>同时移动鼠标为任意旋转
   ![step1](https://github.com/wenboran2002/annot_hoi/blob/main/imgs/any_rotate.gif)
   按<font color=red>g</font>同时移动鼠标为移动
   ![step1](https://github.com/wenboran2002/annot_hoi/blob/main/imgs/translate.gif)
   鼠标拖动可以移动场景，确保各个方位都摆放好
6. ***注意***:先旋转放缩物体使其与图片姿态匹配，再移动到合适位置，因为旋转放缩是参考原点的
7. 标注结束后，点击右上角Export Object Pose and Location保存结果
8. 按a全选并按Del删除当前全部物体
9. 继续点击Load Wbr导入下一个物体，此时不再需要调整视角
10. 如果实在难以匹配，或者人体重建明显有问题，点击右上角delete删除

**注意**
1. 很多图片人体和物体无法精确按照图片摆放，优先保证物体和人相对大小、物体姿态以及位置的准确
2. 参考图片中有各别图片物体框明显不准，这种情况按照经验和常识进行摆放
3. 对于实在无法标注的图片请记录下来
4. 人的位置已经锁定，不可以解锁移动
