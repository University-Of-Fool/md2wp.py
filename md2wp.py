import md2wp.utils as utils

input = open("./demo.md", encoding='utf-8')
md = input.read()
md = md.splitlines()
o = open("./output.txt", "w+", encoding='utf-8')

inCodeBlock=False
inUList=False
inOList=False

for i in range(len(md)):

    #print(md[i])

    line = md[i].split(" ")

    if (md[i] == ""): continue

    # ========代码块（跨行解析）========
    
    if(inCodeBlock):
        if(md[i][0:3]=="```"): # 新行```结束代码块
            utils.writeCodeBlockEnd(o)
            inCodeBlock=False
            continue
        if(md[i][-3:]=="```"): # 代码末尾```结束代码块
            o.write(md[i].rstrip("`"))
            o.write("\n")
            utils.writeCodeBlockEnd(o)
            inCodeBlock=False
            continue
        o.write(md[i])
        o.write("\n")
        continue

    # ========代码块（跨行解析）结束========

    # ========行内样式========
    if(md[i].find("`") !=-1 or md[i].find("*") !=-1 or md[i].find("~~")!=-1 or md[i].find("_") !=-1):
        text=""

        if ((md[i].count("***"))%2 == 0):
            while md[i].count("***") != 0:
                md[i] = md[i].replace("***","<strong><em>",1)
                md[i] = md[i].replace("***","</em></strong>",1)

        if ((md[i].count("**"))%2 == 0):
            while md[i].count("**") != 0:
                md[i] = md[i].replace("**","<strong>",1)
                md[i] = md[i].replace("**","</strong>",1)

        if ((md[i].count("*"))%2 == 0):
            while md[i].count("*") != 0:
                md[i] = md[i].replace("*","<em>",1)
                md[i] = md[i].replace("*","</em>",1)
            
        if ((md[i].count("~~"))%2 == 0):
            while md[i].count("~~") != 0:
                md[i] = md[i].replace("~~","<s>",1)
                md[i] = md[i].replace("~~","</s>",1)

        if ((md[i].count("`"))%2 == 0):
            while md[i].count("`") != 0:
                md[i] = md[i].replace("`","<code>",1)
                md[i] = md[i].replace("`","</code>",1)


    # ========行内样式结束========


    # ========无序列表（跨行解析）========
    if(inUList and (md[i].find("-",0,2)!=-1 and md[i].count("-",0,2)==1)):
        utils.writeUListItem(o,md[i].lstrip(" -"))
        continue
    if (inUList):
        utils.writeUListEnd(o)
        inUList=False
    # ========无序列表（跨行解析）结束========

    # ========图片========
    if(md[i][0:2]=="!["):
        utils.writePic(o)
        continue

    # ========图片结束========

    # ========单行代码块========
    if(md[i] != "```" and md[i][0] == "`" and md[i][-1] == "`"):
        utils.writeCodeBlockStart(o,"")
        o.write(md[i].strip("`"))
        o.write("\n")
        utils.writeCodeBlockEnd(o)
        continue


    # ========单行代码块结束========

    # ========代码块========



    if(md[i][0:3]=="```"):
        inCodeBlock = True
        CodeBlock_Language = md[i].lstrip("`")
        utils.writeCodeBlockStart(o,CodeBlock_Language)
        continue

    # ========代码块结束========

    # ========标题========
    # H1
    
    if(line[0] == "#"):
        utils.writeHeading(o,1,line)
        continue

    # H2
    if(line[0] == "##"):
        utils.writeHeading(o,2,line)
        continue

    # H3
    if(line[0] == "###"):
        utils.writeHeading(o,3,line)
        continue

    # H4
    if(line[0] == "####"):
        utils.writeHeading(o,4,line)
        continue

    # H5
    if(line[0] == "#####"):
        utils.writeHeading(o,5,line)
        continue

    # H6
    if(line[0] == "######"):
        utils.writeHeading(o,6,line)
        continue
    # ========标题结束========

    # ========分割线========
    if(md[i]=="---" or md[i]=="-----" or md[i]=="***" or md[i]=="*****"):
        utils.writeDivideLine(o)
        continue
    # ========分割线结束========


    # ========无序列表========
    
    
    if(md[i].find("-",0,2)!=-1 and md[i].count("-",0,2)==1):
        inUList = True
        utils.writeUListStart(o)
        utils.writeUListItem(o,md[i].lstrip(" -"))
        continue

    # ========无序列表结束========


    utils.writeText(o,md[i])

