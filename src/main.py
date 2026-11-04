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


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Default taste profile: upbeat pop listener
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.80,
        "tempo_bpm": 120,
        "danceability": 0.80,
    }

    # Alternate profile: late-night study listener
    # user_prefs = {
    #     "genre": "lofi",
    #     "mood": "chill",
    #     "energy": 0.40,
    #     "tempo_bpm": 76,
    #     "danceability": 0.60,
    # }

    print(
        f"User profile: genre={user_prefs['genre']}, mood={user_prefs['mood']}, "
        f"energy={user_prefs['energy']}"
    )

    recommendations = recommend_songs(user_prefs, songs, k=5)

    width = 60
    print("\n" + "=" * width)
    print(f"{'TOP RECOMMENDATIONS':^{width}}")
    print("=" * width)
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']}  ({song.get('artist', 'Unknown')})")
        print(f"    Score: {score:.2f}")
        print("    Reasons:")
        for reason in explanation.split("; "):
            if reason:
                print(f"      - {reason}")
        print("-" * width)


if __name__ == "__main__":
    main()
