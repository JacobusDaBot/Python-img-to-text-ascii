import math
from PIL import Image
import tkinter as Tk
master = Tk.Tk()
w = Tk.Canvas(master, width=300, height=50)
w.pack()
canvas_height=50
canvas_width=300




########

ml = 175
lw = 110
########
maax   = 256
miin   = 0
dark   = range(ml,maax)

light  = range(lw,ml)

white  = range(miin,lw)
#########
def start():
    # X is the scale factor
    #X=2
    ml = w12.get()
    lw = w13.get()
    X=round(100/w1.get())+10
    #print(X)
    buttonconfirm.configure(bg='red', text='wait')
    master.update()

    inputimg = Image.open(r'img.png')
    greyimage = inputimg.convert('L')
    greyimage.save('greyimage.tif')


    arrpic = {
        'arrx' :[],
        'arry' :[],
        'arrchar':[],
        'schar' : ''
        }
    n=[]
    i=[]

    ix = 0
    
    ####

    ic = 0
    kt = 0
    K = 0
    #
    def color(img):   
        width, height = img.size
        
        for x in range(0,height-X,X):
            for y in range(0,width-X,X):
                gx=x
                gy=y
                ic = 1
                kt = 0
                while ic < X:
                    
                    c, m, y ,k = img.getpixel((gy, gx))#\
                                 
                    gy = gy+1
                    gx = gx+1
                    if k > ml :
                        kt = ic *255
                        break
                    if k > lw:#lw+(lw*0.5):
                        kt = ic * (lw+1)
                        break
                        
                    kt = kt + k
                    ic +=1            
                K = math.trunc(kt/ic)    
                if K in dark  :
                    arrpic['schar'] = arrpic['schar'] + '▓▓'#'█ ▓ ░ ▒'
               
                elif K in light :
                    arrpic['schar'] = arrpic['schar'] + '▒▒'
                elif K in white :
                    arrpic['schar'] = arrpic['schar'] + '░░'
                else :
                    arrpic['schar'] = arrpic['schar'] + 'q'
                    print(K)
                K=0
                    
                
                    
                    
            arrpic['arrchar'].append(arrpic['schar'])
            arrpic['schar'] =''
      

    img = Image.open(r'greyimage.tif')
    img = img.convert('CMYK')

    color(img)
    a_file = open("blank.txt", "w",encoding='utf-8')
    while ix < len(arrpic['arrchar']):
        a_file.writelines(arrpic['arrchar'][ix])
        a_file.writelines('\n')
        ix += 1
    a_file.close()
    ##rfile = open("blank.txt", "rt",encoding='utf-8')
    ##print(rfile.read()) 
    ##rfile.close()
    buttonconfirm.configure(bg='#ffb3fe', text='generate')
    print('end')
##############3############################################
##def update_scales():
##    w12.configure(from_=w13.get())
##    w13.configure(to=w12.get())
    
l1 = Tk.Label(master, text='scale')
l1.pack()
w1 = Tk.Scale(master, from_=0, to=100, orient=Tk.HORIZONTAL,length=200 )
w1.set(30)
w1.pack()

l12 = Tk.Label(master, text='more dark        v         less dark')
l12.pack()
w12 = Tk.Scale(master, from_=0, to=256, orient=Tk.HORIZONTAL,length=200  )

w12.set(110)
##w12.configure(command=update_scales)
w12.pack()


l13 = Tk.Label(master, text='more white       v          less white')
l13.pack()
w13 = Tk.Scale(master, from_=0, to=256, orient=Tk.HORIZONTAL,length=200 )
w13.set(50)
##w13.configure(command=update_scales)
w13.pack()


buttonconfirm = Tk.Button(master, text='generate', width=25, command=start ,bg='#ffb3fe')
buttonconfirm.pack()


buttonclose = Tk.Button(master, text='close', width=25, command=master.destroy)
buttonclose.pack()
Tk.mainloop()
