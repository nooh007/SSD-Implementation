# SSD-Implementation

This repository implements SSD with Resnet-50 Backbone in Pytorch.

This SSD implementation can be used for any custom dataset, and make sure to follow the steps from the Tutorial to avoid any errors.

The model uses Resnet-50 by default. You could use VGG16 as well by following the steps mentioned in the tutorial to change current configuration.

## Sample Predictions by training SSD on FaceMask dataset 
</br>
<img src="https://github.com/user-attachments/assets/4e09eafd-dd85-4db9-98bf-94bcc974df70" width="300">
<img src="https://github.com/user-attachments/assets/83796363-bb47-4423-add6-7bb1b31d6f18" width="300">

## Plots 
</br>
<img src="https://github.com/user-attachments/assets/809156a7-f031-4441-b248-73428383b220" width="300">
<img src="https://github.com/user-attachments/assets/cafd5f71-3a83-4ad9-8277-7994ca947b57" width="300">

project_ssd
```
     -> data
          -> Train
               ->Train
                   ->JPEGImages
          -> Test
               ->Test
                   ->JPEGImages
          -> Val
               ->Val
                   ->JPEGImages
     -> inference_outputs
          -> images
     -> outputs
          -> map.png
          -> train_loss.png
     -> config.py
     -> model.py         
     -> model_resnet.py
     -> requirements.txt
```


## References

- Implementation inspired by the [FasterRCNN-PyTorch repository by explainingai-code](https://github.com/explainingai-code/FasterRCNN-PyTorch).
