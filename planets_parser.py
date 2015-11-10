import xml.etree.ElementTree as tree #this imports the element tree module that is used to parse xml code

planets_tree = tree.parse('planets.xml') 
root = planets_tree.getroot() 
print root.attrib['name'] #the root is the root of the xml file, so in this case would be solar system

for child in root: #this will allow us to get information on the children of the root
	print "tag = ", child.tag, "attrib = ", child.attrib['name'] #because the result of caling the child attribute will make a dictionary, by specifing that we want to find the value for name (the key for the entry in the dictionary) it will only give us the value (ie the actual name of the panet) basically, it makes the printed output nicer to include the ['name']

 
for element in planets_tree.iter():
	print element.tag, element.attrib #finds and prints all information stored in xml document


for element in planets_tree.iter(tag='moon'): #finds and prints information about elements with the tags moon

	print element.attrib



