def writeHeading(file,level,line):
    text=""
    o = file
    level=str(level)
    o.write("<!-- wp:heading {\"level\":"+level+"} -->\n")
    o.write("<h"+level+">")
    for iii in range(len(line)-1):
        text = text + line[iii+1] + " "
    o.write(text.rstrip())
    o.write("</h" + level + ">\n")
    o.write("<!-- /wp:heading -->\n")
    o.write("\n")

def writeText(file,text):
    o=file
    o.write("<!-- wp:paragraph -->\n")
    o.write("<p>"+text+"</p>\n")
    o.write("<!-- /wp:paragraph -->\n")
    o.write("\n")

def writeCodeBlockStart(file,language):
    o = file
    o.write("<!-- wp:code -->\n")
    o.write("<pre class=\"wp-block-code\"><code>\n")

    
def writeCodeBlockEnd(file):
    o = file
    o.write("</code></pre>\n")
    o.write("<!-- /wp:code -->\n")
    o.write("\n")


def writeDivideLine(file):
    o = file
    o.write("<!-- wp:separator -->\n")
    o.write("<hr class=\"wp-block-separator has-alpha-channel-opacity\"/>\n")
    o.write("<!-- /wp:separator -->\n")
    o.write("\n")


def writeUListStart(file):
    o = file
    o.write("<!-- wp:list -->\n")
    o.write("<ul>")

    
def writeUListEnd(file):
    o = file
    o.write("</ul>\n")
    o.write("<!-- /wp:list -->\n")
    o.write("\n")

def writeUListItem(file,text):
    o=file
    o.write("<li>")
    o.write(text)
    o.write("</li>")

def writePic(file):
    o=file
    o.write("<!-- wp:image -->\n")
    o.write("<figure class=\"wp-block-image\"><img alt=""/></figure>\n")
    o.write("<!-- /wp:image -->\n")
    o.write("\n")