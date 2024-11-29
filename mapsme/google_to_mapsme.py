import os,sys
import numpy as np
import shlex,subprocess
import os,sys,string
from sys import*
import math;
import re
import random

#notes: orange=super, green=restaurant,blue=viewpoint,red=hotel,grey=attention,purple=parking,brown=gas,yellow=toilet

google_map_name=sys.argv[1]#"2021_hiyama_google.kml" #enter the name of the map you download from google
output_map_name=sys.argv[2]#"2021_hiyama.kml" #enter output name

Red="ff0000ff"
Yellow="ff00ffff"
Blue="ffff0000"
Darkblue="ff8B0000"
Navyblue="ff800000"
Blueviolet="ffe22b8a"
Aqua="ffffff00"
Green="ff008000"
Darkgreen="ff003300"
Lime="ff00ff00"
Teal="ff008080"
Olive="ff006666"
Purple="ff800080"
Lavender="fffae6e6"
Indigo="ff82004b"
Orange="ff0080ff"
Orange2="ff0066ff"
Brown="ff336699"
Tan="ff7acaff"
Pink="ffff00ff"
Black="ff000000"
Grey="ff808080"


last=600000

trackcolor=[Red,Yellow,Blue,Green,Purple,Brown,Pink,Navyblue,Aqua,Darkgreen,Lime,Teal,Olive,Tan,Grey,Navyblue,Blueviolet]





final = open(output_map_name,"w")
final.write('<?xml version="1.0" encoding="UTF-8"?>\n')
final.write('<kml xmlns="http://earth.google.com/kml/2.2">\n')
final.write("  <Document>\n")
final.write("  <name>%s</name>\n"%output_map_name)
final.write("  <visibility>1</visibility>\n")

placemark=["placemark-red","placemark-blue","placemark-purple","placemark-yellow","placemark-pink","placemark-brown","placemark-green","placemark-deeppurple","placemark-lightblue","placemark-cyan","placemark-teal","placemark-lime","placemark-deeporange","placemark-gray","placemark-bluegray"]

for i in range(0,len(trackcolor)):
   final.write('    <Style id="line-%s">\n'%trackcolor[i])
   final.write("      <LineStyle>\n")
   final.write("        <color>%s</color>\n"%trackcolor[i])
   final.write("        <width>5</width>\n")
   final.write("      </LineStyle>\n")
   final.write("    </Style>\n")
   final.write('     <StyleMap id="line-%s">\n'%trackcolor[i])
   final.write("      <Pair>\n")
   final.write("        <styleUrl>#line-%s</styleUrl>\n"%trackcolor[i])
   final.write("      </Pair>\n")
   final.write("    </StyleMap>\n")

for i in range(0,len(placemark)):
   final.write('  <Style id="%s">\n'%placemark[i])
   final.write("    <IconStyle>\n")
   final.write("      <Icon>\n")
   final.write("        <href>http://maps.me/placemarks/%s.png</href>\n"%placemark[i])
   final.write("      </Icon>\n")
   final.write("    </IconStyle>\n")
   final.write("  </Style>\n")




#this function only applies to yamap route
def latlonextract(gpxfile,color): #######for yamap gpx files  
   LAT=[]
   LON=[]
   ELE=[]
   routename=str(gpxfile)
   dis=routename.split("-")[0]
   time=routename.split("-")[1]
   ele=routename.split("-")[2]
   for i in range(16,last,2):
      lat=subprocess.getoutput("awk '{print $%s}' %s" %(i,gpxfile))
      lon=subprocess.getoutput("awk '{print $%s}' %s" %(i+1,gpxfile))
      sep=lat.split('=')[0]
      if(sep=="lat"):
         LAT.append(lat.split('"')[1]+",")
         LON.append("          "+lon.split('"')[1]+",")
         ele1=lon.split('>')[2]
         ELE.append(ele1.split('<')[0])
      else:
         break
   final.write("    <Placemark>\n")
   final.write("      <name>%s-%s-%s</name>\n" %(dis,time,ele))
   final.write("      <styleUrl>#line-%s</styleUrl>\n" %color)  
   final.write("      <LineString>\n")
   final.write("        <tessellate>1</tessellate>\n")
   final.write("        <coordinates>\n")
   for i in range(0,len(LAT)-1):
      final.write(LON[i]+LAT[i]+ELE[i]+"\n")
   final.write("        </coordinates>\n")
   final.write("      </LineString>\n")
   final.write("    </Placemark>\n")
   return



