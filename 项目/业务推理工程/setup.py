from distutils.core import setup

setup(
    name="yolov4_traffic",
    version="1.0",
    description="我们的业务模块",
    author="21128826",
    packages=[
        "yolov4_traffic",
        "yolov4_traffic.data",
        "yolov4_traffic.utils",
    ],
    package_data={
        "yolov4_traffic.data":[
            "home.names",
            "home.pt",
            "yolov4-tiny.cfg"
        ],
    }
)