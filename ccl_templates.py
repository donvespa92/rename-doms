# Template file for CFX Command Languange

def templates(name):
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

    template_domain_interface ="""

FLOW: Flow Analysis 1
&replace DOMAIN INTERFACE: !INTERFACE_NAME!
Boundary List1 = !SIDE1!
Boundary List2 = !SIDE2!
    Filter Domain List1 = !DOM1!
    Filter Domain List2 = !DOM2!
    Interface Region List1 = !BND1!
    Interface Region List2 = !BND2!
    Interface Type = !IF_TYPE!
    INTERFACE MODELS:
      Option = General Connection
      FRAME CHANGE:
        Option = None
      END
      PITCH CHANGE:
        Option = None
      END
    END
    MESH CONNECTION:
      Option = Automatic
    END
  END
END   
    
"""

    d_template = {'domain_fluid':template_domain_fluid,
                  'domain_solid':template_domain_solid,
                  'domain_interface':template_domain_interface}
    
    return d_template[name]

