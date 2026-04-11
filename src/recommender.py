from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    return []

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0
    reasons = []

    if user_prefs["favorite_genre"] == song["genre"]:
        score += 20
        reasons.append(f"matches your {user_prefs['favorite_genre']} preference")

    if user_prefs["favorite_mood"] == song["mood"]:
        score += 15
        reasons.append(f"has the {user_prefs['favorite_mood']} you like")

    energy_diff = abs(user_prefs["target_energy"] - song["energy"])
    energy_score = 15 * (1 - energy_diff) # Higher if closer to target energy
    score += energy_score
    reasons.append(f"energy level {song['energy']:.1f}" + 
                   (" matches" if energy_diff < 0.1 else " complements"))

    if user_prefs["likes_acoustic"] and song["acousticness"] > 0.7:
        score += 10
        reasons.append("has the acoustic sound you enjoy")
    
    # Expected return format: (score, reasons)
    return [score, reasons]

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    return []
