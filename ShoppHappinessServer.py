import json

from flask import Flask,jsonify,request
import time
import os
import base64

from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER='upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#将上传文件限制为最大 16 MB 。 如果请求传输一个更大的文件， Flask 会抛出一个RequestEntityTooLarge异常
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024
app_dir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt','png','jpg','xls','JPG','PNG','xlsx','gif','GIF'])

# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/v1/UploadAvatarImg',methods=['POST'],strict_slashes=False)
def UploadAvatarImg():
    try:
        UserId = request.form.get('UserId', 'default UserId value')
        print('UserId is %s' % UserId)

        upload_dir = os.path.join(app_dir, app.config['UPLOAD_FOLDER'])
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        uploaded_file = request.files['avatar']  # 从表单的file字段获取文件，dc_file为该表单的name值
        if uploaded_file and allowed_file(uploaded_file.filename):  # 判断是否是允许上传的文件类型
            fname = secure_filename(uploaded_file.filename)
            print('file name is %s' % fname)
            uploaded_file.save(os.path.join(upload_dir, fname))  # 保存文件到upload目录

    except IOError as ex:
        print("I/O error({0}): {1}".format(ex.errno, ex.strerror))
        return jsonify({"errno": 1, "msg": "upload failure"})

    return jsonify({"errno": 0, "msg": "upload success"})


