import numpy as np

class KeyboardLayout:
    def __init__(self, layout_name="qwerty"):
        self.layout_name = layout_name
        self.grid = self._load_layout(layout_name)
        self.pos_map = self._build_pos_map()
        
        # Accents are less common in English, but we keep them for robustness
        self.direct_accents = set("éèàùç")
        self.composed_accents = set("âêîôûäëïöü")

    def _load_layout(self, name):
        if name == "qwerty":
            # Standard US QWERTY
            return [
                list("`1234567890-="),
                list("qwertyuiop[]\\"),
                list("asdfghjkl;'"),
                list("zxcvbnm,./")
            ]
        elif name == "azerty":
            # Layout AZERTY
            return [
                list("&é\"'(-è_çà)="), 
                list("azertyuiop^$"),
                list("qsdfghjklmù*"),
                list("wxcvbn,;:!")
            ]
        else:
            return [
                list("1234567890"),
                list("qwertyuiop"),
                list("asdfghjkl;"),
                list("zxcvbnm,./")
            ]

    def _build_pos_map(self):
        mapping = {}
        for r, row in enumerate(self.grid):
            for c, char in enumerate(row):
                mapping[char] = (r, c)
        return mapping

    def get_neighbor_keys(self, char):
        """Retourne les touches voisines d'un caractère donné."""
        char = char.lower()
        
        # Gestion des cas particuliers (accents composés ramenés à leur lettre de base pour l'erreur de voisinage ?)
        # Pour l'instant, si c'est un accent composé, on ne trouve pas de voisin direct dans la grille simple
        # sauf si on mappe la lettre de base.
        if char in self.composed_accents:
            # On simplifie : erreur sur la lettre de base
            # ex: ê -> e
            import unicodedata
            char = ''.join(c for c in unicodedata.normalize('NFD', char) if unicodedata.category(c) != 'Mn')

        if char not in self.pos_map:
            # Si toujours pas trouvé (ex: majuscule non gérée ou char spécial), on cherche un random
            return []
        
        r, c = self.pos_map[char]
        neighbors = []
        
        deltas = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        for dr, dc in deltas:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[nr]):
                neighbors.append(self.grid[nr][nc])
                
        return neighbors

    def get_distance(self, char1, char2):
        """Calcule la distance euclidienne entre deux touches."""
        # Normalisation pour les accents composés -> on prend la distance vers la lettre de base
        # (car la main est déjà dans la zone) ou vers la touche morte ?
        # Simplifions : distance vers la lettre de base.
        
        def normalize(c):
            if c in self.composed_accents:
                import unicodedata
                return ''.join(ch for ch in unicodedata.normalize('NFD', c) if unicodedata.category(ch) != 'Mn')
            return c

        c1 = normalize(char1)
        c2 = normalize(char2)

        if c1 not in self.pos_map or c2 not in self.pos_map:
            return 4.0 
            
        r1, c1_pos = self.pos_map[c1]
        r2, c2_pos = self.pos_map[c2]
        
        return np.sqrt((r1 - r2)**2 + (c1_pos - c2_pos)**2)

    def get_random_neighbor(self, char):
        neighbors = self.get_neighbor_keys(char)
        if not neighbors:
            flat_grid = [c for row in self.grid for c in row]
            return np.random.choice(flat_grid)
        return np.random.choice(neighbors)
    
    def is_direct_accent(self, char):
        return char in self.direct_accents
        
    def is_composed_accent(self, char):
        return char in self.composed_accents
