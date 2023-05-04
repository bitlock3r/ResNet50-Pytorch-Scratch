# ResNet50-From-Scratch

![resnet50](https://user-images.githubusercontent.com/100022706/236117171-1355049d-10f1-4308-9025-0937284436de.png)

# ResNet Intuition

As a Neural Network gets very deep, vanishing / exploding gradients become a huge problem. ResNet solves this by using “Skip Connections” where layer 1 output goes directly to layer N input.

The concept of “Residual Block”:


![residualblock](https://user-images.githubusercontent.com/100022706/236117258-c0b74550-858c-4422-a383-ce4fb3ba72f4.png)

# References

- ResNet algorithm due to He et al. (2015). The implementation here also took significant inspiration and follows the structure given in the GitHub repository of Francois Chollet:

## Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun - Deep Residual Learning for Image Recognition (2015)

- Official Paper : @ https://arxiv.org/abs/1512.03385
