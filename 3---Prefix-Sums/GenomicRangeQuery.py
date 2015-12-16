#function to get a minimal impact factor
#of genomes in specified slice of the input sequence S

def solution(S, P, Q):
    #results and the dictionary of nucleotides
    results = []
    #dictionary of genomes
    genomesDict = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    #idea is trivial - build a matrix of 4xN which 
    #for each position in sequence S will show when
    #corresponding nucleotide appears in sequence next time
    #-1 means that it not appears at all
    
    #first of all lets prepare the last column of matrix
    nextNucl = [[-1]*len(S), [-1]*len(S), [-1]*len(S), [-1]*len(S)]
    #notice that 0 is for A, 1 is for C etc
    #first of all in last position any nucleotide will appear
    #last time in that same last position
    nextNucl[genomesDict[S[-1]]-1][-1] = len(S)-1
    
    #now we go FROM END - 1 (end of matrix is populated in prior step)
    #TO THE BEGINNING of the sequence S
    #we populate when each nucleotide appeared last time 
    #looking into the next cell first and later override
    #for current nucleotide its last position with the current one
    for i in range(len(S)-2,-1,-1):
        for j in range(0,4):
            nextNucl[j][i] = nextNucl[j][i+1] 
        #current nucleotide position record
        nextNucl[genomesDict[S[i]]-1][i] = i
    
    #fine, we have our matrix. Now just for each query
    #look up when each of nucleotides appear next time - 
    #before end of query or after
    for i in range(0,len(P)):
        if nextNucl[0][P[i]] != -1 and nextNucl[0][P[i]] <= Q[i]:
            results.append(1)
        elif nextNucl[1][P[i]] != -1 and nextNucl[1][P[i]] <= Q[i]:
            results.append(2)
        elif nextNucl[2][P[i]] != -1 and nextNucl[2][P[i]] <= Q[i]:
            results.append(3)
        else:
            results.append(4)
    return results
