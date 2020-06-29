# coding: UTF-8
#图片识别模块
import tensorflow as tf
import os
import numpy as np
import matplotlib.pyplot as plt


res = ['beerbottle', 'glass', 'metal', 'plastic']

with tf.compat.v1.gfile.FastGFile('D:\\tensorflowmodel\\models-master\\research\\object_detection\\plastic_inference_graph_ssd\\output_graph.pd', 'rb') as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

with tf.compat.v1.Session() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name(
        'final_result:0')  
    # 图片的位置
    for root, dirs, files in os.walk('D:\\tensorflowmodel\\models-master\\research\\object_detection\\objrecog\\recognize\\temp_file'):  
        for file in files:
            image_data = tf.compat.v1.gfile.FastGFile(os.path.join(root, file),
                                            'rb').read()  # 返回数据
            # 预估结果
            predictions = sess.run(softmax_tensor, {
                'DecodeJpeg/contents:0': image_data})  
            predictions = np.squeeze(predictions)

            image_path = os.path.join(root, file)
            print(image_path)
            
            top_k = predictions.argsort()[-1:][::-1]  # 概率最高的一个
            for node_id in top_k:
                score = predictions[node_id]
                print('%s (score=%.5f)' % (res[node_id], score))
            print()

            if score > 0.6:
                # 写入txt文件
                result2txt=str(res[node_id])          # 先将其转为字符串才能写入
                with open('D:\\tensorflowmodel\\models-master\\research\\object_detection\\objrecog\\result.txt','w') as file_handle:   # .txt可以不自己新建,代码会自动新建
                    file_handle.write(result2txt)     # 写入
                    file_handle.close()
                
            else:
                with open('D:\\tensorflowmodel\\models-master\\research\\object_detection\\objrecog\\result.txt','w') as file_handle:   # .txt可以不自己新建,代码会自动新建
                    file_handle.write('Non-recyclable waste')     # 写入
                    file_handle.close()
