#!/usr/bin/python3
"""Gerador de lero-lero.
Gera frases de efeito sem significado real."""

import random

#Cada frase é composta por três partes aleatórias;

parte1 = ["O sistema em desenvolvimento", "O novo protocolo de comunicação", "O algoritmo de otimização"]
parte2 = ["possui excelente desempenho", "oferece garantias de precisão acima da média", "preenche uma lacuna significativa"]
parte3 = ["nas aplicações a que se destina", "em relação às opções disponíveis no mercado", ", provendo ampla vantagem competitiva a seus usuários"]

lingua = int(input("Escolha a língua: 1- português; 2- inglês\n"))

if lingua == 2:
	parte1 = []
	parte2 = []
	parte3 = []

print (random.choice(parte1), random.choice(parte2), random.choice(parte3))
