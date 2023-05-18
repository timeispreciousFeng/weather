# -*- coding: utf-8 -*-
"""
    weather.py
    ~~~~~~~

    Descriptions

    :author: fatedeity :)
    :copyright: (c) 2022
    :date created: 2022-10-10
"""

import sys

import requests


def generate_weather_text(weather: dict) -> str:
    ret = [
        f'位置：{weather.get("province")}-{weather.get("city")}  今天：{weather.get("date")}',
        f'当前：{weather.get("temp")}°C  最低：{weather.get("low")}°C  最高：{weather.get("high")}°C',
        f'空气质量：{weather.get("airQuality")}  湿度：{weather.get("humidity")}',
        f'风向：{weather.get("wind")}  PM2.5：{weather.get("pm25")}',
    ]
    return '\n'.join(ret)


def get_weather(city: str) -> dict:
    url = 'http://autodev.openspeech.cn/csp/api/v2.1/weather'
    params = {
        'openId': 'aiuicus',
        'clientType': 'android',
        'sign': 'android',
        'city': city,
    }
    res = requests.get(url, params=params).json()
    return res['data']['list'][0]


def get_weather_text(city: str) -> str:
    weather = get_weather(city)
    return generate_weather_text(weather)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        ret = [get_weather_text(_) for _ in sys.argv[1:]]
        print('\n\n'.join(ret))
    else:
        print('请求参数错误')
