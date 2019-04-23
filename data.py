from dijkstar import Graph
graph = Graph()


roomNameDict = dict()
roomDirDict = dict()#need to add data to this
graph.add_edge('1', 'F02', {'cost': 18}) #add graph edges
roomNameDict["First floor Entrance"] = "1" #the entrance to a particular floor is the no. of the floor as in this is entrance to the first floor
roomNameDict["Heat transfer lab"] = "F02"
#add the direction sentences according to the syntax as follows...Also add left or right direction whenever required
roomDirDict["1,F02"] = "Walk from entrance of the floor turn left towards the Heat Transfer lab."
roomDirDict["F02,1"] = "From the heat transfer lab walk towards the exit of the floor."
graph.add_edge('F02', 'F06', {'cost': 13})
roomDirDict["F02,F06"] = "Walk towards the opposite lab"
roomDirDict["F06,F02"] = "Walk towards the opposite lab"
roomNameDict["Design Engineering lab"] = "F06"
graph.add_edge('F06', 'F21', {'cost': 55})
roomDirDict["F06,F21"] = "Turn right and then take another right towards DCLD & MPA lab"
roomDirDict["F21,F06"] = "Turn left and then take another left towards design engineering lab"
roomNameDict["DCLD & MPA lab"] = "F21"
graph.add_edge('F21', 'F22', {'cost': 14})
roomDirDict["F21,F22"] = "Walk right towards the adjacent lab for embedded system/project/OOP lab"
roomDirDict["F22,F21"] = "Walk left towards the adjacent lab for DCLD & MPA lab"
roomNameDict["Embedded system/project/oop lab"] = "F22"
graph.add_edge('F22', 'F23', {'cost': 15})
roomDirDict["F22,F23"] = "Walk right towards the adjacent lab for DBMS/computer design and system software lab"
roomDirDict["F23,F22"] = "Walk left towards the adjacent lab for Embedded system/project/OOP lab"
roomNameDict["DBMS/computer design and system software lab"] = "F23"
graph.add_edge('F23', 'F24', {'cost': 27})
roomDirDict["F23,F24"] = "Walk right towards the adjacent lab for dsp/mp lab"
roomDirDict["F24,F23"] = "Walk left towards the adjacent lab for DBMS/computer design and system software lab"
roomNameDict["dsp/mp lab"] = "F24"
graph.add_edge('F24', 'F38', {'cost': 85})
roomDirDict["F24,F38"] = "Turn right and then take another right towards digital communication & microwave lab"
roomDirDict["F38,F24"] = "Turn left and then take another left towards dsp/mp lab"
roomNameDict["digital communication & microwave lab"] = "F38"
graph.add_edge('F38', 'F37', {'cost': 17})
roomDirDict["F38,F37"] = "Walk right towards the adjacent lab for power electronics lab"
roomDirDict["F37,F38"] = "Walk left towards the adjacent lab for digital communication & microwave lab"
roomNameDict["power electronics lab"] = "F37"
graph.add_edge('F37', 'F36', {'cost': 23})
roomDirDict["F37,F36"] = "Walk right towards the adjacent lab for measurement management lab"
roomDirDict["F36,F37"] = "Walk left towards the adjacent lab for power electronics lab"
roomNameDict["measurement management"] = "F36"
graph.add_edge('F36', '1', {'cost': 14})
roomDirDict["F36,1"] = "Walk straight towards the entrance"
roomDirDict["1,F36"] = "Walk straight towards measurement management lab"
roomNameDict["First floor emergency exit 1"] = "E11"
roomNameDict["First floor emergency exit 2"] = "E12"
graph.add_edge('CHMAN', 'E11', {'cost': 20})
graph.add_edge('E11', 'CHMAN', {'cost': 20})
roomDirDict["CHMAN,E11"] = "Walk straight towards the First floor emergency exit 1"
roomDirDict["E11,CHMAN"] = "Walk straight towards Banga sir's cabin"
graph.add_edge('E01', 'E11', {'cost': 40})
graph.add_edge('E11', 'E01', {'cost': 40})
roomDirDict["E01,E11"] = "Head up towards First floor emergency exit 1"
roomDirDict["E11,E01"] = "Head down towards ground floor emergency exit 1"
roomNameDict["Sensors lab"] = "F18"
graph.add_edge('E11', 'F18', {'cost': 13})
graph.add_edge('F18', 'E11', {'cost': 13})
roomDirDict["E11,F18"] = "Turn right towards first lab"
roomDirDict["F18,E11"] = "Turn left towards emergency exit 1"
graph.add_edge('F18', 'F06', {'cost': 45})
graph.add_edge('F06', 'F18', {'cost': 45})
roomDirDict["F18,F06"] = "Take a left turn and then turn right towards design engineering lab"
roomDirDict["F06,F18"] = "Take a right turn and then turn left towards sensors lab"
graph.add_edge('F18', 'F21', {'cost': 27})
graph.add_edge('F21', 'F18', {'cost': 27})
roomDirDict["F21,F18"] = "Take a right turn and then turn left towards sensors lab"
roomDirDict["F18,F21"] = "Take a left turn and then turn right towards DCLD & MPA lab"
graph.add_edge('E12', 'F24', {'cost': 50})
graph.add_edge('F24', 'E12', {'cost': 50})
roomDirDict["E12,F24"] = "Take a right turn and then turn left towards DSP/MP lab"
roomDirDict["F24,E12"] = "Take a left turn and then turn right towards First floor emergency exit 2"

