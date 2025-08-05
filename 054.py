# Level 054

# ------------------------------
# -- "CLASSIFICANDO" ESPÉCIES --
# ------------------------------


class animal: 
    def __init__(self, especie, nome_cientifico, genero, airtag):
        self.especie = especie
        self.nome_cientifico = nome_cientifico
        self.genero = genero
        self.airtag = airtag

if __name__ == "__main__":

    
    animal0 =animal("Jabuti", "Testudinidae", "F", "xxx.xxx.xx")
    animal1 = animal("Arara", "Anodorhynchus hyacinthinus","M", "xxx.xxx.xx")
    animal2 = animal("Anta Gorda", "Tapirus terrestris", "F", "xxx.xxx.xx")
    animal3 = animal("Papagaio", "Psittacidae", "F", "xxx.xx.xx")
    animal4 = animal("Capivara", "Hydrochoerus hydrochaeris", "M", "xxx.xxx.xx")
    print("")
    print("-" * 100)
    print(f"Nome: {animal0.especie}, Nome Científico: {animal0.nome_cientifico}, Gênero: {animal0.genero} & AirTag: {animal0.airtag}")
    print("-" * 100)
    print(f"Nome: {animal1.especie}, Nome Científico: {animal1.nome_cientifico}, Gênero: {animal1.genero} & AirTag: {animal1.airtag}")
    print("-" * 100)
    print(f"Nome: {animal2.especie}, Nome Científico: {animal2.nome_cientifico}, Gênero: {animal2.genero} & AirTag: {animal2.airtag}")
    print("-" * 100)
    print(f"Nome: {animal3.especie}, Nome Científico: {animal3.nome_cientifico}, Gênero: {animal3.genero} & AirTag: {animal3.airtag}")
    print("-" * 100)
    print(f"Nome: {animal4.especie}, Nome Científico: {animal4.nome_cientifico}, Gênero: {animal4.genero} & AirTag: {animal4.airtag}")
    print("-" * 100)
    print("")