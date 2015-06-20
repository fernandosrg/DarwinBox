import random
import math

class DarwinBox:
	def __init__(self):
		self.mutationRate = 0.1
		self.crossoverRate = 0.8
		self.populationLimit = 10
		self.individualLength = 10
		self.matingPoolSize = 100
		self.alphabet = []
		self.population = []
		self.debug = False

	def shouldMutate(self):
		return self.mutationRate > random.random()
	
	def shouldCrossover(self):
		return self.crossoverRate > random.random()
		
	def generateRandomIndividual(self):
		individual = ""
		
		for i in range(0, self.individualLength):
			individual += random.choice(self.alphabet)
		
		return (individual, self.evaluateIndividual(individual))
		
	def generateInitialPopulation(self):
		for i in range(0, self.populationLimit):
			self.population.append(self.generateRandomIndividual())
	
	def crossover(self, individual1, individual2):
		crossoverPoint = random.choice(range(1, self.individualLength))
		
		newIndividual1Code = individual1[0][:crossoverPoint] + individual2[0][crossoverPoint:]
		newIndividual1 = (newIndividual1Code, self.evaluateIndividual(newIndividual1Code))
		
		newIndividual2Code = individual2[0][:crossoverPoint] + individual1[0][crossoverPoint:]
		newIndividual2 = (newIndividual2Code, self.evaluateIndividual(newIndividual2Code))
		
		return (newIndividual1, newIndividual2)
		
	def mutate(self, individual):
		newIndividualGenes = list(individual[0])
		index = random.choice(range(0, self.individualLength))
		newIndividualGenes[index] = random.choice(self.alphabet)
		
		newIndividual = "".join(newIndividualGenes)
		return (newIndividual, self.evaluateIndividual(newIndividual))
		
	def calculateTotalFitness(self):
		totalFitness = 0
		
		for ind in self.population:
			totalFitness += ind[1]
		
		return totalFitness
	
	def generateMatingPool(self):
		matingPool = []
		totalFitness = self.calculateTotalFitness()
		
		for ind in self.population:
			fitnessCoefficient = float(ind[1]) / totalFitness
			
			for i in range(0, int(math.ceil(fitnessCoefficient * self.matingPoolSize))):
				matingPool.append(ind)
		
		return matingPool
		
	def evolve(self):
		newPopulation = []
		
		# Ensures population is even before starting crossover attempt.
		if self.populationLimit % 2 == 1:
			ind = random.choice(self.population)
			
			if(self.shouldMutate()):
				ind = self.mutate(ind)
			
			newPopulation.append(ind)


		# Generates new population
		matingPool = self.generateMatingPool()

		while len(newPopulation) < self.populationLimit :
			index = random.choice(range(0, len(matingPool))	)		
			ind1 = matingPool.pop(index)
			
			index = random.choice(range(0, len(matingPool))	)		
			ind2 = matingPool.pop(index)

			if self.debug: print "Chose", "\"" + ind1[0] + "\"", "and", "\"" + ind2[0] + "\""
			
			if (self.shouldCrossover()):
				oldInd1 = "\"" + ind1[0] + "\""
				oldInd2 = "\"" + ind2[0] + "\""
				children = self.crossover(ind1, ind2)
				ind1 = children[0]
				ind2 = children[1]
				if self.debug: print "Crossover:", oldInd1, "and", oldInd2, "->", "\"" + ind1[0] + "\"", "and", "\"" + ind2[0] + "\""
			
			if(self.shouldMutate()):
				oldInd = "\"" + ind1[0] + "\""
				ind1 = self.mutate(ind1)
				if self.debug: print "Mutated", oldInd, "to", "\"" + ind1[0] + "\""
			
			if(self.shouldMutate()):
				oldInd = "\"" + ind2[0] + "\""
				ind2 = self.mutate(ind2)
				if self.debug: print "Mutated", oldInd, "to", "\"" + ind2[0] + "\""

			if self.debug: print "Resulted in", "\"" + ind1[0] + "\"", "and", "\"" + ind2[0] + "\""
				
			newPopulation.append(ind1)
			newPopulation.append(ind2)

			if self.debug: print ""
		
		self.population = newPopulation
		
	def evaluateIndividual(self, individual):
		return 0;
	
