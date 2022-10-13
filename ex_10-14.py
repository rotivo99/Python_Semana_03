#!/usr/bin/env python3

#Recorte da sequência indo da posição 100 até a 200 para posterior contagem da quantidade de guanina no trecho
dna = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG"

dna_sub = dna[99:200]
print(dna_sub)
print("Há", len(dna_sub), "nucleotídeos nesse recorte da sequência.")

print("Há", dna.count("G"), "guaninas nessa sequência.")

#Recorte da sequência indo da posição 100 até a 200 para posterior contagem de guanina no trecho, mas ignorando maiúsculas e minúsculas
import re

dna_2 = "GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCT"

dna_2_sub = dna_2[99:200]
quant_G = len(re.findall(r'[Gg]', dna_2_sub))

relat = "Na sequência \"{}\" há {} guaninas."
relat_format = relat.format(dna_2_sub, quant_G)
print(relat_format)

#Confirmando o resultado de 35 guaninas ao colocar todos os nucleotídeos em letra maiúscula
dna_2_maiusc = dna_2_sub.upper()
quant_G_maiusc = dna_2_maiusc.count("G")

relat_2 = "Na sequência \"{}\" há {} guaninas."
relat_format_2 = relat_2.format(dna_2_maiusc, quant_G_maiusc)
print(relat_format_2)

#Construindo a sequência reversa de dna_2_maiusc
dna_2_maiusc_rever = dna_2_maiusc[::-1]

#Construindo a fita complementar de dna_2_maiusc
dna_2_maiusc_compl_Gc = dna_2_maiusc.replace("G", "c")
dna_2_maiusc_compl_Cg = dna_2_maiusc_compl_Gc.replace("C", "g")
dna_2_maiusc_compl_At = dna_2_maiusc_compl_Cg.replace("A", "t")
dna_2_maiusc_compl_Ta = dna_2_maiusc_compl_At.replace("T", "a")
dna_compl_final = dna_2_maiusc_compl_Ta.upper()

#Formatando a sequência juntamente com seu reverso
dna_cincotres = "5' {} 3'"
dna_cincotres_compl = "3' {} 5'"
dna_cincotres_rever = "3' {} 5'"

dna_formatado = dna_cincotres.format(dna_2_maiusc)
dna_formatado_compl = dna_cincotres_compl.format(dna_compl_final)
dna_formatado_rever = dna_cincotres_rever.format(dna_2_maiusc_rever)

print('{:<19}'.format("DNA"), dna_formatado)
print('{:<19}'.format("Complemento do DNA"), dna_formatado_compl)
print('{:<19}'.format("DNA reverso"), dna_formatado_rever)
