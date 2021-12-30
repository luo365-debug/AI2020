from distutils.core import setup

setup(
    name="yolov4_login",
    version="1.0",
    description="我们的人脸登录模块",
    author="21128826",
    packages=[
        "yolov4_login",
        "yolov4_login.data",
        "yolov4_login.utils",
    ],
    package_data={
        "yolov4_login.data":[
            "faces.names",
            "faces.pt",
            "yolov4-tiny.cfg"
        ],
    }
)