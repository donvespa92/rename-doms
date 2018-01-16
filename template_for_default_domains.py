# Template file for fluid and solid domains
# Material for solid domains: Aluminium
# Material for fluid domains: Water
# Every other option is set to default

def templates(domtype):
    template_domain_solid = """

# ----- Domain: !DOMAIN_NAME! 

DOMAIN: !DOMAIN_NAME!
		Coord Frame = Coord 0
		Domain Type = !DOMAIN_TYPE!
		Location = !DOMAIN_LOCATION!
		
		DOMAIN MODELS: 
			DOMAIN MOTION: 
				Option = Stationary
			END
			MESH DEFORMATION: 
				Option = None
			END
		END
		
		SOLID DEFINITION: Solid 1
			Material = !DOMAIN_MATERIAL!
			Option = Material Library
			MORPHOLOGY: 
				Option = Continuous Solid
			END
			END
			SOLID MODELS: 
			HEAT TRANSFER MODEL: 
				Option = Thermal Energy
			END
			THERMAL RADIATION MODEL: 
				Option = None
			END
		END		
	END
# -----------------------------------------

"""

    template_domain_fluid = """

# ----- Domain: !DOMAIN_NAME!

DOMAIN: !DOMAIN_NAME!
		Coord Frame = Coord 0
		Domain Type = !DOMAIN_TYPE!
		Location = !DOMAIN_LOCATION!
		
		DOMAIN MODELS: 
			DOMAIN MOTION: 
				Option = Stationary
			END
			MESH DEFORMATION: 
				Option = None
			END
		END
		
		FLUID DEFINITION: Fluid 1
			Material = !DOMAIN_MATERIAL!
			Option = Material Library
			MORPHOLOGY: 
				Option = Continuous Fluid
			END
			END
			FLUID MODELS: 
			HEAT TRANSFER MODEL: 
				Option = Total Energy
			END
			THERMAL RADIATION MODEL: 
				Option = None
			END
		END		
	END
	
# -----------------------------------------

"""

    if domtype == 'fluid':
        return template_domain_fluid
    elif domtype == 'solid':
        return template_domain_solid
    else:
        return False

