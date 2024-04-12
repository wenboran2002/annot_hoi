### Blender
**简介**
基于blender的3d hoi标注工具，从包含human mesh的文件夹读入mesh,同时会自动读入物体的点云以及参考图片，标注者根据参考图片<font color=red>放缩、移动、旋转</font>物体使3d布局符合图片布局。

**下载** （如果电脑已安装blender版本>2.83，需要重新安装一个2.83版本）
* 官网下载：[https://download.blender.org/release/Blender2.83/]
* 安装包：[blender-2.83](https://github.com/username/repository/tree/branch/directory)
  ![install](https://github.com/wenboran2002/annot_hoi/blob/main/imgs/install.png))

**安装插件**
1. 先按a再按Del清楚现有物体
2. 在上边栏选择Edit->Preference->Add-ons,点击install
3. 找到scripts/annot.py并安装，同时在搜索栏搜索annot,找到后在左边方框打√

**标注**
1. 点击右上角Load Wbr,在\src\humans中选择对应的object文件夹
2. 依序load文件，同时会load进物体以及参考图片
3. 用鼠标拖动右上角的z轴朝下，使视角正过来
4. 选中物体，开始标注：
   按<font color=red>s</font>同时移动鼠标为放缩
   按<font color=red>g</font>同时移动鼠标为移动
   按<font color=red>r</font>同时移动鼠标为左右旋转
   按<font color=red>两次r</font>同时移动鼠标为前后旋转
   鼠标拖动可以移动场景，确保各个方位都摆放好
5. 标注结束后，点击右上角Export Object Pose and Location保存结果
6. 按a全选并按Del删除当前全部物体
7. 继续点击Load Wbr导入下一个物体
