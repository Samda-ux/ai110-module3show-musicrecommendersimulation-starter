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
Takes in the genre of the song and based on a user information suggests back songs. For my algorithm I have genre as +3 points (genre matches what the user wants more than anything),mood +2 points(mood also very important. People usually listen to the same kind of song in a row),energy +2 points (very important as if a user prefers a certain kind of energy they would their songs to match well),tempo_bpm +0.5 points(not very important but generally the same pace of song will go together as the user might have a slight preference for it),danceability +1 points (important as it fits closer to the kind of song the user is listening to currently)

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
  favorite_genre, favorite_mood,target_energym, likes_acoustic
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

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

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
