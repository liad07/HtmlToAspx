import os
dircetory=input("enter name of directory\n")
os.mkdir(dircetory)
name=input("enter name of file\n")
f = open(f"{name}.html", "r")
x=f.read().split("\n")
f = open(f"{dircetory}/{name}.aspx", "a")
f.write(f'<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="{name}.aspx.cs" Inherits="{dircetory}.{name}" %>\n')
for y in x:
  if y=="<head>":
    y='<head runat="server">\n'
  if y == "<body>":
    y=""
    f.write("<body>\n")
    f.write('<form id="form1" runat="server">\n')
    f.write('<div>\n')
  if y=="</body>":
    y=''
    f.write("</div>\n")
    f.write("</form>\n")
    f.write("</body>\n")
  f.write(f'{y}\n')
f.close()
