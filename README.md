# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.
Takes in the genre of the song and based on a user information suggests back songs. For my algorithm I have genre as +3 points (genre matches what the user wants more than anything),mood +2 points(mood also very important. People usually listen to the same kind of song in a row),energy is x3 the value to points (very important as if a user prefers a certain kind of energy they would their songs to match well),tempo_bpm +0.5 points(not very important but generally the same pace of song will go together as the user might have a slight preference for it),danceability +1 points (important as it fits closer to the kind of song the user is listening to currently)

Some prompts to answer:

- What features does each `Song` use in your system?
  genre, mood, energy, tempo, danceability
- What information does your `UserProfile` store?
  favorite_genre, favorite_mood,target_energym, likes_acoustic
- How does your `Recommender` compute a score for each song?
  Uses pre determined values for each category and adds up all the values to give a recommendation
- How do you choose which songs to recommend?
  Based on genre, mood, energy, tempo, danceability, etc.
  You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

Run with `python -m src.main` (default pop/happy profile):

```
Loading songs from data/songs.csv...
Loaded songs: 18
User profile: genre=pop, mood=happy, energy=0.8

============================================================
                    TOP RECOMMENDATIONS
============================================================

#1  Sunrise City  (Neon Echo)
    Score: 8.44
    Reasons:
      - genre match: pop (+3.0)
      - mood match: happy (+2.0)
      - energy 0.82 vs target 0.80 (+1.96)
      - danceability 0.79 vs target 0.80 (+0.99)
      - tempo 118 vs target 120 BPM (+0.49)
------------------------------------------------------------

#2  Gym Hero  (Max Pulse)
    Score: 6.10
    Reasons:
      - genre match: pop (+3.0)
      - energy 0.93 vs target 0.80 (+1.74)
      - danceability 0.88 vs target 0.80 (+0.92)
      - tempo 132 vs target 120 BPM (+0.44)
------------------------------------------------------------

#3  Rooftop Lights  (Indigo Parade)
    Score: 5.38
    Reasons:
      - mood match: happy (+2.0)
      - energy 0.76 vs target 0.80 (+1.92)
      - danceability 0.82 vs target 0.80 (+0.98)
      - tempo 124 vs target 120 BPM (+0.48)
------------------------------------------------------------

#4  Night Drive Loop  (Neon Echo)
    Score: 3.28
    Reasons:
      - energy 0.75 vs target 0.80 (+1.90)
      - danceability 0.73 vs target 0.80 (+0.93)
      - tempo 110 vs target 120 BPM (+0.45)
------------------------------------------------------------

#5  Concrete Crown  (Kilo Verse)
    Score: 3.28
    Reasons:
      - energy 0.78 vs target 0.80 (+1.96)
      - danceability 0.85 vs target 0.80 (+0.95)
      - tempo 94 vs target 120 BPM (+0.37)
------------------------------------------------------------
```

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5?
  The recommendation became much weaker as genre is very important
- What happened when you added tempo or valence to the score?
  The recommendation skewed slightly because it started overrepresenting the tempo of the song rather than the song's feel
- How did your system behave for different types of users?
  Some users failed in finding good recommendations as the system didn't accurately recommend

---

#5 Gym Hero (Max Pulse)
Score: 0.00
Reasons:

---

## Limitations and Risks

Summarize some limitations of your recommender.

- It only works on a tiny catalog
  Small Dataset, bad at catching misspells and capitalization, it heavily favors pop

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

When I started swapping up the features and experimenting I started to really understand how to recommend songs better. AI helped me greatly code and understand certain things but I did need to double check them many times as it messed up README and model_card. The recommender surprisingly works quite well. Next time should add more datasets, features or might use ML to get accurate features. On the other hand it does involve a lot of bias as it relies heavily on datasets and the creators preferences rather than an aggregation of users.

## ALL PROFILES

============================================================
HIGH-ENERGY POP  
============================================================
Profile: {'genre': 'pop', 'mood': 'happy', 'energy': 0.8, 'tempo_bpm': 120, 'danceability': 0.8}

#1 Sunrise City (Neon Echo)
Score: 8.44
Reasons: - genre match: pop (+3.0) - mood match: happy (+2.0) - energy 0.82 vs target 0.80 (+1.96) - danceability 0.79 vs target 0.80 (+0.99) - tempo 118 vs target 120 BPM (+0.49)

---

#2 Gym Hero (Max Pulse)
Score: 6.10
Reasons: - genre match: pop (+3.0) - energy 0.93 vs target 0.80 (+1.74) - danceability 0.88 vs target 0.80 (+0.92) - tempo 132 vs target 120 BPM (+0.44)

