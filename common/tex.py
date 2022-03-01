import numpy as np
header = r'''\documentclass{article}
\usepackage[utf8]{inputenc}

\title{title}
\usepackage[utf8x]{inputenc}
\usepackage[russian]{babel}
\usepackage{graphicx}
\usepackage[top=20mm, left=30mm, right=10mm, bottom=20mm, nohead]{geometry}
\usepackage{indentfirst}
\usepackage{csvsimple}
\renewcommand{\baselinestretch}{1.50}
\begin{document}
'''
end = '\end{document}'
class tex:
    def printhead():
        print(header)

    def printend():
        print(end)

    def printline(line):
        print(line.replace('_', '\_') + '\\\\')

    def addimage(name):
        print('\\includegraphics[scale=0.8]{'+name+'}\\\\')

    def section(str, n = 0):
        print('\\'+'sub'*n+'section{'+str+'}')

    def addtable(table ,name, fmt='%1.3f'):
        filename = f"{name}.csv"
        np.savetxt(filename, table, delimiter=",", fmt=fmt)
        table = '\csvautotabular{'+filename+'}\\\\'
        print(table)

    def plaintext(obj):
        print('\\begin{verbatim}\n' +
              f'{obj}\n' +
              '\\end{verbatim}')
