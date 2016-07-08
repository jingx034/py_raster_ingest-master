# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:08:57 2016
Improve on Fri July 8 2016

@author: jingx034

Build xml file
"""

import lxml.etree as ET
import csv
import ntpath

def build_xml(csv_path,xml_path,file_path):
    path,file_name = ntpath.split(xml_path)

        
    Descriptor = ET.Element('StyledLayerDescriptor',version = "1.0.0",xmlns="http://www.opengis.net/sld" )
    
    with open(file_path,'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: 
            if row ['filename'] == file_name[:-4]:
                named = ET.SubElement(Descriptor,'NamedLayer')
                ET.SubElement(named,'Name').text = row['name']
                User = ET.SubElement(named,'UserStyle')
                ET.SubElement(User,'Title').text = row['title']
                ET.SubElement(User,'Abstract').text = row['abstrict']
                feature = ET.SubElement(User,'FeatureTypeStyle')
                rule = ET.SubElement(feature,'Rule')
                raster = ET.SubElement(rule,'RasterSymbolizer')
                colormap = ET.SubElement(raster,'ColorMap',type = row['map_type'])


                with open(csv_path,'rb') as csvfile:
                    read = csv.DictReader(csvfile)
                    for classes in read:
                        #This line for dynamic
                        ET.SubElement(colormap,"ColorMapEntry",color = classes['Color'],quantity = "%s" % classes['Value'],opacity = "${env('%s',0)}"% classes['mnemonics'])

   #This line for basic legend
   #entry = ET.SubElement(colormap,"ColorMapEntry",color = classes['Color'],quantity = "%s" % classes['Value'])
    tree = ET.ElementTree(Descriptor)
    tree.write(xml_path,pretty_print=True,encoding = "utf-8",xml_declaration =True)


#Make sure the the file name in xml_path is the same with filename in style_info.csv!!!
build_xml('C:\Users\jingx034\Desktop\code\legend\Globcover2009_Legend.csv','C:\data\globcover\Globcover2009.xml','C:\data\globcover\style_info.csv')   
  
