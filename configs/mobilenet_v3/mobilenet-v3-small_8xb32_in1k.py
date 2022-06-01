# Refers to https://pytorch.org/blog/ml-models-torchvision-v0.9/#classification

_base_ = [
    '../_base_/models/mobilenet_v3_small_imagenet.py',
    '../_base_/datasets/imagenet_bs128_mbv3.py',
    '../_base_/default_runtime.py',
]

# schedule settings
optimizer = dict(
    type='RMSprop',
    lr=0.064,
    alpha=0.9,
    momentum=0.9,
    eps=0.0316,
    weight_decay=1e-5)

param_scheduler = dict(type='StepLR', by_epoch=True, step_size=2, gamma=0.973)

train_cfg = dict(by_epoch=True, max_epochs=600)
val_cfg = dict(interval=1)  # validate every epoch
test_cfg = dict()
