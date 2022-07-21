import md2wp.utils as utils

input = open("./demo.md", encoding='utf-8')
md = input.read()
md = md.splitlines()
o = open("./output.txt", "w+", encoding='utf-8')

inCodeBlock=False

for i in range(len(md)):

    print(md[i])

    line = md[i].split(" ")

    if (md[i] == ""): continue


    # ========代码块========

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

    utils.writeText(o,md[i])



    ##for ii in range(len(line)):
    #    if 
    ##   else