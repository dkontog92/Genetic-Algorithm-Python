import random as rd

num_in_pop = 40			#Number in population
num_of_genes = 2			#Number of genes in each chromosome
num_of_generations = 1000  
prob_of_cross = 90		# Percentage crossover is probablility of performing crossover
prob_of_mutate = 10
num_of_keepers = 2
RAND_MAX = 10



def calc_fitness(pop_mem,count_pop):
    
	#--------Equation to be optimised----------------------------
    y = (pop_mem[count_pop][0]-5)**2+(pop_mem[count_pop][1]-2)**2
    #------------------------------------------------------------
	
    fitness = abs(y)
    return fitness

def print_sorted(fitness, pop_mem):
        print '\nSorted generation'
        i = 0
        sorted_pop = []
        for fit,pop in sorted(zip(fitness,pop_mem)):
            
            print 'Member ' + str(i) +':\t%.3f, ' % pop[0] + '%.3f' % pop[1]  + '\tFitness: '+ str(fit)
            i = i + 1
            sorted_pop.append(pop)
        return sorted_pop


def main():

    pop_mem = []
    fitness = []
    print '-----------Initial Population-------------'
    #Generate random initial population
    for i in range(num_in_pop):
        random_nums = []
        for j in range(num_of_genes):
			
            random_nums.append(RAND_MAX*rd.random()) 

        pop_mem.append(random_nums)
        fitness.append(calc_fitness(pop_mem,i))
        print 'Member ' + str(i) +':\t%.3f, ' % pop_mem[i][0] + '%.3f' % pop_mem[i][1]+ '\tFitness: '+ str(fitness[i])
    
    
    #Print population in order of fitness and sort pop_mem
    pop_mem = print_sorted(fitness,pop_mem)
    
    
    command = 0
    #Loop through generations
    for count_generations in range(1,num_of_generations+1):
        #print '\nGeneration number %d best fitness is %.3f.' % (count_generations, sorted(fitness)[0])
        while(command != 2):
          command = input('\nPress 1 to calculatate next generation or 2 to calculate all generations: ')
          if command == 1 or command == 2:
             break
         
        
        #Produce offsprings
        pop_mem_new = []
        
        #Add in pop_mem_new the keepers from the previous generation (fittest members)
        for keeper in range(num_of_keepers):     
            pop_mem_new.append(pop_mem[keeper])
            
        #Crossover
        for count_mem in range(num_in_pop-num_of_keepers):
            
            member = []
            #Choose two parents. First parent is chosen from the top 3 
            #parents of the previous generation
            while True:
                parent1 = rd.randint(0,2)
                parent2 = rd.randint(0,num_in_pop-1)
                if parent1 != parent2:
                    break
            
            #1st crossover technique
            for count_gene in range(num_of_genes):
                if pop_mem[parent1][count_gene] > pop_mem[parent2][count_gene]:
                    max_gene = pop_mem[parent1][count_gene]
                    min_gene = pop_mem[parent2][count_gene]
                else:
                    max_gene = pop_mem[parent2][count_gene]
                    min_gene = pop_mem[parent1][count_gene]
                
                member.append(rd.uniform(min_gene,max_gene))
            
            
            
            #Mutation. Mutates 1 of the 2 genes randomly
            if rd.random() <= prob_of_mutate:
               if rd.random() < 0.5:
                  member[0] = RAND_MAX*rd.random()
               else:
                  member[1] = RAND_MAX*rd.random()
            pop_mem_new.append(member)
        
        fitness = []   
        for pop in range(num_in_pop):
            fitness.append(calc_fitness(pop_mem_new,pop))
        pop_mem = print_sorted(fitness,pop_mem_new)
        print '\nGeneration number %d best fitness is %.3f.' % (count_generations, sorted(fitness)[0])
		
		
if __name__ == "__main__":
	main()
		
