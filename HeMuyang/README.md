# 何沐阳
## 元培学院 1800017780
# 动漫头像的生成

这是何沐阳同学负责部分的说明文档。

**动漫头像生成.pptx**是6月5日project报告的slide。

何沐阳首先在[DCGAN-tensorflow](https://github.com/carpedm20/DCGAN-tensorflow)的基础上实现了一个Deep Convolution Generative Adversarial Networks用于动漫头像的生成。

- 代码见DCGAN.py
- 其中训练数据集为faces.zip，来自知乎用户何之源的文章[GAN学习指南：从原理入门到制作生成Demo](https://zhuanlan.zhihu.com/p/24767059)
- 训练生成的数据集为generated_faces.zip

在此基础上，何沐阳希望做到给定特征，生成动漫头像，参考了github上[Animation-Avatar-Generation](https://github.com/Universalzby/Anime-avatar-generate-with-GAN/blob/master/Gan.ipynb)中的ACGAN，即*Conditional Image Synthesis With Auxiliary Classifier GANs*, Odena A, 2017。

ACGAN的Discriminator除了被用来给真实度评分，其提取的图像特征还被用来做分类，判定输入图片的类别。生成器除了提供一个噪音，还需要提供一个类条件。Loss Function在无条件GAN的基础上添加了一个分类损失项，训练Discriminator的时候，会引导Discriminator对数据集中图片做出正确分类，训练Generator的时候会引导生成器产生与类条件一致的结果。

何沐阳使用了原repo中的代码，见ACGAN-code，训练集使用了原repo提供的set，见ACGAN-image，效果图见ACGAN-result。
