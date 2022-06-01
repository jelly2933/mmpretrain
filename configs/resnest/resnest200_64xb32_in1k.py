_base_ = [
    '../_base_/models/resnest200.py',
    '../_base_/datasets/imagenet_bs32.py',
    '../_base_/default_runtime.py',
    './_randaug_policies.py',
]

# dataset settings

# lighting params, in order of BGR
EIGVAL = [55.4625, 4.7940, 1.1475]
EIGVEC = [
    [-0.5836, -0.6948, 0.4203],
    [-0.5808, -0.0045, -0.8140],
    [-0.5675, 0.7192, 0.4009],
]

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='RandAugment',
        policies={{_base_.policies}},
        num_policies=2,
        magnitude_level=12),
    dict(type='EfficientNetRandomCrop', scale=320, backend='pillow'),
    dict(type='RandomFlip', prob=0.5, direction='horizontal'),
    dict(type='ColorJitter', brightness=0.4, contrast=0.4, saturation=0.4),
    dict(
        type='Lighting',
        eigval=EIGVAL,
        eigvec=EIGVEC,
        alphastd=0.1,
        to_rgb=False),
    dict(type='PackClsInputs'),
]

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='EfficientNetCenterCrop', crop_size=320, backend='pillow'),
    dict(type='PackClsInputs'),
]

# schedule settings
optimizer = dict(
    type='SGD',
    lr=0.8,
    momentum=0.9,
    weight_decay=1e-4,
    paramwise_cfg=dict(bias_decay_mult=0., norm_decay_mult=0.))

param_scheduler = [
    # warm up learning rate schedule
    dict(
        type='LinearLR',
        start_factor=1e-6,
        by_epoch=True,
        begin=0,
        end=5,
        # update by iter
        convert_to_iter_based=True),
    # main learning rate scheduler
    dict(
        type='CosineAnnealingLR',
        T_max=265,
        by_epoch=True,
        begin=5,
        end=270,
    )
]

train_cfg = dict(by_epoch=True, max_epochs=270)
