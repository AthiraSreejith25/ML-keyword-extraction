#!/usr/bin/python3

#importing relevant packages
from gensim.summarization import keywords
from rake_nltk import Rake
import csv


#names of the article files
files = ['Brainstem_pathologies','Epidemiology of Parkinson’s Disease','Hydroxytyrosol as anti-parkinsonian molecule','Introduction Parkinson']

#top ten keywords of each method gets stored here
gensim_out = []
rake_nltk_out = []


for i in files:

	with open('{}.txt'.format(i),'r',encoding='utf-8') as file:

		text = file.read()

		#using Gensim for keywords
		gensim_out.append(keywords(text).split('\n')[:10])

		#using Rake_nltk for keywords
		nltk_var = Rake()

		nltk_var.extract_keywords_from_text(text)

		rake_nltk_out.append(nltk_var.get_ranked_phrases()[:10])


#writing the output as csv
with open('out.csv','w') as output:

	writer = csv.writer(output)

	writer.writerows([['file'],['gensim'],['rake_nltk'],['']])

	for i in range(len(files)):

		writer.writerows([[files[i]],gensim_out[i],rake_nltk_out[i],[]])