---

#3 Rooftop Lights (Indigo Parade)
Score: 5.38
Reasons: - mood match: happy (+2.0) - energy 0.76 vs target 0.80 (+1.92) - danceability 0.82 vs target 0.80 (+0.98) - tempo 124 vs target 120 BPM (+0.48)

---

#4 Night Drive Loop (Neon Echo)
Score: 3.28
Reasons: - energy 0.75 vs target 0.80 (+1.90) - danceability 0.73 vs target 0.80 (+0.93) - tempo 110 vs target 120 BPM (+0.45)

---

#5 Concrete Crown (Kilo Verse)
Score: 3.28
Reasons: - energy 0.78 vs target 0.80 (+1.96) - danceability 0.85 vs target 0.80 (+0.95) - tempo 94 vs target 120 BPM (+0.37)

---

============================================================
CHILL LOFI  
============================================================
Profile: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.4, 'tempo_bpm': 76, 'danceability': 0.6}

#1 Midnight Coding (LoRoom)
Score: 8.43
Reasons: - genre match: lofi (+3.0) - mood match: chill (+2.0) - energy 0.42 vs target 0.40 (+1.96) - danceability 0.62 vs target 0.60 (+0.98) - tempo 78 vs target 76 BPM (+0.49)

---

#2 Library Rain (Paper Lanterns)
Score: 8.36
Reasons: - genre match: lofi (+3.0) - mood match: chill (+2.0) - energy 0.35 vs target 0.40 (+1.90) - danceability 0.58 vs target 0.60 (+0.98) - tempo 72 vs target 76 BPM (+0.48)

---

#3 Focus Flow (LoRoom)
Score: 6.48
Reasons: - genre match: lofi (+3.0) - energy 0.40 vs target 0.40 (+2.00) - danceability 0.60 vs target 0.60 (+1.00) - tempo 80 vs target 76 BPM (+0.48)

---

#4 Spacewalk Thoughts (Orbit Bloom)
Score: 4.99
Reasons: - mood match: chill (+2.0) - energy 0.28 vs target 0.40 (+1.76) - danceability 0.41 vs target 0.60 (+0.81) - tempo 60 vs target 76 BPM (+0.42)

---

#5 Coffee Shop Stories (Slow Stereo)
Score: 3.31
Reasons: - energy 0.37 vs target 0.40 (+1.94) - danceability 0.54 vs target 0.60 (+0.94) - tempo 90 vs target 76 BPM (+0.43)

---

============================================================
DEEP INTENSE ROCK  
============================================================
Profile: {'genre': 'rock', 'mood': 'intense', 'energy': 0.9, 'tempo_bpm': 150, 'danceability': 0.6}

#1 Storm Runner (Voltline)
Score: 8.41
Reasons: - genre match: rock (+3.0) - mood match: intense (+2.0) - energy 0.91 vs target 0.90 (+1.98) - danceability 0.66 vs target 0.60 (+0.94) - tempo 152 vs target 150 BPM (+0.49)

---

#2 Gym Hero (Max Pulse)
Score: 5.07
Reasons: - mood match: intense (+2.0) - energy 0.93 vs target 0.90 (+1.94) - danceability 0.88 vs target 0.60 (+0.72) - tempo 132 vs target 150 BPM (+0.41)

---

#3 Ashes in the Wire (Grave Signal)
Score: 3.12
Reasons: - energy 0.97 vs target 0.90 (+1.86) - danceability 0.45 vs target 0.60 (+0.85) - tempo 168 vs target 150 BPM (+0.41)

---

#4 Sunrise City (Neon Echo)
Score: 2.99
Reasons: - energy 0.82 vs target 0.90 (+1.84) - danceability 0.79 vs target 0.60 (+0.81) - tempo 118 vs target 150 BPM (+0.34)

---

#5 Pulse Theory (Kinetic Grid)
Score: 2.97
Reasons: - energy 0.95 vs target 0.90 (+1.90) - danceability 0.92 vs target 0.60 (+0.68) - tempo 128 vs target 150 BPM (+0.39)

---

============================================================
SAD BUT HYPED  
============================================================
Profile: {'genre': 'blues', 'mood': 'sad', 'energy': 0.9, 'tempo_bpm': 160, 'danceability': 0.9}

#1 Rain on the Delta (Big Earl Moss)
Score: 6.59
Reasons: - genre match: blues (+3.0) - mood match: sad (+2.0) - energy 0.38 vs target 0.90 (+0.96) - danceability 0.48 vs target 0.90 (+0.58) - tempo 70 vs target 160 BPM (+0.05)

