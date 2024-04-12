# 背景介绍
我们经常看到把小说转成的视频,他们是怎么制作的呢？

第一步是把小说原文转成图片

第二步在把图片加上配乐，剪辑成视频(一般借助剪辑软件完成，本项目不关注)

本项目主要关注第一步，如何把小说文本转成图片

效果图见 pictures 文件夹

加上剪辑后的完整视频见 https://www.bilibili.com/video/BV1FH4y1T7Ew/

 
# 依赖
需要pillow库，并且由于某些原因，必须使用9.5.0及以前的版本

`pip install pillow==9.5.0`

否则会报getsize的错（因为pillow 10.0就不支持getsize了）

可以理解为一个兼容性bug了，感兴趣的朋友可以自己修改这个bug

# Quick Start
## 1. 修改文件路径
放置好txt文本文件和一个用来存放输出图片的空文件夹

比如我的txt文本文件是“知乎推广文.txt”

输出文件夹是"pcitures"

我就在python代码里修改这里：

```python
    file_path = '知乎推广文.txt'
    output_folder = 'pictures'
```

## 2. 设置每张图片行数、图片大小、字体、行间距等 

会将指定的文本文件按每3行一个图片的方式，转成一张张600x900的图片

（这里行数、字体、图片像素大小、图片背景色、行间距、上下留白，左右空隙都是可以修改的）


### 设置行数
设置行数，即每张图片显示小说文本的多少行

修改`liens_per_image即可`

我默认是每张图显示原文三行（差不多是人眼睛每次看的数量了,也有100多字，再多就不好看了）

```python
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
           
```
### 设置图片大小、图片背景色、字体大小

我因为自己本身要把图片上传到手机端，所以设置了600x900的图片大小，文字用的是微软的simhei字体，设置的比较大 fontsize=40

图片大小是image_width和image_height，看着改就行

左右空隙是Left_margin

上下留白是upper_margin

行间距是line_height

这三个参数都是匹配的字体大小font_size，字体越大则空隙留白行间距越大

```python
def create_image(text, font_path='simhei.ttf', font_size=40):
    image_width=600
    image_height=900
    image_size=(image_width,image_height)
    left_margin=font_size
    upper_margin=font_size*2
    line_height=font_size+10 #行间距
    letter_per_line=(image_width-2*left_margin) // font_size

    # 创建一个空白图片
    image = Image.new('RGB', image_size, color=(255, 255, 255)) # 背景颜色在这里改

```

## 3. 执行
直接执行text2pic.py即可

执行完看输出文件夹的图片，如果不好看请回到第2步调节参数

如果执行报错了请看pillow库是否安装了9.5.0版本的

`pip install pillow==9.5.0`

# Others

如果有其他问题请提issue，谢谢
