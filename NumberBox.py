import DarwinBox

class NumberBox (DarwinBox.DarwinBox):
	def evaluateIndividual(self, individual):
		value = 0
		
		for c in list(individual):
			value += int(c)
		
		return value

	def averageFitness(self):
		totalFitness = 0.0
		for ind in self.population:
			totalFitness += ind[1]
		return totalFitness / len(self.population)

db = NumberBox()
db.alphabet = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
db.individualLength = 10
db.populationLimit = 100
db.matingPoolSize = 1000
db.generateInitialPopulation()

print db.averageFitness()
db.population.sort(key=lambda x: -x[1])
print db.population[0]

for i in range(1, 100):
	db.evolve()

print ""

print db.averageFitness()
db.population.sort(key=lambda x: -x[1])
print db.population[0]

