from distutils.core import setup

setup(
    name="trafficapp",
    version="1.0",
    description="交通标志智能识别",
    author="21128826",
    packages=[
        "trafficapp.biz",
        "trafficapp.devs",
        "trafficapp.guis",
    ],
    package_data={
        
    }
)