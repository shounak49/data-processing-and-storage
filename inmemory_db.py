class InMemoryDB:
    def __init__(self):
        # main database storage
        self.data = {}
        # temporary storage for transaction
        self.temp_data = None
        self.is_in_transaction = False
    
    def get(self, key):
        # returns value for key, or None if it doesn't exist
        # only looks at committed data
        if key in self.data:
            return self.data[key]
        return None
    
    def put(self, key, val):
        # can only put if we're in a transaction
        if not self.is_in_transaction:
            raise Exception("Cannot put without a transaction")
        
        # add to temporary data
        self.temp_data[key] = val
    
    def begin_transaction(self):
        if self.is_in_transaction:
            raise Exception("Transaction already in progress")
        
        # start transaction by copying current data
        self.is_in_transaction = True
        self.temp_data = self.data.copy()
    
    def commit(self):
        # save changes permanently
        if not self.is_in_transaction:
            raise Exception("No active transaction")
        
        self.data = self.temp_data
        self.temp_data = None
        self.is_in_transaction = False
    
    def rollback(self):
        # throw away changes
        if not self.is_in_transaction:
            raise Exception("No active transaction")
        
        self.temp_data = None
        self.is_in_transaction = False
