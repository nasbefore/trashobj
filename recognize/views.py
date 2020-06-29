from django.shortcuts import render
# from datetime import datetime
from django.http import HttpResponse
import os

# Create your views here.

# def msgproc(request):
#     datalist = []
#     if request.method == "POST":
#         userA = request.POST.get("userA", None)
#         userB = request.POST.get("userB", None)
#         msg = request.POST.get("msg", None)
#         time = datetime.now()
#         with open('msgdata.txt', 'a+') as f:
#             f.write("{}--{}--{}--{}--\n".format(userB, userA,\
#                             msg, time.strftime("%Y-%m-%d %H:%M:%S")))
#     if request.method == "GET":
#         userC = request.GET.get("userC", None)
#         if userC != None:
#             with open("msgdate.txt", "r") as f:
#                 cnt = 0
#                 for line in f:
#                     linedata = line.split('--')
#                     if linedata[0] == userC:
#                         cnt = cnt + 1
#                         d = {"userA":linedata[1], "msg":linedata[2]\
#                              , "time":linedata[3]}
#                         datalist.append(d)
#                     if cnt >= 10:
#                         break
#     return render(request, "index.html", {"data":datalist})
n = 0
def upload_file(request):
    # 请求方法为POST时，进行处理
    global n
    if request.method == "POST":
        # 获取上传的文件，如果没有文件，则默认为None
        if request.POST.get('up'): 
            File = request.FILES.get("myfile", None)
            if File is None:
                return HttpResponse("没有需要上传的文件")
            else:
                # 打开特定的文件进行二进制的写操作
                # print(os.path.exists('/temp_file/'))
                with open("./recognize/temp_file/test.jpg", 'wb+') as f:
                    # 分块写入文件
                    for chunk in File.chunks():
                        f.write(chunk)
                # return HttpResponse("UP LOAD!")

        if request.POST.get('app'): 
            os.system('python D:\\tensorflowmodel\\models-master\\research\\object_detection\\objrecog\\recognize\\templates\\Test1.py')

        if request.POST.get('app1'): 
            os.system('python D:\\tensorflowmodel\\models-master\\research\\object_detection\\objrecog\\recognize\\templates\\Test.py')

        if request.POST.get('app2'): 
            os.system('python D:\\tensorflowmodel\\models-master\\research\\object_detection\\objrecog\\recognize\\templates\\camera.py')

    datalist = []
    if request.method == "GET":
        if os.path.isfile("result.txt"):
            with open("result.txt", "r", encoding='utf-8') as f:
                for line in f:
                    linedata = line.split('--')
                    d = {"result": linedata[0],}
                    datalist.append(d)
        #这边datalist.pop()有点危险,一旦到时候没有输出,就将这个pop注释掉试试看
        #datalist.pop()

    return render(request, "index.html", {"data":datalist})

    # return render(request, "index.html")
    #这里的test01app需要删去,这里显示的是我请求页面之后返回的是哪一个页面
# Create your views here.
