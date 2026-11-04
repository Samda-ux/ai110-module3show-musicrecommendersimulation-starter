# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

**Algorithmic approach (plain language):**

Think of the recommender as a judge giving every song in the catalog a points score out of 8.5, based on how well it fits what the listener says they like. The listener describes their taste with a favorite genre, a mood, and how energetic, danceable and fast they want the music to be.

- **Genre (up to 3 points):** If the song's genre is exactly the listener's favorite, it gets 3 points. Otherwise it gets none. Genre is worth the most because it is usually the biggest deal-breaker.
- **Mood (up to 2 points):** If the song's mood (happy, chill, intense, and so on) matches, it gets 2 points.
- **Energy (up to 2 points):** The closer the song's energy is to what the listener wants, the more points it gets. A perfect match earns the full 2, and the points shrink as the gap grows.
- **Danceability (up to 1 point):** Works the same way as energy, but counts for less.
- **Tempo (up to 0.5 points):** The closer the speed (beats per minute) is to the target, the more points. A song 100 or more BPM away gets nothing.

Once every song has a score, the recommender sorts them from highest to lowest and shows the top 5. For each one, it also lists exactly where the points came from (for example "genre match: pop (+3.0)"), so the listener can see *why* a song was picked.

The key idea is that genre and mood are yes-or-no matches that give big point jumps, while energy, danceability and tempo are "how close" measures that give partial credit. A song that misses on genre can still rank well if it nails the mood and feel.

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
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

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
