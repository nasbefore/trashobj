# coding: UTF-8
#视频模块
import cv2, os, time
import numpy as np
from multiprocessing import Process
import _thread
import tensorflow as tf
import os
import numpy as np
import matplotlib.pyplot as plt

class CamaroCap(object):
    # 打开摄像头
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    # 图片信息打印
    def get_image_info(self, image):
        print(type(image))
        print(image.shape)
        print(image.size)
        print(image.dtype)
        pixel_data = np.array(image)
        print(pixel_data)


    with tf.compat.v1.gfile.FastGFile('D:\\tensorflowmodel\\models-master\\research\\object_detection\\plastic_inference_graph_ssd\\output_graph.pd', 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')
    # 逐帧读取数据并保存图片到本地制定位置
    def Camaro_image(self):
        i = 0
        with tf.compat.v1.Session() as sess:
            softmax_tensor = sess.graph.get_tensor_by_name(
                'final_result:0')
            while (1):
                '''
                ret：True或者False，代表有没有读取到图片
                frame：表示截取到一帧的图片
                '''
                ret, frame = self.cap.read()
                ret, frame = self.cap.read()
                
                
                # 保存图片
                cv2.imwrite(r"D:\\tensorflowmodel\\models-master\\research\\object_detection\\objrecog\\recognize\\temp_file\\" + 'a' + ".jpg", frame)
                res = ['beerbottle', 'glass', 'metal', 'waterbottle']
                image_data = tf.compat.v1.gfile.FastGFile("D:\\tensorflowmodel\\models-master\\research\\object_detection\\objrecog\\recognize\\temp_file\\a.jpg",'rb').read()  # Returns the contents of a file as a string.
                predictions = sess.run(softmax_tensor, {
                                'DecodeJpeg/contents:0': image_data})  # tensorboard中的graph中可以看到DecodeJpeg/contents是模型的输入变量名字
                predictions = np.squeeze(predictions)

                top_k = predictions.argsort()[-1:]

                for node_id in top_k:
                    score = predictions[node_id]

                if score > 0.6:
                    cv2.putText(frame,res[node_id]+":"+str(score),(50,50),cv2.FONT_HERSHEY_PLAIN,2.0,(0,0,255),2)
                
                else:
                    cv2.putText(frame,"Non-recyclable waste",(50,50),cv2.FONT_HERSHEY_PLAIN,2.0,(0,0,255),2)
                # 展示图片
                cv2.imshow('capture', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                
if __name__ == '__main__':
    outmasages = CamaroCap()
    outmasages.Camaro_image()
    outmasages.cap.release()
    cv2.destroyAllWindows()


