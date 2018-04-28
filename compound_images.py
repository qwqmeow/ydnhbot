#!/usr/bin/env python
# coding:utf-8

# ref:https://www.cnblogs.com/lilinwei340/p/6474170.html
from PIL import Image, ImageFont, ImageDraw
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def compound_image(input_img,text=None):
    base_img = Image.open(ur'base_img.jpg')
    box = (217, 532, 358, 654)
    tmp_img = Image.open(ur'./{}'.format(input_img))
    # tmp_img = tmp_img.convert('1') # convert image to black and white

    #region = tmp_img.crop((0,0,304,546)) #选择一块区域
    #或者使用整张图片
    region = tmp_img

    #使用 paste(region, box) 方法将图片粘贴到另一种图片上去.
    # 注意，region的大小必须和box的大小完全匹配。但是两张图片的mode可以不同，合并的时候回自动转化。如果需要保留透明度，则使用RGMA mode
    #提前将图片进行缩放，以适应box区域大小
    # region = region.rotate(180) #对图片进行旋转
    region = region.resize((box[2] - box[0], box[3] - box[1]))
    base_img.paste(region, box)
    if text:
        draw = ImageDraw.Draw(base_img)
        font = ImageFont.truetype("./font.ttf", 18)
        position = [(447, 578), (447, 596), (447, 615)]
        for index, char in enumerate(text[:3]):
            draw.text(position[index], char, font=font, fill=(0,0,0))
    base_img.save('./out.png') #保存图片

if __name__ == '__main__':
    compound_image(input_img = 'tmp.png', text = u'佩奇了')