def googleextract(filename):  #for google car route  kml files
    Googlekml = open(filename,"r")
    googlekml = Googlekml.readlines()
    name=[]
    coorstartline=[]
    coorendline=[]
    for i in range(0,len(googlekml)): #if wrong,change to 148
       if (googlekml[i].find("<coordinates>") >= 0 and googlekml[i+2].find("</coordinates>") == -1):
          coorstartline.append(i)
          if(googlekml[i-5].find("<name>")>=0):#filter out "<![CDATA[Directions from McDonald's to Fresta]]>"
             if(googlekml[i-5].find("<![CDATA[")>=0):
                name.append((googlekml[i-5].split("<name><![CDATA[")[1].split("]]></name>")[0]))
             else:                            
                name.append((googlekml[i-5].split("<name>"))[1].split("</name>")[0])
          elif(googlekml[i-4].find("<name>")):
             #print(i+1,i-3)
             if(googlekml[i-4].find("<![CDATA[")>=0):
                name.append((googlekml[i-4].split("<name><![CDATA[")[1].split("]]></name>")[0]))
             else:                           
                name.append((googlekml[i-4].split("<name>"))[1].split("</name>")[0])
       if (googlekml[i].find("</coordinates>") >= 0 and googlekml[i-2].find("<coordinates>") == -1):
          coorendline.append(i)
    #print(name)
    Color=random.sample(range(len(trackcolor)), len(name))
    for k in range(0,len(name)):
       final.write("    <Placemark>\n")
       final.write("     <name>%s</name>\n"%name[k])
       final.write("      <styleUrl>#line-%s</styleUrl>\n"%trackcolor[Color[k]])
       final.write("      <LineString>\n")
       final.write("        <tessellate>1</tessellate>\n")
       final.write("        <coordinates>\n")
       for j in range(coorstartline[k]+1,coorendline[k]):
         final.write(googlekml[j])
       final.write("        </coordinates>\n")
       final.write("      </LineString>\n")
       final.write("    </Placemark>\n")



"""
def deleteroute(filename,routename):
    Googlekml = open(filename,"r")
    googlekml = Googlekml.readlines()
    name=[]
    coorstartline=[]
    coorendline=[]
#    print(len(googlekml)
    for i in range(0,len(googlekml)):
       if (googlekml[i].find("<styleUrl>#line") >= 0 and googlekml[i-1].find("<Pair>") == -1 ):
           print((googlekml[i-1].split("<name>"))[1].split("</name>")[0])
    for i in range(0,len(googlekml)): 
       if (googlekml[i].find("<coordinates>") >= 0 and googlekml[i+2].find("</coordinates>") == -1):
          coorstartline.append(i)
          if(googlekml[i-5].find("<name>")>=0):
             name.append((googlekml[i-5].split("<name>"))[1].split("</name>")[0])
          elif(googlekml[i-4].find("<name>")):                      
             name.append((googlekml[i-4].split("<name>"))[1].split("</name>")[0])
       if (googlekml[i].find("</coordinates>") >= 0 and googlekml[i-2].find("<coordinates>") == -1):
          coorendline.append(i)
    for i in range(0,len(name)):
        if(routename==name[i]):
           value=i
           print("value: ",i)
    output = open("new_route.kml","w")
    for i in range(0,coorstartline[value]-5):
        output.write(googlekml[i])
    for i in range(coorendline[value]+3,len(googlekml)):
        output.write(googlekml[i])         


"""

