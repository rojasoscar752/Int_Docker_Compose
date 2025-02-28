# models.py
class YourTable:
    def __init__(self, id, name, created_at):
        self.id = id
        self.name = name
        self.created_at = created_at

    def __repr__(self):
        return f"<YourTable(id={self.id}, name={self.name}, created_at={self.created_at})>"
