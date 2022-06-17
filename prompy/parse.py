from strictyaml import load, Map, Str, Int, Seq, YAMLError

IN_SCHEMA = Map({"endpoint": Str(), "token": Str()})
OUT_SCHEMA = Map({"format": Str(), 
		  "name": Str(),
		  "storage": Map({
			"type": Str(),
			"config": Map({
				"bucket": Str(),
				"endpoint": Str(),
				"access_key": Str(),
				"secret_key": Str(),
			}),
		  }),
		})

def inconfig(infile="input-config.yaml", outfile="output-config.yaml"):
	with open(infile) as f:
		return load(f.read(), IN_SCHEMA)

def outconfig(outfile="output-config.yaml"):
	with open(outfile) as f:
		return load(f.read(), OUT_SCHEMA)