graph.add_edge('0', '1', {'cost': 56})
graph.add_edge('1', '0', {'cost': 56})
roomDirDict["0,1"] = "Turn right and take stairs going up. Then turn right towards the entrance"
roomDirDict["1,0"] = "Turn right and take stairs going down. Then turn right towards the entrance"
graph.add_edge('E12', 'E02', {'cost': 40})
graph.add_edge('E02', 'E12', {'cost': 40})
roomDirDict["E02,E12"] = "Head up towards First floor emergency exit 2"
roomDirDict["E12,E02"] = "Head down towards ground floor emergency exit 2"


roomNameDict["Ground floor emergency exit 1"] = "E01"
roomNameDict["Ground floor emergency exit 2"] = "E02"
graph.add_edge('E02', 'G09', {'cost': 33})
graph.add_edge('G09', 'E02', {'cost': 33})
roomDirDict["E02,G09"] = "Take a right turn and then turn left towards CPPS lab(lab 4)"
roomDirDict["G09,E02"] = "Take a left turn and then turn right towards Ground floor emergency exit 2"

roomNameDict["Ground floor Entrance"] = "0" 
graph.add_edge('G27', 'G26', {'cost': 2})
roomNameDict["Analog electronic circuit lab"] = "G27"
roomNameDict["Digital logic and design lab"] = "G26"
roomDirDict["G27,G26"] = "Walk to the adjacent lab of analog electronic circuit lab"
roomDirDict["G26,G27"] = "Walk to the adjacent lab of Digital logic and design lab"
graph.add_edge('G26', 'G25', {'cost': 5}) 
roomNameDict["Fluid mechanics & machine lab"] = "G25"
roomDirDict["G26,G25"] = "Walk towards the opposite lab for fluid mechanics and machine lab"
roomDirDict["G25,G26"] = "Walk towards the opposite lab for digital logic and design lab"
graph.add_edge('G25', 'G24', {'cost': 13})
roomNameDict["Physics lab"] = "G24"
roomDirDict["G25,G24"] = "Walk to the lab next to fluid mechanic and machine lab"
roomDirDict["G24,G25"] = "Walk to the lab before physics lab"
graph.add_edge('G24', 'G14', {'cost': 50})
roomNameDict["Chemistry lab"] = "G14"
roomDirDict["G24,G14"] = "Take a left turn and walk straight till chemistry lab"
roomDirDict["G14,G24"] = "Walk straight and take a right turn towards physics lab"
graph.add_edge('G25', 'G14', {'cost': 48})
roomDirDict["G25,G14"] = "Walk straight from fluid mechanics and machine lab towards chemistry lab"
roomDirDict["G25,G14"] = "Walk straight from chemistry lab towards fluid mechanics and machine lab"
graph.add_edge('G14', 'G13', {'cost': 16})
roomDirDict["G14,G13"] = "Turn left towards computer center(lab 8)"
roomDirDict["G14,G13"] = "Turn left towards chemistry lab"
roomNameDict["Computer centre"] = "G13"
graph.add_edge('G13', 'CHMAN', {'cost': 15})
roomDirDict["G13,CHMAN"] = "Turn left towards Banga sir's cabin"
roomDirDict["CHMAN,G13"] = "Turn right towards computer center(lab 8)"
roomNameDict["Banga sir's cabin"] = "CHMAN"
graph.add_edge('G14', 'CHMAN', {'cost': 10})
roomDirDict["G14,CHMAN"] = "Walk straight and turn left for Banga sir's cabin"
roomDirDict["CHMAN,G14"] = "Turn right towards chemistry lab"
graph.add_edge('G25', 'CHMAN', {'cost': 37})
roomDirDict["CHMAN,G25"] = "Turn left and walk straight towards fluid mechanic and machine lab"
roomDirDict["G25,CHMAN"] = "Walk straight towards Banga sir's cabin"
graph.add_edge('G13', 'G12', {'cost': 17})
roomDirDict["G13,G12"] = "Walk right towards the adjacent lab for engineering drawing lab(lab 7)"
roomDirDict["G12,G13"] = "Walk left towards the adjacent lab for computer center(lab 8)"
roomNameDict["Engineering drawing"] = "G12"
graph.add_edge('G12', 'G11', {'cost': 19})
roomDirDict["G12,G11"] = "Walk right towards the adjacent lab for DSA & DAA lab(lab 6)"
roomDirDict["G11,G12"] = "Walk left towards the adjacent lab for engineering drawing lab(lab 7)"
roomNameDict["DSA & DAA"] = "G11"
graph.add_edge('G11' ,'G10', {'cost':15})
roomDirDict["G11,G10"] = "Walk right towards the adjacent lab for OS & UNIX lab(lab 5)"
roomDirDict["G10,G11"] = "Walk left towards the adjacent lab for DSA & DAA lab(lab 6)"
roomNameDict["OS and LINUX lab"] = "G10"
graph.add_edge('G10', 'G09', {'cost': 17})
roomDirDict["G10,G09"] = "Walk right towards the adjacent lab for CPPS lab(lab 4)"
roomDirDict["G09,G10"] = "Walk left towards the adjacent lab for OS & UNIX lab(lab 5)"
roomNameDict["CPPS lab"] = "G09"
graph.add_edge('G09', 'G08', {'cost': 71})
roomDirDict["G09,G08"] = "Take a right and then take another right towards the CSE project lab"
roomDirDict["G08,G09"] = "Take a left and then another left towards CPPS lab(lab 4)"
roomNameDict["CSE project lab"] = "G08"
graph.add_edge('G08', 'G07', {'cost': 17})
roomDirDict["G08,G07"] = "Walk right towards the adjacent lab for computer graphics lab"
roomDirDict["G07,G08"] = "Walk left towards the adjacent lab for CSE project lab"
roomNameDict["Computer Graphics"] = "G07"
graph.add_edge('G07', 'G06', {'cost': 19})
roomDirDict["G07,G06"] = "Walk right towards the adjacent lab for language lab"
roomDirDict["G06,G07"] = "Walk left towards the adjacent lab for computer graphics lab"
roomNameDict["Language lab"] = "G06"
graph.add_edge('G06', '0', {'cost': 12})
roomDirDict["G06,0"] = "Walk straight towards the entrance"
roomDirDict["0,G06"] = "Walk straight towards language lab"

