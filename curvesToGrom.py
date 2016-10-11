#
# Copyright (c) 2014 Bigbigsun Software Inc.
# ----------------------------------------------------
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided 'AS IS' and subject to the Bigbigsun programming
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Bigbigsun Source Code License. All rights
# not expressly granted therein are reserved by Bigbigsun Software Inc.
#
# Author:      EriLee
# Email:       EriLee@bigbigsun.com
# DateTime:    [09:17:07 2016-08-31]
# Description: [v002]_select cvrve's set create new pgGroomNode


## Use Peregrine Labs Yeti for Maya2015 v2.0.19

import maya.cmds as cmds


def curvesToGrom(sel_set,sel_obj):
	if cmds.nodeType(sel_obj) != "mesh":
		sel_obj = cmds.listRelatives(sel_obj,shapes=True)[0]
	
	### create pgYetiGroom node
	newPgYetiGroom = cmds.createNode('pgYetiGroom')
	cmds.connectAttr(sel_obj + ".worldMesh[0]",newPgYetiGroom + ".inputGeometry",f=True)
	cmds.connectAttr("time1.outTime",newPgYetiGroom+".currentTime",f=True)

	### rename the parent and node

	transforms = cmds.listRelatives(newPgYetiGroom,p=True)[0]
	cmds.rename(newPgYetiGroom,"tempPgYetiGroomName")
	transform_name = cmds.rename(transforms,"pgYetiGroom")
	newPgYetiGroom = cmds.rename("tempPgYetiGroomName",transform_name + "Shape" )

	### curves to Yeti Groom,Use Yeti's command
	cmds.pgYetiCommand(newPgYetiGroom,convertFromCurves=sel_set,inputGeometry=sel_obj,stepSize=0.1)



if __name__ == "__main__":
	sel_tagObj = cmds.ls(sl=True)
	curvesToGrom(sel_tagObj[0],sel_tagObj[1])