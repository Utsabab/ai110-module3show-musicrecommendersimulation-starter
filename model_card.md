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

- The dataset is 35% very high energy songs creating high-energy bias. 
- There are unique genres. Among 20 songs there are 14 unique genres. Users whose genre doesn't match get permanent -55 pts penalty.
- Users outside mainstream genres permanently capped at 45 pts creating genre + mpdd weights dominance.

Prompts:  

- Features it does not consider  

tempo_bpm and danceability could help context-specific recommendations.

- Genres or moods that are underrepresented  

11/15 moods appear only once and 15/17 genres appeard only once.

- Cases where the system overfits to one preference

When genre and mood match, that will be enough to lock it in top song regardless of how much other features contribute.

- Ways the scoring might unintentionally favor some users  

Users with pop + happy preference have 2.8x advantage to blues user.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  

user_prefs = {"favorite_genre": "pop", "favorite_mood": "happy", "target_energy": 0.8}

User with electronic genre preference but wants acoustic, electronic genre has least acoustic
user_prefs = {"favorite_genre": "electronic", "favorite_mood": "energetic", "target_energy": 0.85, "likes_acoustic": True, "target_valence": 0.80}

User with classical genre preference but wants high enerrgy song which is unlikely
user_prefs = {"favorite_genre": "classical", "favorite_mood": "melancholic", "target_energy": 0.95, "target_valence": 0.30}

User wants metal song but peaceful mood, that can't happen
user_prefs = {"favorite_genre": "metal", "favorite_mood": "peaceful", "target_energy": 0.95, "target_valence": 0.30, "likes_acoustic": False}

- What you looked for in the recommendations

Looked for how each of the edge cases recommends songs.

- What surprised you

User searching for classical and high energy song got recommended metal song Thunder Strike as it has high energy match even though genre and mood don't match.

- Any simple tests or comparisons you ran  

User looking for electronic genre usually have high energy and low acoustic preference.
While users looking classical song recommendations have low energy and high acoustic preference.

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
