class Account:
    id: str
    acc_no: str
    owner_contact_id: str

    def __int__(self, id, acc_no, owner_contact_id):
        self.id = id
        self.acc_no = acc_no
        self.owner_contact_id = owner_contact_id

    def get_id(self):
        return self.id

    def set_id(self, _id):
        self.id = _id

    def get_acc_no(self):
        return self.acc_no

    def set_acc_no(self, acc_no):
        self.acc_no = acc_no

    def get_owner_contact_id(self):
        return self.owner_contact_id

    def set_owner_contact_id(self, owner_contact_id):
        self.owner_contact_id = owner_contact_id