@app.route('/v1/UploadMerchandise',methods=['POST'],strict_slashes=False)
def UploadMerchandise():
    merchandise_name = request.form.get('merchandise_name', 'default FileDesc value')
    print('merchandise_name is %s' % merchandise_name)

    merchandise_price = request.form.get('merchandise_price', 'default merchandise_price value')
    print('merchandise_price is %s' % merchandise_price)

    merchandise_desc = request.form.get('merchandise_desc', 'default merchandise_desc value')
    print('merchandise_desc is %s' % merchandise_desc)

    upload_dir = os.path.join(app_dir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    uploaded_files = request.files.getlist("upload_file[]")
    try:
        for uploaded_file in uploaded_files:
            if uploaded_file and allowed_file(uploaded_file.filename):  # 判断是否是允许上传的文件类型
                fname = secure_filename(uploaded_file.filename)
                print('file name is %s' % fname)
                uploaded_file.save(os.path.join(upload_dir, fname))  #保存文件到upload目录
            else:
                return jsonify({"errno":1,"msg":"upload failure"})
    except IOError:
        return jsonify({"errno": 1, "msg": "upload failure"})

    return jsonify({"errno": 0, "msg": "upload success"})


@app.route('/v1/UploadMerchandiseInfo',methods=['POST'],strict_slashes=False)
def UploadMerchandiseInfo():
    for key in request.args.keys():
        print(key, " : ", request.args.get(key))

    upload_dir = os.path.join(app_dir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    uploaded_files = request.files.getlist("dc_file[]")
    try:
        for uploaded_file in uploaded_files:
            if uploaded_file and allowed_file(uploaded_file.filename):  # 判断是否是允许上传的文件类型
                fname = secure_filename(uploaded_file.filename)
                print('file name is %s' % fname)
                uploaded_file.save(os.path.join(upload_dir, fname))  #保存文件到upload目录
            else:
                return jsonify({"errno": 1, "msg": "upload failure"})
    except IOError:
        return jsonify({"errno":1,"msg":"upload failure"})

    return jsonify({"errno": 0, "msg": "upload success"})


# ============================ below functions are just for testing =======================
@app.route('/uploadJson',methods=['POST'],strict_slashes=False)
def api_uploadJson():
    json_data = request.get_json()
    # print(json_data.keys())
    for key in json_data.keys():
        print ("key = %s, value = %s" % (key, json_data[key]))

    # print(json_data["userId"])

    return jsonify({"errno": 0, "msg": "upload success"})





@app.route('/api/upload4',methods=['POST'],strict_slashes=False)
def api_upload4():
    for key in request.args.keys():
        print(key, " : ", request.args.get(key))

    upload_dir = os.path.join(app_dir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    uploaded_files = request.files.getlist("dc_file[]")
    try:
        for uploaded_file in uploaded_files:
            if uploaded_file and allowed_file(uploaded_file.filename):  # 判断是否是允许上传的文件类型
                fname = secure_filename(uploaded_file.filename)
                print('file name is %s' % fname)
                uploaded_file.save(os.path.join(upload_dir, fname))  #保存文件到upload目录
            else:
                return jsonify({"errno": 1, "msg": "upload failure"})
    except IOError:
        return jsonify({"errno":1,"msg":"upload failure"})

    return jsonify({"errno": 0, "msg": "upload success"})


@app.route('/api/upload3',methods=['POST'],strict_slashes=False)
def api_upload3():
    FileDesc = request.form.get('FileDesc', 'default FileDesc value')
    print('FileDesc is %s' % FileDesc)

    FileDesc2 = request.form.get('FileDesc2', 'default FileDesc2 value')
    print('FileDesc is %s' % FileDesc2)

    upload_dir = os.path.join(app_dir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    uploaded_files = request.files.getlist("dc_file[]")
    try:
        for uploaded_file in uploaded_files:
            if uploaded_file and allowed_file(uploaded_file.filename):  # 判断是否是允许上传的文件类型
                fname = secure_filename(uploaded_file.filename)
                print('file name is %s' % fname)
                uploaded_file.save(os.path.join(upload_dir, fname))  #保存文件到upload目录
            else:
                return jsonify({"errno":1,"msg":"upload failure"})
    except IOError:
        return jsonify({"errno": 1, "msg": "upload failure"})

    return jsonify({"errno": 0, "msg": "upload success"})



@app.route('/api/upload2',methods=['POST'],strict_slashes=False)
def api_upload2():
    firstname = request.form.get('firstname','default first name value')
    lastname = request.form.get('lastname','default last name value')
    print('first name is %s' % firstname)
    print('last name  is %s' % lastname)

    upload_dir = os.path.join(app_dir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    uploaded_files = request.files.getlist("dc_file[]")
    try:
        for uploaded_file in uploaded_files:
            if uploaded_file and allowed_file(uploaded_file.filename):  # 判断是否是允许上传的文件类型
                fname = secure_filename(uploaded_file.filename)
                print('file name is %s' % fname)
                uploaded_file.save(os.path.join(upload_dir, fname))  #保存文件到upload目录
            else:
                return jsonify({"errno":1,"msg":"upload failure"})
    except IOError:
        return jsonify({"errno": 1, "msg": "upload failure"})

    return jsonify({"errno": 0, "msg": "upload success"})

@app.route('/api/upload',methods=['POST'],strict_slashes=False)
def api_upload():
    upload_dir = os.path.join(app_dir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    uploaded_file = request.files['dc_file']  # 从表单的file字段获取文件，dc_file为该表单的name值
    if uploaded_file and allowed_file(uploaded_file.filename):  # 判断是否是允许上传的文件类型
        fname = secure_filename(uploaded_file.filename)
        print('file name is %s' % fname)
        ext = fname.rsplit('.',1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        new_filename=str(unix_time) + '.' + ext  # 修改了上传的文件名
        uploaded_file.save(os.path.join(upload_dir, new_filename))  #保存文件到upload目录
        return jsonify({"errno":0,"msg":"upload success"})
    else:
        return jsonify({"errno":1001,"msg":"upload failure"})


json_str = '''
{
   "results": [
      {
        "id": 1,
        "name": "茵曼2017冬装新款套头圆领落肩间色宽松文艺针织衫女",
        "numOfSongs": 13,
        "thumbnail_url": "http://10.4.1.72/ShoppingBackend/images/merchandise1.png"
      },
    
      {
        "id": 2,
        "name": "V领长袖罗纹显瘦长袖",
        "numOfSongs": 8	,
        "thumbnail_url": "http://10.4.1.72/ShoppingBackend/images/merchandise2.png"
      },
    
      {
        "id": 3,
        "name": "半高领百搭条纹落肩袖",
        "numOfSongs": 11,
        "thumbnail_url": "http://10.4.1.72/ShoppingBackend/images/merchandise3.png"
      },
    
      {
        "id": 4,
        "name": "立领收腰绣花长袖百搭宽松外套",
        "numOfSongs": 12,
        "thumbnail_url": "http://10.4.1.72/ShoppingBackend/images/merchandise4.png"
      },
    
      {
        "id": 5,
        "name": "圆领条纹提花百搭保暖套头毛",
        "numOfSongs": 14,
        "thumbnail_url": "http://10.4.1.72/ShoppingBackend/images/merchandise5.png"
      },
    
      {
        "id": 6,
        "name": "落肩羊腿长袖宽松套头毛织毛衣",
        "numOfSongs": 28,
        "thumbnail_url": "http://10.4.1.72/ShoppingBackend/images/merchandise6.png"
      },
    
      {
        "id": 7,
        "name": "头高领蝙蝠袖撞色袖口休闲毛织衫",
        "numOfSongs": 38,
        "thumbnail_url": "http://10.4.1.72/ShoppingBackend/images/merchandise7.png"
      },
    
      {
        "id": 8,
        "name": "活良品文艺民族风刺绣百搭长袖开衫毛衣女秋冬外套",
        "numOfSongs": 8	,
        "thumbnail_url": "http://10.4.1.72/ShoppingBackend/images/merchandise8.png"
      },
    
      {
        "id": 9,
        "name": "印花格子POLO领长袖衬衫衬",
        "numOfSongs": 11,
        "thumbnail_url": "http://10.4.1.72/ShoppingBackend/images/merchandise9.png"
      },
    
      {
        "id": 10,
        "name": "羽绒服女撞色拼接连帽长款羽绒服女中长款",
        "numOfSongs": 17,
        "thumbnail_url": "http://10.4.1.72/ShoppingBackend/images/merchandise10.png"
      }
   ]
}'''


#访问方式： 1 浏览器中http://http://192.168.1.88:5000/scut_query_user?id=5
#           2 advanced rest client中也只能用http://http://192.168.1.88:5000/query_user?id=5
@app.route('/scut_query_user')
def query_user():
    id = request.args.get('id')
    print('id is %d' % int(id))
    # method2 : use json string to return
    return json_str

    #method1: generate a json
    # data = {}
    # data['key'] = 'value'
    # json_data = json.dumps(data)
    # return json_data

@app.route("/login")
def login():
    name = request.args.get('name')
    password = request.args.get('password')

    print('name is %s' % name)
    print('password is %s' % password)

    data = {}
    if(name == "hello" and password == "world"):
        data['status'] = 'success'
    else:
        data['status'] = 'failure'
    json_data = json.dumps(data)
    return json_data


@app.route('/index/<user>', methods=['GET', 'PUT', 'POST', 'DELETE'])
def hello_world2(user):
    api_key = request.args.get('api_key')
    print('api_key is %s' % api_key)

    data = {}
    data['status'] = '%s hao yang de' % user
    json_data = json.dumps(data)
    return json_data

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/scut")
def scut_default():
    return json_str

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
