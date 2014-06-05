import sys

def setup(core, object):
	object.setAttachment('radial_filename', 'deeds/harvesterDeed')
	object.setAttachment('ConstructorTemplate', 'object/installation/mining_ore/construction/shared_construction_mining_ore_harvester_style_heavy.iff')
	object.setAttachment('StructureTemplate', 'object/installation/mining_liquid/shared_mining_liquid_moisture_harvester_elite.iff')	
	object.setAttachment('LotRequirement', 3)
	object.setIntAttribute('examine_maintenance_rate', 120)
	return