
###################################################
# this code implements a basic blockchain program #
# creaton of actual blockchain called bac_chain   #
# author: and_bac 2019                            #
###################################################

import hashlib
import json
import datetime as date
from bac_chain import Block 

class Bac_Chain(): #these are the actual blocks used for the transactions and the creation of the bac_chain blockchain
    def __init__(self):
        self.chain=[self.genesis(),]

    def genesis(self):
        return Block(0, date.datetime.now(), "init_block_data", "")
    
    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, newBlock):
        newBlock.prev_hash=self.get_last_block().hash
        newBlock.hash=newBlock.hash_calc()
        self.chain.append(newBlock)

    def validate(self):
        for i in range(1, len(self.chain)):
            prev_block=self.chain[i-1]
            curr_block=self.chain[i]
            if (curr_block.hash != curr_block.hash_calc()):
                print ("invalid block")
                return False
            elif (curr_block.prev_hash != prev_block.hash):
                print ("invalid hash, so invalid chain")
                return False
        return True , print("well done mrbacco, your chain is a valid blockchain ")


bac = Bac_Chain()

bac.add_block(Block(1, date, 90879087))
bac.add_block(Block(2, date, 23353))
bac.add_block(Block(3, date, 9-923353))

'''
for x in range (100):

    bac.add_block(Bac_Chain("Bac_Chain " + str(n+1)))
'''

for n in bac.chain:
    print(n)
print(bac.validate())
