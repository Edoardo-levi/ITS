#! /bin/bash

#crea la directory "planets"

mkdir planets

#per ogni pianeta 

for planet in mercurio venere terra marte giove saturno urano nettuno 
do 
	#crea un file con il nome del pianeta nella directory "planets"
	touch planets/$planet
done
