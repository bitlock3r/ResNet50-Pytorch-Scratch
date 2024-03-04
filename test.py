import torch
import torch.nn as nn
from resnet50 import ResNet50

if __name__ == '__main__':
    random_image = torch.rand(8, 3, 128, 128)  
    model = ResNet50()
    predictions = model(random_image) 
    print(predictions[0])
