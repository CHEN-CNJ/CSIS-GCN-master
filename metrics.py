import tensorflow as tf

def masked_softmax_cross_entropy(preds, labels, mask):
    """Softmax cross-entropy loss with masking."""
    loss = tf.nn.softmax_cross_entropy_with_logits(logits=preds, labels=labels)
    mask = tf.cast(mask, dtype=tf.float32)
    mask /= tf.reduce_mean(mask)  # 对损失进行归一化，以避免掩码对损失的影响
    loss *= mask  # 将损失张量乘以掩码张量，以过滤掉不需要计算损失的样本
    return tf.reduce_mean(loss)


def masked_accuracy(preds, labels, mask):
    correct_prediction = tf.equal(tf.argmax(preds, 1), tf.argmax(labels, 1))
    accuracy_all = tf.cast(correct_prediction, tf.float32)
    mask = tf.cast(mask, dtype=tf.float32)
    mask /= tf.reduce_mean(mask)
    accuracy_all *= mask
    return tf.reduce_mean(accuracy_all)


def softmax_cross_entropy(preds, labels):
    loss = tf.nn.softmax_cross_entropy_with_logits(logits=preds, labels=labels)
    return tf.reduce_mean(loss)

def accuracy(preds, labels):
    correct_prediction = tf.equal(tf.argmax(preds, 1), tf.argmax(labels, 1))
    accuracy_all = tf.cast(correct_prediction, tf.float32)
    return tf.reduce_mean(accuracy_all)



