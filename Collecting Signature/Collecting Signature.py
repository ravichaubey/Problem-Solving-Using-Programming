#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 08:50:05 2020

@author: ravi
"""
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):

    sorted_segments = sorted(segments, key=lambda x: x.end)

    points = []
    while sorted_segments:
        segment = sorted_segments.pop(0)
        point = segment.end
        points.append(point)

        for s in sorted_segments[:]:
            if s.start <= point <= s.end:
                sorted_segments.remove(s)

    return points


if __name__ == "__main__":
    
    data = []
    
    n = int(input())
    for i in range(n):
        ai,bi = map(int,input().split())
        data.append(ai)
        data.append(bi)
    
    segments = list(
        map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=" ")