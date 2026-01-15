from PIL import Image, ImageDraw, ImageFont

# 600x400のサンプル画像を作成
img = Image.new('RGB', (600, 400), color='#FFE5E5')
draw = ImageDraw.Draw(img)

# テキストを中央に配置
text = "Sample Image"
# デフォルトフォントを使用
try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
except:
    font = ImageFont.load_default()

# テキストの境界ボックスを取得
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# 中央配置の座標を計算
x = (600 - text_width) // 2
y = (400 - text_height) // 2

# テキストを描画
draw.text((x, y), text, fill='#CC0000', font=font)

# 画像を保存
img.save('images/sample.png')
print("Sample image created: images/sample.png")
