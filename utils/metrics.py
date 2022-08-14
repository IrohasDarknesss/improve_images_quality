import tensorflow as tf

def psnr_metrics(x1, x2):
    return tf.image.psnr(x1, x2, max_val=255)