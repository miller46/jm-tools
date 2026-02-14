from setuptools import setup, find_packages

REQUIRED = [
    "openai",
    "asyncio",
    "requests",
    "discord.py",
    "tiktoken",
    "tweepy",
    "web3==5.15.0",
    "python-telegram-bot==11.1.0",
    "marshmallow_dataclass>=8.5.8",
    "unicorn_binance_rest_api==1.5.0",
    "kucoin_python==1.0.11",
    "gemini-python-unoffc==0.1",
    "coinbasepro==0.4.1",
    "beautifulsoup4>=4.11.1",
    "selenium>=4.8.2",
    "webdriver-manager==3.8.5",
    "websocket-client",
]

setup(
    name='jm-utility-belt',
    version='2.0.12',
    description='JM Utility Belt',
    author='jack',
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIRED,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
