"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from src.recommender import load_songs, recommend_songs  # python -m src.main
except ImportError:
    from recommender import load_songs, recommend_songs  # python src/main.py


# Standard taste profiles
PROFILES = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.80,
        "tempo_bpm": 120,
        "danceability": 0.80,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.40,
        "tempo_bpm": 76,
        "danceability": 0.60,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.90,
        "tempo_bpm": 150,
        "danceability": 0.60,
    },
}

# Adversarial / edge-case profiles meant to trick the scoring logic
EDGE_CASE_PROFILES = {
    # Conflicting: sad mood but very high energy (the only sad song is low energy)
    "Sad but Hyped": {
        "genre": "blues",
        "mood": "sad",
        "energy": 0.90,
        "tempo_bpm": 160,
        "danceability": 0.90,
    },
    # Genre and mood that don't exist in the catalog
    "Unknown Genre": {
        "genre": "k-pop",
        "mood": "dreamy",
        "energy": 0.70,
        "tempo_bpm": 115,
        "danceability": 0.75,
    },
    # Energy outside the 0-1 range
    "Out-of-Range Energy": {
        "genre": "metal",
        "mood": "angry",
        "energy": 1.50,
        "tempo_bpm": 170,
        "danceability": 0.50,
    },
    # No preferences at all
    "Empty Profile": {},
}


def print_recommendations(name: str, user_prefs: dict, songs: list) -> None:
    """Print the top 5 recommendations for one profile in a readable block."""
    recommendations = recommend_songs(user_prefs, songs, k=5)

    width = 60
    print("\n" + "=" * width)
    print(f"{name.upper():^{width}}")
    print("=" * width)
    print(f"Profile: {user_prefs or '(empty)'}")
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']}  ({song.get('artist', 'Unknown')})")
        print(f"    Score: {score:.2f}")
        print("    Reasons:")
        for reason in explanation.split("; "):
            if reason:
                print(f"      - {reason}")
        print("-" * width)


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for name, user_prefs in {**PROFILES, **EDGE_CASE_PROFILES}.items():
        print_recommendations(name, user_prefs, songs)


if __name__ == "__main__":
    main()
