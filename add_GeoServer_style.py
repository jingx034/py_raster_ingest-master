# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:08:57 2016

@author: jingx034

Build xml file
"""

import lxml.etree as ET
import csv

# the input file path need to be change
filepath = r'C:\Users\jingx034\Desktop\code\legend\Globcover2009_Legend.csv'
outpath = r'C:\data\globcover\Globcover2009.xml'


Descriptor = ET.Element('StyledLayerDescriptor',version = "1.0.0",xmlns="http://www.opengis.net/sld" )

named = ET.SubElement(Descriptor,'NamedLayer')
ET.SubElement(named,'Name').text = "Globcover2009_legend"


User = ET.SubElement(named,'UserStyle')
ET.SubElement(User,'Title').text = "Global Land Cover 2009 Legend"
ET.SubElement(User,'Abstract').text = "Wen fill in"

feature = ET.SubElement(User,'FeatureTypeStyle')
rule = ET.SubElement(feature,'Rule')
raster = ET.SubElement(rule,'RasterSymbolizer')
colormap = ET.SubElement(raster,'ColorMap',type = "intervals")


with open(filepath,'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:  
       #This line for dynamic
       entry = ET.SubElement(colormap,"ColorMapEntry",color = row['Color'],quantity = "%s" % row['Value'],opacity = "${env('%s',0)}"% row['mnemonics'])
       
       #This line for basic legend
       #entry = ET.SubElement(colormap,"ColorMapEntry",color = row['Color'],quantity = "%s" % row['Value'])



tree = ET.ElementTree(Descriptor)
tree.write(outpath,pretty_print=True,encoding = "utf-8",xml_declaration =True)