def foldertype(inputfilename):
    foldername=["hotel","restaurant","tourist spots","convenience store","supermarket","mountain","gas","parking","attention","special","museum","others"]
    name_with_icon=["hotel","restaurant","tourist spots","supermarket","mountain","gas","parking","museum"]
    File= open(inputfilename,"r")
    inputfile = File.readlines()
    folderbegin=[]
    folderend=[]
    name=[]
    for j in range(0,len(foldername)):
        for i in range(0,len(inputfile)):
           if(inputfile[i].find("<Folder>")>=0 and inputfile[i+1].find(foldername[j]) >=0 and inputfile[i+1].find("Directions") == -1):
              folderbegin.append(i)
              name.append(foldername[j])
              for k in range(i,len(inputfile)):
                 if(inputfile[k].find("</Folder>")>=0):
                    folderend.append(k)
                    break
    for k in range(0,len(name)):
       if(name[k]=="hotel"):
          color="red"
          icon="Hotel"
       elif(name[k]=="restaurant"):
          color="green"
          icon="Food"
       elif(name[k]=="tourist spots"):
          color="blue"
          icon="Viewpoint"
       elif(name[k]=="convenience store"):
          color="yellow"
       elif(name[k]=="supermarket"):
          color="green"
          icon="Shopping"
       elif(name[k]=="mountain"):
          color="blue"
          icon="Mountain"
       elif(name[k]=="gas"):
          color="brown"
          icon="Gas"
       elif(name[k]=="parking"):
          color="purple"
          icon="Parking"
       elif(name[k]=="attention"):
          color="grey"
       elif(name[k]=="special"):
          color="orange"
       elif(name[k]=="museum"):
          color="blue"
          icon="Museum"
       elif(name[k]=="others"):
          color="bluegray"
#    for m in range(0,len(folderbegin)):
       for l in range(folderbegin[k],folderend[k]): #
              if(inputfile[l].find("<Placemark>")>=0):
                    final.write("  <Placemark>\n")
                    if(inputfile[l+1].find("<name><![CDATA[")>=0):
                        temp_name=(inputfile[l+1].split("<name><![CDATA[")[1].split("]]></name>")[0])
                        final.write("    <name>"+temp_name+"</name>/n")
                    else:                       
                        final.write("    <name>"+inputfile[l+1].split("<name>")[1])
                    final.write("    <styleUrl>#placemark-%s</styleUrl>\n"%color)
                    final.write("    <Point><coordinates>\n")
                    if(inputfile[l+2].find("<description>")>=0):
                       final.write(inputfile[l+6])
                    else:
                       final.write(inputfile[l+5])
                    final.write("    </coordinates></Point>\n")
                    final.write('    <ExtendedData xmlns:mwm="https://maps.me">\n')
                    if((name[k] in name_with_icon) == True):
                       final.write("       <mwm:icon>%s</mwm:icon>\n"%icon)
                    if(inputfile[l+2].find("<description>")>=0):
                       final.write('       <mwm:description>\n')#<mwm:lang code="default">
                       final.write("         "+'<mwm:lang code="default">'+inputfile[l+2].split("<description>")[1].split("</description>")[0]+"</mwm:lang>"+"\n")
                       final.write("       </mwm:description>\n")
                    final.write("    </ExtendedData>\n")
                    final.write("  </Placemark>\n")
                    

