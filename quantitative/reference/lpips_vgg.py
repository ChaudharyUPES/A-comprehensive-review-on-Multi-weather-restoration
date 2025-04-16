import lpips
loss_fn = lpips.LPIPS(net='vgg')

def calculate_lpips(gt, restored):
    gt_tensor = lpips.im2tensor(gt)
    res_tensor = lpips.im2tensor(restored)
    return loss_fn(gt_tensor, res_tensor).item()