graph.add_edge('F02', '1', {'cost': 18})
graph.add_edge('F06', 'F02', {'cost': 13})
graph.add_edge('F21', 'F06', {'cost': 55})
graph.add_edge('F22', 'F21', {'cost': 14})
graph.add_edge('F23', 'F22', {'cost': 15})
graph.add_edge('F24', 'F23', {'cost': 27})
graph.add_edge('F38', 'F24', {'cost': 85})
graph.add_edge('F37', 'F38', {'cost': 17})
graph.add_edge('F36', 'F37', {'cost': 23})
graph.add_edge('1', 'F36', {'cost': 14})

graph.add_edge('G26', 'G27', {'cost': 2})
graph.add_edge('G25', 'G26', {'cost': 5}) 
graph.add_edge('G24', 'G25', {'cost': 13})
graph.add_edge('G14', 'G24', {'cost': 50})
graph.add_edge('G14', 'G25', {'cost': 48})
graph.add_edge('G13', 'G14', {'cost': 16})
graph.add_edge('CHMAN', 'G13', {'cost': 15})
graph.add_edge('CHMAN', 'G14', {'cost': 10})
graph.add_edge('CHMAN', 'G25', {'cost': 37})
graph.add_edge('G12', 'G13', {'cost': 17})
graph.add_edge('G11', 'G12', {'cost': 19})
graph.add_edge('G10' ,'G11', {'cost':15})
graph.add_edge('G09', 'G10', {'cost': 17})
graph.add_edge('G08', 'G09', {'cost': 71})
graph.add_edge('G07', 'G08', {'cost': 17})
graph.add_edge('G06', 'G07', {'cost': 19})
graph.add_edge('0', 'G06', {'cost': 12})