#continue description not added, check hand_sample.kml
#find out the color number of each type, the corresponding color to icon
def colortype(inputfilename):
    File= open(inputfilename,"r")
    inputfile = File.readlines()
    color_with_icon=["red","blue","green","purple","brown","orange"]   
    for i in range (0,len(inputfile)):# find out the cut
        if(inputfile[i].find("<coordinates>")>=0 and inputfile[i+2].find("</coordinates>")==-1):
           cut=i
           break
        else:
           cut=len(inputfile)
    for i in range (0,cut):
        if(inputfile[i].find("0288D1")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="blue"
           icon="Viewpoint"
        elif(inputfile[i].find("FF5252")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="red"
           icon="Hotel"
        elif(inputfile[i].find("0F9D58")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="green"
           icon="Food"
        elif(inputfile[i].find("9C27B0")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="purple"
           icon="Parking"
        elif(inputfile[i].find("795548")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="brown"
           icon="Gas"
        elif(inputfile[i].find("F57C00")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="orange"
           icon="Shopping"
        elif(inputfile[i].find("FBC02D")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="orange"
           icon="Shopping"
        elif(inputfile[i].find("F9A825")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="orange"
           icon="Shopping"
        elif(inputfile[i].find("1A237E")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="blue"
           icon="Viewpoint"
        elif(inputfile[i].find("757575")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="gray"
        elif(inputfile[i].find("BDBDBD")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="gray"
        elif(inputfile[i].find("7CB342")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="lime"
        elif(inputfile[i].find("000000")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="gray"
        elif(inputfile[i].find("0097A7")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="teal"
        elif(inputfile[i].find("4E342E")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="brown"
           icon="Gas"
        elif(inputfile[i].find("673AB7")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="purple"
           icon="Parking"
        elif(inputfile[i].find("FFEA00")>=0 and inputfile[i].find("<styleUrl>")>=0):
           color="yellow"
        if(inputfile[i].find("<styleUrl>#icon")>=0 and inputfile[i-1].find("key")==-1): #check if it is an icon,not line and with description
           final.write("  <Placemark>\n")
           if(inputfile[i-1].find("<description>")>=0): #if it is an icon,
             if(inputfile[i-2].find("<name><![CDATA[")>=0):
                temp_name=(inputfile[i-2].split("<name><![CDATA[")[1].split("]]></name>")[0])
                final.write("    <name>"+temp_name+"</name>/n")
             else:
                final.write("    <name>"+inputfile[i-2].split("<name>")[1])
                #print(i-2,inputfile[i-2].split("<name>")[1])
             final.write("    <styleUrl>#placemark-%s</styleUrl>\n"%color)
             final.write("    <Point><coordinates>\n")
             final.write("        "+inputfile[i+3])
             final.write("    </coordinates></Point>\n")  
             final.write('    <ExtendedData xmlns:mwm="https://maps.me">\n')
             if((color in color_with_icon) == True):
                 final.write("       <mwm:icon>%s</mwm:icon>\n"%icon)
             final.write("       <mwm:description>")
             final.write("         "+'<mwm:lang code="default">'+inputfile[i-1].split("<description>")[1].split("</description>")[0]+"</mwm:lang>"+"\n")
             final.write("       </mwm:description>\n")
           else: #if it is an icon,not line and with description
             print("line: ",i,inputfile[i-1].replace("\n","")," done")
             if(inputfile[i-1].find("<name>")>=0 and inputfile[i-1].find("</name>")>=0):
                temp_name=(inputfile[i-1].split("<name>")[1].split("</name>")[0])
                #print("case if:",temp_name)
                print("line: ",i,inputfile[i-1].replace("\n","")," done")
                final.write("    <name>"+temp_name+"</name>\n")
#                final.write("    <name>"+temp_name)
             else:
                #print("case else: ",inputfile[i-2].split("<name>"))
                final.write("    <name>"+inputfile[i-2].split("<name>")[1]+"</name>\n")
             final.write("    <styleUrl>#placemark-%s</styleUrl>\n"%color)
             final.write("    <Point><coordinates>\n")
             final.write("        "+inputfile[i+3])
             final.write("    </coordinates></Point>\n")  
             final.write('    <ExtendedData xmlns:mwm="https://maps.me">\n')
             if((color in color_with_icon) == True):
                 final.write("       <mwm:icon>%s</mwm:icon>\n"%icon)
           final.write("    </ExtendedData>\n")                     
           final.write("  </Placemark>\n")
    return



colortype(google_map_name)
googleextract(google_map_name)

#gpx_route_name=["hiyama/km4.4-hr4.4-ele500-.gpx","hiyama/km4.5-hr4-ele500-.gpx"]

#Color=random.sample(range(len(trackcolor)), len(gpx_route_name))
#for i in range(0,len(gpx_route_name)):
#    latlonextract(gpx_route_name[i],trackcolor[Color[i]])


final.write("  </Document>\n")
final.write("</kml>")
final.close()

print(f"{output_map_name} successfully created")

#deleteroute("allroute.kml","Directions from 广大 to Fukutomi Park Golf Course")
