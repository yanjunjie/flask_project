#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: score_digital.py
@time: 2017/6/28 下午2:34
"""


from app_frontend.models import ScoreDigital
from app_frontend.tools.db import get_row, get_rows, get_row_by_id, add, edit, delete


def get_score_digital_row_by_id(score_digital_id):
    """
    通过 id 获取积分信息
    :param score_digital_id:
    :return: None/object
    """
    return get_row_by_id(ScoreDigital, score_digital_id)


def get_score_digital_row(*args, **kwargs):
    """
    获取积分信息
    :param args:
    :param kwargs:
    :return: None/object
    """
    return get_row(ScoreDigital, *args, **kwargs)


def add_score_digital(score_digital_data):
    """
    添加积分信息
    :param score_digital_data:
    :return: None/Value of score.id
    """
    return add(ScoreDigital, score_digital_data)


def edit_score_digital(score_digital_id, score_digital_data):
    """
    修改积分信息
    :param score_digital_id:
    :param score_digital_data:
    :return: Number of affected rows (Example: 0/1)
    """
    return edit(ScoreDigital, score_digital_id, score_digital_data)


def delete_score_digital(score_digital_id):
    """
    删除积分信息
    :param score_digital_id:
    :return: Number of affected rows (Example: 0/1)
    """
    return delete(ScoreDigital, score_digital_id)


def get_score_digital_rows(page=1, per_page=10, *args, **kwargs):
    """
    获取积分列表（分页）
    Usage:
        items: 信息列表
        has_next: 如果本页之后还有超过一个分页，则返回True
        has_prev: 如果本页之前还有超过一个分页，则返回True
        next_num: 返回下一页的页码
        prev_num: 返回上一页的页码
        iter_pages(): 页码列表
        iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2) 页码列表默认参数
    :param page:
    :param per_page:
    :param args:
    :param kwargs:
    :return:
    """
    rows = get_rows(ScoreDigital, page, per_page, *args, **kwargs)
    return rows
