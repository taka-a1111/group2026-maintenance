# メールアドレス画像を作る（Inter Bold・#0F62B4・下線・透明背景）。引数：アドレス 出力 [色]
import sys
from PIL import Image, ImageDraw, ImageFont
addr, out = sys.argv[1], sys.argv[2]
col = tuple(int(sys.argv[3][i:i+2],16) for i in (1,3,5)) if len(sys.argv)>3 else (0x0F,0x62,0xB4)
f = ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-Bold.otf', SIZE := int(sys.argv[4]) if len(sys.argv)>4 else 56)
d0 = ImageDraw.Draw(Image.new('RGBA',(10,10)))
l,t,r,b = d0.textbbox((0,0), addr, font=f)
W, H = 1105, 96
im = Image.new('RGBA',(W,H),(0,0,0,0)); d = ImageDraw.Draw(im)
x = (W-(r-l))//2 - l
d.text((x, 10), addr, font=f, fill=col+(255,))
bb = im.getbbox()
d.rectangle([bb[0]-4, 89, bb[2]+4, 91], fill=col+(255,))
im.save(out, optimize=True); print(out, im.getbbox())
