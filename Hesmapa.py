from Array import *
from Map import *
from random import randint, randrange
class HashMap(object):
    def __init__(self, capacity=128):
        self._table = DynamicArray(capacity)
        self._size = 0
        self._capacity = self._table.capacity
        self._init_buckets()
        self._board_values = self._init_table()

        self.prime = 109345121
        self._a = 1 + randrange(self.prime-1)
        self._b = randrange(self.prime)

    def __len__(self):
        return self._size

    def __iter__(self):
        for bucket in self._table:
            if len(bucket) != 0:
                for key in bucket:
                    yield key

    def __getitem__(self, key):
        compressed_index = self._compress_key(key)
        return self._bucket_getitem(compressed_index, key)

    def __setitem__(self, key, value):
        compressed_index = self._compress_key(key)
        self._bucket_setitem(compressed_index, key, value)

    def __delitem__(self, key):
        compressed_index = self._compress_key(key)
        self._bucket_delitem(compressed_index, key)

    def __contains__(self, key):
        compressed_index = self._compress_key(key)
        bucket = self._table[compressed_index]
        if key in bucket:
            return True
        else:
            return False

    def _init_buckets(self):
        for i in range(self._capacity):
            self._table.append(Map())

    def _init_table(self):
        table = []
        for i in range(7):
            column = []
            for j in range(7):
                numbers = []
                for k in range(4):                     #ako bude problema staviti 4
                    numbers.append(randint(0, 195))
                column.append(numbers)
            table.append(column)
        return table

    def _Zobrist_hashing(self, key):
        hashed = 0
        for i in range(0,7,1):
            for j in range(0,7,1):
                piece = key[i][j]
                field = self._board_values[i][j]
                if piece=="B":
                    znak=3
                if piece=="W":
                    znak=2
                if piece=="*":
                    znak=1
                if piece=="-":
                    znak=0
                table_value = field[znak]
                hashed=hashed^(table_value)
        return hashed

    def _compress_key(self, key):

        Zobrist_key = self._Zobrist_hashing(key)
        hashed_key = (Zobrist_key*self._a + self._b) % self.prime
        return hashed_key % self._capacity

    def _bucket_getitem(self, index, key):
        bucket = self._table[index]
        return bucket[key]

    def _bucket_setitem(self, index, key, value):
        bucket = self._table[index]
        bucket[key] = value

    def _bucket_delitem(self, index, key):
        bucket = self._table[index]
        if len(bucket) == 0:
            raise KeyError("Key does not exist !")
        else:
            del bucket[key]
