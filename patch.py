import re

webui_file = '../../js/webui.js'
f = open(webui_file,'r')
text = f.read()
f.close()

patched = re.sub(r'theContextMenu\.add\(\[CMENU_CHILD, theUILang.Labels, _bf\]\);\n\s*theContextMenu\.add\(\[CMENU_SEP\]\);', "//theContextMenu.add([CMENU_CHILD, theUILang.Labels, _bf]);\n//theContextMenu.add([CMENU_SEP]);",text)
if patched is not None:
    w = open(webui_file,'w')
    w.write(patched)
    w.close()
else:
    print "no match found"

addtorrent_file = '../../php/addtorrent.php'
f = open(addtorrent_file,'r')
text = f.read()
text = text.replace("$label = trim($_REQUEST['label']);",'$label = trim($_SERVER["PHP_AUTH_USER"]);')
f.close()
w = open(addtorrent_file,'w')
w.write(text)
w.close()


