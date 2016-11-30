# coding: utf-8
from __future__ import print_function
from PIL import Image
import sys

'''
print ('參數個數為：', len(sys.argv), '個參數。')
print ('參數列表：', str(sys.argv))
'''

def main():
    with Image.open(sys.argv[1]) as srcImg:
        width, height = srcImg.size
        dstImg = Image.new('L', (width, height), 'white')   # Create graylevel image.
        for y in range(height):
            for x in range(width):
                #rgb = (srcImg.getpixel((x, y)), srcImg.getpixel((x, y)), srcImg.getpixel((x, y)))
                rgb = srcImg.getpixel((x, y))
                dstImg.putpixel((width-1-x, height-1-y), rgb)
        dstImg.save('ans2.png')
        
main()
