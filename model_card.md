# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

Give your model a short, descriptive name.  
VibingAndFinding

---

## 2. Intended Use

Describe what your recommender is designed to do and who it is for.

Prompts:

- What kind of recommendations does it generate
  Simple recommendations that might not match exactly to what the user would consume
- What assumptions does it make about the user
  They have a heavy preference for genre, mood and energy as it accounts for 7.5/8.5
- Is this for real users or classroom exploration
  Classroom exploration

---

## 3. How the Model Works

Explain your scoring approach in simple language.

Prompts:

- What features of each song are used (genre, energy, mood, etc.)
  Genre: 3 points, only for an exact match.
  Mood: 2 points, only for an exact match.
  Energy: up to 2 points; the closer to the target, the more it gets.
  Danceability: up to 1 point, scored the same "closer is better" way.
  Tempo: up to 0.5 points, with nothing for songs 100 or more BPM away from the target.
- What user preferences are considered
  The listeners gives genre, mood, energy, danceability and tempo.
  How does the model turn those into a score
  Every song is checked against the listener's preferences and earns points for each one it matches or comes close to.
  The points are added up, giving a total out of 8.5. All the songs are sorted from highest to lowest score, and the top 5 are shown.
  Each recommendation lists where its points came from, so the listener can see why it was picked.
- What changes did you make from the starter logic
  The starter code was empty: it didn't load songs, score them or rank them. I added more songs to the CSV file, the point system, sorted by score and a recommender.

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data

Describe the dataset the model uses.

Prompts:

- How many songs are in the catalog
- What genres or moods are represented
- Did you add or remove data
- Are there parts of musical taste missing in the dataset

---

## 5. Strengths

Where does your system seem to work well

Prompts:

- User types for which it gives reasonable results
- Any patterns you think your scoring captures correctly
- Cases where the recommendations matched your intuition

---

## 6. Limitations and Bias

Where the system struggles or behaves unfairly.

Prompts:

- Features it does not consider
  - Acousticness, valence, lyrics, and listening context are ignored
- Genres or moods that are underrepresented
  - Most genres and moods have only one song
- Cases where the system overfits to one preference
  - Genre and mood outweigh all numeric features, so a lofi song beats an ambient song that might the user better
- Ways the scoring might unintentionally favor some users
  - Pop and lofi listeners get several strong matches, while users with rare tastes get very little

---

## 7. Evaluation

How you checked whether the recommender behaved as expected.

Prompts:

- Which user profiles you tested
  High-Energy Pop, Chill Lofi, Deep Intense Rock, Sad but Hyped, Unknown Genre(k-pop, dreamy),
  Case Mismatch, Out-of-Range Energy
- What you looked for in the recommendations
  Genre and mood were the most looked in recommending stuff. Next was energy
- What surprised you
  Capital letters broke it, empty profile still returns 5 songs
- Any simple tests or comparisons you ran
  High Energy Pop and Chill Lofi share no songs which shows that the algorithm has some effectiveness
  High energy Pop and deep intense rock both share many commonalities

---

## 8. Future Work

Ideas for how you would improve the model next.

Prompts:

- Additional features or preferences
- Better ways to explain recommendations
- Improving diversity among the top results
- Handling more complex user tastes

---

## 9. Personal Reflection

A few sentences about your experience.

Prompts:

- What you learned about recommender systems
- Something unexpected or interesting you discovered
- How this changed the way you think about music recommendation apps
