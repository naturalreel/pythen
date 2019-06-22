URL_FUNC_DICT=dict()

def route(url):
    def set_func(func):
        #URL_FUNC_DICT["/index.py"]=index
        URL_FUNC_DICT[url]=func
        def call_func(*args,**kwargs):
            return func(*args,**kwargs)
        return call_func
    return set_func
@route("/index.py")
def index():
    with open("./templates/index.html",encoding='UTF-8') as f:
        return  f.read()
@route("/center.py")
def center():
    with open("./templates/center.html",encoding='UTF-8')as f:
        return f.read()
# URL_FUNC_DICT={
#     "/index.py":index,
#     "/center.py":center
# }
def application(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    file_name = env['PATH_INFO']
    # file_name="/index.py"
    '''
    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return "Hello World!"
    '''

    func=URL_FUNC_DICT[file_name]
    return func()