_base_ = [
    '../_base_/models/swin_transformer/large_224.py',
    '../_base_/datasets/imagenet_bs64_swin_224.py',
    '../_base_/schedules/imagenet_bs1024_adamw_swin.py',
    '../_base_/default_runtime.py'
]

# runtime settings
default_hooks = dict(optimizer=dict(grad_clip=dict(max_norm=5.0)))
