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
        """Returns the neighboring keys for a given character."""
        char = char.lower()
        
        # Handle special cases (composed accents reduced to their base letter for neighborhood errors?)
        # For now, if it's a composed accent, no direct neighbor is found in the simple grid
        # unless the base letter is mapped.
        if char in self.composed_accents:
            # Simplifying: error on the base letter
            # e.g. ê -> e
            import unicodedata
            char = ''.join(c for c in unicodedata.normalize('NFD', char) if unicodedata.category(c) != 'Mn')

        if char not in self.pos_map:
            # If still not found (e.g. unhandled uppercase or special char), search for a random one
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
        """Calculates the Euclidean distance between two keys."""
        # Normalization for composed accents -> use distance to the base letter
        # (as the hand is already in the area) or toward the dead key?
        # Simplifying: distance to the base letter.
        
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
