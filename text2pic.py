from PIL import Image, ImageDraw, ImageFont

def create_image(text, font_path='simhei.ttf', font_size=40):
    image_width=600
    image_height=900
    image_size=(image_width,image_height)
    left_margin=font_size
    upper_margin=font_size*2
    line_height=font_size+10 #行间距
    letter_per_line=(image_width-2*left_margin) // font_size

    # 创建一个空白图片
    image = Image.new('RGB', image_size, color=(255, 255, 255))

    # 创建一个绘图对象
    draw = ImageDraw.Draw(image)

    # 加载字体
    font = ImageFont.truetype(font_path, font_size)
    
    text=text.split('\n')

    line=0

    for i in range(len(text)):
        while len(text[i]) >= letter_per_line:
            draw.text((left_margin, upper_margin+line_height*line), text[i][0:letter_per_line], font=font, fill=(0, 0, 0))
            text[i]=text[i][letter_per_line:]
            line += 1
        # 在图片上添加文本
        if(len(text[i]) < letter_per_line):       
            draw.text((left_margin, upper_margin+line_height*line), text[i], font=font, fill=(0, 0, 0))
            line += 1

    return image



def read_file_and_create_images(file_path, output_folder, lines_per_image=3):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        lines = content.split()
        num_lines = len(lines)
        num_images = (num_lines + lines_per_image - 1) // lines_per_image

        for i in range(num_images):
            start = i * lines_per_image
            end = min((i + 1) * lines_per_image, num_lines)
            text = '\n'.join(lines[start:end])
            image = create_image(text,"C:\\Windows\\Fonts\\simhei.ttf")
            image.save(f'{output_folder}/image_{i}.png')
            
            

if __name__ == '__main__':
    file_path = '知乎推广文.txt'
    output_folder = 'pictures'
    read_file_and_create_images(file_path,  output_folder, 3)
    print("done")
