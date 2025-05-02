using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

class GeneticAlgorithm
{
    static Random rand = new Random();
    static string target = "Object Detection";
    static int populationSize = 100;
    static int chromosomeLength = target.Length;
    static double mutationRate = 0.01;
    static string geneSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";

    class Individual
    {
        public string Genes;
        public int Fitness;

        public Individual(string genes)
        {
            Genes = genes;
            Fitness = CalculateFitness(genes);
        }
    }

    static int CalculateFitness(string genes)
    {
        int score = 0;
        for (int i = 0; i < target.Length; i++)
        {
            if (genes[i] != target[i])
                score++;
        }
        return score;
    }

    static string GenerateRandomChromosome()
    {
        return new string(Enumerable.Range(0, chromosomeLength)
            .Select(_ => geneSet[rand.Next(geneSet.Length)]).ToArray());
    }

    static Individual Crossover(Individual parent1, Individual parent2)
    {
        int pivot = rand.Next(chromosomeLength);
        string childGenes = parent1.Genes.Substring(0, pivot) + parent2.Genes.Substring(pivot);
        return new Individual(childGenes);
    }

    static void Mutate(ref Individual individual)
    {
        char[] chars = individual.Genes.ToCharArray();
        for (int i = 0; i < chars.Length; i++)
        {
            if (rand.NextDouble() < mutationRate)
                chars[i] = geneSet[rand.Next(geneSet.Length)];
        }
        individual.Genes = new string(chars);
        individual.Fitness = CalculateFitness(individual.Genes);
    }

    static Individual RunGA(out int generations, out long milliseconds)
    {
        Stopwatch stopwatch = Stopwatch.StartNew();
        generations = 0;

        List<Individual> population = Enumerable.Range(0, populationSize)
            .Select(_ => new Individual(GenerateRandomChromosome()))
            .ToList();

        while (true)
        {
            generations++;
            population = population.OrderBy(i => i.Fitness).ToList();

            Console.WriteLine($"Generation {generations}: {population[0].Genes} (Fitness: {population[0].Fitness})");

            if (population[0].Fitness == 0)
                break;

            List<Individual> newPopulation = new List<Individual>();
            for (int i = 0; i < populationSize; i++)
            {
                Individual parent1 = population[rand.Next(populationSize / 2)];
                Individual parent2 = population[rand.Next(populationSize / 2)];
                Individual child = Crossover(parent1, parent2);
                Mutate(ref child);
                newPopulation.Add(child);
            }
            population = newPopulation;
        }

        stopwatch.Stop();
        milliseconds = stopwatch.ElapsedMilliseconds;
        return population[0];
    }

    static void Main()
    {
        int totalGenerations = 0;
        long totalTime = 0;

        for (int i = 1; i <= 3; i++)
        {
            Console.WriteLine($"\nRun {i}:");
            int gens;
            long ms;
            var result = RunGA(out gens, out ms);
            Console.WriteLine($"Found password '{result.Genes}' in {gens} generations and {ms} ms.");
            totalGenerations += gens;
            totalTime += ms;
        }

        Console.WriteLine($"\nAverage Generations: {totalGenerations / 3}");
        Console.WriteLine($"Average Time: {totalTime / 3} ms");
    }
}
