import pymel.core as pm
import maya.cmds
import random

window_name = "Sphere's Trail"
if maya.cmds.window(window_name, exists=True):
    maya.cmds.deleteUI(window_name)
    
def set_color(*args):
	print('This will set the color by getting rgb value from slider')
	num = slider2.getRgbValue()
	print('slider numbers', num)
	
	for s in pm.ls(selection=True):
		print(s)
		pm.polyColorPerVertex(rgb=num, colorDisplayOption=True)

def create_shapes(*args):
	print('This will create shapes')
	num = slider1.getValue()
	print('Number of shapes to be created:', num)
	
	i = 0
	while i < num:
		value = float(i)/num
		angle = random.randint(0,359)
		radius = random.uniform(0.5,2)
		height= random.uniform(0.5,1)
		x,y,z = pm.pointOnCurve('curve1', pr=value, turnOnPercentage=True)
		
		x1 = random.uniform(x-3, x+3)
		y1 = random.uniform(y-3, y+3)
		z1 = random.uniform(z-3, z+3)
		
		shape = options.getValueArray4()		
		j = random.randint(0,3)
		if shape[j] ==True:
			if j ==0:
				figure = pm.polyTorus(r=radius, sr=0.25)
				pm.move(x1,y1,z1,figure)
				i+=1
			elif j ==1:
				figure = pm.polyCone( sx=1, sy=1.5, sz=0.5, r=radius, h=height)
				pm.move(x1,y1,z1,figure)
				i+=1
			elif j==2:
				figure = pm.polySphere(r=radius)
				pm.move(x1,y1,z1,figure)
				i+=1
			elif j==3:
				figure = pm.polyCylinder(r=radius, h=height)
				pm.move(x1,y1,z1,figure)
				i+=1
			pm.select(figure)
			pm.rotate(angle, 0, 0, r=True)
			pm.select(clear=True)

with pm.window():
    with pm.autoLayout():
    	slider1 = pm.intSliderGrp(label='Number of Shapes', minValue=2, maxValue=60, field=True, value=2)
    	options = pm.checkBoxGrp(numberOfCheckBoxes=4, label='Select shapes', labelArray4=['Torus', 'Cone', 'Sphere', 'Cylinder'])
        pm.button(label='Generate Shapes', command=create_shapes)
        slider2 = pm.colorSliderGrp(label='Set Color', rgb=(1, 0, 1))
        button = pm.button(label='Change color', command=set_color)
	
