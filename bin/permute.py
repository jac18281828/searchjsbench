import json

def permutation(ary, k):
   if k == len(ary) or MAX == len(ary):
      print(' '.join(ary))
   else:
      for i in range(k, len(ary)):
         ary[k], ary[i] = ary[i], ary[k]
         permutation(ary, k+1)
         ary[k], ary[i] = ary[i], ary[k]
         
if __name__ == '__main__':
    with open('data/datadict.json', 'r') as datastream:
        dict = json.load(datastream)
        permutation(list(dict.keys()), 0)
