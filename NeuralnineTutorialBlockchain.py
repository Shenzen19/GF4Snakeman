import hashlib

class lockCoinBlock:

    def __init__(self, previousblockhash, transactionlist):
        
        self.previousblockhash = previousblockhash
        self.transactionlist = transactionlist

        self.blockdata = " - ".join(transactionlist) + " - " + previousblockhash
        self.blockhash = hashlib.sha256(self.blockdata.encode()).hexdigest()


t1 = "Bob send 2 LC to Bill"
t2 = "Jim send 4.1 LC to Bob"
t3 = "Joe send 3.2 LC to Jim"
t4 = "Trimson send 0.3 LC to Bill"
t5 = "Mill send 1 LC to Joe"
t6 = "Jimbo send 5.4 LC to Mill"

initialBlock = lockCoinBlock("Initial Message", [t1, t2])

print(initialBlock.blockdata)
print(initialBlock.blockhash)

secondBlock = lockCoinBlock(initialBlock.blockhash, [t3, t4])

print(secondBlock.blockdata)
print(secondBlock.blockhash)

thirdBlock = lockCoinBlock(secondBlock.blockhash, [t5, t6])

print(thirdBlock.blockdata)
print(thirdBlock.blockhash)