---

#2 Gym Hero (Max Pulse)
Score: 3.28
Reasons: - energy 0.93 vs target 0.90 (+1.94) - danceability 0.88 vs target 0.90 (+0.98) - tempo 132 vs target 160 BPM (+0.36)

---

#3 Pulse Theory (Kinetic Grid)
Score: 3.22
Reasons: - energy 0.95 vs target 0.90 (+1.90) - danceability 0.92 vs target 0.90 (+0.98) - tempo 128 vs target 160 BPM (+0.34)

---

#4 Storm Runner (Voltline)
Score: 3.20
Reasons: - energy 0.91 vs target 0.90 (+1.98) - danceability 0.66 vs target 0.90 (+0.76) - tempo 152 vs target 160 BPM (+0.46)

---

#5 Sunrise City (Neon Echo)
Score: 3.02
Reasons: - energy 0.82 vs target 0.90 (+1.84) - danceability 0.79 vs target 0.90 (+0.89) - tempo 118 vs target 160 BPM (+0.29)

---

============================================================
UNKNOWN GENRE  
============================================================
Profile: {'genre': 'k-pop', 'mood': 'dreamy', 'energy': 0.7, 'tempo_bpm': 115, 'danceability': 0.75}

#1 Night Drive Loop (Neon Echo)
Score: 3.35
Reasons: - energy 0.75 vs target 0.70 (+1.90) - danceability 0.73 vs target 0.75 (+0.98) - tempo 110 vs target 115 BPM (+0.47)

---

#2 Rooftop Lights (Indigo Parade)
Score: 3.27
Reasons: - energy 0.76 vs target 0.70 (+1.88) - danceability 0.82 vs target 0.75 (+0.93) - tempo 124 vs target 115 BPM (+0.46)

---

#3 Sunrise City (Neon Echo)
Score: 3.20
Reasons: - energy 0.82 vs target 0.70 (+1.76) - danceability 0.79 vs target 0.75 (+0.96) - tempo 118 vs target 115 BPM (+0.48)

---

#4 Concrete Crown (Kilo Verse)
Score: 3.13
Reasons: - energy 0.78 vs target 0.70 (+1.84) - danceability 0.85 vs target 0.75 (+0.90) - tempo 94 vs target 115 BPM (+0.40)

---

#5 Island Sun Fever (Sol Rasta Collective)
Score: 3.06
Reasons: - energy 0.60 vs target 0.70 (+1.80) - danceability 0.80 vs target 0.75 (+0.95) - tempo 76 vs target 115 BPM (+0.30)

---

============================================================
OUT-OF-RANGE ENERGY  
============================================================
Profile: {'genre': 'metal', 'mood': 'angry', 'energy': 1.5, 'tempo_bpm': 170, 'danceability': 0.5}

#1 Ashes in the Wire (Grave Signal)
Score: 7.38
Reasons: - genre match: metal (+3.0) - mood match: angry (+2.0) - energy 0.97 vs target 1.50 (+0.94) - danceability 0.45 vs target 0.50 (+0.95) - tempo 168 vs target 170 BPM (+0.49)

---

#2 Storm Runner (Voltline)
Score: 2.07
Reasons: - energy 0.91 vs target 1.50 (+0.82) - danceability 0.66 vs target 0.50 (+0.84) - tempo 152 vs target 170 BPM (+0.41)

---

#3 Gym Hero (Max Pulse)
Score: 1.79
Reasons: - energy 0.93 vs target 1.50 (+0.86) - danceability 0.88 vs target 0.50 (+0.62) - tempo 132 vs target 170 BPM (+0.31)

---

#4 Pulse Theory (Kinetic Grid)
Score: 1.77
Reasons: - energy 0.95 vs target 1.50 (+0.90) - danceability 0.92 vs target 0.50 (+0.58) - tempo 128 vs target 170 BPM (+0.29)

---

#5 Sunrise City (Neon Echo)
Score: 1.59
Reasons: - energy 0.82 vs target 1.50 (+0.64) - danceability 0.79 vs target 0.50 (+0.71) - tempo 118 vs target 170 BPM (+0.24)

---

============================================================
EMPTY PROFILE  
============================================================
Profile: (empty)

#1 Sunrise City (Neon Echo)
Score: 0.00
Reasons:

---

#2 Midnight Coding (LoRoom)
Score: 0.00
Reasons:

---

#3 Storm Runner (Voltline)
Score: 0.00
Reasons:

---

#4 Library Rain (Paper Lanterns)
Score: 0.00
Reasons:

---

#5 Gym Hero (Max Pulse)
Score: 0.00
Reasons:

---
