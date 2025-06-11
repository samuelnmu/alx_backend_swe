class team:
    def __init__(self, teams):
        self.teams = teams
        
    def __len__(self):
        return len(self.teams)
    
members = team(["Samuel", "Alice", "Tracy", "Stacy"])
print (len(members))