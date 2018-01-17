#V1实现基本的展示型壁球小游戏，

#框架---1.引入pygame库及sys库
import  pygame,sys

#框架---2.初始化initial()及设置
pygame.init()
size = width, height = 1000,600
speed = [1,1]
WHITE = 255,255,255
screen = pygame.display.set_mode(size)#模式设置函数 参数为一个二元元组，表示窗口宽和高
pygame.display.set_caption("pygame壁球_展示版")#标题设置
ball = pygame.image.load("turtle.jpg")#载入一个图片表示为一个surface对象 pygame使用内部定义的surface对象表示所有载入的图像，其中。get_rect()方法返回一个覆盖图像的矩形Rect对象
ballrect = ball.get_rect()#利用get_rect()返回相应的矩形对象
#框架---3.获取事件并诼类响应
    #框架3.4.均处于一个死循环
while True:
    for event in pygame.event.get():#pygame.event.get()--从事件栈中获取事件
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed[0],speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

#框架---4.刷新屏幕
    screen.fill(WHITE)#背景填充 黑色（BLACK = 0，0，0）白色（WHITE = 255，255，255）
    screen.blit(ball,ballrect)#screen.blit(src,dest)---将一个图像绘制在另一个图像上，即将src绘制到dest位置上。通过rect对象引导对壁球的绘制。
    pygame.display.update()#刷新屏幕  update（）---只是更新有变化的部分 flip()---重新绘制整个窗口
