import easygui
import easygui as g
import generate_yellow as gen
import editor.editors
# as editors
message = '是否生成?'
message1 = '22'
def moveFileto(sourceDir,  targetDir):
    import os
    import shutil 
    shutil.copy(sourceDir,  targetDir)
def uiShow(message):
    while (1):
        Yes_or_No = easygui.buttonbox(title=" 高清人头 ",msg=message, choices=['生成','关闭'])
        if Yes_or_No == '生成': 
            #easygui.buttonbox(title=" 高清人头 ",msg = '生成中',choices=[])
            gen.main()
            Look = easygui.buttonbox(title=" 高清人头 ",msg = '生成成功',choices=['点击查看'])
            if Look == '点击查看':
                for i in range(20):
                    stillLook = 1
                    while stillLook:
                        imgp = './result/'+str(i).zfill(4) + '.png'
                        choi = easygui.buttonbox(title=" 高清人头 ",image = imgp ,choices=['下一张','不看了','保存'])
                        if choi == '进行修改':
                            direct = easygui.choicebox(msg="调整的方向?",title="高清人头",choices=("年龄","笑容","性别","眼睛的闭合程度","脸的宽度"))
                            if direct == None:
                                continue
                            coeffs = easygui.enterbox(msg="调整的幅度，请输入一个-5~5之间的实数")
                            if coeffs == None:
                                continue
                            editors.modify(i,direct,coeffs)
                            imgpa = './editor/result/'+str(i).zfill(4) + '.png'
                            cho = easygui.buttonbox(title=" 高清人头 ",image = imgpa,choices=['返回','保存'])
                            while cho == imgpa:
                                cho = easygui.buttonbox(title=" 高清人头 ",image = imgpa,choices=['返回','保存'])
                            if cho == '保存':
                                dir = g.filesavebox(filetypes=["*.png"],default="1.png")
                                if dir != None:
                                    moveFileto(imgpa,dir)
                                continue
                            if cho == '返回':
                                continue
                        if choi == '下一张':
                            break
                        if choi =='不看了':
                            easygui.buttonbox(title=" 高清人头 ",msg = '胡舟径 1800012801',choices=['关闭'])
                            stillLook = 0
                            break
                        if choi == '保存':    
                            dir = g.filesavebox(filetypes=["*.png"],default="1.png")
                            if dir != None:
                                moveFileto(imgp,dir)
                            break
                    if stillLook ==0:
                        break
                        
            else:
                break
        if Yes_or_No == '关闭':
            break
        else:
            break
 
if __name__ == '__main__':
    uiShow(message)